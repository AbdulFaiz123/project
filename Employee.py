class Employee:

    def __init__(self,empno,name,q,salary,dept_name):
        self.empno=empno
        self.name=name
        self.q=q
        self.salary=salary
        self.dept_name=dept_name

    def show_info(self):
        print(f"{self.empno} - {self.name} - {self.q} - {self.salary} - {self.dept_name}")
    def increment_salary(self,inc_amount):
        self.salary+=inc_amount
        print(f"{self.name}salary after increment:{self.salary}")