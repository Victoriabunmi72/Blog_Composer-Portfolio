import openai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


class OpenAIService:
    def generate_article(self, keyword: str) -> str:
        openai.api_key = api_key
        user_prompt = keyword
        chat_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="You are an expert writer and a blogger, \
            you can write a very comprehensive article on any \
            words passed as prompt" + "\n" + user_prompt,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.73,
            presence_penalty=0
        )
        generated_article = chat_response['choices'][0]['text'].replace(
            "?", "")

        return generated_article
