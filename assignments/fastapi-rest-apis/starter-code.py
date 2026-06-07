from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

users: List[User] = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
    User(id=3, name="Charlie", email="charlie@example.com"),
]

@app.get("/", response_model=dict)
def root():
    return {"message": "FastAPI user directory is running."}

@app.get("/users", response_model=List[User])
def list_users(domain: Optional[str] = None):
    if domain:
        return [user for user in users if user.email.endswith(domain)]
    return users

@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    next_id = max([existing.id for existing in users], default=0) + 1
    new_user = User(id=next_id, name=user.name, email=user.email)
    users.append(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Run this app with:
# uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
