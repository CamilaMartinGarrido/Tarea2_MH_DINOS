import random
from Operadores.Operator import Operator

class OnePointCrossover(Operator):
    def __init__(self):
        pass

    #c1 y c2 > conjuntos de valores respectivamente 

    def run(self, c1, c2):
        # Manejo de valores nulos
        c1 = [x for x in c1 if x is not None]
        c2 = [x for x in c2 if x is not None]

        # Punto de corte
        point = random.randint(0, min(len(c1), len(c2)) - 1)

        children1 = c1[: point] + c2[ point:]
        children2 = c2[: point] + c1[point:]
        return children1, children2


