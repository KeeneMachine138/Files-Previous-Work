class Employee:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def give_raise(self, percent):
        self.pay = (self.pay * percent) + self.pay

class Manager(Employee):
    def __init__(self, name, pay):
        Employee.__init__(self, name, 'mgr', pay)
        
    def give_raise(self, percent, bonus=.10):
        Employee.give_raise
        self.pay = (self.pay * percent) + self.pay + (self.pay * bonus)
        
m = Manager("Scott Schanke", 500000)
m.give_raise(.10)
print(m.pay)
