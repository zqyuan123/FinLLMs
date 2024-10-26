import random
from Graph.formula_graph import *
from config import params
from Graph.generator import *
from FormatData.process_table import process as process_table
from FormatData.process_text import process as process_text
from utils.json_utils import write_json
if __name__ == '__main__':

    funs = get_funs(input_path=params.formula_input_path,
                    t_num=params.traversed_num,
                    output_path=params.formula_output_path,
                    max_variable_number=params.max_variable_number,
                    max_dsl_program_step=params.max_dsl_program_step)

    generate(fun_path=params.formula_output_path,
             num_formula=params.generate_num_per_formula,
             begin_time=params.start_time,
             end_time=params.end_time,
             output_table_path=params.table_output_path,
             output_text_path=params.text_output_path,
             max_retry=params.max_retry,)