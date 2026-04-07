import pandas as pd

df=pd.read_csv("DataProcessing/data_one.csv")

df['query']=df['query'].str.lower()
df['query']=df['query'].str.strip()

df=df.dropna(subset=['query']) # row wise duplicates removes

df=df.drop_duplicates(subset=['timestamp']) # row wise duplicates removal from the timestamp

df['query']=df['query'].str.replace(r'[^\w\s]','',regex=True)

# df['user_id']=df['user_id'].drop_duplicates() # column wise duplicates removal. not recomended

# df['user_id']=df['user_id'].fillna('')

# df['query']=df['query'].fillna('')

# df['timestamp']=df['timestamp'].drop_duplicates()
# df['timestamp']=df['timestamp'].fillna('')
print(df)