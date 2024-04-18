# Se importa la libreria pandas con el alias pd
import pandas as pd

# Se crea una lista con las edades
edades = [19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22,19,29,19,22,23,19,30,19,20]

# Se crea un DataFrame a partir de la lista 'data' con una columna llamada 'Edades'
df = pd.DataFrame(edades, columns=['Edades'])

# Se define una funcion que toma un DataFrame 'df' como argumento
def analisis_estadistico(df):
    # Condición que verifica si la lista está vacía. Si no lo está sigue el proceso de calculo
    if df.empty:
        print("La lista de edades está vacía.")
    else: 
        # Calcular la frecuencia absoluta de cada edad
        data_frame = df['Edades'].value_counts().reset_index()

        # Renombrar las columnas
        data_frame.columns = ['Edades', 'fi']

        # Calcular la frecuencia acumulada
        data_frame['Fi'] = data_frame['fi'].cumsum()

        # Calcular la frecuencia relativa
        data_frame['fr'] = (data_frame["fi"] / data_frame["fi"].sum()).round(2)

        # Calcular la frecuencia relativa acumulada
        data_frame["Fr"] = data_frame["fr"].cumsum()

        # Calcular el porcentaje de la frecuencia relativa
        data_frame["pi%"] = data_frame["fr"] * 100

        # Calcular el porcentaje de la frecuencia relativa acumulada
        data_frame["Pi%"] = data_frame["Fr"] * 100

        # Retornar el DataFrame con las estadisticas calculadas
        return data_frame

# Llamar a la funcion que devuelve los calculos de frecuencias e imprimir
print(analisis_estadistico(df))