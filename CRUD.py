from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    age:int
    course:str

student_db =[]

#CRUD = CREATE READ UPDATE DELETE

#create - add new student
@app.post("/student")
def create_student(student:Student):
    for s in student_db:
        if s.id == student.id:
            raise HTTPException(400, "Student already exists")
    

    student_db.append(student)
    return{"message": "student added sucessfully" , "student":student}

#GET ALL STUDENT
@app.get("/student")
def get_all_student():
    return student_db

# READ - Get single student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for s in students_db:
        if s.id == student_id:
            return s
    raise HTTPException(404, "Student not found")


# UPDATE - Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    for i, s in enumerate(students_db):
        if s.id == student_id:
            students_db[i] = updated
            return {"message": "Student updated", "student": updated}
    raise HTTPException(404, "Student not found")


# DELETE - Remove student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students_db):
        if s.id == student_id:
            students_db.pop(i)
            return {"message": "Student deleted"}
    raise HTTPException(404, "Student not found")