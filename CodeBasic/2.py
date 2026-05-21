import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7, 
    max_tokens=None,
    timeout=None,
)

prompt = PromptTemplate(
    template = 'I want to open a resturate for my {cusinie} food. Suggest fency name for this, only one name'
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"cusinie": "Indian"})
print(result)

