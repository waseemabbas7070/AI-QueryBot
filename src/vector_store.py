from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4

def create_vector_store(texts):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
    
    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )
    
    uuids = [str(uuid4()) for _ in range(len(texts))]
    vector_store.add_documents(documents=texts, ids=uuids)
    
    return vector_store.as_retriever(search_kwargs={"k": 4})