import math
  
class Rational:
    def __init__(self, a = None, b = None):
        if ((a == None) and (b == None)):
            self.num = 0
            self.den = 1
            self.num_sign = 1
            self.den_sign = 1
        elif ((a != None) and (b == None)):
            self.num = abs(a)
            self.den = 1
            if (a >= 0):
                self.num_sign = 1
            else:
                self.num_sign = -1
        else:
            if (a < 0):
                self.num_sign = -1
            else:
                self.num_sign = 1
            if (b < 0): 
                self.den_sign = -1
            else:
                self.den_sign = 1;      
            self.num = abs(a)
            self.den = abs(b)

    staticmethod
    def gcd(first, second):
        if (first < second): 
                t = first
                first = second
                second = t
        while (second != 0):
            t = second
            second = first % second
            first = t     
        return abs(first)
    def __eq__(self, other):
        if (self.isNaN() or other.isNaN()): return False
        if (self.num == 0 and other.num == 0): return True
        if ((self.num_sign*self.den_sign) != (other.num_sign*other.den_sign)): return False
        if (self.den ==0 and other.den == 0): return True
        if ((self.num*other.den) == (self.den*other.num)):
            return True
        return False

    def __add__(self, o):
        if (self.isNaN() or o.isNaN()): return Rational(0,0)
        if (self.den == 0 and o.den == 0):
            if(self.num_sign == o.num_sign):
                temp1 = self.num_sign*self.num
            else:
                temp1 =0
            temp2 = 0
            return Rational(temp1, temp2)

        elif (self.den == 0 and o.den != 0):
            temp1 = self.num_sign * self.num
            temp2 = 0
            return (Rational(temp1,temp2))
        elif (self.den != 0 and o.den == 0):
            temp1 = o.num_sign * o.num
            temp2 = 0
            return Rational(temp1,temp2)
        else:
            if ((self.num_sign/self.den_sign) != (o.num_sign / o.den_sign)):
                temp1 = (self.num_sign*self.num *o.den_sign*o.den + o.num_sign*o.num * self.den_sign*self.den)
                if (temp1 == 0): return Rational(0, 1)  
            else:
                temp1 = self.num_sign* self.num * o.den_sign*o.den + o.num_sign*o.num * self.den*self.den_sign
            temp2 = self.den_sign*self.den * o.den*o.den_sign
            return Rational (temp1, temp2)
        return Rational(0,0)

    def __sub__(self, o):
        if (self.isNaN() or o.isNaN()): return Rational(0, 0)
        if (self.den == 0 and o.den == 0):
            if(self.num_sign != o.num_sign):
                temp1=self.num_sign*self.num
            else:
                temp1=0
            temp2 = 0
            return Rational(temp1, temp2)
        elif (self.den == 0 and o.den != 0):
            temp1 = self.num_sign * self.num
            temp2 = 0
            return (Rational(temp1, temp2))
        elif (self.den != 0 and o.den == 0):
            temp1 = o.num_sign * o.num
            temp2 = 0
            return Rational(-temp1, temp2)
        else:
            if ((self.num_sign / self.den_sign) != (o.num_sign / o.den_sign)):
                temp1 = (self.num_sign * self.num * o.den_sign * o.den - o.num_sign * o.num * self.den_sign * self.den)
                if (temp1 == 0): return Rational(0, 1)
            else:
                temp1 = self.num_sign * self.num * o.den_sign * o.den - o.num_sign * o.num * self.den * self.den_sign
            temp2 = self.den_sign * self.den * o.den * o.den_sign
            return Rational(temp1, temp2)
        return Rational(0, 0)

    def __mul__(self, o):
        if (self.isNaN() or o.isNaN()): return Rational(0, 0)
        if (self.den == 0 and o.den == 0):
            temp1 = self.num_sign * self.num*o.num_sign
            temp2 = 0
            return Rational(temp1, temp2)
        elif (self.den == 0 and o.den != 0):
            if((self.num == 0) or (o.num == 0)):
                temp1= 0
            else:
                temp1= self.num_sign * o.num_sign * self.num
            temp2 = 0
            return (Rational(temp1, temp2))
        elif (self.den != 0 and o.den == 0):
            if((self.num == 0) or (o.num == 0)):
                temp1=0
            else:
                temp1=self.num_sign*o.num_sign*o.num
            temp2 = 0
            return Rational(temp1, temp2)
        else:
            if ((self.num_sign / self.den_sign) != (o.num_sign / o.den_sign)):
                temp1 = (self.num_sign * self.num * o.num_sign * o.num )
                if (temp1 == 0): return Rational(0, 1)
            else:
                temp1 = self.num_sign * self.num *  o.num_sign * o.num
            temp2 = self.den_sign * self.den * o.den * o.den_sign
            return Rational(temp1, temp2)
        return Rational(0, 0)

    def __truediv__(self, o):
        if (self.isNaN() or o.isNaN()): return Rational(0, 0)
        if (self.den == 0 and o.den == 0):
            temp1 = self.num_sign * self.num * o.den_sign*o.den
            temp2 = 0
            return Rational(temp1, temp2)
        elif (self.den == 0 and o.den != 0):
            if((self.num == 0) or (o.den == 0)):
                temp1 = 0
            else:
                temp1=self.num_sign * o.num_sign * o.den_sign * self.num * o.den
            temp2 = 0
            return (Rational(temp1, temp2))
        elif (self.den != 0 and o.den == 0):
            temp1 = 0
            if((self.den == 0) or (o.num == 0)):
                temp2=0
            else:
                temp2=self.den_sign * o.num_sign * o.num * self.den
            return Rational(temp1, temp2)
        else:
            if ((self.num_sign / self.den_sign) != (o.num_sign / o.den_sign)):
                temp1 = (self.num_sign * self.num * o.den_sign * o.den)
                if (temp1 == 0): return Rational(0, 1)
            else:
                temp1 = self.num_sign * self.num * o.den_sign * o.den
            temp2 = self.den_sign * self.den * o.num * o.num_sign
            return Rational(temp1, temp2)
        return Rational(0, 0)

    def __float__(self):
        if ((self.den == 0) and (self.num !=0)):
            return math.inf
        elif ((self.den == 0) and (self.num == 0)):
            return math.nan
        else:
            return self.num_sign* self.den_sign*self.num/self.den

    def __bool__(self):
        if ((self.num == 0) and (self.den !=0)):
            return False
        else:
            return True
    def numerator(self):
        return self.num

    def denominator(self):
        return self.den

    def isNaN(self):
        if((self.num==0)and (self.den==0)):
            return True
        else:
            return False

        
  
