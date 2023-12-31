from llama_index import(
    StorageContext,
    load_index_from_storage)
from llama_index.query_engine import RetrieverQueryEngine
import time
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['TOKENIZERS_PARALLELISM']='false'

# Number of chunks you would like to use for an answer.
# Set to 1 to save money.
k=3

# Rebuild storage context from the chunkstorage
storage_context = StorageContext.from_defaults(persist_dir='./chunkstorage')
 
# Load index
loadedIndex = load_index_from_storage(storage_context)
# loadedIndex._service_context.llm_predictor.llm.model_name="text-davinci-003"


retriever = loadedIndex.as_retriever()
# retriever.similarity_top_k=k

# Construct the query engine based on the retriever,
# and response_mode.
query_engine = RetrieverQueryEngine.from_args(
    retriever=retriever,
    response_mode= 'compact'
)

timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename ="Llama"+timestamp + ".txt"

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("User: Welcome to OpenAI chat!\n\n")

while (True):
    p=input("Enter quit to quit, or enter your prompt: ")
    p=p.strip()
    if (p==""):
        continue
    if (p=="quit"):
        break

    response = query_engine.query(p)    
    
    print("\nAI says:\n", response, "\n\n")

    with open(filename, 'a') as f:
        f.write("User:\n" + p + "\n\n")
        f.write("AI:\n" + str(response) + "\n\n")

print("Thank you for using us!")