from fastapi import Body, FastAPI # import FastAPI, ... from fastapi module

app = FastAPI() # acknowledge the creation of a FastAPI instance

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
]

@app.get("/books") # annotation to let FastAPI know that path will be going to be returning follow method ← request URL: 127.0.0.1:8000/books
async def read_all_books(): # create a python async function which stands for asynchronous dev. 'async' keyword is optional, not necessary.
    return BOOKS



@app.get("/books/{book_title}") # `path parameter` to get specific book by title
async def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].lower() == book_title.lower():
            return book


@app.get("/books/") # `query parameter` to get books by category    
async def read_category_by_query(category: str): 
    books_to_return = []
    for book in BOOKS:
        if book.get('category').lower() == category.lower():
            books_to_return.append(book)
    return books_to_return


# Assignment: get books by author using `query parameter`
@app.get("/books/byauthor/")
async def read_author_by_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').lower() == author.lower():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/") # multiple `path` and `query parameters` to get books by author and category
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').lower() == book_author.lower() and \
            book.get('category').lower() == category.lower():
            books_to_return.append(book)

    return books_to_return


# Assignment: get books by author using only path parameter
@app.get("/books/byauthor/{author}") # get books by author using only path parameter
async def read_author_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').lower() == author.lower():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book") # create a new book using POST method
async def create_book(new_book=Body()): # GET method cannot hold Body() data, so we use POST method here
    BOOKS.append(new_book)


@app.put("/books/update_book") # update an existing book using PUT method
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').lower() == updated_book.get('title').lower():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}") # delete a book using DELETE method
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').lower() == book_title.lower():
            BOOKS.pop(i)
            break



# To run the app, use the command: uvicorn books:app --reload
# where:
# - app: the name of FastAPI instance
# - books: the name of the file (without .py extension) where app is defined
# - --reload: makes the server restart after code changes (useful for development)
#---------------------------------------------------------------
# Swagger UI documentation (integrated in FastAPI) will be available at: http://localhost:8000/docs for interactive API exploration.
#---------------------------------------------------------------
# Stop at: "\06. Project 2 - Move Fast with FastAPI\1. Books 2 Project Overview.mp4"