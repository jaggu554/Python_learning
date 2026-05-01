import pandas as pd

df=pd.read_csv("/Users/jagadeeswarreddyvankala/Documents/PYTHON/DataProcessing/data.csv",header=None)

df.columns= ['text'] # assuming csv file contains text column in the csv


df['clean_text']=df['text'].str.strip() # removing the files

df['clean_text']=df['clean_text'].str.lower()

df['clean_text']=df['clean_text'].str.replace(r'[^\w\s]','',regex=True)
df['clean_text']=df['clean_text'].str.replace(NaN,'',regex=True)

df=df.drop_duplicates(subset=['clean_text'])
print(df)

