import requests
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


app = FastAPI()

class FoodOrder(BaseModel):
    user_id: int
    food_item: str
    quantity: int
    price: float


# database order database
orders_db = {}

@app.post("/orders/")
async def create_order(order: FoodOrder):
    # get the user data from userservice 
    user_response = requests.get(f"http://127.0.0.1:8000/user/{order.user_id}")

    if user_response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")

    # calculate total price of it
    total_price = order.quantity * order.price
    order_id = len(orders_db) + 1
    orders_db[order_id] = {"user_id": order.user_id, "food_item": order.food_item, "quantity": order.quantity, "total_price": total_price, "status": "Pending"}
    return {"order_id": order_id, "user": user_response.json(), "order": orders_db[order_id]}


# get the status and details of each order
@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    order = orders_db.get(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order Not Found")

    return {"order_id": order_id, "order": order}