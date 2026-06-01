from fastapi import FastAPI, HTTPException

app = FastAPI()

products = []
customers = []
orders = []

@app.get("/")
def root():
    return {"message":"Inventory Management API"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: dict):
    for p in products:
        if p["sku"] == product["sku"]:
            raise HTTPException(400,"SKU already exists")
    products.append(product)
    return product

@app.get("/customers")
def get_customers():
    return customers

@app.post("/customers")
def add_customer(customer: dict):
    customers.append(customer)
    return customer

@app.get("/orders")
def get_orders():
    return orders

@app.post("/orders")
def add_order(order: dict):
    orders.append(order)
    return order
