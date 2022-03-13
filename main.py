from Trabajo.dicotomica import *

from Trabajo.topologia import *

from Trabajo.especificaciones import *

if __name__=="__main__":

  from Trabajo.dicotomica import dicotomia, dicot
  print("Ejercicio 1a")
  tabla = [3,5,1,8,9,2,0,7,6,4]
  print(tabla)
  resultado = dicotomia(tabla)
  print("La tabla ordenada es: {}".format(resultado.ordenar()))

  print("Ejercico 1b")
  final = dicot(tabla)
  print ("La tabla ordenada a partir de una lista vacia es {}".format(final.ordenar_lista()))

  from Trabajo.topologia import Lista
  print ("Ejercicio 2")
  L = [3,14,1,9,6,5,8,10,2]
  resultado = Lista(L)
  print ("El resultado es {}".format(resultado.ordenacion()))