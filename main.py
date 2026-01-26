
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from supabase import create_client

db = create_client("https://dhikypixwsvfxzfcgdjw.supabase.co", "sb_publishable_aEWNWDnikMA0k6qOPnEEeg_4kniO_qF")


app = FastAPI(title= "MET Bank")

@app.get("/books")
def all_books():
    mgs = db.table("books").select("*").execute()
    return  mgs

@app.post("/books")    
async def book_added(request : Request):
    data=await request.json()
    mgs = db.table("books").insert(data).execute()
    return {"message":"our book is added"}





