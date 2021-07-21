import sys

class Person:
  """ Person object """
  def __init__(self, first_name, last_name, weight, height):
    # fill attributes with parameters received
    self.first_name = first_name
    self.last_name = last_name
    self.weight = weight
    self.height = height
    
  def calc_BMI(self):
    # calculate BMI and returns calculation
    return (self.weight * 703) / self.height ** 2
  
  def __str__(self):
    # prints the result when the object is printed
    returnText = "First Name: {1}{0}Last Name: {2}{0}"\
    "Weight: {3}{0}Height: {4}{0}BMI: {5}{0}Result: {6}{0}"\
    .format("\n",self.first_name, self.last_name, self.weight, self.height, self.calc_BMI(), self.check_health())
    return (returnText)
  
  def print_self(self):
    returnText = "First Name: {1}{0}Last Name: {2}{0}"\
    "Weight: {3}{0}Height: {4}{0}BMI: {5}{0}Result: {6}{0}"\
    .format("\n",self.first_name, self.last_name, self.weight, self.height, self.calc_BMI(), self.check_health())
    print(returnText)
    
  
  def check_health(self):
    bmi = self.calc_BMI()
    if bmi < 18.5:
      return "underweight"
    elif bmi < 25:
      return "healthy"
    elif bmi < 30:
      return "overweight"
    else:
      return "obesity"

p = Person('Sergio','Zavarce',108,62)
p2 = Person('Luis','Perez',185,58)
p.print_self()
p2.print_self()
