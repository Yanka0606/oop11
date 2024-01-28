class Student:
    lst_all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.lst_all_students.append(self)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score(self.grades)}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @staticmethod
    def average_score(diction: dict, key=None) -> float:
        sum_of_marks = 0
        count_of_all_marks = 0
        if key is None:
            for i in diction:
                for j in diction[i]:
                    count_of_all_marks += 1
                    sum_of_marks += j
            return sum_of_marks / count_of_all_marks
        else:
            if key in diction:
                for i in diction[key]:
                    sum_of_marks += i
                return sum_of_marks / len(diction[key])
            else:
                return 0

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_score(self.grades) > other.average_score(other.grades)
        print('Невозможно сравнить!')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_score(self.grades) < other.average_score(other.grades)
        print('Невозможно сравнить!')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_score(self.grades) == other.average_score(other.grades)
        print('Невозможно сравнить!')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lst_all_lecturer = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lst_all_lecturer.append(self)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score(self.grades)}')

    @staticmethod
    def average_score(diction: dict, key=None) -> float:
        sum_of_marks = 0
        count_of_all_marks = 0
        if key is None:
            for i in diction:
                for j in diction[i]:
                    count_of_all_marks += 1
                    sum_of_marks += j
            return 0 if count_of_all_marks == 0 else sum_of_marks / count_of_all_marks
        else:
            if key in diction:
                for i in diction[key]:
                    sum_of_marks += i
                return 0 if len(diction[key]) == 0 else sum_of_marks / len(diction[key])
            else:
                return 0

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score(self.grades) > other.average_score(other.grades)
        print('Невозможно сравнить!')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score(self.grades) < other.average_score(other.grades)
        print('Невозможно сравнить!')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score(self.grades) == other.average_score(other.grades)
        print('Невозможно сравнить!')


class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# функция подсчета средней оценки студента по курсу

def average_score_all_students(lst_all_students: list, course: str) -> None:
    for student in lst_all_students:
        for name_of_course, marks in student.grades.items():
            if course == name_of_course:
                average = sum(marks) / len(marks)
                print(f"Студент: {student.name} {student.surname}\n"
                      f"Курс: {name_of_course}\n"
                      f"Cредняя оценка за домашние задания: {average}\n")


# функция подсчета средней оценки лектора по курсу
def average_score_all_lecturer(lst_all_lecturer: list, course: str) -> None:
    for lector in lst_all_lecturer:
        for name_of_course, marks in lector.grades.items():
            if course == name_of_course:
                average = sum(marks) / len(marks)
                print(f"Лектор: {lector.name} {lector.surname}\n"
                      f"Курс: {name_of_course}\n"
                      f"Cредняя оценка за лекции: {average}\n")


# Создаем 3 экземпляра класса Student

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

best_student2 = Student('Vasiliy', 'Ivanov', 'your_gender')
best_student2.finished_courses += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.grades['Git'] = [10, 8, 6, 10, 9]
best_student2.grades['Python'] = [9, 10, 7]

best_student3 = Student('Ivan', 'Lysenkov', 'your_gender')
best_student3.finished_courses += ['Введение в программирование']
best_student3.courses_in_progress += ['Git']
best_student3.grades['Git'] = [5, 8, 6, 7, 9]
best_student3.grades['Python'] = [10, 10, 9]

# Вывод информации по студентам

print(f'Студент {best_student.name} {best_student.surname}')
print(f'окончил курс: {best_student.finished_courses}')
print(f'в данный момент изучает: {best_student.courses_in_progress}')
print(f'оценки по всем курсам: {best_student.grades}')

print(f'Студент {best_student2.name} {best_student2.surname}')
print(f'окончил курс: {best_student2.finished_courses}')
print(f'в данный момент изучает: {best_student2.courses_in_progress}')
print(f'оценки по всем курсам: {best_student2.grades}')

print(f'Студент {best_student3.name} {best_student3.surname}')
print(f'окончил курс: {best_student3.finished_courses}')
print(f'в данный момент изучает: {best_student3.courses_in_progress}')
print(f'оценки по всем курсам: {best_student3.grades}')

# Создаем 3 экземпляра класса Lecturer

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Ivan', 'Pronin')
cool_lecturer2.courses_attached += ['Git']

cool_lecturer3 = Lecturer('Sergey', 'Barabanov')
cool_lecturer3.courses_attached += ['Введение в программирование']
cool_lecturer3.courses_attached += ['Git']

# Вывод информации по лекторам

print(f'Лектор {cool_lecturer.name} {cool_lecturer.surname} '
      f'читает лекции на курсе: {cool_lecturer.courses_attached}')
print(
    f'Лектор {cool_lecturer2.name} {cool_lecturer2.surname} '
    f'читает лекции на курсе: {cool_lecturer2.courses_attached}')
print(
    f'Лектор {cool_lecturer3.name} {cool_lecturer3.surname} '
    f'читает лекции на курсе: {cool_lecturer3.courses_attached}')

