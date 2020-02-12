class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        print('{}正在愉快的玩耍'.format(self._name))

    def watch_av(self):
        if self._age >= 18:
            print('{}正在观看动作片'.format(self._name))
        else:
            print('{}只能观看熊出没'.format(self._name))

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    def study(self, course):
        print('{}的{}正在学习{}'.format(self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print('{}{}正在讲{}'.format(self._name, self._title, course))


def main():
    stu = Student("王大锤", 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('杨京辉', 100, '运维狗')
    t.teach('猫和老鼠')
    t.watch_av()

if __name__ == "__main__":
    main()