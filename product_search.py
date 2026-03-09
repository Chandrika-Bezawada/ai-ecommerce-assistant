import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://real-time-product-search.p.rapidapi.com/search-v2"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}


def search_products(query):

    params = {
        "q": query,
        "country": "in",
        "language": "en"
    }

    response = requests.get(URL, headers=HEADERS, params=params)

    data = response.json()

    products = []

    items = data.get("data", {}).get("products", [])

    for p in items[:8]:

        title = p.get("product_title")

        price = p.get("offer", {}).get("price")

        photo = None
        if p.get("product_photos"):
            photo = p["product_photos"][0]

        store = p.get("offer", {}).get("store_name")

        link = p.get("offer", {}).get("offer_page_url")

        if not link:
            link = p.get("product_page_url")

        products.append({
            "title": title,
            "price": price,
            "image": photo,
            "store": store,
            "link": link
        })

    return products