
import json
from tqdm import tqdm
from tatqa.FinQA_tqa import Qa, FinQA
from general_utils import *

def format_tqa_str(context):
    context = context.replace('\u00a0', " ")
    context = context.replace('-', " ")
    context = context.replace(';', " ;")
    context = context.replace('. ', " . ")
    context = context.replace(', ', " , ")
    context = context.replace('(', "( ")
    context = context.replace(')', " )")
    context = context.replace('$', " $ ")
    context = context.replace('%', " %")
    context = context.replace('\"', "")
    return context

def filter_gold(value_list, time_list, text_list):
    valid_flag = 1
    gold_inds = {}

    num_list = value_list + time_list
    num_list_flag = value_list + time_list
    for (index, text) in enumerate(text_list):
        num_text = re.findall(r"\d+\.?\d*", text)
        if len(num_text) > 15:
            return 0, {}
        for num in num_text:
            if str_to_num(num) in num_list:
                gold_inds['text_' + str(index + 1)] = text
                if str_to_num(num) in num_list_flag:
                    num_list_flag.remove(str_to_num(num))
    if len(num_list_flag) != 0:
        valid_flag = 0
    return valid_flag, gold_inds

def convert_tat_qa(path):
    finqas = []
    with open(path, encoding='utf-8') as input_file:
        input_data = json.load(input_file)
        n = 0
        for entry in tqdm(input_data):
            table = entry['table']['table']
            for i in range(0, len(table)):
                for j in range(0, len(table[i])):
                    table[i][j] = format_tqa_str(table[i][j])
            post_text = []
            for text in entry['paragraphs']:
                text_new = format_tqa_str(text['text'])
                post_text.append(text_new)
            for qs in entry['questions']:
                if qs['answer_type'] != 'arithmetic':
                    continue
                scale = qs['scale']
                question = qs['question']
                exe_ans = qs['answer']
                answer = str(exe_ans)
                program = qs['derivation']
                gold_inds = []
                qa = Qa(question, program, exe_ans, answer, gold_inds, scale)
                n += 1
                finqa = FinQA(str(n), [], table, post_text, qa)
                finqa.format_tatqa_program()
                finqa.set_gold()
                if finqa.flag:
                    continue
                print(finqa.qa.program)
                print(finqa.qa.exe_ans)
                finqas.append(finqa)
    return finqas