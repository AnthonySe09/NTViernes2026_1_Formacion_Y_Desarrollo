import pandas as pd


#funcion para describir la estructura general del data set
def describirEstructura(data_frame_limpio):
    print("***** ESTRUCTURA GENERAL *****")
    print(f"Numero de filas: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles {list(data_frame_limpio.columns)}")

#Funcion para describir estadisticas del data frame
def describirEstadisticas(data_frame_limpio):
    print("\n***** ESTADISTICAS GENERALES *****")
    
    columnas = ["evaluationId", "employeeId", "courseId", "score"]
    columnas_existentes = [col for col in columnas if col in data_frame_limpio.columns]
    
    if columnas_existentes:
        print(data_frame_limpio[columnas_existentes].describe())
    else:
        print("No hay columnas numéricas disponibles para describir.")

#funcion para medir las columnas categoricas
def describirCategoricas(data_frame_limpio):
    print("\n***** FRECUENCIAS CATEGORICAS *****")
    
    if "evaluationType" in data_frame_limpio.columns:
        print("TIPOS DE EVALUACION")
        print(data_frame_limpio['evaluationType'].value_counts())
        print()
    
    if "comments" in data_frame_limpio.columns:
        print("COMENTARIOS")
        print(data_frame_limpio['comments'].value_counts())

#Funcion para describir los rangos de fechas
def describirFechas (data_frame_limpio):
    print("\n***** RANGOS DE FECHAS *****")
    
    if "evaluationDate" in data_frame_limpio.columns:
        print(f"fecha minima: {data_frame_limpio['evaluationDate'].min()}")
        print(f"fecha maxima: {data_frame_limpio['evaluationDate'].max()}")
    else:
        print("No hay columna de fechas disponible.")