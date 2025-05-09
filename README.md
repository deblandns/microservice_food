# 🍽️ Microservices-Based Food Ordering System (Python + FastAPI)

This is a simple microservice-based application built using **FastAPI** that demonstrates how to structure microservices in Python.

## 🧩 Project Overview

The system consists of three independent microservices:

1. **User Service** - Manages user information.
2. **Order Service** - Allows users to place food orders.
3. **Invoice Service** - Generates invoices based on food orders.

Each service is isolated, runs independently, and communicates with others via REST APIs.

---

## 🚀 Microservices Breakdown

### 1. 👤 User Service
- Endpoint to **create** a user.
- Endpoint to **get** a user by ID.

### 2. 🛒 Order Service
- Accepts orders from users for food items.
- Validates that the user exists via a request to User Service.
- Calculates total price = quantity × price.

### 3. 🧾 Invoice Service
- Generates invoices from order data.
- Fetches order details from Order Service.

---

## 📦 Tech Stack

- **Python 3.8+**
- **FastAPI** for building APIs
- **Uvicorn** as ASGI server
- **Requests** library for inter-service communication

---

## 🔧 Setup & Running the Services

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-microservices-food-order.git
cd fastapi-microservices-food-order


## for installing the fastapi uvicorn and requests
pip install fastapi uvicorn requests


## run the service 
uvicorn user_service:app --reload --port 8000


## run the order 
uvicorn order_service:app --reload --port 8001


## run the invoice
uvicorn invoice_service:app --reload --port 8002


1. to create the user 

post request: POST http://127.0.0.1:8000/users/
{
  "name": "John Doe",
  "email": "john@example.com"
}



2. Place an Order request: POST http://127.0.0.1:8001/orders/

{
  "user_id": 1,
  "food_item": "Pizza",
  "quantity": 2,
  "price": 12.5
}


3. Generate an Invoice: POST http://127.0.0.1:8002/invoices/
{
  "order_id": 1
}


Folder Structure

project/
├── user_service.py       # User microservice
├── order_service.py      # Order microservice
├── invoice_service.py    # Invoice microservice
└── README.md