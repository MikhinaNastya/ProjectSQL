from database import Session
from models import Student, Class, Grades

def create_class(
        session: Session,
        id: int,
        name: str
):
    new_class = Class(
        id=id,
        name=name
    )
    session.add(new_class)
    return new_class

def create_student(
        session: Session,
        id: int,
        name: str,
        class_id: int
):
    new_student = Student(
        id=id,
        name=name,
        class_id=class_id
    )
    session.add(new_student)
    return new_student

def create_grades(
        session: Session,
        id: int,
        student_id: int,
        grade: int,
):
    new_grade = Grades(
        id=id,
        student_id=student_id,
        grade=grade
    )
    session.add(new_grade)
    return new_grade