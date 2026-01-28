
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from supabase import create_client

db = create_client("https://dhikypixwsvfxzfcgdjw.supabase.co", "sb_publishable_aEWNWDnikMA0k6qOPnEEeg_4kniO_qF")


app = FastAPI(title= "library management system")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Library Management System API"}

@app.get("/books")
async def get_books():
    books =db.table("books").select("*").execute()
    return books.data() 

@app.get("/books/{book_id}")
async def get_book(book_id: int):    
    book=db.table("books").select("*").eq("id", book_id).execute()
    if not book.data():
        return JSONResponse(status_code=404, content={"message": "Book not found"})
    return book.data()

@app.post("/books")
async def create_book(book: dict):
    new_book = db.table("books").insert(book).execute()
    return new_book.data()

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: dict):
    updated_book = db.table("books").update(book).eq("id", book_id).execute()
    if not updated_book.data():
        return JSONResponse(status_code=404, content={"message": "Book not found"})
    return updated_book.data()

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    deleted_book = db.table("books").delete().eq("id", book_id).execute()
    if not deleted_book.data():
        return JSONResponse(status_code=404, content={"message": "Book not found"})
    return {"message": "Book deleted successfully"}

@app.get("/authors")
async def get_authors():
    authors =db.table("authors").select("*").execute()
    return authors.data()   

@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    author=db.table("authors").select("*").eq("id", author_id).execute()
    if not author.data():
        return JSONResponse(status_code=404, content={"message": "Author not found"})
    return author.data()

@app.post("/authors")
async def create_author(author: dict):
    new_author = db.table("authors").insert(author).execute()
    return new_author.data()

@app.put("/authors/{author_id}")
async def update_author(author_id: int, author: dict):
    updated_author = db.table("authors").update(author).eq("id", author_id).execute()
    if not updated_author.data():
        return JSONResponse(status_code=404, content={"message": "Author not found"})
    return updated_author.data()

@app.delete("/authors/{author_id}")
async def delete_author(author_id: int):
    deleted_author = db.table("authors").delete().eq("id", author_id).execute()
    if not deleted_author.data():
        return JSONResponse(status_code=404, content={"message": "Author not found"})
    return {"message": "Author deleted successfully"}








