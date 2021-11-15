from Students import *
from Mentors import *


def course_mid_grades(list_students, course):
    amount_grades = 0
    mid_grades = 0

    for student in list_students:
        if not isinstance(student, Student): return "Ошибка, один из студенов не существует"
        if course not in (student.courses_in_progress or student.finished_courses):
            return "Ошибка, у 1го из студентов нету данного курса"

        for grade in student.grades[course]:
            amount_grades += 1
            mid_grades += int(grade)

    return mid_grades / amount_grades


def course_mid_lec_rating(list_lecturers, course):
    amount_ratings = 0
    mid_rating = 0

    for lector in list_lecturers:
        print(lector.rating)
        if not isinstance(lector, Lecturer): return "Ошибка, один из лекторов не существует"
        if course not in (lector.courses_attached and lector.rating):
            return "Ошибка, у 1го из лекторов нету данного курса или оценок по нему"

        for rating in lector.rating[course]:
            amount_ratings += 1
            mid_rating += int(rating)

    return mid_rating / amount_ratings


student1 = Student("Игорь", "Бутенко", "М")
student2 = Student("Астольфо", "ХЗ", "Трап")
lecturer1 = Lecturer("Роман", "Романов")
lecturer2 = Lecturer("Алексей", "Новиков")
reviewer1 = Reviewer("Анастасия", "Богданова")
reviewer2 = Reviewer("Франсуа де", "Николь")

student1.courses_in_progress += ['python']
student2.courses_in_progress += ['python']
reviewer1.courses_attached +=['python']
reviewer1.rate_hw(student1, "python", 10)
reviewer1.rate_hw(student1, "python", 10)
reviewer1.rate_hw(student1, "python", 10)
reviewer1.rate_hw(student2, "python", 10)
reviewer1.rate_hw(student2, "python", -1)

list_students = [student1, student2]

print(course_mid_grades(list_students, "python"))

lecturer1.courses_attached += ['python']
lecturer2.courses_attached += ['python']
student1.rate_lec(lecturer1, 'python', 7)
student1.rate_lec(lecturer1, 'python', 90)
student1.rate_lec(lecturer1, 'python', 9)
student1.rate_lec(lecturer2, 'python', 90)
student1.rate_lec(lecturer2, 'python', -6)

list_lecturers = [lecturer1, lecturer2]

print(course_mid_lec_rating(list_lecturers, "python"))