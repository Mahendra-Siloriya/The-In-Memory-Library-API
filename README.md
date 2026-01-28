# The In-Memory Library API

## 1. Project Title & Goal
A REST API built using Flask that manages a library book inventory using strictly in-memory storage (no database).

---

## 2. Setup Instructions

### Step 1: Install dependencies
pip install flask

Step 2: Run the application
flask --app app.py --debug

Step 3: Base URL
http://127.0.0.1:5000

3. The Logic (How I Thought)

Why did I choose this approach?

Flask was chosen because it is lightweight and easy to understand for building REST APIs.
The problem required in-memory storage, so a Python dictionary was used to store book data.
Each book is uniquely identified using its id, making retrieval and deletion fast.

What was the hardest bug you faced, and how did you fix it?

I faced a 415 Unsupported Media Type error while adding books.
The issue was caused by missing Content-Type: application/json and an empty request body in Postman.
I fixed it by correctly sending JSON using Body → raw → JSON in Postman.

4. Output Screenshots (Postman Proof)
Add Book – POST /addbooks
![Add Book Screenshot]([screenshots/post_add_books.png](https://github.com/Mahendra-Siloriya/The-In-Memory-Library-API/blob/9066dce5262bdce2c0ded0eaf18b4913d89ed483/screenshots/post_add_books.png.png))


Get Book by ID – GET /books/{id}
![GET Book By ID Screenshot](screenshots/get_book_by_id.png)

Search Books by Year – GET /books/search?year=2024
![Search Book By Year Screenshot](screenshots/get_books_by_year)

Delete Book – DELETE /books/{id}
![Delete Book By ID Screenshot](screenshots/delete_book_by_id.png)


Delete Book (Not Found Case)
![Deleted Book Not Found Screenshot](screenshots/deleted_book_not_found.png)


These screenshots prove that the API works correctly using in-memory data.

5. Future Improvements (If I Had 2 More Days)

Add database support (MySQL) for persistence
Add update book endpoint (PUT)
Add authentication for secure access

