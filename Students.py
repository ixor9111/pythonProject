from Mentors import *


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, score):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 <= int(score) <= 10:
                if course in lecturer.rating:
                    lecturer.rating[course] += [int(score)]
                else:
                    lecturer.rating[course] = [int(score)]
            else:
                return 'Ошибка, оценка может быть в границах 0 - 10'
        else:
            return 'Ошибка'

    def _mid_grades(self):
        mid_grades = 0
        amount_grades = 0

        for course in self.grades:
            for rating in self.grades[course]:
                mid_grades += int(rating)
                amount_grades += 1
        if amount_grades != 0:
            return mid_grades / amount_grades
        else:
            return 0

    def __str__(self):
        str = f"Имя: {self.name} \nФамилия: {self.surname} \n" \
              f"Средняя оценка за домашнее задание: {self._mid_grades()} \n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"

        return str

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._mid_grades() < other._mid_grades()

    def __le__(self, other):
        if isinstance(other, Student):
            return self._mid_grades() <= other._mid_grades()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._mid_grades() == other._mid_grades()

    def __ne__(self, other):
        if isinstance(other, Student):
            return self._mid_grades() != other._mid_grades()

    def __ge__(self, other):
        if isinstance(other, Student):
            return self._mid_grades() >= other._mid_grades()
