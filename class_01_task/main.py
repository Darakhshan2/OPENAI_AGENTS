from agents import Agent, Runner

from connection import config

translator_agent= Agent(
    name = "Translator-Agent",
    instructions = "Translate the given text from english language to urdu language"
)

input_value_user = input("Enter the text you want to translate: ")

result = Runner.run_sync(translator_agent,
                         input_value_user,
                         run_config=config)
print(f"Translated text: {result.final_output}")