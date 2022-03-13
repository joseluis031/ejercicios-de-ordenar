class Lista:
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