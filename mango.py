
from agents import AsyncOpenAI , OpenAIChatCompletionsModel,  Runner, Agent ,set_tracing_disabled
from rich import print
from dotenv import load_dotenv
import os



set_tracing_disabled(True)
load_dotenv()

key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")
print(key)
print(base_url)


Gemini_client = AsyncOpenAI(api_key = key ,base_url= base_url)
Model = OpenAIChatCompletionsModel(model = "gemini-2.5-flash", openai_client = Gemini_client)
agent = Agent(name = "waleed" ,
              instructions = "you are helpfull assistant ",
              model = Model)
res = Runner.run_sync(starting_agent = agent , input = "what is 2+18 = ?. give me answer in detail with emogis")
print(res.final_output)




