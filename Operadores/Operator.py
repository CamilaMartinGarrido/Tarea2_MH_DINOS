class Operator:
    #cx > probabilidad min de cruce
    #cy > probabilidad max de cruce
    #vx > probabilidad min de cruce de vecinos
    #vy > probabilidad max de cruce de vecinos
    #mx > probabilidad min de mutacion
    #my > probabilidad max de mutacion
    #r > conjunto de restricciones

    def __init__(self):
        self.cx = 0.5
        self.cy = 1.0
        self.vx = 0.5
        self.vy = 1.0
        self.mx = 0.1
        self.my = 0.5
        self.r = [(self.cx,self.cy),(self.vx,self.vy),(self.mx,self.my)]

    def run(self):
      pass
