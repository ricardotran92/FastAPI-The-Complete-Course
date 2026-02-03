## 04. FastAPI Setup & Installation

Once you create a Virtual Environment do you need to activate the environment before use?
→ *Yes*

What is a Python Virtual Environment?
→ *An environment that is isolated from other Python environments on your machine.*

---

## 05. Project 1 - FastAPI Request Method Logic

What is a query parameter?
→ *Sort and filter through data that is not marked by a path parameter*

Which is the proper way to create a Path Parameter in FastAPI?
→ *@app.get(“/user/{user_id}”)*

What is a path parameter?
→ *Variables that are part of the API URL*

Path parameter APIs should be placed before Query parameter APIs.

---

## 06. Project 2 - Move Fast with FastAPI

What is Pydantic?
→ *Pydantic is used for data parsing and data validation*

What is the purpose of model_config within our class BookRequest(BaseModel)?
→ *To create a more descriptive request within our Swagger documentation*

Status Codes:
- 1xx → Information Response: Request Processing.
- 2xx → Success: Request Successfully complete
  + 200: OK → Standard Response for a Successful Request. Commonly used for successful Get requests when data is being returned.
  + 201:    → The request has been successful, creating a new resource. Used when a POST creates an entity.
  + 204: No → The request has been successful, did not create an entity nor return anything. Commonly used with PUT requests.
- 3xx → Redirection: Further action must be complete
- 4xx → Client Errors: An error was caused by the client.
  + 400: Bad → Cannot process request due to client error. Commonly used for invalid request methods.
  + 401: Unauthorized → Client does not have valid authentication for target resource
  + 404: Not → The clients requested resource can not be found
  + 422: Unprocessable Entity → Semantic Errors in Client Request
- 5xx → Server Errors: An error occurred on the server.
  + 500: Internal Server Error → Generic Error Message, when an unexpected issue on the server happened.

How to specify a successful status code will be returned in FastAPI?
→ *@app.get(“/”, status_code=status.HTTP_201_CREATED)*


## 09. API Request Methods

What is Depends() in FastAPI?
→ *A way to declare things that are required for the application/function to work by injecting the dependencies*

## 11. Authenticate Requests

What is a JWT made up of?
→ *All of the above*

What does JWT stand for?
→ *JSON Web Token*

JWT is used when:
→ *Sending Authorization / Information Exchange*

