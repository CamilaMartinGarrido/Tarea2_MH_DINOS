import random
from Operadores.Operator import Operator

class OnePointMutate(Operator):
    def __init__(self):
        super().__init__()

    def run(self, c1):
        step = 0.01
        r = self.r
        tolerance = 1e-9  # Añade una pequeña tolerancia

        #varia un elemento al azar
        point = random.randint(0, len(c1) - 1)

        if abs(c1[point] - r[point][0]) < tolerance:
          c1[point] += step
        elif abs(c1[point] - r[point][1]) < tolerance:
          c1[point] -= step
        else:
          c1[point] += random.choice([-step, step])
        return c1
