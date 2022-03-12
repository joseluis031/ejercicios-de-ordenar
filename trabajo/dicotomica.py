class dicotomia:
  def __init__(self,tabla):
     self.tabla = tabla

  def ordenar(self):
    self.tabla.sort()
    return self.tabla

class dicot:
  def __init__(self,tabla):
    dicotomia.__init__(self,tabla)
    l = []
    self.l = l
  def ordenar_lista(self):
    dicotomia.ordenar(self)
    for i in self.tabla:
      self.l.append(i)
    return self.l

if __name__ == "__main__":
  tabla = [3,5,1,8,9,2,0,7,6,4]
  print(tabla)
  resultado = dicotomia(tabla)
  print("La tabla ordenada es: {}".format(resultado.ordenar()))
  final = dicot(tabla)
  print ("La tabla ordenada a partir de una lista vacia es: {}".format(final.ordenar_lista()))