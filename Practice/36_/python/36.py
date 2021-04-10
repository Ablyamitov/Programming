import math
import copy
from enum import Enum

  
  
class coord_system(Enum):
	Cartesian = 0
	Polar = 1
  
class Point:
	def __init__(self,a1 = 0,a2 = 0,coord_system = coord_system.Cartesian):
		if (type(a1) == str):
			self.x = float( a1[1 : a1.find(',')].strip() )
			self.y = float( a1[a1.find(',') + 1: -2].strip() )
		else:
			if (coord_system == coord_system.Cartesian):
				self.x = a1
				self.y = a2
			else:	
				self.x = math.cos(a2) * a1
				self.y = math.sin(a2) * a1



	def get_x(self):
		return self.x

	def get_y(self): 
		return self.y


	def get_r(self):
		return math.sqrt(self.x*self.x + self.y*self.y)


	def get_phi(self):
		return math.atan2(self.y, self.x)


	def set_x(self,x):
		self.x = x


	def set_y(self,y): 
		self.y = y

	def set_r(self,r):
		self.x = math.cos(self.get_phi()) * r
		self.y = math.sin(self.get_phi()) * r

	def set_phi(self,phi):
		self.x = math.cos(phi) * self.get_r()
		self.y = math.sin(phi) * self.get_r()


	def __repr__(self):
		return f'Point({self.x},{self.y})'

	def __str__(self):
		return f'({self.x},{self.y})'
	def __eq__(self, other):
		return (abs(self.x - other.x) < 10**-10) and (abs(self.y - other.y) < 10**-10)

	def __ne__(self, other):
		return not self == other



with open('data.txt') as fin:
    original = [Point(p) for p in fin.readline().split(', ')]
  
simulacrum = copy.deepcopy(original)
for p in simulacrum:
    print(p, end='')
    p.set_x(p.get_x() + 10)
    p.set_phi(p.get_phi() + 180*math.pi/180)
    p.set_y(-p.get_y())
    p.set_x(-p.get_x() - 10)
    print(p)
  
print('\nIt works!\n' if simulacrum == original else '\nIt not works!\n')