from math import gcd, copysign
class Rational:  
    def __init__(self, num=0, den=1):
        
        if type(num) == str:
            num = num.replace(" ", "")
            if "/" in num:
                frac = str(num).split("/")             
                if not frac[1].isdigit():
                    raise ValueError("Cannot create a rational from this str: " + frac[0] + "/" + frac[1] )
                else:
                    num, den = int(frac[0]), int(frac[1])
            elif "." in num:
                num = float(num)
            elif num.isdigit():
                num = int(num)
            elif type(num) !=int:
                raise ValueError("Cannot create a rational from this str: "+ str(num))
            
        if type(num) == float:
            frac = str(num).split('.')
            n = len(frac[1]) 
            num = int(frac[0]+frac[1])
            den = 10**n
     
        if type(num) !=int:
            raise ValueError("Cannot create a rational with a numerator of "+ str(type(num)))
        elif type(den) !=int:
            raise ValueError("Cannot create a rational with a denominator of"+ str(type(den)))
        elif den == 0:
            # print("Cannot create", str(self.n),"/", str(self.d),": zero in denominator")
            raise ZeroDivisionError("Cannot create "+ str(num)+"/"+str(den)+" : zero in denominator")

        self.n = num
        self.d = den        
        
        divcom = gcd(num, den)
        divcom = copysign(divcom, den)
        self.n = int(self.n / divcom)
        self.d = int(self.d / divcom)
        self.r =  self.n, self.d

    def __frction__(self, num, den):

        if type(num) == str:
            num = num.replace(" ", "")
            if "/" in num:
                frac = str(num).split("/")             
                if not frac[1].isdigit():
                    raise ValueError("Cannot create a rational from this str: " + frac[0] + "/" + frac[1] )
                else:
                    num, den = int(frac[0]), int(frac[1])
            elif "." in num:
                num = float(num)
            elif num.isdigit():
                num = int(num)
            elif type(num) !=int:
                raise ValueError("Cannot create a rational from this str: "+ str(num))
            
        if type(num) == float:
            frac = str(num).split('.')
            n = len(frac[1]) 
            num = int(frac[0]+frac[1])
            den = 10**n
     
        if type(num) !=int:
            raise ValueError("Cannot create a rational with a numerator of "+ str(type(num)))
        elif type(den) !=int:
            raise ValueError("Cannot create a rational with a denominator of"+ str(type(den)))
        elif den == 0:
            # print("Cannot create", str(self.n),"/", str(self.d),": zero in denominator")
            raise ZeroDivisionError("Cannot create "+ str(num)+"/"+str(den)+" : zero in denominator")

        self.n = num
        self.d = den        
        
        divcom = gcd(num, den)
        divcom = copysign(divcom, den)
        self.n = int(self.n / divcom)
        self.d = int(self.d / divcom)
        self.r =  self.n, self.d

                
    def __add__(self, other) :
        rat = Rational()
        if type(other) == int :
            rat.n = (self.n*1) + (other*self.d)
            rat.d = self.d*1
        elif type(other) == float :
            other = Rational(other)
            rat.n = (self.n*other.d) + (self.d*other.n)
            rat.d = self.d*other.d
        elif self.d == other.d :
            rat.n = self.n + other.n
            rat.d = self.d
        else:
            rat.n = self.n*other.d + self.d*other.n
            rat.d = self.d*other.d
        return rat
     
     
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other) :
        rat = Rational()
  
        if type(other) == int :
            rat.n = (self.n*1) - (other*self.d)
            rat.d = self.d*1
        elif type(other) == float :
            other = Rational(other)
            rat.n = (self.n*other.d) - (self.d*other.n)
            rat.d = self.d*other.d
        elif self.d == other.d :
            rat.n = self.n - other.n
            rat.d = self.d
        else:
            rat.n = self.n*other.d - self.d*other.n
            rat.d = self.d*other.d
        return rat
     
    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return (new_num, new_den)

    
    def __mul__(self, other):
        rat = Rational()
        if type(other) == int :
            rat.n = self.n*other
            rat.d = self.d*1
        elif type(other) == float :
            other = Rational(other)
            rat.n = (self.n*other.n)
            rat.d = self.d*other.d
        else:
            rat.n = self.n*other.n
            rat.d = self.d*other.d
        return rat
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __float__(self):
        return self.n/self.d
    
    def get_denominator(self):
        return self.d
    
    def __str__(self) -> str:
        if self.d == 1:
            s = '%d' % (self.n)            
        else:
            s = '%d/%d' % (self.n,self.d)
        return s
    
    def __repr__(self):
        num, den = self.r
        s = "Rational({}, {})".format(num, den)
        return s
    




