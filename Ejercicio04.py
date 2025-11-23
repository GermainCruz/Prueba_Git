import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Tienda:
    def __init__(self):
        self.lista_ventas = []

    def registrar_Ventas(self):
        while True:    
            try:
                n = int(input("Número de ventas que ha realizado: "))
                
                for i in range(n):
                    print(f"\nVenta N°{i+1}:")

                    producto = input("Producto: ")
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: "))

                    venta = {"Producto": producto, "Cantidad":cantidad, "Precio": precio}

                    self.lista_ventas.append(venta)

            except ValueError:
                print("Debes ingresar un NÚMERO ENTERO")
            else:
                if n > 0:
                    return n
                elif n == 0:
                    print("Debes ingresar un número DIFERENTE de CERO")
                else:
                    print("Debes ingresar un número entero POSITIVO")

    def exportando_a_dataframe(self):
        dataframe = pd.DataFrame(self.lista_ventas)
        print("\nDataframe generado: ")
        print(dataframe)
        return dataframe
    
    def realizar_calculos(self, dataframe):
        if dataframe.empty:
            print("No hay ventas registradas")
            return None        
        
        total_vendido = (dataframe['Cantidad'] * dataframe['Precio']).sum()
        
        ventas_por_producto = dataframe.groupby('Producto')['Cantidad'].sum()
        producto_mas_vendido = ventas_por_producto.idxmax()
        # Para el gráfico:
        dataframe['Ingreso'] = dataframe['Cantidad'] * dataframe['Precio']
        ventas_por_producto_dinero = dataframe.groupby('Producto')['Ingreso'].sum()

        ingresos_por_transaccion = (dataframe['Cantidad'] * dataframe['Precio'])
        promedio = np.mean(ingresos_por_transaccion)

        print(f"\nTotal vendido: {total_vendido}")
        print(f"Producto más vendido: {producto_mas_vendido}")
        print(f"Promedio de ventas por transacción: {promedio}")
        
        return ventas_por_producto_dinero

    def graficar_ventas_por_Producto(self, ventas_por_producto):
        if ventas_por_producto is None:
            print("No hay datos para graficar")
            return
        
        print("Gráfico: ")
        #Crear gráfico de barras:
        plt.bar(ventas_por_producto.index, ventas_por_producto.values, color='red', alpha=0.7)

        # Personalización opcional
        plt.title("Gráfico de barras")
        plt.xlabel("Productos")
        plt.ylabel("Ventas")
        plt.show()        
        
# Main
tiendita = Tienda()
tiendita.registrar_Ventas()
dataframe = tiendita.exportando_a_dataframe()
ventas_por_producto_dinero = tiendita.realizar_calculos(dataframe)
tiendita.graficar_ventas_por_Producto(ventas_por_producto_dinero)