def equal(a, b, e=1E-10):
    if -e < a - b < e: return True
    else: return False
  
if (Rational.gcd(91, 65) == 13 and
    Rational.gcd(10, 3) == 1 and
    Rational.gcd(-10, 3) == 1 and
    Rational.gcd(10, -3) == 1 and
    Rational.gcd(-10, -3) == 1 and
    Rational.gcd(30, 10) == 10 and
    Rational.gcd(10, 30) == 10 and
    Rational.gcd(0, 10) == 10 and
    Rational.gcd(10, 0) == 10
    ): print('gcd test passed')
else: print('gcd test failed')
  
if (not Rational(22, 0).isNaN() and
    not Rational(22, 9).isNaN() and
    not Rational(0, 9).isNaN() and
    not Rational(-22, 9).isNaN() and
    not Rational(-22, 0).isNaN() and
    Rational(0, 0).isNaN()
    ): print('isNaN test passed')
else: print('isNaN test failed')
  
if (Rational(22, 0) == Rational(22, 0) and
    Rational(22, 0) == Rational(9, 0) and
    not(Rational(22, 0) == Rational(22, 9)) and
    not(Rational(22, 0) == Rational(-22, 9)) and
    not(Rational(22, 0) == Rational(-22, 0)) and
    not(Rational(22, 0) == Rational(0, 9)) and
    not(Rational(22, 0) == Rational(0, 0)) and
  
    Rational(22, 9) == Rational(22, 9) and
    Rational(22, 9) == Rational(-22, -9) and
    Rational(22, 9) == Rational(110, 45) and
    Rational(22, 9) == Rational(-110, -45) and
    not(Rational(22, 9) == Rational(-22, 9)) and
    not(Rational(22, 9) == Rational(22, -9)) and
    not(Rational(22, 9) == Rational(9, 22)) and
    not(Rational(22, 9) == Rational(22, 0)) and
    not(Rational(22, 9) == Rational(-22, 0)) and
    not(Rational(22, 9) == Rational(0, 9)) and
    not(Rational(22, 9) == Rational(0, 0)) and
  
    Rational(0, 1) == Rational(0, 1) and
    Rational(0, 1) == Rational(0, 9)  and
    Rational(0, 1) == Rational(0, -9)  and
    not(Rational(0, 1) == Rational(22, 9))  and
    not(Rational(0, 1) == Rational(-22, 9))  and
    not(Rational(0, 1) == Rational(22, 0)) and
    not(Rational(0, 1) == Rational(-22, 0)) and
    not(Rational(0, 1) == Rational(0, 0)) and
  
    Rational(-22, 9) == Rational(-22, 9) and
    Rational(-22, 9) == Rational(22, -9) and
    Rational(-22, 9) == Rational(-110, 45) and
    Rational(-22, 9) == Rational(110, -45) and
    not(Rational(-22, 9) == Rational(-22, -9)) and
    not(Rational(-22, 9) == Rational(22, 9)) and
    not(Rational(-22, 9) == Rational(9, -22)) and
    not(Rational(-22, 9) == Rational(22, 0)) and
    not(Rational(-22, 9) == Rational(-22, 0)) and
    not(Rational(-22, 9) == Rational(0, 9)) and
    not(Rational(-22, 9) == Rational(0, 0)) and
  
    Rational(-22, 0) == Rational(-22, 0) and
    Rational(-22, 0) == Rational(-9, 0) and
    not(Rational(-22, 0) == Rational(22, 9)) and
    not(Rational(-22, 0) == Rational(-22, 9)) and
    not(Rational(-22, 0) == Rational(22, 0)) and
    not(Rational(-22, 0) == Rational(0, 9)) and
    not(Rational(-22, 0) == Rational(0, 0)) and
  
    not(Rational(0, 0) == Rational(0, 0))
    ): print('Equality test passed')
