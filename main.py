from sqlalchemy.sql import func
from models import Student, Class, Grades
from crud import create_class, create_student, create_grades
from database import Session

if __name__ == "__main__":
    with Session() as session:
        # Создание класса
        new_class = create_class(
            session=session,
            id=3,
            name="11В"
        )
        session.commit()

        # Создание студента
        new_student = create_student(
            session=session,
            id=10,
            name="Соболев",
            class_id=1
        )
        session.commit()

        # Создание оценки
        new_grade = create_grades(
            session=session,
            id=10,
            student_id=10,
            grade=10
        )
        session.commit()

       # Средняя оценка учеников
        avg_student_grade = session.query(func.avg(Grades.grade)).scalar()
        print("Средняя оценка учеников:", avg_student_grade)

        # Средняя оценка класса
        avg_class_grade = session.query(func.avg(Grades.grade)).join(Student).filter(Student.class_id == class_.id).scalar()
        print("Средняя оценка класса:", avg_class_grade)

        # Топ-3 учеников по оценкам
        top_students = session.query(Student).order_by(Grades.grade.desc()).limit(3).all()
        print("Топ-3 учеников:")
        for student in top_students:
            print(student.name, "-", session.query(func.avg(Grades.grade)).filter(Grades.student_id == student.id).scalar())

        # Топ-3 классов по оценкам
        top_classes = session.query(Class).join(Student).join(Grades).group_by(Class.id).order_by(
            func.avg(Grades.grade).desc()).limit(3).all()
        print("Топ-3 классов:")
        for class_ in top_classes:
            print(class_.name, "-",
                  session.query(func.avg(Grades.grade)).join(Student).filter(Student.class_id == class_.id).scalar())

        session.close()

