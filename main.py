import pandas as pd

# Ruta al archivo Excel
archivo_excel = 'D:/USER/Documents/1_carreras-con-impacto/1_fase_desarrollo-proyecto/resultados.xlsx'



# Elegir la hoja específica que deseas leer.
# Puedes poner el nombre de la hoja o el índice
nombre_hoja = 'No_experimentos'

# Leer el archivo Excel especificando la hoja
df = pd.read_excel(archivo_excel, sheet_name=nombre_hoja)

# Mostrar las primeras filas para comprobar la carga
print(df.head())