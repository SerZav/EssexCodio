class Person:
     """Represents a generic Person."""
     def __init__(self, first, last, weight, height):
          self.first_name = first
          self.last_name = last
          self.weight_in_lbs = weight
          self.height_in_inches = height

print(Person)
# output: <class '__main__.Person'>
