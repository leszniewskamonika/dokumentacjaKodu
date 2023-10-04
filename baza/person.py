class Person:
    def __init__(self, firstName, lastName, homeCountry):
        self.firstName = firstName
        self.lastName = lastName
        self.homeCountry = homeCountry

    def printName(self):
        print(self.firstName, self.lastName)

    def printCountry(self):
        print(self.homeCountry)

class Student(Person):
    def __init__(self, firstName, lastName, homeCountry, universityName):
        super().__init__(firstName, lastName, homeCountry)
        self.universityName = universityName

    def printUniversity(self):
        print(self.universityName)