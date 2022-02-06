import numpy as np
import os
import pandas as pd
import math

path = '.'

filename_read = os.path.join(path, "Planet_input.csv")
table_file = pd.read_csv(filename_read, na_values=['NA', '?'])


class Planet():

 def __init__(self, table_file):
  self.planet = table_file
  # number of teleportation stations
  self.stations_qtt = self.planet["X"][1]
  self.start = [0.00, 0.00, 0.00]
  self.end = self.planet.iloc[0].tolist()

 def stations_locations(self):
  '''
  creates a dictionary with values being 
  coordinates of the teleportation stations.
  '''
  stations = {}
  for i in range(2, int(self.stations_qtt) + 2):
   station = self.planet.iloc[i].tolist()
   x = station[0]
   y = station[1]
   z = station[2]
   stations[i - 2] = [x, y, z]

  return stations

 def f_distance(self, location1, location2):
  '''
  calculates distance between two teleportation stations 
  in the 3 dimensional Cartesian coordinate system.
  '''
  x1 = location1[0]
  y1 = location1[1]
  z1 = location1[2]

  x2 = location2[0]
  y2 = location2[1]
  z2 = location2[2]

  distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
  return round(distance, 2)

 def shortest_path(self):
  '''
  finds the shortest path from Earth to Zearth
  '''
  stations = self.stations_locations()
  # at the begining distance to all the stations is infinity
  total_number_of_stations = int(self.stations_qtt + 2)
  path = []  # storing visited teleportation stations

  current_location = self.start
  cost1 = {}
  # distances from the starting station to the each intermediate teleportation station
  for i in range(len(stations)):
   distance = self.f_distance(self.start, list(stations.values())[i])
   cost1[i] = distance
  shortest_path = min(cost1.values())
  index = list(cost1.keys())[list(cost1.values()).index(shortest_path)]
  next_location = stations[index]
  path.append(shortest_path)
  del stations[index]

  cost2 = {}
  for i in range(len(stations)):
   distance = self.f_distance(next_location, list(stations.values())[i])
   cost2[i] = distance
  shortest_path = min(cost2.values())
  index = list(cost2.keys())[list(cost2.values()).index(shortest_path)]
  next_location = stations[index + 1]
  path.append(shortest_path)

  distance = self.f_distance(next_location, self.end)
  path.append(shortest_path)
  return path

 def run(self):
  '''
  returns one real number to 2 decimal places, representing 
  the maximum distance of the safest path from Earth to Zearth.
  '''
  stations = self.stations_locations()
  shortest_path = self.shortest_path()
  answer = max(shortest_path)
  return format(answer, '.2f')


def main():
 planet = Planet(table_file)
 shortest_path = planet.run()
 print(shortest_path)


if __name__ == '__main__':
 main()
