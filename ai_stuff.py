#import openai
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key="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", model="gpt-4")
'''
# Initialize the OpenAI API with your API key
openai.api_key = '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'

def chat_with_gpt():
    print("Chat with GPT-4! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Use the OpenAI API to get a response from GPT-4
        response = openai.Completion.create(
            engine="davinci",  # Use the "davinci" engine, which is the most capable
            prompt=user_input,
            max_tokens=30  # Limit the response to 150 tokens
        )
        print(f"GPT-4: {response.choices[0].text.strip()}")

if __name__ == "__main__":
    chat_with_gpt()
'''

