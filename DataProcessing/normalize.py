
import re

data=[
    "Hey!!! check this out 👉 https://example.com 😄",
    "ERROR 500 at /api/user?id=123",
    "Contact me at john123@gmail.com",
    "HELLOOOOO!!!!!",
    "What is GPT-4???   ",
]


def cleaned_text(text):
    # to lowercase 
    text=text.strip().lower()

    #remove rest call
    text=re.sub(r"htpp\S+","",text)

    #remove the email from the data
    text=re.sub(r"\S+@\S+","",text)

    # remove special characters
    text=re.sub(r"[^a-zA-Z0-9\s]","",text)

    #remove the mulitple spaces with single space
    text=re.sub(r'\s+',' ',text).strip()

    text=re.sub(r"(.)\1+",r"\1\1",text)

    return text;


cleaned_text=[cleaned_text(t) for t in data]

print(cleaned_text)
