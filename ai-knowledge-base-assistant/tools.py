from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.tools import Tool

import os

# Load and embed docs
def load_and_embed_docs():
    # Load PDFs & text files
    loader = DirectoryLoader('data', glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(splits, embeddings)
    
    os.makedirs("vector_store", exist_ok=True)
    vector_store.save_local("vector_store")
    return f"Loaded {len(splits)} text chunks and created vector index."

def ask_knowledge_base(query: str):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("vector_store", embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    answer = "No answer found."
    sources = ""
    if docs:
        combined = "\n".join([doc.page_content for doc in docs])
        answer = f"Found answer based on docs:\n{combined[:500]}..."
        sources = ", ".join(set([doc.metadata.get('source', '') for doc in docs]))

    return f"Answer: {answer}\nSources: {sources}"

tools = [
    Tool(name="load_docs",
         func=load_and_embed_docs,
         description="Load and embed company documents for question answering."),
    Tool(name="ask_knowledge_base",
         func=ask_knowledge_base,
         description="Ask a question to the knowledge base built from loaded documents.")
]
