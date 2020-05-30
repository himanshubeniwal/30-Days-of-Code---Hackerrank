class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        n = len(self.scores)
        avg = sum(self.scores)/n
        if avg<=100 and avg>=90:
            return 'O'
        if avg<=89 and avg>=80:
            return 'E'
        if avg<=79 and avg>=70:
            return 'A'
        if avg<=69 and avg>=55:
            return 'P'
        if avg<=54 and avg>=40:
            return 'D'
        if avg<=39:
            return 'T'

line = input().split()
