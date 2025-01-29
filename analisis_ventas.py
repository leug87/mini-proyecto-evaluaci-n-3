import pandas as pd

archivo_csv = r"C:\Users\mabo_\OneDrive\Escritorio\proyecto_ventas\ventas_productos.csv"

# Cargar el archivo en un DataFrame
df = pd.read_csv(archivo_csv, sep=";")

# Mostrar las primeras filas
print(df.head())

df['Precio_Total'] = df['Cantidad'] * df['Precio']
print(df.head())

import matplotlib.pyplot as plt

plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.savefig('grafico_precios.png')  # Guardar el gráfico como PNG
plt.show()