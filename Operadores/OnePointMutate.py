import random

class OnePointMutate:
    def __init__(self):
        pass

    def run(self, c):
       
       #varia un elemento al azar
        point = random.randint(0, min(len(c)) - 1)
        c[point] += random.choice([-0.01, 0.01])
        return c