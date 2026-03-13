def get_numeric_price(price_str):

    if not price_str:
        return float("inf")

    try:
        price = price_str.replace("₹", "").replace(",", "")
        return float(price)
    except:
        return float("inf")


def get_brand_score(title):

    title = title.lower()

    premium_brands = [
        "sony",
        "jbl",
        "bose",
        "sennheiser",
        "apple",
        "samsung",
        "realme",
        "oneplus",
        "vivo",
        "iqoo"
    ]

    mid_brands = [
        "boat",
        "noise",
        "oppo",
        "redmi",
        "poco"
    ]

    if any(b in title for b in premium_brands):
        return -2000

    if any(b in title for b in mid_brands):
        return -800

    return 0


def get_value_score(price):

    """
    Encourage mid-range products instead of always
    picking the cheapest item.
    """

    if price < 2000:
        return 500

    if 2000 <= price <= 10000:
        return -500

    if 10000 <= price <= 30000:
        return -1000

    return 0


def compare_products(products):

    best_product = None
    best_score = float("inf")

    for p in products:

        price = get_numeric_price(p["price"])

        brand_score = get_brand_score(p["title"])

        value_score = get_value_score(price)

        score = price + brand_score + value_score

        if score < best_score:
            best_score = score
            best_product = p

    reason = "✔ Best value considering price, brand reputation, and product value"

    return best_product, reason