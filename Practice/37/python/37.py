import math
from enum import Enum

def equal(a, b, e=1E-10):
    if -e < a - b < e: return True
    else: return False  
  
  

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
		if type(other) == Point:
			return (abs(self.x - other.x) < 10**-10) and (abs(self.y - other.y) < 10**-10)
		else:
			return False

	def __ne__(self, other):
		return not self == other
          

class Vector:
	unit_vector = Point()

	def __init__(self,begin = 0,end = 0):
		if(begin == 0 and end == 0):
			self.unit_vector = Point(1,0)
		elif((begin == 0 and end !=0)or (end == 0 and begin != 0)):
			if(begin == 0):
				self.unit_vector = end
			else:
				self.unit_vector = begin
		else:
			self.unit_vector = Point(end.get_x() - begin.get_x(), end.get_y() - begin.get_y())



	def __eq__(self,other):
		if(self.unit_vector == other.unit_vector):
			return True
		else:
			return False

	def __neg__(self):
		return Vector(Point(-self.unit_vector.get_x(), -self.unit_vector.get_y()))


	def __add__(self,other):
		Summation = Point()
		Summation.set_x( self.unit_vector.get_x() + other.unit_vector.get_x() )
		Summation.set_y( self.unit_vector.get_y() + other.unit_vector.get_y() )
		return Vector(Summation)

	def __sub__(self,other):
		subtraction = Point()
		subtraction.set_x(self.unit_vector.get_x() - other.unit_vector.get_x())
		subtraction.set_y(self.unit_vector.get_y() - other.unit_vector.get_y())
		return Vector(subtraction)

	def __mul__(self, other):
		if type(other) == int:
			Multiplication = Point()
			Multiplication.set_x( self.unit_vector.get_x() * other )
			Multiplication.set_y( self.unit_vector.get_y() * other )
			return Vector(Multiplication)
		else:
			return self.length() * other.length() * math.cos(self.unit_vector.get_phi() - other.unit_vector.get_phi())

	def length(self):
		return self.unit_vector.get_r()



				
a = Vector(Point(1, 2))
b = Vector(Point(-2, 0), Point(-1, 2))
if a == b and b == a: print('Equality test passed')
else: print('Equality test failed')
  
na  = Vector(Point(-1, -2))
ox  = Vector(Point( 1,  0))
nox = Vector(Point(-1,  0))
oy  = Vector(Point( 0,  1))
noy = Vector(Point( 0, -1))
if a == -na and na == -a and -ox == nox and -oy == noy: print('Invert test passed')
else: print('Invert test failed')
  
if ox + oy + oy == a and -ox == -a + oy + oy: print('Summation test passed')
else: print('Summation test failed')
  
if -ox + oy == oy - ox and -oy + ox == ox - oy: print('Subtraction test passed')
else: print('Subtraction test failed')
  
if (ox * 3 == ox + ox + ox and
    oy * 3 == oy + oy + oy and
    ox * (-3) == -ox - ox - ox and
    oy * (-3) == -oy - oy - oy): print('Multiplication by number test passed')
else: print('Multiplication by number test failed')

if (equal(ox.length(), 1) and
	equal(oy.length(), 1) and
	equal((ox * 3 + oy * 4).length(), 5)): print('Length test passed')
else: print('Length test failed')

if (equal(ox*ox, ox.length()**2) and
	equal(oy*oy, oy.length()**2) and
	equal((ox*3 + oy*4)*(ox*3 + oy*4), (ox*3 + oy*4).length()**2)): print('Multiplication by Vector test passed')
else: print('Multiplication by Vector test failed')