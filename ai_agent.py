from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# AI PRODUCT RECOMMENDATION
def choose_best_product(products):

    product_text = ""

    for i, p in enumerate(products, 1):
        product_text += f"""
{i}. {p['title']}
Price: {p['price']}
Rating: {p.get('rating','N/A')}
Store: {p['store']}
"""

    prompt = f"""
You are an expert AI shopping assistant.

Compare the following products and decide which one is the BEST option.

Consider:
- product rating
- brand reputation
- product quality
- value for money
- price

Products:
{product_text}

Return exactly in this format:

Winner: <product name>

Reason: <short explanation>
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# AI CHAT ASSISTANT
def shopping_chat(question, products):

    product_context = ""

    for p in products:
        product_context += f"""
Product: {p['title']}
Price: {p['price']}
Rating: {p.get('rating','N/A')}
Store: {p['store']}
"""

    prompt = f"""
You are an AI shopping assistant.

Available products:

{product_context}

User question:
{question}

Answer the question using the product information above.
If the information is not available, politely say you don't have that data.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content