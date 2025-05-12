# auth.py
from fastapi import HTTPException, Depends
from pydantic import BaseModel
import hashlib, datetime
from database import app, get_db

def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

class Signup(BaseModel):
    email: str
    username: str
    password: str
    confirm_password: str

class Signin(BaseModel):
    email: str
    password: str

class Reset(BaseModel):
    email: str
    new_password:str

@app.post("/auth/signup")
def signup(data: Signup, db=Depends(get_db)):
    if data.password != data.confirm_password:
        raise HTTPException(400, "Passwords do not match")
    cur = db.execute("SELECT id FROM users WHERE email = ?", (data.email,))
    if cur.fetchone():
        raise HTTPException(400, "Email already registered")
    db.execute(
      "INSERT INTO users(email,username,password,created_at) VALUES(?,?,?,?)",
      (data.email, data.username, hash_pw(data.password), datetime.datetime.utcnow().isoformat())
    )
    db.commit()
    return {"msg": "User created"}
@app.post("/auth/signin")
def signin(data: Signin, db=Depends(get_db)):
    pw = hash_pw(data.password)
    cur = db.execute("SELECT id FROM users WHERE email = ? AND password = ?", (data.email, pw))
    row = cur.fetchone()
    if not row:
        raise HTTPException(401, "Invalid credentials")
    return {"msg": "Signed in", "user": row["id"]}

@app.post("/auth/password-reset")
def reset_password(data: Reset, db=Depends(get_db)):
    cur = db.execute("SELECT id FROM users WHERE email = ?", (data.email,))
    if not cur.fetchone():
        raise HTTPException(404, "User not found")
    new_pw = hash_pw(data.new_password)
    db.execute("UPDATE users SET password = ? WHERE email = ?", (new_pw, data.email))
    db.commit()
    return {"msg": "Sucess"}
