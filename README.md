# ejercicios-de-ordenar
El link de este repositorio es el siguiente:[GitHub](https://github.com/joseluis031/ejercicios-de-ordenar.git)

Hemos resuelto la tarea "Ejercicios de Ordenar", en la carpeta "Trabajo" y he realizado los UML correspondientes.

## Código de ejercicio de dicotomica
```class dicotomia:
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
  ```
  
  ## UML del ejercicio de dicotomica
  
  ![dicotomia uml](https://user-images.githubusercontent.com/91721888/158071371-430aa8d1-4bdd-42c9-97d5-f36b2613402d.png)

## Código del ejercicio de topologia
```class Lista:
    def __init__(self,L):
        self.L = L
    def ordenacion(self):
        for i in range(len(self.L)-1):
            for j in range(len(self.L)-1):
                if self.L[j]>self.L[j+1]:
                   print("Intercambio {} por {} ".format(self.L[j], self.L[j+1]))
                   self.L[j],self.L[j+1],self.L[j]
        return self.L
    
if __name__ == "__main__":  #no consigo que se ordene la lista
    L = [3,14,1,9,6,5,8,10,2]
    resultado = Lista(L)
    print ("El resultado es {}".format(resultado.ordenacion()))
```
## UML del ejercicio de topologia
   
   ![topologia uml](https://user-images.githubusercontent.com/91721888/158071438-33531812-3cc9-4425-8cd2-c02d5e354130.png)
