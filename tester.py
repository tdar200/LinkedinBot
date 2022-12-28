import pandas as pd

df = pd.read_excel('CompaniesMessaging.xlsx')

# df = df.drop(df.index[0])
# df.to_excel('CompaniesMessaging.xlsx', index=False)
print(df.head(5))
