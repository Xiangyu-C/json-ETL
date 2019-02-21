# Data Migration

## Problem statement

Imagine a scenario where you were given the task create an ETL (Extract, Transform, Load) so that API data is consumable by business analysts. Fortunately, your co-workers have already done the Extract step and has provided you with a .zip file containing retail order data in the raw JSON format. Your project manager has put you on the task to support these business analysts so that they can query that data using SQL from a PSQL database.
While you’re at it, they would also want you to create a user table that would contain summary metrics that you think business analysts would find useful.  
**Note:** Keep in mind that the newly created tables have to be sanely structured and those steps should be reproducible with the expectation that the **ETL would run daily**.

## My approach:
`check files in data folder
 if contains json files:  \n
     data = json.load(file)
 normalized the value of orders key and make a dataframe
 and append to a list
     all_dfs.append(json_normalzie(data['orders]))
 make a complete dataframe or we can process one at a time
     complete_df = pd.concat(all_dfs)
 extract users information
 then save to postgresql
 orders.save_to_postgres
 users.save_to_postgres
 `
 
