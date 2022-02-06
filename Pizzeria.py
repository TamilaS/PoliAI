import numpy as np
import os
import pandas as pd

path = "."

filename_read = os.path.join(path, "Pizzeria_input.csv")
file = pd.read_csv(filename_read, na_values=['NA', '?'])


class Pizzeria():

 def __init__(self, file):
  self.pizzeria = file
  self.size = self.pizzeria["N"][0]
  # number of pizzarias
  self.quantity = self.pizzeria["M"][0]

 def create_city(self):
  '''
  creates a city 
  '''
  city = np.zeros((self.size, self.size), dtype=int)
  return city

 def f_location(self):
  '''
  locations of pizzarias in the city
  '''
  location = {}
  for i in range(1, self.quantity + 1):
   x = self.pizzeria["N"][i] - 1
   y = self.pizzeria["M"][i] - 1
   location[i] = [x, y]
  return location

 def f_delivery(self):
  '''
  distance of a deliver guy can reach
  '''
  delivery_list = []
  for i in range(1, self.quantity + 1):
   delivery = int(self.pizzeria["R"][i])
   delivery_list.append(delivery)
  return delivery_list

 def greatest_selection(self):
  '''
  returns the number of pizzerias that deliver pizzas to the block 
  with the greatest selection of pizzas.
  '''
  location = self.f_location()
  delivery = self.f_delivery()
  city = self.create_city()

  for i in range(1, self.quantity + 1):
   a = location[i][0]
   b = location[i][1]
   city[a, b] += 1
   delivery_pizzaria = delivery[i - 1]
   for i in range(1, delivery_pizzaria + 1):
    if a == 0 or a == (self.size - 1) or b == 0 or b == (self.size - 1):  # corners and sides
     if a != 0:
      city[a - i, b] += 1  # u
     if a != (self.size - 1):
      city[a, b + i] += 1  # r
     if b != (self.size - 1):
      city[a + i, b] += 1  # d
     if b != 0:
      city[a, b - i] += 1  # l

     if self.quantity - i > 0:
      if (a == 0 and b == 0) or (a == 0 and b != 0 and b != (self.size - 1)) or (
              a != 0 and a != (self.size - 1) and b == 0):
       city[a + i, b + i] += 1  # upper right diagonal
      if (a == (self.size - 1) and b == (self.size - 1)) or (a == 0 and b != 0 and b != (self.size - 1)) or (
              a != 0 and a != (self.size - 1) and b == (self.size - 1)):
       city[a + i, b - i] += 1  # upper left diagonal
      if (a == 0 and b == (self.size - 1)) or (a != 0 and a != (self.size - 1) and b == 0) or (
              a == (self.size - 1) and b != 0 and b != (self.size - 1)):
       city[a - i, b + i] += 1  # lower right diagonal
      if (a == (self.size - 1) and b == 0) or (a == (self.size - 1) and b != 0 and b != (self.size - 1)) or (
              a != 0 and a != (self.size - 1) and b == (self.size - 1)):
       city[a - i, b - i] += 1  # lower left diagonal

    elif a < self.size and b < self.size:  # neighbours in adjacent locations
     if self.quantity - i >= 0:
      city[a, b + i] += 1  # r
      city[a, b - i] += 1  # l
      city[a + i, b] += 1  # d
      city[a - i, b] += 1  # u
     if self.quantity - i > 0:
      city[a - i, b - i] += 1  # lower left diagonal
      city[a + i, b + i] += 1  # upper right diagonal
      city[a - i, b + i] += 1  # lower right diagonal
      city[a + i, b - i] += 1  # upper left diagonal

  city = np.flipud(city)
  greatest_selection_number = np.amax(city)
  return greatest_selection_number


def main():
 pizzeria = Pizzeria(file)
 greatest_selection = pizzeria.greatest_selection()
 print(greatest_selection)


if __name__ == '__main__':
 main()
