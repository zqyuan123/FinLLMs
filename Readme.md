# FinLLMs
## Experiment
For the data used in the paper, see: 
[Experiment Data](https://github.com/zqyuan123/FinLLMs/tree/main/experiment-data)

The model used in the experiment:
[FinQA](https://github.com/czyssrs/FinQA), [DyRRen](https://github.com/nju-websoft/DyRRen)

For the display and description of the original data and generated data samples, see:
[Data](https://github.com/zqyuan123/FinLLMs/tree/main/data/Readme.md)

## Installation
Windows or Linux
```
python==3.10
pip install networkx
pip install openai
```

## Configuration
All parameters and settings are in config.py
```python
formula_input_path = 'data/function.json'
traversed_num = 5
formula_output_path = 'data/all_function.json'
max_variable_number = 5
max_dsl_program_step = 4
# VPN settings
proxies = {'http': "http://127.0.0.1:7890", 'https': "http://127.0.0.1:7890"}
table_output_path = "data/table.json"
text_output_path = "data/text.json"
api_key = "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"
output_path = 'data/table-text'
finqa_path = "D:\\code\\DataGenerate\\json"
max_gold = 5
# Whether generated data is mixed with finqa data
blend = False
train_rate = 0.75
test_rate = 0.15
# generator config
max_retry = 5
start_time = 2010
end_time = 2022
generate_num_per_formula = 50
```
## Formulas
All formulas are stored in file [Formula](https://github.com/zqyuan123/FinLLMs/tree/main/data/all_function_indent.py). An example of a formula is provided below, which includes the following parts.
```json
[
    {
        "target": "profit*n",
        "variables": [
            "income*n",
            "expenses*n"
        ],
        "formula": [
            "subtract",
            "income*n",
            "expenses*n"
        ]
    }
]
```
This JSON element represents that during a certain period,  `profit = income - expenses`
## RUN
After completing the api, path and other parameter settings, run the main function directly.
```commandline
cd FinLLMs
python main.py
```


