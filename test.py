#!/usr/bin/env python3
import sys
from collections import Counter


class Person(object):
    '''
    返回具有给定名称的Person对象
    '''

    def __init__(self,name):
        self.name = name

    def get_details(self):
        '''
        返回包含人名的字符串
        '''
        return self.name

    def get_grade(self):
        return 0


class Student(Person):
    """docstring for Student"""
    def __init__(self, name, branch, year, grade):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
        self.grade = grade


    def get_details(self):
        return "{} studies {} and is in {} year.".format(self,self.branch,self.year)


    def get_grade(self):
        
        common = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] == 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        print("Pass: {}, Fail: {}".format(n1.n2))


class Teacher(Person):
    """docstring for Teacher"""
    def __init__(self,name,papers,grade):
        Person.__init__(self,name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teachs {}".format(self.name,',' .join(self.papers))

    def get_grade(self):
        s = []
        common = Counter(self.grade).most_common(4)
        for i,j in common:
            s.append("{}: {}".format(i,j))
        print(',' .join(s))

if sys.argv[1] == "student":
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_details()
if sys.argv[1] == "teacher":
    teacher1 = Teacher('Prashad'， ['C', 'Python'], sys.argv[2])
    teacher1.get_grade()




