from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import Tool
import os
load_dotenv()

def langchain_agent(user_question):
    llm = OpenAI(temperature = 0)
    tools = load_tools(["serpapi"], llm = llm, serpapi_api_key=os.getenv("SERPAPI_API_KEY")) ## uses SerpAI which takes the latest google search results
    prompt = """
You are a virtual chat bot assistant working for Morgan & Morgan, one of the largest law firms in the United States. 
Your role is to provide detailed information about anything related to the government, law, court proceedings, and other topics of that nature to clients. You will only be able to answer prompts related to the government, law, court proceedings, and other topics of that nature.
If you cannot answer a prompt in a germane manner and under the conditions I have listed for you, respond by saying that you are unable to answer it and that you need more details.


The following sentence will be your clients question.
Client: I have a question about depositions.

"""    
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    prompt = prompt.replace("I have a question about depositions.", f"Client: {user_question}")
    result = agent.run(prompt)
    return(str(result))


'''
def generate_law(paperwork):
    
    llm = OpenAI(temperature=0) ## temperature defines the creativity of the answers. 0=no creativity
    
    prompt_Template = PromptTemplate(
        input_variables=['paperwork'],
        template="I am a client involved in a legal case that wants to know what a {paperwork} is."
    )
    client_chain =LLMChain(llm=llm, prompt=prompt_Template)
    response = client_chain({'paperwork': paperwork})
    return response
'''

if __name__ == "__main__":
 
    langchain_agent("Are depositions hard?")



