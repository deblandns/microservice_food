from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    email: str


# user memory database
users_db = {}


@app.post("/users/")
async def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = user
    return {"user_id": user_id, "user": user}



@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")

    return {"user_id": user_id, "user": user}