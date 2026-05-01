from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter=SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=40
)

text = """
Artificial Intelligence is transforming industries by enabling machines to perform tasks that typically require human intelligence.

Machine learning is a subset of AI that allows systems to learn patterns from data and improve performance over time.

Cricket is a popular sport in India and has millions of fans worldwide.

Football is played across many countries and is one of the most popular global sports.

Healthcare systems use artificial intelligence for disease prediction and medical diagnosis.

Stock markets depend on economic indicators and financial data analysis.
"""

chunks=splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print(f"\n----{i+1}----")
    print(chunk)