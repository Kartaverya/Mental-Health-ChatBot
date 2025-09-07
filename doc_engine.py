import os 
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv 

load_dotenv() 
llama_llm = LlamaOpenAI(model="gpt-3.5-turbo",api_key=os.getenv("OPENAI_API_KEY"))

PERSIST_DIR="index_storage"

if os.path.exists(PERSIST_DIR):
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index=load_index_from_storage(storage_context)

else:    
    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)    
query_engine = index.as_query_engine(llm=llama_llm)

def query_documents(user_query: str)-> str:
    return str(query_engine.query(user_query))
