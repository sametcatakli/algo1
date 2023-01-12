from math import gcd, copysign

class Rational():

    def __init__(self, num=0, den=1):
        if type(num) != int:
            raise ValueError("Cannot create a rational with a numerator of " + str(type(num)))
        elif type(den) != int:
            raise ValueError("Cannot create a rational with a denominator of " + str(type(den)))
        else:
            self.num = num
            self.den = den
            if self.den == 0:
                raise ZeroDivisionError("Cannot create " + str(self.num) + "/" + str(self.den) + ": zero in denominator")
            else:
                g = gcd(self.num, self.den)
                g = int(copysign(g, self.den))
                self.num = self.num // g
                self.den = self.den // g
           
    def get_denominator(self):
        return self.den

    def __str__(self):
        if self.den == 1:
            res = str(self.num)
        else:
            res =  str(self.num) + "/" + str(self.den)

        return res
      

    