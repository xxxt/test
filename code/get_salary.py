from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000

class Programer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour

class Salamen(Employee):
    """销售员"""

    def __init__(self, name, salas=0.0):
        super().__init__(name)
        self.salas = salas

    def get_salary(self):
        return 1800 + self.salas * 0.05

class EmployeeFactory():

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salamen(*args, **kwargs)
        return emp
    

def main():
    emps = [
        EmployeeFactory.create('M', 'aa'),
        EmployeeFactory.create('P', 'bb', 120),
        EmployeeFactory.create('P', 'cc', 85),
        EmployeeFactory.create('S', 'dd', 123000),
    ]
    for emp in emps:
        print('{}:{}元'.format(emp.name, emp.get_salary()))


if __name__ == "__main__":
    main()