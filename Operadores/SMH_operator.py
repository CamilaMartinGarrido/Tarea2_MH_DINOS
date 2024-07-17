import random

class SMH_operator:
    def __init__(self):
        pass

    def run(self, c):
        
       #varia todos los elementos
        for i in range(len(c)):
            c[i] += random.choice([-0.01, 0.01])
        return c
    