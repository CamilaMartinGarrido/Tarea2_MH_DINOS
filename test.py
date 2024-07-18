
from Operadores.OnePointMutate import OnePointMutate
from Operadores.OnePointCrossover import OnePointCrossover
from Operadores.SMH_operator import SMH_operator



mutate = OnePointMutate()
crossover = OnePointCrossover()
smh = SMH_operator()
#definir restricciones y soluciones
pc = (0.5, 1)
cv = (0.5, 1)
pm = (0.1, 0.5)
r = list((pc,cv,pm))

test1 = list((0.5, 0.5, 0.1))
test2 = list((0.8, 0.8, 0.1))

#tiene en cuenta las restricciones y los limites de estas
#print para calbrar
print(crossover.run(test1,test2)) #Ok
print(mutate.run(test1,r)) #Ok
print(smh.run(test1,r)) #Ok
print(crossover.run(mutate.run(test1,r),smh.run(test1,r)))