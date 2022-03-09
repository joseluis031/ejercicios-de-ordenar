from dicotomia import *

from topologia import *

from especificaciones import *

if __name__=="__main__:

v = int(input("Elija el ejercicio que desea ejecutar(1-3): "))
if v == 1:
  from class import dicotomia
elif v == 2:
  from class import topologia
elif v == 3:
  from class import especificaciones
else:
  print("Introduzcaun numero del 1 al 3 por favor:")
