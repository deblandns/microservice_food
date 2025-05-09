import requests
import time

# create new user for users section
# create a new user
response = requests.post(url="http://127.0.0.1:8000/users/", json={"name": "hossein", "email": "hoseinnysyan1385@gmail.com"})
print(response.json())


time.sleep(1)
# get the user data from api
response_get_user = requests.get(url=f"http://127.0.0.1:8000/user/{1}")
print(response_get_user.json())


time.sleep(1)
# place the order
response_place_order = requests.post(url="http://127.0.0.1:8001/orders/", json={"user_id": 1, "food_item": "Pizza", "quantity": 2, "price": 10.5})
print(response_place_order.json())


time.sleep(1)
# generate the invoice
invoice_generator = requests.post(url="http://127.0.0.1:8002/invoices/", json={"order_id": 1})
print(invoice_generator.json())