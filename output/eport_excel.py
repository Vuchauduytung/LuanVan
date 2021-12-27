import pandas as pd

df_json = pd.read_json("customers_data.json")
df_json.to_excel("customers_data.xlsx")
