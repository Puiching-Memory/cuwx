import math

class ExponentialEaseOut():
    def func(t: float) -> float:
        if t == 1:
            return 1
        return 1 - math.pow(2, -10 * t)
    

print(ExponentialEaseOut.func(0.02))