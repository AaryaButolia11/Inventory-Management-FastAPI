# Inventory Manager

A simple **Inventory Management Web App** built with **React** on the frontend and **FastAPI** on the backend.  
This project was my first experience learning **FastAPI**, and it demonstrates basic CRUD operations (Create, Read, Update, Delete) for managing products.

<img width="1542" height="892" alt="image" src="https://github.com/user-attachments/assets/6ff4a9bb-38a0-4748-9c51-e0f3b7a3cc4b" />

---

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [FastAPI Basics Learned](#fastapi-basics-learned)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)

---

## Project Description

This project is a basic inventory management system that allows users to:

- Add new products
- View a list of products
- Edit existing products
- Delete products
- Filter and sort products by ID, name, price, and quantity

The frontend is built with **React**, including features like form validation, search, sorting, and auto-dismiss messages.  
The backend is built with **FastAPI** and uses **SQLAlchemy** with PostgreSQL for database management.

---

## Features

- Full **CRUD operations** for products
- **Search** by product ID, name, or description
- **Sorting** by ID, name, price, or quantity
- Responsive UI with **React**
- Auto-dismiss **success/error messages**
- Persistent storage with **PostgreSQL** and **SQLAlchemy**
- CORS enabled for local frontend-backend communication

---

## Technologies Used

- **Frontend:** React, CSS  
- **Backend:** FastAPI, Python, SQLAlchemy  
- **Database:** PostgreSQL  
- **Other:** Axios for HTTP requests  

---

## Setup Instructions

### Backend (FastAPI)

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
2. Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlalchemy psycopg2 pydantic

3. Set up PostgreSQL and configure your database in database.py.

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload


5. Open API docs at http://localhost:8000/docs

Frontend (React)

1. Navigate to the frontend folder:
    ```bash
    cd frontend


2. Install dependencies:
    ```bash
    npm install


3. Start the React app:
    ```bash
    npm start


4. The app should open at http://localhost:3000

## FastAPI Basics Learned

Creating a FastAPI app: app = FastAPI()

Defining routes: @app.get(), @app.post(), @app.put(), @app.delete()

Request validation: Using Pydantic models for request data

Dependency Injection: Using Depends() to manage DB sessions

CORS Middleware: To allow requests from React frontend

CRUD with SQLAlchemy: Creating, reading, updating, and deleting database records

Automatic API docs: Available at /docs with Swagger UI

## API Endpoints
Method-Endpoint-Description
GET	/products	Get all products
GET	/products/{id}	Get a product by ID
POST	/products	Add a new product
PUT	/products	Update an existing product
DELETE	/products	Delete a product by ID
Screenshots

<img width="1896" height="1007" alt="image" src="https://github.com/user-attachments/assets/ba0c6c6a-d2c8-4292-a424-ce2eae652a3f" />

List of products with sorting and search
<img width="872" height="531" alt="image" src="https://github.com/user-attachments/assets/23a88791-483f-448c-a095-260eeaa17f87" />


Form to add or edit a product
<img width="862" height="338" alt="image" src="https://github.com/user-attachments/assets/be92e23c-317c-4f69-935f-70d5b8e6777f" />
<img width="861" height="597" alt="image" src="https://github.com/user-attachments/assets/751f5160-2ef0-40fc-a48c-5e0da2c817d6" />


Success message after CRUD operations
<img width="1401" height="1022" alt="image" src="https://github.com/user-attachments/assets/88409f7e-91ac-4542-917a-3db067a7fde1" />
<img width="867" height="876" alt="image" src="https://github.com/user-attachments/assets/a5c53b4f-c671-4e1d-8b87-9521298496ee" />

Database - PostgreSQL
<img width="1918" height="1142" alt="image" src="https://github.com/user-attachments/assets/cbc08214-8382-4237-9dd1-a82bddcd011d" />


## This project was a great hands-on introduction to FastAPI, React, and building full-stack web applications.
