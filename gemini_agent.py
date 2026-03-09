from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_best_product(product):

    prompt = f"""
    A user is shopping online.

    Recommended product:
    Name: {product['title']}
    Price: {product['price']}
    Store: {product['store']}

    Explain briefly why this product is a good recommendation.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text