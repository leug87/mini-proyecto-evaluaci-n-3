import pandas as pd

archivo_csv = r"C:\Users\mabo_\OneDrive\Escritorio\proyecto_ventas\ventas_productos_2.csv"

# Cargar el archivo en un DataFrame
df = pd.read_csv(archivo_csv, sep=";")

# Mostrar las primeras filas
print(df.head())