else: print('Equality test failed')
  
if (Rational(22, 0) + Rational(22, 0) == Rational(22, 0) and
    Rational(22, 9) + Rational(22, 0) == Rational(22, 0) and
    Rational(0, 9) + Rational(22, 0) == Rational(22, 0) and
    Rational(-22, 9) + Rational(22, 0) == Rational(22, 0) and
    (Rational(-22, 0) + Rational(22, 0)).isNaN() and
  
    Rational(22, 0) + Rational(22, 9) == Rational(22, 0) and
    Rational(22, 9) + Rational(22, 9) == Rational(44, 9) and
    Rational(0, 9) + Rational(22, 9) == Rational(22, 9) and
    Rational(-22, 9) + Rational(22, 9) == Rational(0, 9) and
    Rational(-22, 0) + Rational(22, 9) == Rational(-22, 0) and
  
    Rational(22, 0) + Rational(0, 1) == Rational(22, 0) and
    Rational(22, 9) + Rational(0, 1) == Rational(22, 9) and
    Rational(0, 9) + Rational(0, 1) == Rational(0, 9) and
    Rational(-22, 9) + Rational(0, 1) == Rational(-22, 9) and
    Rational(-22, 0) + Rational(0, 1) == Rational(-22, 0) and
  
    Rational(22, 0) + Rational(-22, 9) == Rational(22, 0) and
    Rational(22, 9) + Rational(-22, 9) == Rational(0, 9) and
    Rational(0, 9) + Rational(-22, 9) == Rational(-22, 9) and
    Rational(-22, 9) + Rational(-22, 9) == Rational(-44, 9) and
    Rational(-22, 0) + Rational(-22, 9) == Rational(-22, 0) and
  
    (Rational(22, 0) + Rational(-22, 0)).isNaN() and
    Rational(22, 9) + Rational(-22, 0) == Rational(-22, 0) and
    Rational(0, 9) + Rational(-22, 0) == Rational(-22, 0) and
    Rational(-22, 9) + Rational(-22, 0) == Rational(-22, 0) and
    Rational(-22, 0) + Rational(-22, 0) == Rational(-22, 0) and
  
    (Rational(22, 0) + Rational(0, 0)).isNaN() and
    (Rational(22, 9) + Rational(0, 0)).isNaN() and
    (Rational(0, 9) + Rational(0, 0)).isNaN() and
    (Rational(-22, 9) + Rational(0, 0)).isNaN() and
    (Rational(-22, 0) + Rational(0, 0)).isNaN()
    ): print('Summation test passed')
else: print('Summation test failed')
  
