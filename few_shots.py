few_shots = [
    {'Question' : "What was the cost per opt in in October 2023?",
     'SQLQuery' : "SELECT SUM(ad_spend) / SUM(opt_ins) AS cost_per_opt_in FROM example_1 WHERE week_of BETWEEN '2023-10-01' AND '2023-10-31'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "62.59"},
    {'Question': "What was the cost per booked call in October 2023?",
     'SQLQuery':"SELECT SUM(ad_spend) / SUM(booked_calls) AS cost_per_booked_call FROM example_1 WHERE week_of BETWEEN '2023-10-01' AND '2023-10-31'",
     'SQLResult': "Result of the SQL query",
     'Answer': "256.32"},
    {'Question': "What was the ROAS in October 2023?",
     'SQLQuery' : "SELECT SUM(revenue) / SUM(ad_spend) AS ROAS FROM example_1 WHERE week_of BETWEEN '2023-10-01' AND '2023-10-31",
     'SQLResult': "Result of the SQL query",
     'Answer': "2.1921808988287297"} ,
     {'Question' : "What was the return on ad spend in June 2024?" ,
      'SQLQuery': "SELECT SUM(revenue) / SUM(ad_spend) AS ROAS FROM example_1 WHERE week_of BETWEEN '2024-06-01' AND '2024-06-30",
      'SQLResult': "Result of the SQL query",
      'Answer' : "4.801367181646181"}
]