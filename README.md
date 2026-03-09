# 🛒 AI E-Commerce Product Discovery Agent

An AI-powered web application that helps users **discover, compare, and select the best products across multiple e-commerce platforms** based on price and availability.

The system searches products in real-time, displays product details, allows users to add items to a cart, and generates a **comparison table to help users choose the best product**.

Built using **Python, Streamlit, and external product APIs**, this project demonstrates how AI-assisted tools can improve online shopping decisions.

---

# 🚀 Features

### 🔍 Product Search

Users can search for products such as:

Laptop under 70000
Mobile under 20000
Headphones under 5000

The system retrieves relevant products from multiple platforms.

---

### 🖼 Product Display

Each product displays:

* Product image
* Product title
* Price
* Store name
* Buy Now link to the actual product page

---

### 🛒 Add to Cart

Users can add products to a shopping cart.

The cart sidebar displays:

* Selected products
* Total number of items
* Total price
* Remove item option

---

### 📊 Product Comparison Table

The system generates a **comparison table sorted by price (Low → High)** to help users analyze products quickly.

The table includes:

* Product Name
* Price
* Store
* Clickable Product Link

---

### ⭐ Best Product Recommendation

The system automatically recommends the **best product** based on pricing and availability.

Example recommendation:

⭐ Best Product Recommendation
Lenovo 14" Intel Core i5 Laptop
Reason: Lowest price among available products.

---

# 🧠 System Workflow

1. User enters a product query
2. Application fetches product data from APIs
3. Products are displayed with details
4. Users can add products to cart
5. Products are compared in a price table
6. System recommends the best option

---

# 🏗 Project Structure

```
ecommerce-agent/
│
├── app.py              # Main Streamlit application
├── product_search.py   # Fetches product data from API
├── compare.py          # Logic for product comparison
├── requirements.txt    # Python dependencies
├── .env                # API keys (not uploaded to GitHub)
└── README.md           # Project documentation
```

---

# ⚙️ Technologies Used

* Python
* Streamlit
* Pandas
* REST APIs
* RapidAPI / Product APIs

---

# 📦 Installation

### 1️⃣ Clone the repository

git clone https://github.com/your-username/ecommerce-agent.git

cd ecommerce-agent

---

### 2️⃣ Create virtual environment

python -m venv venv

Activate environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

### 4️⃣ Add API Keys

Create a `.env` file and add your API keys:

RAPIDAPI_KEY=your_api_key_here

---

### 5️⃣ Run the application

streamlit run app.py

---

# 📷 Application Preview

Main Interface:

* Product search
* Product display cards
* Add to cart option

Comparison Section:

* Product comparison table
* Best product recommendation

Cart Sidebar:

* Added products
* Total price calculation

---

# 🎯 Future Improvements

* AI-based product recommendation using LLMs
* Price drop alerts
* User preference filters (budget, brand, RAM, etc.)
* Product rating analysis
* Multi-platform price tracking

---

# 📌 Use Cases

* Smart shopping assistant
* Price comparison tool
* E-commerce analytics platform
* AI-powered buying advisor

---

# 👩‍💻 Author

**Chandrika Bezawada**
B.Tech – Artificial Intelligence & Machine Learning

---

# ⭐ If you like this project

Please give this repository a **star on GitHub ⭐**
