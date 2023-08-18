import re
from general_utils import *
from postfix import *
class Qa:
    def __init__(self, question, program, exe_ans, answer, gold_inds, scale):
        self.question = question
        self.program = program
        self.exe_ans = exe_ans
        self.answer = answer
        self.gold_inds = gold_inds
        self.scale = scale

    def get_dict(self):
        res = {'question': self.question, 'program': self.program, 'exe_ans': self.exe_ans, 'answer': self.answer,
               'gold_inds': self.gold_inds}
        return res


class FinQA:
    def __init__(self, this_id, pre_text, table, post_text, Qa):
        self.all_nums = []
        self.num_index = {}
        self.gold_index = {}
        self.flag = False
        self.id = this_id
        self.OPERATORS = ('+', '-', '*', '/')
        self.op_str_dict = {'+': 'add', '-': 'subtract', '*': 'multiply', '/': 'divide'}
        self.pre_text = pre_text
        '''
        for i in range(0, len(pre_text)):
            pre_text[i] = remove_mart(pre_text[i])
            tmpN = re.findall(r"\d+\.?\d*", pre_text[i])
            self.all_nums += tmpN
            for n in tmpN:
                self.num_index[str(n)] = 'text_' + str(i + 1)
                self.gold_index[str(n)] = pre_text[i]
        '''
        self.table = table
        self.post_text = post_text
        for i in range(0, len(post_text)):
            post_text[i] = remove_mart(post_text[i])
            tmpN = re.findall(r"\d+\.?\d*", post_text[i])
            self.all_nums += tmpN
            for n in tmpN:
                self.num_index[str(n)] = 'text_' + str(len(pre_text) + i + 1)
                self.gold_index[str(n)] = post_text[i]
        self.qa = Qa
        self.nums = []
        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                self.table[i][j] = remove_mart(str(table[i][j]))
        for i in range(1, len(self.table)):
            content = table_row_to_text(self.table[0], self.table[i])
            tmpN = re.findall(r"\d+\.?\d*", content)
            self.all_nums += tmpN
            for n in tmpN:
                self.num_index[str(n)] = 'table_' + str(i + 1)
                self.gold_index[str(n)] = content

    def format_tatqa_program(self):
        text = self.qa.program.replace(' ', '')
        text = text.replace('[', '(')
        text = text.replace(',', '')
        text = text.replace('$', '')
        text = text.replace(']', ')')
        if ' average' in self.qa.question:
            text = text.replace('/', '/const_')
            text = text.replace('/const_(', '/(')
        if self.qa.scale == 'percent':
            text = text.replace('-1', '- const_1')
        if 'millions' in text:
            self.flag = True
        if 'thousands' in text:
            self.flag = True
        if 'million' in text:
            self.flag = True
        if 'thousand' in text:
            self.flag = True
        if 'billions' in text:
            self.flag = True
        if 'billion' in text:
            self.flag = True
        infix = tokenize(text)
        postfix_list, nums = infix_to_postfix(infix)
        self.nums = nums
        self.postfix_to_program(postfix_list)
        invalid_flag, exe_res = get_res(self.qa.program, self.table)
        if invalid_flag == 1:
            self.flag = True
        else:
            self.qa.exe_ans = exe_res

            if is_num(self.qa.exe_ans):
                self.qa.exe_ans = round(self.qa.exe_ans, 5)
            else:
                self.flag = True

    def postfix_to_program(self, postfix_list):
        operands = []
        program = ''
        n = 0
        for i, item in enumerate(postfix_list):
            if item not in self.OPERATORS:
                operands.append(item)
            else:
                op = self.op_str_dict[item]
                arg2 = operands.pop()
                arg1 = operands.pop()
                if arg1[0] == '-' and arg2[0] == '-' and op == 'subtract':
                    op = 'add'
                    t = arg1
                    arg1 = arg2
                    arg2 = t
                    arg1 = arg1[1:]
                    arg2 = arg2[1:]
                elif arg2[0] == '-' and op == 'subtract':
                    op = 'add'
                    arg2 = arg2[1:]
                elif arg2[0] == '-' and op == 'add':
                    op = 'subtract'
                    arg2 = arg2[1:]
                elif arg1[0] == '-' or arg2[0] == '-':
                    self.flag = True
                arg1, arg2 = self.format_arg(arg1, arg2)
                program += op + '(' + str(arg1) + ', ' + str(arg2) + ')'
                if i != len(postfix_list) - 1:
                    program += ', '
                operands.append('#' + str(n))

                n += 1
        self.qa.program = program



    def set_gold(self):
        gold_inds = {}
        len_pre = len(self.pre_text)
        flag = False
        for i in range(0, len(self.nums)):
            if str(self.nums[i]) == '165.2':
                print(123)
            if self.nums[i] in self.all_nums:
                ind = self.num_index[str(self.nums[i])]
                gold_inds[ind] = self.gold_index[str(self.nums[i])]
                flag = True
                break
        if not flag:
            self.flag = True
        '''
        for num in self.nums:
            for i in range(0, len(self.pre_text)):
                content = self.pre_text[i]
                if str(num) in content:
                    inds = 'text_' + str(i + 1)
                    gold_inds[inds] = content
                    flag = True
                    break
                if flag:
                    continue
            for i in range(0, len(self.post_text)):
                content = self.post_text[i]
                if str(num) in content:
                    inds = 'text_' + str(len_pre + i + 1)
                    gold_inds[inds] = content
                    flag = True
                    break
                if flag:
                    continue
            for i in range(1, len(self.table)):
                content = table_row_to_text(self.table[0], self.table[i])
                if str(num) in content:
                    inds = 'table_' + str(i + 1)
                    gold_inds[inds] = content
                    flag = True
                    break
        '''
        self.qa.gold_inds = gold_inds

    def format_arg(self, arg1, arg2):
        arg1 = arg1.replace(',', '')
        arg1 = arg1.replace('$', '')
        arg2 = arg2.replace(',', '')
        arg2 = arg2.replace('$', '')
        if '%' in arg1 and '%' not in arg2:
            arg1 = arg1.replace('%', '')
            farg = float(arg1)/100.0
            arg1 = str(farg)
        if '%' not in arg1 and '%' in arg2:
            arg2 = arg2.replace('%', '')
            farg = float(arg2)/100.0
            arg2 = str(farg)
        if '%' in arg1 and '%' in arg2:
            arg2 = arg2.replace('%', '')
            arg1 = arg1.replace('%', '')
        if is_number(arg1) and str(arg1) not in self.all_nums:
            if str_to_num(arg1) < 0 or str_to_num(arg1) > 10:
                self.flag = True
            arg1 = 'const_' + str(arg1)
            if '.' in str(arg1):
                self.flag = True

        if is_number(arg2) and str(arg2) not in self.all_nums:
            if str_to_num(arg2) < 0 or str_to_num(arg2) > 10:
                self.flag = True
            arg2 = 'const_' + str(arg2)
            if '.' in str(arg2):
                self.flag = True

        return arg1, arg2

    def get_dict(self):
        res = {'id': self.id, 'pre_text': self.pre_text, 'table': self.table, 'post_text': self.post_text, 'qa': self.qa.get_dict()}
        return res
