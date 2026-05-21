# Advanced Chain
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7, 
    max_tokens=None,
    timeout=None,
)

parser = RunnablePassthrough()

summary_prompt = PromptTemplate(template="Summarize {news}")
translate_prompt = PromptTemplate(template="Translate this summary to Hindi: {summary}")

chain = (
    {"summary": summary_prompt | llm | parser} # Step 1: Create summary
    | translate_prompt                            # Step 2: Pass summary to next prompt
    | llm                                       # Step 3: Run model again
    | parser                                      # Step 4: Final string output
)

response = chain.invoke({"news": """Two weeks after swearing-in, Tamil Nadu Chief Minister Joseph Vijay expanded his cabinet today by inducting 23 new MLAs. The newly sworn-in cabinet members include 21 lawmakers from Vijay's own Tamilaga Vettri Kazhagam (TVK) party and two from ally Congress.

Chief Minister Vijay had initially taken the oath of office alongside nine ministers from his own party, the TVK. Following the latest expansion, the Chief Minister allocated portfolios to the newly inducted ministers while also tweaking several responsibilities that had been assigned during the initial swearing-in.

With this expansion, the Congress party marks its return to the Tamil Nadu cabinet after nearly six decades. The entry follows party president Mallikarjun Kharge's approval of two Congress MLAs, Rajesh Kumar and P Vishwanathan, for ministerial roles.

The political shift comes after the Congress contested the Tamil Nadu assembly elections in alliance with the DMK, which was voted out after just one term. Actor-turned-politician Vijay's TVK, launched in February 2024, emerged as the single-largest party but fell 10 seats short of a majority in the 234-member assembly.

Seeking to bridge the gap, Vijay secured Congress' support on the condition that "communal forces" be kept out of the alliance. The alliance was further strengthened when the Viduthalai Chiruthaigal Katchi (VCK) and the Left parties extended their backing, pushing the TVK-led coalition comfortably past the majority mark."""})


# print(response)


if isinstance(response.content, list):
    for block in ai_msg.content:
        if isinstance(block, dict) and block.get('type') == 'text':
            print(block.get('text'))
        else:
            print(block)
else:
    print(response.content)