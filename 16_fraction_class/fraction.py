class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = gcd(numerator, denominator)
        
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor


    # Getter
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    # Setters
    @numerator.setter
    def numerator(self, value):
        self._numerator = value
    
    @denominator.setter
    def denominator(self, value):
        if (value == 0):
            print("Incorrect logic: denominator cannot be zero")
            self._denominator = 1
        else:
            self._denominator = value
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # Multiplication operator
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    # Addition
    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    # Subtraction
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    # <
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    # >
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    # ==
    def __et__(self, other):
        return self.__cmp__(other) > 0


    # Compare 
    def __cmp__(self, other):
        temp = self.__sub__(other)
        if temp.numerator > 0:
            return 1
        elif temp.numerator < 0:
            return -1
        else:
            return 0

    
def gcd(n,d):
    gcd = 1
    k = 1
    while k <= n and k <= d:
        if n % k == 0 and d % k == 0:
            gcd = k
        k += 1
    
    return gcd

frac = Fraction(2, 3)
print(frac)

frac.numerator = 3
frac.denominator = 0
print(frac)

frac2 = Fraction(4, 5)
print(f"{frac} * {frac2} = {frac * frac2}") # frac.__mul__(frac2)
print(f"{frac} + {frac2} = {frac + frac2}") # frac.__add__(frac2)
print(f"{frac} - {frac2} = {frac - frac2}") # frac.__sub__(frac2)
print(f"{frac} < {frac2} is {frac < frac2}") # frac.__lt__(frac2)
print(f"{frac} > {frac2} is {frac > frac2}") # frac.__gt__(frac2)
print(f"{frac} = {frac2} is {frac == frac2}") # frac.__et__(frac2)
