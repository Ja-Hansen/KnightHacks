from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain


load_dotenv()

def generate_law(paperwork):
    
    llm = OpenAI(temperature=0) ## temperature defines the creativity of the answers. 0=no creativity
    
    prompt_Template = PromptTemplate(
        input_variables=['paperwork'],
        template="I am a client involved in a legal case that wants to know what a {paperwork} is."
    )
    client_chain =LLMChain(llm=llm, prompt=prompt_Template)
    response = client_chain({'paperwork': paperwork})
    return response

if __name__ == "__main__":
 
   paper = input("Hello! Which document would you like to ")
   print(generate_law("deposition"))