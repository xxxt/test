from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 150 * self._working_hour

class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._salas = sales
    
    @property
    def salas(self):
        return self._salas
    
    @salas.setter
    def salas(self, salas):
        self._salas = salas
    
    def get_salary(self):
        return 1200 + self._salas * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('B'),
        Manager('CV'), Salesman('D'),
        Programmer('NN')
    ]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入{}工作时长'.format(emp.name)))
        elif isinstance(emp, Salesman):
            emp.salas = float(input('请输入{}的销售额'.format(emp.name)))
        print('{}本月工资为{}'.format(emp.name, emp.get_salary()))
        

if __name__ == "__main__":
    main()