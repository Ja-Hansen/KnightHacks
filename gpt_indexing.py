
from llama_index import (
    StorageContext,
    load_index_from_storage,
)
from llama_index.query_engine import RetrieverQueryEngine
import time
import os

    
# Set environment variables
os.environ["OPENAI_API_KEY"] = "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"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Number of chunks you would like to use for an answer.
# Set to 1 to save money.
k = 3
# Rebuild storage context from the chunk storage
storage_context = StorageContext.from_defaults(persist_dir="./chunkstorage")

# Load index
loadedIndex = load_index_from_storage(storage_context)


timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename = "Llama" + timestamp + ".txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("User: Welcome to OpenAI chat!\n\n")

user_input = lit.text_input("Enter your prompt:")
if lit.button("Submit"):
    user_input = user_input.strip()
    if user_input == "":
        lit.warning("Please enter a prompt.")
    else:
        response = loadedIndex.as_retriever().query(user_input)

        lit.text("\nAI says:")
        lit.text(response)

        with open(filename, "a") as f:
            f.write("User:\n" + user_input + "\n\n")
            f.write("AI:\n" + str(response) + "\n\n")

lit.text("Thanks for using our chatbot!")


    
        
        # Check if the folder exists; if not, create it
