class Student:
  def __init__(self, name, surname, gender, finished_courses, courses_in_progress, grades, grades_lecturer):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.grades_lecturer = {}
  def rate_hww(self, lecturer, course, grade):
      if isinstance(lecturer, lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __init__(self, midl):
      self.midl_grade_st = self.grades = {} / n

  def __str__(self):
      print(f"Имя: {self.name}, Фамилия: {self.surname},{self.midl_grade_st}, {self.courses_in_progress}, {self.finished_courses}")


  def add_courses(self, course_name):
      self.finished_courses.append(course_name)


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.name = name
        self.surname = surname


    def __init__(self, midl):
        self.midl_grade_le = self.grades = {}/len(self.grades)

    def __str__(self):
        print(f"Имя: {self.name}, Фамилия: {self.surname},{self.midl_grade_le} ")
class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
      print(f"Имя: {self.name}, Фамилия: {self.surname} ")


def __it__(self, midl_grade):
    self.get_avg() <midl_grade.get_avg()
    return self.grades<midl_grade.grades


Student1 = Student["Anna","Andreeva","girl"]
Student1.courses_in_progress = ["Python", "1c"]
Lecturer1 = Lecturer["Boris", "Ivanov"]
Lecturer.grades = ["10", [9]]
Reviewer1 = Reviewer["Oleg", "Petrov"]
Reviewer.courses_attached = ["Python", "1c"]


print(self.midl_grade_le.__it__(self.midl_grade_st))


