import pandas as pd

df=pd.read_csv("/Users/jagadeeswarreddyvankala/Documents/PYTHON/DataProcessing/data_one.csv")

# remove duplicates
df=df.dropna(subset=['query'])

df['query']=(df['query'].str.lower().str.strip().str.replace(r'\s+[^\w]'," ",regex=True))


df=df.drop_duplicates(subset=['query','timestamp'])

# df=df.reset_index(drop=True)

print(df)

