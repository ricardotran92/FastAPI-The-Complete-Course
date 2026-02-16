# Terminology

IDE: Intergated Development Environment (e.g. Visual Studio Code)
FastAPI: framework
Uvicorn: web server to run FastAPI
Pydantics: python library that is used for data modeling, data parsing, and has efficient error handling
BaseModel: pydantics model
** operator will pass the key/value from BookRequest() into the Book() constructor


---
## CRUD to HTTP Mapping

Imagine you are managing a list of "Products" on a website. The base endpoint (**API Endpoint**) would likely be `/api/products`.

| CRUD     | HTTP Method | Endpoint (URL)      | Result                                 |
| ---------- | ----------- | ------------------- | -------------------------------------- |
| **Create** | `POST`      | `/api/products`     | Adds a new product to the database.    |
| **Read**   | `GET`       | `/api/products/123` | Retrieves details for product ID 123.  |
| **Update** | `PUT`       | `/api/products/123` | Replaces the info for product 123.     |
| **Delete** | `DELETE`    | `/api/products/123` | Removes product 123 from the database. |

---

### The "Restaurant" Analogy

To make this more grounded, imagine you're at a restaurant:

1. **The Menu (Endpoint):** This is the list of things you can interact with.
2. **The Request (HTTP Method):** You telling the waiter what to do with a menu item (Order it, ask what's in it, or change your order).
3. **The Server:** The kitchen that processes your request and sends back a response (your food or a "Sold Out" message).

---

URL

```plaintext
%20 = space
```

# 08. Setup Database

## SQLite3

Go to: https://www.sqlite.org/download.html
Go to Precompiled Binaries for Windows
Select and download `sqlite-tools-win-x64-<version>.zip`
Extract to: C:\Program Files\sqlite
Open Environmental Properties, by typing: 🪟 + `ENV`
Environment Variables > System variables > Path > New > paste: `C:\Program Files\sqlite`.
Check 1st priorty path: 
```bash
$ where sqlite3
C:\Program Files\sqlite\sqlite3.exe
C:\adb-fastboot\platform-tools\sqlite3.exe
```

### Setting up todos.db


```bash
$sqlite3 todos.db
```

```sql
.schema
insert into todos(title, description, priority, complete) values ('Go the store', 'Pick up eggs', 5, False);
select * from todos;
insert into todos(title, description, priority, complete) values ('Cut the lawn', 'Grass is getting long', 3, False);
select * from todos;
insert into todos(title, description, priority, complete) values ('Feed the dog', 'he is getting hungry', 5, False);
.mode column
select * from todos;
.mode markdown 
select * from todos;
.mode box
select * from todos;
.mode table
select * from todos;
insert into todos(title, description, priority, complete) values ('Test element', 'He is getting hungry', 5, False);
delete from todos where id = 4;
select * from todos;
insert into todos(title, description, priority, complete) values ('A new test element', 'He is getting hungry', 5, False);
select * from todos;
delete from todos where id = 4;
select * from todos;
```

## Alembic

|Alembic Command|Details|
|---|---|
|alembic init <folder name>|Initializes a new, generic environment|
|alembic revision -m <message>|Creates a new revision of the environment|
|alembic upgrade <revision #>|Run our upgrade migration to our database|
|alembic downgrade -1| Run our downgrade migration to our database|