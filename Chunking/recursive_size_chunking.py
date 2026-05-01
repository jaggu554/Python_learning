from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt","r") as f:
    text=f.read()


recursive_splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks=recursive_splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print("chunk :",i+1)
    print(chunk)
    print("=="*30)