from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def create_chat_chain(retriever):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        api_key='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'
    )
    
    prompts = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant for question answering task.
        Use the following retrieved context to generate answer. Keep it short and concise.
        If you do not find anything from the context then just say I do not know
        \n\n {context}"""),
        ("human", "{input}")
    ])
    
    q_chain = create_stuff_documents_chain(llm, prompts)
    return create_retrieval_chain(retriever, q_chain)