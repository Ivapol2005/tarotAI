# interpreter.py

import os
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv(os.path.join(os.path.dirname(__file__), '../../config/.env'))

endpoint = "https://models.github.ai/inference"
model_name = "meta/Meta-Llama-3.1-8B-Instruct"
token = os.environ["IVAPOL_LLM_API"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_tarot_interpretation(spread_description: str) -> str:
    try:
        response = client.complete(
            messages=[
                SystemMessage("""
You are an expert Tarot reader. Provide:
    1. Concise symbolic interpretation
    2. Practical advice
    3. Psychological insights
Use 3-5 sentences maximum.
                """),
                UserMessage(f"Analyze this spread:\n{spread_description}")
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=500,
            model="meta/Meta-Llama-3.1-8B-Instruct"
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error getting interpretation: {str(e)}"


# print(response.choices[0].message.content)
