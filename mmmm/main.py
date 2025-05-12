# main.py
from fastapi import FastAPI
import uvicorn

import auth
import journal
import share

app = FastAPI()

# ── AUTH ENDPOINTS ───────────────────────────────────────────
app.post("/auth/signup", tags=["Auth"])(auth.signup)
app.post("/auth/signin", tags=["Auth"])(auth.signin)
app.post("/auth/password-reset", tags=["Auth"])(auth.reset_password)

# ── JOURNAL CRUD ENDPOINTS ───────────────────────────────────
app.get("/journals", tags=["Journals"])(journal.list_journals)
app.post("/journals", tags=["Journals"])(journal.add_journal)
app.get("/journals/{jid}", tags=["Journals"])(journal.get_journal)
app.put("/journals/{jid}", tags=["Journals"])(journal.edit_journal)
app.delete("/journals/{jid}", tags=["Journals"])(journal.delete_journal)

# ── SHARING ENDPOINTS ────────────────────────────────────────
app.post("/journals/{jid}/share", tags=["Sharing"])(share.share_journal)
# app.delete("/journals/{jid}/share", tags=["Sharing"])(share.revoke_share)
#app.get("/journals/{jid}/share", tags=["Sharing"])(share.list_shares)

