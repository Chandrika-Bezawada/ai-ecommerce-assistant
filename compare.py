def get_numeric_price(price_str):

    if not price_str:
        return float("inf")

    try:
        price = price_str.replace("₹", "").replace(",", "")
        return float(price)
    except:
        return float("inf")


def compare_products(products):

    best_product = None
    best_score = float("inf")

    for p in products:

        price = get_numeric_price(p["price"])

        score = price

        if score < best_score:
            best_score = score
            best_product = p

    reason = "✔ Lowest price among the available products"

    return best_product, reason