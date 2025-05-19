class Coche:
    def __init__ (self, gasolina):
        self.gasolina = gasolina        

    def arrancar(self):
        if self.gasolina > 0:
            print("arrancar")
        else:
            print("No arrancar")
            
    def avanzar(self):
        if self.gasolina >= 5:
            self.gasolina -= 5
            print(f"El coche avanzo. Gasolina restante: {self.gasolina}")
        else:
            print("No hay suficiente gasolina para avanzar")



BMW = Coche(100)
BMW.arrancar()

for i in range(BMW.gasolina // 5):
    BMW.avanzar()

