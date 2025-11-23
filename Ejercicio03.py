import numpy as np
import matplotlib.pyplot as plt

class SimularDados:
    def __init__(self):
        self.lista_resultados = []

    def ingresar_Cantidad_Dados(self):
        while True: 
            try:
                nroDados = int(input("Número de dados a lanzar: "))
            
            except ValueError:
                print("Debes ingresar un número ENTERO")
            else:
                if nroDados>0:
                    return nroDados
                else:
                    print("Debes ingresar un NÚMERO POSITIVO y DIFERENTE de CERO")

    def lanzar_Dados(self, nroDados):
        print("RESULTADOS:")
        resultados = np.random.randint(1, 7, nroDados, int)
        self.lista_resultados = resultados.tolist()
        print(f"Resultados de {nroDados} dados: {self.lista_resultados}")
    
    def realizar_Calculos(self):
        media = np.mean(self.lista_resultados)
        varianza = np.var(self.lista_resultados)
        valores, frecuencias = np.unique(self.lista_resultados, return_counts=True)
        valores = valores.tolist()
        frecuencias = frecuencias.tolist()

        print(f"La media es: {media}")
        print(f"La varianza es: {varianza}")
        print(f"Los valores son {valores} y su frecuencia es {frecuencias}")

        return valores, frecuencias

    def graficar(self, valores, frecuencias):  
        print("Gráfico: ")  
        # Crear gráfico de barras
        plt.bar(valores, frecuencias, color='skyblue', alpha=0.7)

        # Personalización opcional
        plt.title("Gráfico de barras")
        plt.xlabel("Caras de un dado")
        plt.ylabel("Frecuencia")
        plt.show()

# Main
dadito = SimularDados()
nroDados = dadito.ingresar_Cantidad_Dados()
dadito.lanzar_Dados(nroDados)
valores, frecuencias = dadito.realizar_Calculos()
dadito.graficar(valores, frecuencias)


# numpy.random.randint(low, high=None, size=None, dtype=int)
# (mínimo, máximo, N° de números aleatorios, tipo de dato)