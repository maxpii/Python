class Employee:
    num_of_emps = 0
    raise_amount = 1.7

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.num_of_emps += 1

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getPay(self):
        return self.pay

    def getName(self):
        return self.first_name + " " + self.last_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)


string1 = "Manu-Fighter-10"
string2 = "Hanu-Loser-1"
string3 = "Someone-Something-5"

first, last, pay = string1.split("-")
print(first, last, pay)
emp1 = Employee(first, last, pay)
