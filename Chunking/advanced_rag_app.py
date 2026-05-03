from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from unstructured.partition.pdf import partition_pdf
from sklearn.metrics.pairwise import cosine_similarity

from groq import Groq

import pdfplumber
import numpy as np


client=Groq(api_key="")




# ================
# Extract Text
# ================
def extract_pdf(pdf_path):
    all_text=[]

    # ---- text extraction -----
    elements = partition_pdf(pdf_path)
    for el in elements:
        txt=str(el).strip()
        if txt:
            all_text.append(txt)

    # --- table + text+fallback ----
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables=page.extract_tables({
                "vertical_strategy":"text",
                "horizontal_strategy":"text"
            })


            for table in tables:
                for row in table:
                    clean_text=[str(c) for c in row if c]

                    if clean_text:
                        all_text.append("Table :"+" | ".join(clean_text))

    return all_text


# =============
# clean up data
# =============

import re

def clean_text(data):
    seen = set()
    cleaned = []

    for item in data:
        item = str(item)

        # Fix merged words (camel case issues)
        item = re.sub(r'([a-z])([A-Z])', r'\1 \2', item)

        # Fix missing spaces after punctuation
        item = re.sub(r'([.,])([A-Za-z])', r'\1 \2', item)

        # Remove extra spaces
        item = re.sub(r'\s+', ' ', item)

        item = item.strip()

        if item and item not in seen:
            seen.add(item)
            cleaned.append(item)

    return cleaned


# ===================
# Recurisive Chunking
# ===================

def recursive_chunking(text_data):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=150
    )

    chunks = splitter.split_text("\n\n".join(text_data))
    return chunks

# =================
# semantic chunking
# =================

def semantic_grouping(chunks,embeddings,threshold=0.7):

    vectors=embeddings.embed_documents(chunks)

    final_chunks=[]

    current_group=[chunks[0]]
    current_vectors=[vectors[0]]

    for i in range(1,len(chunks)):
        # centriod of group
        centriod=np.mean(current_vectors,axis=0)

        sim=cosine_similarity([centriod],[vectors[i]])[0][0]

        if sim >threshold:
            current_group.append(chunks[i])
            current_vectors.append(vectors[i])
        else:
            final_chunks.append("\n".join(current_group))
            current_group=[chunks[i]]
            current_vectors=[vectors[i]]

    final_chunks.append("\n".join(current_group))
    return final_chunks
    


# ================
# Query ReWriting
# ================

def rewrite_query(query):
    prompt = f"""
Rewrite the query into a simple natural language sentence for semantic search.

Rules:
- Do NOT generate SQL
- Do NOT generate code
- Do NOT generate multiple options
- Return ONLY one short sentence

Query: {query}

Rewritten Query:
"""

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content.strip()
            

        
# ===========
# ReRanking
# ===========

def rerank(query,docs):
    scored=[]
    
    for doc in docs:
        prompt = f"""
Return ONLY a number between 1 and 10.

Query: {query}
Document: {doc.page_content}
"""
        response=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role":"user",
                "content":prompt
            }]
        )

        try:
            score=float(response.choices[0].message.content.strip())
        except:
            score=0
        scored.append((doc,score))
    
    scored.sort(key= lambda x:x[1] ,reverse=True)

    return [doc for doc,_ in scored[:2]]

# ============
# Final Answer
# ============

def generate_answer(query,docs):
    context="\n\n".join([d.page_content for d in docs])

    prompt = f"""
Answer the question using the context below.

The context may contain formatting issues, but extract the meaning carefully.

Context:
{context}

Question:
{query}

Answer:
"""
    
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content

# ==================
# MAIN PIPELiNE
# ==================

def run_rag(pdf_path,query):

    print("\n Extracting PDF")
    raw_data=extract_pdf(pdf_path)

    print("\n cleaning... ")
    cleaned=clean_text(raw_data)

    print("\n Recursive chunking...")
    chunks=recursive_chunking(cleaned)

    print("Embeddings...")
    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("semantic grouping...")
    hybrid_chunks=semantic_grouping(chunks,embeddings)

    print("Building vector db")
    vector_db=FAISS.from_texts(hybrid_chunks,embeddings)

    print("\n Rewriting query")
    improved_query=rewrite_query(query)
    print("\n improved_query :",improved_query)

    print("\n Retriveing from the vector DB")
    retrieved=vector_db.similarity_search(improved_query,k=10)

    for i, doc in enumerate(retrieved):
        print(f"\n--- Retrieved {i+1} ---\n")
        print(doc.page_content)

    print("Reranking....")
    best_docs=rerank(improved_query,retrieved[:2])

    print("\n Generating the answer")
    answer=generate_answer(query,best_docs)

    return answer


# ==========
# run rag
# ==========


pdf_path="/Users/jagadeeswarreddyvankala/Downloads/smaple.pdf"
query="what is Residual Dropout?"
result=run_rag(pdf_path,query)

print("\n =======Final Answer ========")
print(result)



    