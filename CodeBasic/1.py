import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from langchain_core.prompts import PromptTemplate

load_dotenv()
GeminiApiKey = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GeminiApiKey)

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1, 
    max_tokens=None,
    timeout=None,
)

prompt_template_name = PromptTemplate(
    input_variables = ['cusinie'],
    template = 'I want to open a resturate for my {cusinie} food. Suggest fency name for this'
)
# print(prompt_template_name.format(cusinie='Indian'))

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
            f.write()
            print(block.get('text'))
        else:
            print(block)
else:
    print(ai_msg.content)