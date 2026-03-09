import streamlit as st
import pandas as pd
from product_search import search_products
from compare import compare_products

st.set_page_config(page_title="AI Shopping Agent")

st.title("🛒 AI E-Commerce Product Discovery Agent")


# SESSION STATE
if "cart" not in st.session_state:
    st.session_state.cart = []

if "products" not in st.session_state:
    st.session_state.products = []


# SEARCH PRODUCT
query = st.text_input("Search for a product")

if st.button("Search"):

    if not query:
        st.warning("Please enter a product name")

    else:

        products = search_products(query)

        if not products:
            st.error("No products found")
        else:
            st.session_state.products = products


# DISPLAY PRODUCTS
if st.session_state.products:

    st.subheader("Products Found")

    for i, p in enumerate(st.session_state.products):

        cols = st.columns([1,2])

        with cols[0]:
            if p["image"]:
                st.image(p["image"], width="stretch")

        with cols[1]:

            st.write("###", p["title"])
            st.write("💰 Price:", p["price"])
            st.write("🏬 Store:", p["store"])

            col1, col2 = st.columns(2)

            # BUY NOW
            with col1:
                if p["link"]:
                    st.markdown(
                        f'<a href="{p["link"]}" target="_blank">🛒 Buy Now</a>',
                        unsafe_allow_html=True
                    )

            # ADD TO CART
            with col2:
                if st.button("Add to Cart", key=i):
                    st.session_state.cart.append(p)
                    st.success("Added to cart!")

        st.write("---")


# PRODUCT COMPARISON TABLE
if st.session_state.products:

    st.subheader("📊 Product Comparison Table (Low → High Price)")

    comparison_data = []

    for p in st.session_state.products:

        try:
            numeric_price = int(p["price"].replace("₹","").replace(",",""))
        except:
            numeric_price = 999999999

        comparison_data.append({
            "Product": p["title"],
            "Price": p["price"],
            "Store": p["store"],
            "Product Link": p["link"],
            "price_value": numeric_price
        })

    df = pd.DataFrame(comparison_data)

    # SORT BY PRICE
    df = df.sort_values(by="price_value")

    # REMOVE HELPER COLUMN
    df = df.drop(columns=["price_value"])

    st.data_editor(
        df,
        column_config={
            "Product Link": st.column_config.LinkColumn(
                "Product Link",
                help="Click to open product page"
            )
        },
        hide_index=True,
        width="stretch"
    )


# BEST PRODUCT RECOMMENDATION
if st.session_state.products:

    best_product, reason = compare_products(st.session_state.products)

    if best_product:

        st.subheader("⭐ Best Product Recommendation")

        cols = st.columns([1,2])

        with cols[0]:
            if best_product["image"]:
                st.image(best_product["image"], width="stretch")

        with cols[1]:

            st.write("###", best_product["title"])
            st.write("💰 Price:", best_product["price"])
            st.write("🏬 Store:", best_product["store"])

            st.success(reason)


# CART SIDEBAR
st.sidebar.title("🛒 Cart")

if not st.session_state.cart:

    st.sidebar.write("Cart is empty")

else:

    total_price = 0

    for idx, item in enumerate(st.session_state.cart):

        st.sidebar.write(f"**{item['title']}**")
        st.sidebar.write(item["price"])

        try:
            price_value = int(item["price"].replace("₹","").replace(",",""))
            total_price += price_value
        except:
            pass

        if st.sidebar.button("Remove", key=f"remove{idx}"):

            st.session_state.cart.pop(idx)
            st.rerun()

        st.sidebar.write("---")

    st.sidebar.write(f"### Total Items: {len(st.session_state.cart)}")
    st.sidebar.write(f"### Total Price: ₹{total_price}")