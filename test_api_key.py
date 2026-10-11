import os
from openai import RateLimitError, OpenAI
from dotenv import load_dotenv


def check_ai_tokens():
    client = OpenAI()
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input="Hello"
        )
        print("API request successful")
        return True
    except RateLimitError:
        print("Rate limit or quota issue")
        return False

def check_api_key():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("API key loaded successfully!")
        return True

    else:
        print("API key not found!")
        return False

def system_check():
    if check_api_key() and check_ai_tokens():
        return
