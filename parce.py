

# Import necessary classes and functions from the specified modules
from llama_index import(
	GPTVectorStoreIndex,
	SimpleDirectoryReader,
	LLMPredictor,
	ServiceContext)
from langchain.chat_models import ChatOpenAI
import os


# Set the OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = "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"



# Set an environment variable to disable parallelism in tokenizers 
# (this is often done to avoid a specific warning message related to tokenizers)
os.environ['TOKENIZERS_PARALLELISM']='false'

# Load documents from the './data' directory using the SimpleDirectoryReader
# file_name = "user_documents/" + ask_files + '.pdf'

# documents = SimpleDirectoryReader(file_name).load_data()
documents = SimpleDirectoryReader('./user_documents').load_data()

# documents = ask_files.load_data()

# Define the model name to be used
modelName = "text-davinci-003"

# Initialize a predictor using the ChatOpenAI model with specified parameters
predictor=LLMPredictor(llm=ChatOpenAI(temperature=0,
                    model_name=modelName))
    
# Create a service context with default settings, specifying the predictor and chunk size
serv_context = ServiceContext.from_defaults(
    llm_predictor=predictor,
    chunk_size=600
    )

# Create an index using the GPTVectorStoreIndex. This index will represent the documents 
# in a format suitable for querying using the GPT model.
index=GPTVectorStoreIndex.from_documents(documents,
                        service_context=serv_context)

# Persist (save) the index data to the "./chunkstorage" directory
index.storage_context.persist(
    persist_dir="./chunkstorage")

# Print a message indicating where the modeled data has been saved
print("Written modeled data in ./chunkstorage folder")
