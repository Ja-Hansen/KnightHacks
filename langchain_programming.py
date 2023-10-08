from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

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

def langchain_agent():
    llm = OpenAI(temperature = 0)
    tools = load_tools(["google-search"], llm = llm, google_cse_id="AIzaSyAb4woDoe0I8d1gpL1TrBf-Tc0abPMClak")
    prompt_Template = PromptTemplate(
        input_variables=[],
        template="You are designed to be a friendly and consise chatbox that is under a company called Morgan&Morgan, which is Americas' largest law firm. You are required to answer questions from clients who need assistance with law firm proceedings."
    )
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    question = "How challenging is a deposition?"
    prompt = prompt_Template.format(question)
    result = agent.run(prompt)
    print(result)
if __name__ == "__main__":
 
    langchain_agent()