from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter

final_chunks=[]

with open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt","r") as f:
    text=f.read()

recursive_splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
)


recursive_chunks=recursive_splitter.split_text(text)

for i,recur_chunk in enumerate(recursive_chunks):
    print(f"\n----chunk {i+1}----")
    print(recur_chunk)


character_splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=" "
)

for chunk in recursive_chunks:
    sub_chunks=character_splitter.split_text(chunk)
    final_chunks.extend(sub_chunks)

print("=="*20,"print the final chunks","=="*20)
for i,f_chunk in enumerate(final_chunks):
    print(f"\n---chunk{i+1}---")
    print(f_chunk)



