class Lista:
  def __init__(self,lista):
    self.lista = lista
  def ordenacion(self):
    for i in range(len(self.lista)-1):
      for j in range(len(self.lista)-1):
        if self.lista[j]>self.lista[j+1]:
          print("Intercambio {} por {} ".format(self.lista[j], self.lista[j+1]))
          self.lista[j],self.lista[j+1],self.lista[j]
    return self.lista
          