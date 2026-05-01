from langchain_text_splitters import TokenTextSplitter

with open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt","r") as f:
    text=f.read()

token_splitter=TokenTextSplitter(
    chunk_size=50,
    chunk_overlap=10 
)

chunks=token_splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print(f"\n----chunk {i+1}---")
    print(chunk)