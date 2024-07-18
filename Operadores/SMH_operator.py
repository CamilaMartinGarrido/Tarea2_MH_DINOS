import random

class SMH_operator:
    def __init__(self):
        pass

    def run(self, c, r):
        step = 0.01
        tolerance = 1e-9  # Añade una pequeña tolerancia
        
       #varia todos los elementos
        for i in range(len(c)):
            if abs(c[i] - r[i][0]) < tolerance:
               c[i] += step
            elif abs(c[i] - r[i][1]) < tolerance:
               c[i] -= step
            else:
               c[i] += random.choice([-step, step])
        return c
    