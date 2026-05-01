from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


loader=PyPDFLoader("/Users/jagadeeswarreddyvankala/Downloads/java8_interview_practice_50plus.pdf")

documnets=loader.load()

def clean_text(text):
    text=text.replace("\n"," ")
    text=" ".join(text.split())
    return text

full_text=" ".join(clean_text(doc.page_content) for doc in documnets)


recurisvie_splitter=RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=50
)

chunks=recurisvie_splitter.split_text(full_text)

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db=FAISS.from_texts(chunks,embeddings)

query="Indices of Max Elements"

result=vector_db.similarity_search(query,k=2)

for i in result:
    print(i.page_content,"\n")


