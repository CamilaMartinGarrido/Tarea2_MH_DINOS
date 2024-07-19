import random
from Operadores.Operator import Operator

class SMH_operator(Operator):
    def __init__(self):
         super().__init__()

    def run(self, c1):
        step = 0.01
        r = self.r
        tolerance = 1e-9  # Añade una pequeña tolerancia
        
       #varia todos los elementos
        for i in range(len(c1)):
            if abs(c1[i] - r[i][0]) < tolerance:
               c1[i] += step
            elif abs(c1[i] - r[i][1]) < tolerance:
               c1[i] -= step
            else:
               c1[i] += random.choice([-step, step])
        return c1
    