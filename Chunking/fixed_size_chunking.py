# from langchain_text_splitters import CharacterTextSplitter

# splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=20,separator="")


# # text=open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt",'r').read()

# with open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt","r") as f:
#     text=f.read()

# print(f"total text len :{len(text)}")

# chunks=splitter.split_text(text)
# print("Total chunks:", len(chunks))
# print("=======fixed size chunking======")
# for i,chunk in enumerate(chunks):
#     print(i+1 ," ",chunk)


from langchain_text_splitters import CharacterTextSplitter

splitter=CharacterTextSplitter(
chunk_size=100,
chunk_overlap=30,
separator=""
)

with open("/Users/jagadeeswarreddyvankala/Downloads/sample_doc.txt","r") as f:
    text=f.read()

print(f"Total length of text {len(text)}")

chunks=splitter.split_text(text)

print(f"total chunks length {len(chunks)}")
for i,chunk in enumerate(chunks):
    print(f"{i+1}:{chunk}\n")