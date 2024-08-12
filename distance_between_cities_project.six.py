from pystyle import *
from geopy.distance import geodesic
Write.Print("[-] this program for Distance between Cities Test\n",Colors.red, interval=0.01)

Write.Print(Box.DoubleCube("Example 6"), Colors.orange, interval=0.01)

first_place = (33.575729,7.706956)
second_place = (30.427755, 9.598107)
distance = int(geodesic(first_place, second_place).km)

Write.Print(Box.DoubleCube(f"Distance between Cities is:\n{distance} KM"), Colors.green, interval=0.01)