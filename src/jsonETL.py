import pandas as pd
import json
import os
from pandas.io.json import json_normalize
from sqlalchemy import create_engine


all_dfs = []

for filename in os.listdir('data'):
	if filename.endswith('json'):
		with open(filename, 'r') as f:
			data = json.load(f)
			df = json_normalize(data['orders'])
			all_dfs.append(df)

orders = pd.concat(all_dfs)

users = orders[['user_id', 'email', 'contact_email', 
                'phone', 'customer_locale']].drop_duplicates()
orders.drop(['user_id', 'email', 'contact_email', 'phone', 'customer_locale'], 
	          axis=1, inplace=True)

engine = create_engine('postgresql://xiangyu:password@localhost:5432/jsonETL')
orders.to_sql('orders', engine)
users.to_sql('users', engine)

