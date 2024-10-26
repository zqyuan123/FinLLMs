# Data Example

## FinQA Data Sample

```json
[
    {
        "pre_text":[
            "if libor changes by 100 basis points , our annual interest expense would change by $ 3.8 million ."
        ],
        "post_text":[
            "interest rate to a variable interest rate based on the three-month libor plus 2.05% ( 2.05 % ) ( 2.34% ( 2.34 % ) as of october 31 , 2009 ) .",
            "currently , our largest foreign currency exposure is the euro , primarily because our european operations have the highest proportion of our local currency denominated expenses .",
            "the market risk associated with our derivative instruments results from currency exchange rate or interest rate movements that are expected to offset the market risk of the underlying transactions , assets and liabilities being hedged .",
            "we do not believe that there is significant risk of nonperformance by these counterparties because we continually monitor the credit ratings of such counterparties .",
            "$ ( 6781 ) $ ( 38294 ) the calculation assumes that each exchange rate would change in the same direction relative to the u.s .",
            "the amounts potentially subject to credit risk ( arising from the possible inability of counterparties to meet the terms of their contracts ) are generally limited to the amounts , if any , by which the counterparties 2019 obligations under the contracts exceed our obligations to the counterparties .",
            "the following table illustrates the effect that a 10% ( 10 % ) unfavorable or favorable movement in foreign currency exchange rates , relative to the u.s .",
            "in addition to the direct effects of changes in exchange rates , such changes typically affect the volume of sales or the foreign currency sales price as competitors 2019 products become more or less attractive .",
            "the terms of these contracts are for periods matching the duration of the underlying exposure and generally range from one month to twelve months .",
            "while the contract or notional amounts of derivative financial instruments provide one measure of the volume of these transactions , they do not represent the amount of our exposure to credit risk .",
            "the counterparties to the agreements relating to our foreign exchange instruments consist of a number of major international financial institutions with high credit ratings .",
            "our sensitivity analysis of the effects of changes in foreign currency exchange rates does not factor in a potential change in sales levels or local currency selling prices. .",
            "in the notes to consolidated financial statements contained in item 8 of this annual report on form 10-k , we regularly hedge our non-u.s .",
            "relative to foreign currency exposures existing at october 31 , 2009 and november 1 , 2008 , a 10% ( 10 % ) unfavorable movement in foreign currency exchange rates over the course of the year would not expose us to significant losses in earnings or cash flows because we hedge a high proportion of our year-end exposures against fluctuations in foreign currency exchange rates .",
            "dollar , would have on the fair value of our forward exchange contracts as of october 31 , 2009 and november 1 , 2008: .",
            "foreign currency exposure as more fully described in note 2i .",
            "fair value of forward exchange contracts after a 10% ( 10 % ) unfavorable movement in foreign currency exchange rates asset ( liability ) .",
            "$ 20132 $ ( 9457 ) fair value of forward exchange contracts after a 10% ( 10 % ) favorable movement in foreign currency exchange rates liability .",
            "dollar-based exposures by entering into forward foreign currency exchange contracts .",
            "dollar ."
        ],
        "filename":"ADI/2009/page_49.pdf",
        "table_ori":[
            [
                "",
                "October 31, 2009",
                "November 1, 2008"
            ],
            [
                "Fair value of forward exchange contracts asset (liability)",
                "$6,427",
                "$(23,158)"
            ],
            [
                "Fair value of forward exchange contracts after a 10% unfavorable movement in foreign currency exchange rates asset (liability)",
                "$20,132",
                "$(9,457)"
            ],
            [
                "Fair value of forward exchange contracts after a 10% favorable movement in foreign currency exchange rates liability",
                "$(6,781)",
                "$(38,294)"
            ]
        ],
        "table":[
            [
                "",
                "october 31 2009",
                "november 1 2008"
            ],
            [
                "fair value of forward exchange contracts asset ( liability )",
                "$ 6427",
                "$ -23158 ( 23158 )"
            ],
            [
                "fair value of forward exchange contracts after a 10% ( 10 % ) unfavorable movement in foreign currency exchange rates asset ( liability )",
                "$ 20132",
                "$ -9457 ( 9457 )"
            ],
            [
                "fair value of forward exchange contracts after a 10% ( 10 % ) favorable movement in foreign currency exchange rates liability",
                "$ -6781 ( 6781 )",
                "$ -38294 ( 38294 )"
            ]
        ],
        "qa":{
            "question":"what is the the interest expense in 2009?",
            "answer":"380",
            "explanation":"",
            "ann_table_rows":[],
            "ann_text_rows":[
                1
            ],
            "steps":[
                {
                    "op":"divide1-1",
                    "arg1":"100",
                    "arg2":"100",
                    "res":"1%"
                },
                {
                    "op":"divide1-2",
                    "arg1":"3.8",
                    "arg2":"#0",
                    "res":"380"
                }
            ],
            "program":"divide(100, 100), divide(3.8, #0)",
            "gold_inds":{
                "text_1":"if libor changes by 100 basis points , our annual interest expense would change by $ 3.8 million ."
            },
            "exe_ans":3.8,
            "tfidftopn":{
                "text_14":"dollar , would have on the fair value of our forward exchange contracts as of october 31 , 2009 and november 1 , 2008: .",
                "text_0":"interest rate to a variable interest rate based on the three-month libor plus 2.05% ( 2.05 % ) ( 2.34% ( 2.34 % ) as of october 31 , 2009 ) ."
            },
            "model_input":[
                [
                    "text_0",
                    "interest rate to a variable interest rate based on the three-month libor plus 2.05% ( 2.05 % ) ( 2.34% ( 2.34 % ) as of october 31 , 2009 ) ."
                ],
                [
                    "text_1",
                    "if libor changes by 100 basis points , our annual interest expense would change by $ 3.8 million ."
                ],
                [
                    "text_14",
                    "dollar , would have on the fair value of our forward exchange contracts as of october 31 , 2009 and november 1 , 2008: ."
                ]
            ],
            "program_re":"divide(3.8, divide(100, 100))",
            "gold_text":{
                "text_0":"if libor changes by 100 basis points , our annual interest expense would change by $ 3.8 million ."
            },
            "Gold_cell_coor":[]
        }
    }
]
```

