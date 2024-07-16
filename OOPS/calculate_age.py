Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import datetime,date

class Person:
    def __init__(self,name,gender,DOB):
        self.name = name
        self.gender = gender
        self.DOB = datetime.strptime(DOB,'%d-%m-%Y')

    
    def age_of_person(self):
        age_year = (date.today().year-self.DOB.year)
        age_month = date.today().month-self.DOB.month
        if age_month < 0:
            return age_year -1
        else:
            return age_year

    def person_age(self):
        age = date.today().year - self.DOB.year - ((date.today().month,date.today().day) < (self.DOB.month,self.DOB.day))
        return age
    
        

p = Person("Miles","M",'16-07-1996')
print(p.age_of_person())
print(p.person_age())
