class params():
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