## Generated Data Sample

```json
[
    {
        "id": "12648",
        "pre_text": [
            "In the year 2020, our company experienced a total profit of  $ 250000. ",
            "This was achieved by generating revenues and after deducting the business costs of  $ 150000. ",
            "Our diligent efforts and strategic decisions allowed us to maximize our financial gains, resulting in a commendable level of profitability. ",
            " Moving forward to 2021, our company's total profits continued to climb, reaching a remarkable amount of  $ 275000. ",
            "Despite the challenges faced in the ever-evolving market, we managed to effectively control our business costs which were recorded at  $ 165000. ",
            "This prudent management of expenses played a crucial role in sustaining our business growth and amplifying our financial standing. ",
            " Looking ahead to the year 2022, we anticipate even more prosperous results. ",
            "With an expected total profit of  $ 310000 and business costs estimated at  $ 180000, we remain confident in our ability to achieve financial success. ",
            "By consistently evaluating our operations and making informed decisions, we strive to further enhance our profitability and secure long-term sustainability. ",
            " As a company, we are committed to utilizing our resources effectively, optimizing revenues, and diligently managing costs. "
        ],
        "table": [
            [
                "",
                "2020",
                "2021",
                "2022"
            ],
            [
                "total_profits",
                "250000",
                "275000",
                "310000"
            ],
            [
                "business_cost",
                "150000",
                "165000",
                "180000"
            ]
        ],
        "post_text": [],
        "qa": {
            "question": "between 2020 and 2021 , what was the change rate in business cost",
            "program": "subtract(165000, 150000), divide(#0, 150000)",
            "exe_ans": 0.1,
            "answer": "0.1",
            "gold_inds": {
                "table_2": "the business_cost of 2020 is 150000 ; the business_cost of 2021 is 165000 ; the business_cost of 2022 is 180000 ;"
            }
        }
    }
]
```