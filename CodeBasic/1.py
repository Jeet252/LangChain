import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from langchain_core.prompts import PromptTemplate

load_dotenv()



model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7, 
    max_tokens=None,
    timeout=None,
)

prompt_template_name = PromptTemplate(
    input_variables = ['cusinie'],
    template = 'I want to open a resturate for my {cusinie} food. Suggest fency name for this, only one name'
)

messages = [
    (
        "human",
        prompt_template_name.format(cusinie='Indian')
    )
]

ai_msg = model.invoke(messages)

# Extract and print only the text content of the response
if isinstance(ai_msg.content, list):
    for block in ai_msg.content:
        if isinstance(block, dict) and block.get('type') == 'text':
            print(block.get('text'))
        else:
            print(block)
else:
    print(ai_msg.content)