if ((Rational(22, 0) - Rational(22, 0)).isNaN() and
    Rational(22, 9) - Rational(22, 0) == Rational(-22, 0) and
    Rational(0, 9) - Rational(22, 0) == Rational(-22, 0) and
    Rational(-22, 9) - Rational(22, 0) == Rational(-22, 0) and
    Rational(-22, 0) - Rational(22, 0) == Rational(-22, 0) and
  
    Rational(22, 0) - Rational(22, 9) == Rational(22, 0) and
    Rational(22, 9) - Rational(22, 9) == Rational(0, 9) and
    Rational(0, 9) - Rational(22, 9) == Rational(-22, 9) and
    Rational(-22, 9) - Rational(22, 9) == Rational(-44, 9) and
    Rational(-22, 0) - Rational(22, 9) == Rational(-22, 0) and
  
    Rational(22, 0) - Rational(0, 1) == Rational(22, 0) and
    Rational(22, 9) - Rational(0, 1) == Rational(22, 9) and
    Rational(0, 9) - Rational(0, 1) == Rational(0, 9) and
    Rational(-22, 9) - Rational(0, 1) == Rational(-22, 9) and
    Rational(-22, 0) - Rational(0, 1) == Rational(-22, 0) and
  
    Rational(22, 0) - Rational(-22, 9) == Rational(22, 0) and
    Rational(22, 9) - Rational(-22, 9) == Rational(44, 9) and
    Rational(0, 9) - Rational(-22, 9) == Rational(22, 9) and
    Rational(-22, 9) - Rational(-22, 9) == Rational(0, 9) and
    Rational(-22, 0) - Rational(-22, 9) == Rational(-22, 0) and
  
    Rational(22, 0) - Rational(-22, 0) == Rational(22, 0) and
    Rational(22, 9) - Rational(-22, 0) == Rational(22, 0) and
    Rational(0, 9) - Rational(-22, 0) == Rational(22, 0) and
    Rational(-22, 9) - Rational(-22, 0) == Rational(22, 0) and
    (Rational(-22, 0) - Rational(-22, 0)).isNaN() and
  
    (Rational(22, 0) - Rational(0, 0)).isNaN() and
    (Rational(22, 9) - Rational(0, 0)).isNaN() and
    (Rational(0, 9) - Rational(0, 0)).isNaN() and
    (Rational(-22, 9) - Rational(0, 0)).isNaN() and
    (Rational(-22, 0) - Rational(0, 0)).isNaN()
    ): print('Subtraction test passed')
else: print('Subtraction test failed')
  
if (Rational(22, 0) * Rational(22, 0) == Rational(22, 0) and
    Rational(22, 9) * Rational(22, 0) == Rational(22, 0) and
    (Rational(0, 9) * Rational(22, 0)).isNaN() and
    Rational(-22, 9) * Rational(22, 0) == Rational(-22, 0) and
    Rational(-22, 0) * Rational(22, 0) == Rational(-22, 0) and
  
    Rational(22, 0) * Rational(22, 9) == Rational(22, 0) and
    Rational(22, 9) * Rational(22, 9) == Rational(22*22, 9*9) and
    Rational(0, 9) * Rational(22, 9) == Rational(0, 9) and
    Rational(-22, 9) * Rational(22, 9) == Rational(-22*22, 9*9) and
    Rational(-22, 0) * Rational(22, 9) == Rational(-22, 0) and
  
    (Rational(22, 0) * Rational(0, 1)).isNaN() and
    Rational(22, 9) * Rational(0, 1) == Rational(0, 9) and
    Rational(0, 9) * Rational(0, 1) == Rational(0, 9) and
    Rational(-22, 9) * Rational(0, 1) == Rational(0, 9) and
    (Rational(-22, 0) * Rational(0, 1)).isNaN() and
  
    Rational(22, 0) * Rational(-22, 9) == Rational(-22, 0) and
    Rational(22, 9) * Rational(-22, 9) == Rational(-22*22, 9*9) and
    Rational(0, 9) * Rational(-22, 9) == Rational(0, 9) and
    Rational(-22, 9) * Rational(-22, 9) == Rational(22*22, 9*9) and
    Rational(-22, 0) * Rational(-22, 9) == Rational(22, 0) and
  
    Rational(22, 0) * Rational(-22, 0) == Rational(-22, 0) and
    Rational(22, 9) * Rational(-22, 0) == Rational(-22, 0) and
    (Rational(0, 9) * Rational(-22, 0)).isNaN() and
    Rational(-22, 9) * Rational(-22, 0) == Rational(22, 0) and
    Rational(-22, 0) * Rational(-22, 0) == Rational(22, 0) and
  
    (Rational(22, 0) * Rational(0, 0)).isNaN() and
    (Rational(22, 9) * Rational(0, 0)).isNaN() and
    (Rational(0, 9) * Rational(0, 0)).isNaN() and
    (Rational(-22, 9) * Rational(0, 0)).isNaN() and
    (Rational(-22, 0) * Rational(0, 0)).isNaN()
    ): print('Multiplication test passed')
