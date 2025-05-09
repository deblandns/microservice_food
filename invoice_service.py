import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InvoiceRequest(BaseModel):
    order_id: int

# database of invoices
invoices_db = {}

@app.post("/invoices/")
async def create_invoice(invoice_request: InvoiceRequest):
    # get the order detail from the service
    order_response = requests.get(f"http://127.0.0.1:8001/orders/{invoice_request.order_id}")

    # exception of order response
    if order_response == "404":
        raise HTTPException(status_code=404, detail="Order Not Found")
    
    order = order_response.json()["order"]

    # generate invoice for response 
    invoice = {
        "invoice_id": len(invoices_db) + 1,
        "order_id": invoice_request.order_id,
        "food_item": order["food_item"],
        "quantity": order["quantity"],
        "total_price": order["total_price"],
        "status": "Paid",
        "invoice_details": f"Invoice for {order['quantity']} x {order['food_item']} costing ${order['total_price']}"
    }
    invoices_db[invoice['invoice_id']] = invoice

    return {"invoice_id": invoice['invoice_id'], "invoice": invoice}


@app.get("invoices/{invoice_id}")
async def get_invoice(invoice_id: int):
    invoice = invoices_db.get(invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice Not Found")
    return {"invoice_id": invoice_id, "invoice": invoice_id}