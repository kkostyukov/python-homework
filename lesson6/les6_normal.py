# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Human:
    def __init__(self, last_name, first_name, middle_name=None):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def fio(self):
        return " ".join([x for x in [self.last_name, self.first_name, self.middle_name] if x])


class Teacher(Human):
    def __init__(self, lesson: str, last_name, first_name, middle_name=None):
        self.lesson = lesson
        super().__init__(last_name, first_name, middle_name)

class SuperTEacher(Teacher):
    def __init__(self, lesson: str, last_name, first_name, middle_name=None, param=None):
        self.par = param
        super().__init__(lesson, last_name, first_name, middle_name)


class Group:

    def __init__(self, name):
        self.name = name
        self._teachers = []

    def add_teacher(self, teacher: Teacher):
        self._teachers.append(teacher)

    def get_lessons(self):
        return {x.lesson for x in self._teachers}

    def get_teachers(self):
        return self._teachers


class Student(Human):
    def __init__(self, group: Group, first_name, father: Human,
                 mother: Human):
        self.group = group
        self.father = father
        self.mother = mother
        super().__init__(father.last_name, first_name, father.first_name)

    def get_lessons(self):
        return self.group.get_lessons()


class School:
    def __init__(self):
        self.students = set()

    def add_student(self, student: Student):
        self.students.add(student)

    def get_all_groups(self):
        return {x.group for x in self.students}

    def get_student_by_group(self, group: Group):
        return [x for x in self.students if x.group == group]


if __name__ == '__main__':
    math_teacher = Teacher("Math", "George", "Cantor")
    phisics_teacher = Teacher("Phisics", "Issak", "Newton")
    enaglisg_teaher = Teacher("English", "Ball", "Sara")

    group_5a = Group("5A")
    group_5a.add_teacher(math_teacher)
    group_5a.add_teacher(enaglisg_teaher)

    group_6B = Group("6B")
    group_6B.add_teacher(phisics_teacher)
    group_6B.add_teacher(enaglisg_teaher)

    f1 = Human("Osborne", "Frank")
    m1 = Human("Osborne", "Kelley")

    f2 = Human("Shepherd", "John")
    m2 = Human("Shepherd", "Lucy")

    student1 = Student(group_6B, "Michael", f1, m1)
    student2 = Student(group_5a, "Christopher", f1, m1)
    student3 = Student(group_6B, "Mary", f2, m2)
    student4 = Student(group_5a, "Harvey", f2, m2)
    student5 = Student(group_5a, "Ruth", f2, m2)

    school = School()
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_student(student4)
    school.add_student(student5)

    for group in school.get_all_groups():
        print(group.name)

    for student in school.get_student_by_group(group_5a):
        print(student.fio())

    for lesson in student1.get_lessons():
        print(lesson)

    print(student2.father.fio())
    print(student2.mother.fio())

    for teacher in group_5a.get_teachers():
        print(teacher.fio())
