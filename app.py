import streamlit as st
import pandas as pd
import time
from product_search import search_products
from ai_agent import choose_best_product, shopping_chat

st.set_page_config(page_title="AI Shopping Agent")

st.title("🛒 AI E-Commerce Product Discovery Agent")

# SESSION STATES
if "cart" not in st.session_state:
    st.session_state.cart = []

if "products" not in st.session_state:
    st.session_state.products = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# PRODUCT SEARCH
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


# DISPLAY PRODUCTS (GRID STYLE)
if st.session_state.products:

    st.subheader("Products Found")

    cols = st.columns(3)  # 3 products per row

    for i, p in enumerate(st.session_state.products):

        with cols[i % 3]:

            if p["image"]:
                st.image(p["image"], width="stretch")

            st.write("###", p["title"])
            st.write("💰 Price:", p["price"])
            st.write("⭐ Rating:", p.get("rating","N/A"))
            st.write("🏬 Store:", p["store"])

            if p["link"]:
                st.markdown(
                    f'<a href="{p["link"]}" target="_blank">🛒 Buy Now</a>',
                    unsafe_allow_html=True
                )

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
            "Rating": p.get("rating","N/A"),
            "Store": p["store"],
            "Product Link": p["link"],
            "price_value": numeric_price
        })

    df = pd.DataFrame(comparison_data)

    df = df.sort_values(by="price_value")

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


# AI RECOMMENDATION
if st.session_state.products and len(st.session_state.products) >= 3:

    st.subheader("⭐ AI Best Product Recommendation")

    top_products = st.session_state.products[:3]

    with st.spinner("AI analyzing products..."):

        ai_result = choose_best_product(top_products)

    st.info("🤖 AI Decision")
    st.write(ai_result)


# 💬 AI CHAT ASSISTANT
if st.session_state.products:

    st.subheader("💬 AI Shopping Assistant")

    # Display previous chat messages
    for chat in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(chat["user"])

        with st.chat_message("assistant"):
            st.write(chat["ai"])

    # Chat input
    user_question = st.chat_input("Ask something about the products...")

    if user_question:

        with st.chat_message("user"):
            st.write(user_question)

        with st.spinner("AI thinking..."):

            answer = shopping_chat(
                user_question,
                st.session_state.products
            )

        # Typing animation
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            typed_text = ""

            for char in answer:
                typed_text += char
                message_placeholder.markdown(typed_text)
                time.sleep(0.01)

        st.session_state.chat_history.append(
            {"user": user_question, "ai": answer}
        )


# CART SIDEBAR
st.sidebar.title("🛒 Cart")

if not st.session_state.cart:

    st.sidebar.write("Cart is empty")

else:

    total_price = 0

    for idx,item in enumerate(st.session_state.cart):

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