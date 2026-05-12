# starter-code.py
# Assignment: Building REST APIs with FastAPI
# Use this file as your starting point. Fill in the TODO sections to complete the assignment.

# Install dependencies first:
#   pip install fastapi uvicorn pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create the FastAPI app instance
app = FastAPI()

# In-memory list to store student records
students = [
    # TODO: Add at least 3 hardcoded students here, each with id, name, and grade
]


# TODO: Define a Pydantic model for a Student with fields: id (int), name (str), grade (str)
class Student(BaseModel):
    pass


# TODO: Implement GET / — return a welcome message as JSON
@app.get("/")
def root():
    pass


# TODO: Implement GET /students — return the full list of students
@app.get("/students")
def get_students():
    pass


# TODO: Implement GET /students/{student_id} — return the student with the matching id
#       Return HTTP 404 if the student is not found
@app.get("/students/{student_id}")
def get_student(student_id: int):
    pass


# TODO: Implement POST /students — accept a Student body and add it to the list
@app.post("/students")
def create_student(student: Student):
    pass


# Run the app with:
#   uvicorn starter-code:app --reload --port 8000
