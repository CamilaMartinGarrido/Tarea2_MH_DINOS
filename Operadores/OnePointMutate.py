import random

class OnePointMutate:
    def __init__(self):
        pass

    def run(self, c, r):
        step = 0.01
        tolerance = 1e-9  # Añade una pequeña tolerancia

        #varia un elemento al azar
        point = random.randint(0, len(c) - 1)

        print(point)
        if abs(c[point] - r[point][0]) < tolerance:
          c[point] += step
        elif abs(c[point] - r[point][1]) < tolerance:
          c[point] -= step
        else:
          c[point] += random.choice([-step, step])
        return c
