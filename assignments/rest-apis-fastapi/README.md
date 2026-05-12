# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to build a REST API using the FastAPI framework in Python, practicing route creation, request handling, and returning JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description

Create a basic FastAPI application with a root endpoint and at least one additional route that returns structured data as a JSON response.

#### Requirements

Completed program should:

- Install and import `fastapi` and `uvicorn`
- Define a FastAPI app instance
- Implement a `GET /` route that returns a welcome message, e.g.:

```json
{ "message": "Welcome to the Student API!" }
```

- Implement a `GET /students` route that returns a hardcoded list of at least 3 students, each with `id`, `name`, and `grade` fields
- Run the app using `uvicorn` on port `8000`

### 🛠️ Add Create and Retrieve Endpoints

#### Description

Extend the API to allow creating a new student record and retrieving a single student by their ID.

#### Requirements

Completed program should:

- Define a `Student` model using `pydantic` with fields: `id` (int), `name` (str), and `grade` (str)
- Implement a `POST /students` route that accepts a JSON body and adds the student to the in-memory list
- Implement a `GET /students/{student_id}` route that returns the student with the matching `id`
- Return a `404` response with an error message if the student is not found, e.g.:

```json
{ "detail": "Student not found" }
```

- Demonstrate all endpoints using example requests in comments or a separate test block
