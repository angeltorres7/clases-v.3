class Coche:
    def __init__ (self, gasolina):
       self.gasolina = gasolina        


    def arrancar(self):
       if self.gasolina >0:
            print("arrancar")
       else:
            print("No arrancar")
            
    def avanzar(self):
        if self.gasolina > 0:
            self.gasolina -= 5
            print(f"El coche avanzo. Gasolina restante: {self.gasolina}")
        else:
            print("No hay suficiente gasolina para avanzar")
  
BMW=Coche(100)
BMW.arrancar()

while BMW.gasolina >= -1:
    BMW.avanzar() 
    
print(BMW)   