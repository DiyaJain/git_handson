from .sum import *
from .sub import *
from .multiply import *
from .divide import *

def calculation(x,y):
    addition = add(x,y)
    print(addition)
    subtraction = sub(x,y)
    print(subtraction)
    multiplication = multi(x,y)
    print(multiplication)
    division = divide(x,y)
    print(division)
