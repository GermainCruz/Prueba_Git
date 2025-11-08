import numpy as np
import matplotlib.pyplot as plt

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_Estudiante = []
    
    def ingresar_Datos(self):
        while True:    
            try:
                print(f"\nHola, estudiante {self.nombre}")
                nro = int(input("Número de elementos de la lista de notas: "))
                for i in range(nro):
                    num = int(input(f"Ingrese nota N°{i+1}: "))
                    self.lista_Estudiante.append(num)
            except ValueError:
                print("Debes ingresar un NÚMERO ENTERO")
            else:
                if nro>0:
                    return nro
                elif nro == 0:
                    print("Debes ingresar un número DIFERENTE de CERO")
                else:
                    print("Debes ingresar un número entero POSITIVO")    

    def calcular_Promedio(self):
        return np.mean(self.lista_Estudiante)

    def calcular_Mayor(self):
        return np.max(self.lista_Estudiante)
    
    def calcular_Menor(self):
        return np.min(self.lista_Estudiante)

    def graficar_Notas(self):
        # Datos
        ejex = []
        for i in range(len(self.lista_Estudiante)):
            ejex.append(i+1)
        
        # Uso de plot
        plt.plot(ejex, self.lista_Estudiante, linestyle='-', marker='o', color='red', label="Línea de notas")

        # Personalización opcional
        plt.title('Gráfico de Líneas')
        plt.xlabel('Nota N°')
        plt.ylabel('Notas')
        plt.legend()
        plt.grid(True)

        # Mostrar el gráfico
        plt.show()

# Main: 
estudiante = Estudiante("Germain")
estudiante.ingresar_Datos()
print(f"\nPromedio: {estudiante.calcular_Promedio()}")
print(f"Nota mayor: {estudiante.calcular_Mayor()}")
print(f"Nota menor: {estudiante.calcular_Menor()}")
print("\nGráfico: ")
estudiante.graficar_Notas()