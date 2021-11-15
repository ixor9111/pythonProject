import Students


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def _mid_rating(self):
        mid_rating = 0
        amount_rating = 0

        for course in self.rating:
            for rating in self.rating[course]:
                mid_rating += int(rating)
                amount_rating += 1

        return mid_rating / amount_rating

    def __str__(self):
        str = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._mid_rating()}"
        return str

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._mid_rating() < other._mid_rating()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._mid_rating() <= other._mid_rating()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._mid_rating() == other._mid_rating()

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self._mid_rating() != other._mid_rating()

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self._mid_rating() >= other._mid_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Students.Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= int(grade) <= 10:
                if course in student.grades:
                    student.grades[course] += [int(grade)]
                else:
                    student.grades[course] = [int(grade)]
            else:
                return "Оценка может быть только в диапозоне 0 - 10"
        else:
            return 'Ошибка'

    def __str__(self):
        str = f"Имя: {self.name} \nФамилия: {self.surname}"
        return str
