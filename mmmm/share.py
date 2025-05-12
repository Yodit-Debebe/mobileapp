# share.py
from fastapi import HTTPException, Depends
from pydantic import BaseModel
from database import app, get_db

class ShareIn(BaseModel):
    email: str
    permission: str  # "view" or "edit"

# stub: look up user_id by email
def lookup_user_id(email: str, db) -> int:
    row = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
    if not row:
        raise HTTPException(404, "User not found")
    return row["id"]

@app.post("/journals/{jid}/share")
def share_journal(jid: int, data: ShareIn, db=Depends(get_db)):
    uid = lookup_user_id(data.email, db)
    db.execute("""
      INSERT INTO journal_shares(journal_id,user_id,permission)
      VALUES(?,?,?)
    """, (jid, uid, data.permission))
    db.commit()
    return {"msg": "Shared"}

# You dont have a way to revoke permission in the front-end, So this is disabled currently
# @app.delete("/journals/{jid}/share")
# def revoke_share(jid: int, data: ShareIn, db=Depends(get_db)):
#     uid = lookup_user_id(data.email, db)
#     res = db.execute("""
#       DELETE FROM journal_shares
#       WHERE journal_id = ? AND user_id = ?
#     """, (jid, uid))
#     if res.rowcount == 0:
#         raise HTTPException(404, "Share not found")
#     db.commit()
#     return {"msg": "Access revoked"}
