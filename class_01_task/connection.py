from agents import  OpenAIChatCompletionsModel ,AsyncOpenAI , RunConfig
from dotenv import load_dotenv
import os 

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Gemini api key is not accessable")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",    
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client = external_client
)
config= RunConfig(
    model = model,
    model_provider=external_client,
   
)
