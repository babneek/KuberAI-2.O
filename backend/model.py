# model.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not found in environment variables.")

# Initialize OpenAI client with OpenRouter endpoint
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"  # OpenRouter endpoint
)

def get_llm_response(query: str) -> str:
    """
    Query OpenRouter LLM with user input.
    """
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  # Changed to Mistral model
            messages=[
                {"role": "system", "content": "You are Kuber AI, a financial assistant that only answers about gold investment."},
                {"role": "user", "content": query}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
