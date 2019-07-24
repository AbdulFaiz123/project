from Employee import Employee

lst_emp = []
def load_emp():
    with open("empdata.txt") as f:
         fdata = f.readlines()
         print(fdata)
         for data in fdata:
             edata = data.strip("\n").split(",")
             empno = int(edata[0])
             ename=edata[1]
             salary = int(edata[3])
             dept_name= edata[4]
             emp = Employee(empno,ename,q,salary,dept_name)
             lst_emp.append(emp)
    print(f"total employees count:{len(lst_emp)}")
def showdeptname():

    dnames = set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)
load_emp()
showdeptname()
def                                                                              
