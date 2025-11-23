import pandas as pd
import matplotlib.pyplot as plt
class Curso:
    def __init__(self):
        self.lista_estudiantes = []

    def ingresar_Datos(self):   
        try:
            nro = int(input("Ingrese el número estudiantes: "))
            
            for i in range(nro):
                print(f"\nEstudiante N°{i+1}")
                
                nombre = input("Nombre: ")
                promedio = float(input("Promedio: "))

                estudiante = {"Nombre":nombre, "Promedio":promedio} 
                self.lista_estudiantes.append(estudiante)
        except ValueError:
            print("Debes ingresar un NÚMERO ENTERO")
        else:
            if nro>=0:
                return nro
            else:
                print("Debes ingresar un número entero POSITIVO")      

    def exportando_a_dataframe(self):
        dataframe = pd.DataFrame(self.lista_estudiantes)
        if dataframe.empty:
            print("Dataframe vacío.")
            return None
        else:
            print("\nDataframe generado: ")
            print(dataframe)
            return dataframe

    def graficar_histograma(self, dataframe):
        try:
            if dataframe is None:
                raise ValueError("El Dataframe está vacío. No se puede graficar.")
            plt.hist(dataframe['Promedio'], bins=20, color='green', alpha=0.7)  # alpha: es la transparencia de las barras
            # Personalización opcional
            plt.title('Histograma de Promedios')
            plt.xlabel('Promedio')
            plt.ylabel('Cantidad de Estudiantes')
            plt.grid(True)

            # Mostrar el histograma
            plt.show()
        except Exception as e:
            print(f"Error al graficar: {e}")

# Main
curso = Curso()
curso.ingresar_Datos()
dataframe = curso.exportando_a_dataframe()
curso.graficar_histograma(dataframe)