class Employee:

    def __init__(self, name, salary, phone, start_date):
        self.name = name 
        self.salary = salary 
        self.phone = phone 
        self.start_date = start_date

    def __str__(self):
        return f"Name: {self.name}, Salary: ${self.salary}, Phone: {self.phone}, Start date: {self.start_date}"

    def get_employment_details(self):
        return(self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return(self.name, self.phone)

employee1 = Employee("Renae", 145000, " 123456789", "12/07/2020")

employee2 = Employee("Benjamin", 110000, "123456789", "03/04/2020")

print(employee1)
print(employee1.get_employment_details())
print(employee2)
print(employee2.get_contact_details())