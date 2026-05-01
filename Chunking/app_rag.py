from unstructured.partition.pdf import partition_pdf
import pdfplumber
import pymupdf
import fitz


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from groq import Groq


client=Groq(api_key="Enter your api key here use it")

pdf_path="/Users/jagadeeswarreddyvankala/Downloads/smaple.pdf"

all_text=[]

# # Text+structure
# elements=partition_pdf(pdf_path)

# for i,el in enumerate(elements):
    
#     all_text.append(str(el).strip())

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables=page.extract_tables({
            "vertical_strategy":"text",
            "horizontal_strategy":"text"
        })
        
        for table in tables:
            for row in table:
                row_text=" | ".join(str(c) for c in row)
                all_text.append(f"Table :{row_text}")

        text=page.extract_text()
        if text:
            all_text.append(text)
        
        if text and "PPL" not in text:
            words=page.extract_words()
            for w in words:
                all_text.append(w.get("text", str(w)))



# def clean_pdf(text):
#     text=text.replace(" \n "," ")
#     text=" ".join(text.split())
#     return text

# All_text=clean_pdf(all_text)
final_text=list(set(all_text))

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db=FAISS.from_texts(final_text,embeddings)

query="Who is Jagadeeswar Reddy?"

result=vector_db.similarity_search(query,k=2)

context="\n\n".join(res.page_content for res in result)

prompt=f"""Answer the question from the below context only
query:{query}
context:{context}
answer:
"""

response=client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role":"user",
         "content":prompt
         }
    ]
)

print(response.choices[0].message.content)