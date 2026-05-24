import json
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

load_dotenv()

DEMO_WORDS = [
  "PIXEL", "SPACE", "SHARK", "BRAIN", "FLAME", "PLANT", "GHOST", "MAGIC", "STARS", 
  "CLOCK", "STORM", "HEART", "MUSIC", "OCEAN", "DREAM", "CHESS", "RIVER", "FAIRY", 
  "SNAKE", "BREAD", "LEMON", "CANDY", "FRUIT", "CLOUD", "LIGHT", "SOUND", "EARTH", 
  "GLASS", "STONE", "GRASS", "SWEET", "SHINE", "BLADE", "DANCE", "TIGER", "WATER", 
  "SMILE", "LUNCH", "MOUNT", "GREEN", "WHITE", "BLACK", "SMOKE", "WAVES", "CROWN", 
  "PEARL", "BRUSH", "HOUSE", "SHIRT", "CHAIR"
]

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7, 
    max_tokens=None,
    timeout=None,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are the "Hint Master," a clever and helpful assistant for a 5-letter word guessing game. Your job is to provide a single, cryptic but helpful hint for a specific secret word without ever revealing the word itself.
Rules for Hint Generation:
1. Do not mention the secret word in your response.
2. Do not use the secret word's root or any variations of it.
3. Provide exactly one sentence.
4. Focus the hint on the word's definition, a common association, a synonym, or a situational context where the word is used.
5. Keep it fun and slightly challenging—don't make it too easy."""),
    ("human", "{word}"),
])

parser = StrOutputParser()

chain = prompt | model | parser


all_words =[]
while len(all_words) < len(DEMO_WORDS):
    try:
        print(f"generating hints for {DEMO_WORDS[len(all_words)]} {len(all_words)} / {len(DEMO_WORDS)}")
        hint = chain.invoke({"word": DEMO_WORDS[len(all_words)]})
        word_data = {'word': DEMO_WORDS[len(all_words)], 'hint': hint}
        all_words.append(word_data)
        with open('word.json', 'w') as f:
            json.dump(all_words, f, indent=4)
        if len(all_words) == len(DEMO_WORDS):
            break
    except ChatGoogleGenerativeAIError as e:
        print("\n⚠️ Rate limit hit! Waiting 15 seconds for the 1-minute window to clear...")
        print("waiting for 200 second")
        time.sleep(200)
        print("waiting for another 200 second")
        time.sleep(200)
        print("waiting is complete")

    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        break

with open('word.json', 'w') as f:
    json.dump(all_words, f, indent=4)