else: print('Multiplication test failed')
  
if ((Rational(22, 0) / Rational(22, 0)).isNaN() and
    Rational(22, 9) / Rational(22, 0) == Rational(0, 9) and
    Rational(0, 9) / Rational(22, 0) == Rational(0, 9) and
    Rational(-22, 9) / Rational(22, 0) == Rational(0, 9) and
    (Rational(-22, 0) / Rational(22, 0)).isNaN() and
  
    Rational(22, 0) / Rational(22, 9) == Rational(22, 0) and
    Rational(22, 9) / Rational(22, 9) == Rational(9, 9) and
    Rational(0, 9) / Rational(22, 9) == Rational(0, 9) and
    Rational(-22, 9) / Rational(22, 9) == Rational(-9, 9) and
    Rational(-22, 0) / Rational(22, 9) == Rational(-22, 0) and
  
    Rational(22, 0) / Rational(0, 1) == Rational(22, 0) and
    Rational(22, 9) / Rational(0, 1) == Rational(22, 0) and
    (Rational(0, 9) / Rational(0, 1)).isNaN() and
    Rational(-22, 9) / Rational(0, 1) == Rational(-22, 0) and
    Rational(-22, 0) / Rational(0, 1) == Rational(-22, 0) and
  
    Rational(22, 0) / Rational(-22, 9) == Rational(-22, 0) and
    Rational(22, 9) / Rational(-22, 9) == Rational(-9, 9) and
    Rational(0, 9) / Rational(-22, 9) == Rational(0, 9) and
    Rational(-22, 9) / Rational(-22, 9) == Rational(9, 9) and
    Rational(-22, 0) / Rational(-22, 9) == Rational(22, 0) and
  
    (Rational(22, 0) / Rational(-22, 0)).isNaN() and
    Rational(22, 9) / Rational(-22, 0) == Rational(0, 9) and
    Rational(0, 9) / Rational(-22, 0) == Rational(0, 9) and
    Rational(-22, 9) / Rational(-22, 0) == Rational(0, 9) and
    (Rational(-22, 0) / Rational(-22, 0)).isNaN() and
  
    (Rational(22, 0) / Rational(0, 0)).isNaN() and
    (Rational(22, 9) / Rational(0, 0)).isNaN() and
    (Rational(0, 9) / Rational(0, 0)).isNaN() and
    (Rational(-22, 9) / Rational(0, 0)).isNaN() and
    (Rational(-22, 0) / Rational(0, 0)).isNaN()
    ): print('Division test passed')
else: print('Division test failed')
  
if (equal(float(Rational(-22, -9)), 22/9.0) and
    equal(float(Rational(-9, -9)), 1) and
    equal(float(Rational(-6, -9)), 6/9.0) and
    equal(float(Rational(0, -9)), 0) and
    equal(float(Rational(6, -9)), -6/9.0) and
    equal(float(Rational(9, -9)), -1) and
    equal(float(Rational(22, -9)), -22/9.0) and
    math.isinf(float(Rational(-9, 0))) and
    math.isnan(float(Rational(0, 0))) and
    math.isinf(float(Rational(9, 0))) and
    equal(float(Rational(-22, 9)), -22/9.0) and
    equal(float(Rational(-9, 9)), -1) and
    equal(float(Rational(-6, 9)), -6/9.0) and
    equal(float(Rational(0, 9)), 0) and
    equal(float(Rational(6, 9)), 6/9.0) and
    equal(float(Rational(9, 9)), 1) and
    equal(float(Rational(22, 9)), 22/9.0)
    ): print('Conversion to double test passed')
else: print('Conversion to double test failed')
  
if (bool(Rational(-22, -9)) and
    bool(Rational(-9, -9)) and
    bool(Rational(-6, -9)) and
    not bool(Rational(0, -9)) and
    bool(Rational(6, -9)) and
    bool(Rational(9, -9)) and
    bool(Rational(22, -9)) and
    bool(Rational(-9, 0)) and
    bool(Rational(0, 0)) and
    bool(Rational(9, 0)) and
    bool(Rational(-22, 9)) and
    bool(Rational(-9, 9)) and
    bool(Rational(-6, 9)) and
    not bool(Rational(0, 9)) and
    bool(Rational(6, 9)) and
    bool(Rational(9, 9)) and
    bool(Rational(22, 9))
    ): print('Conversion to bool test passed')
else: print('Conversion to bool test failed')