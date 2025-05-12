# journal.py
from fastapi import HTTPException, Depends, Header
from pydantic import BaseModel
import datetime
from database import app, get_db

def get_current_user_id(x_user_id: int = Header(...)) -> int:
    return x_user_id

class JournalIn(BaseModel):
    title: str
    content: str

@app.get("/journals")
def list_journals(
    db=Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    owned = db.execute("SELECT * FROM journals WHERE owner_id = ?", (user_id,)).fetchall()
    shared = db.execute("""
      SELECT j.*, s.permission FROM journals j
      JOIN journal_shares s ON j.id = s.journal_id
      WHERE s.user_id = ?
    """, (user_id,)).fetchall()
    return {"owned": [dict(r) for r in owned], "shared": [dict(r) for r in shared]}

@app.post("/journals")
def add_journal(
    data: JournalIn,
    db=Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    db.execute("""
      INSERT INTO journals(owner_id,title,content,created_at)
      VALUES(?,?,?,?)
    """, (user_id, data.title, data.content, datetime.datetime.utcnow().isoformat()))
    db.commit()
    return {"msg": "Journal created"}

@app.get("/journals/{jid}")
def get_journal(
    jid: int,
    db=Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    row = db.execute("SELECT * FROM journals WHERE id = ?", (jid,)).fetchone()
    if not row:
        raise HTTPException(404, "Not found")
    return dict(row)

@app.put("/journals/{jid}")
def edit_journal(
    jid: int,
    data: JournalIn,
    db=Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    row = db.execute("SELECT owner_id FROM journals WHERE id = ?", (jid,)).fetchone()
    if not row or row["owner_id"] != user_id:
        raise HTTPException(403, "Forbidden")
    db.execute("""
      UPDATE journals SET title = ?, content = ?
      WHERE id = ?
    """, (data.title, data.content, jid))
    db.commit()
    return {"msg": "Updated"}

@app.delete("/journals/{jid}")
def delete_journal(
    jid: int,
    db=Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    row = db.execute("SELECT owner_id FROM journals WHERE id = ?", (jid,)).fetchone()
    if not row or row["owner_id"] != user_id:
        raise HTTPException(403, "Forbidden")
    db.execute("DELETE FROM journals WHERE id = ?", (jid,))
    db.commit()
    return {"msg": "Deleted"}
