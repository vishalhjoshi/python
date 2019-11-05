class Employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name+self.last_name+'@ourcompany.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Developer(Employee):
    def __init__(self,first_name,last_name,pay,prog_lang):
        super().__init__(first_name,last_name,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first_name,last_name,pay,employees=None):
        super().__init__(first_name,last_name,pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("Name : ",emp.full_name(),'| Email : ',emp.email,'| Prog_Lang : ',emp.prog_lang)

developers = [
Developer('Vishal','Joshi',50000,'python'),
Developer('Pradip','Bhoi',40000,'php'),
Developer('Shubham','Patil',45000,'c#'),
Developer('Rizwan','Shaikh',35000,'JavaScript')]

# for developer in developers:
#     print(developer.full_name(),':',developer.prog_lang)

mgr_1 = Manager('Donald','Tatya',80000,developers)

new_developer = Developer("Naru","Patil",15000,'Java')

mgr_1.remove_emp(developers[3])
mgr_1.add_emp(new_developer)
mgr_1.print_emp()