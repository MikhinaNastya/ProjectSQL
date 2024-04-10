from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base, engine

class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='class_')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_id = Column(Integer, ForeignKey('class.id'))
    class_ = relationship('Class', back_populates='students')
    grades = relationship('Grades', back_populates='student')


class Grades(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='grades')
    grade = Column(Integer)

Base.metadata.create_all(engine)