# Создаем 3 экземпляра класса Reviewer

cool_reviewer = Reviewer('John', 'Smith')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Evgeniy', 'Vasin')
cool_reviewer2.courses_attached += ['Git']

cool_reviewer3 = Reviewer('Dmitriy', 'Bagin')
cool_reviewer3.courses_attached += ['Введение в программирование']

# Вывод информации по экспертам

print(
    f'Эксперт {cool_reviewer.name} {cool_reviewer.surname} '
    f'проверяет работы на курсе: {cool_reviewer.courses_attached}')
print(
    f'Эксперт {cool_reviewer2.name} {cool_reviewer2.surname} '
    f'проверяет работы на курсе: {cool_reviewer2.courses_attached}')
print(
    f'Эксперт {cool_reviewer3.name} {cool_reviewer3.surname} '
    f'проверяет работы на курсе: {cool_reviewer3.courses_attached}')

# Выставляем оценки студентам

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer2.rate_hw(best_student2, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'Git', 10)
cool_reviewer3.rate_hw(best_student3, 'Python', 10)
cool_reviewer2.rate_hw(best_student3, 'Git', 10)

# Вывод измененных оценок студентов

print(f'Студенту {best_student.name} {best_student.surname} выставили новые оценки: {best_student.grades}')
print(f'Студенту {best_student2.name} {best_student2.surname} выставили новые оценки: {best_student2.grades}')
print(f'Студенту {best_student3.name} {best_student3.surname} выставили новые оценки: {best_student3.grades}')

# Студенты пытаются выставить оценки лекторам

best_student.rate_lectur(cool_lecturer, 'Python', 10)
best_student.rate_lectur(cool_lecturer, 'Python', 5)
best_student2.rate_lectur(cool_lecturer, 'Python', 9)
best_student2.rate_lectur(cool_lecturer, 'Python', 8)
best_student.rate_lectur(cool_lecturer, 'Git', 10)
best_student.rate_lectur(cool_lecturer, 'Git', 5)
best_student2.rate_lectur(cool_lecturer, 'Git', 9)
best_student2.rate_lectur(cool_lecturer, 'Git', 8)
best_student.rate_lectur(cool_lecturer2, 'Python', 10)
best_student.rate_lectur(cool_lecturer2, 'Python', 5)
best_student2.rate_lectur(cool_lecturer2, 'Python', 9)
best_student2.rate_lectur(cool_lecturer2, 'Python', 8)
best_student.rate_lectur(cool_lecturer2, 'Git', 10)
best_student.rate_lectur(cool_lecturer2, 'Git', 5)
best_student2.rate_lectur(cool_lecturer2, 'Git', 9)
best_student2.rate_lectur(cool_lecturer2, 'Git', 8)

# Вывод информации об оценках лекторов

print(f'Лектор {cool_lecturer.name} {cool_lecturer.surname} имеет оценки: {cool_lecturer.grades}')
print(f'Лектор {cool_lecturer2.name} {cool_lecturer2.surname} имеет оценки: {cool_lecturer2.grades}')
print(f'Лектор {cool_lecturer2.name} {cool_lecturer3.surname} имеет оценки: {cool_lecturer3.grades}')

# Вывод информации с использованием метода __str__ в классах

print(best_student)
print(best_student2)
print(best_student3)

print(cool_reviewer)
print(cool_reviewer2)
print(cool_reviewer3)

print(cool_lecturer)
print(cool_lecturer2)
print(cool_lecturer3)

# Сравнение студентов и лекторов

if best_student > best_student2:
    print(f'Средняя оценка студента {best_student.name} {best_student.surname} '
          f'выше в сравнении с {best_student2.name} {best_student2.surname}')
elif best_student < best_student2:
    print(f'Средняя оценка студента {best_student.name} {best_student.surname} '
          f'ниже в сравнении с {best_student2.name} {best_student2.surname}')
else:
    print(f'Средняя оценка студента {best_student.name} {best_student.surname} '
          f'равна средней с {best_student2.name} {best_student2.surname}')

if cool_lecturer > cool_lecturer2:
    print(f'Средняя оценка лектора {cool_lecturer.name} {cool_lecturer.surname} '
          f'выше в сравнении с {cool_lecturer2.name} {cool_lecturer2.surname}')
elif cool_lecturer < cool_lecturer2:
    print(f'Средняя оценка лектора {cool_lecturer.name} {cool_lecturer.surname} '
          f'ниже в сравнении с {cool_lecturer2.name} {cool_lecturer2.surname}')
else:
    print(f'Средняя оценка лектора {cool_lecturer.name} {cool_lecturer.surname} '
          f'равна средней с {cool_lecturer2.name} {cool_lecturer2.surname}')

# Средние оценки за домашние задания студентов и за лекции по конкретным курсам

print(average_score_all_students(Student.lst_all_students, 'Python'))
print(average_score_all_lecturer(Lecturer.lst_all_lecturer, 'Python'))



