import pandas as pd

#Funcion para describir la estructura general del dataset
def describir_estructura(data_frame_limpio):
    print("*** ESTRUCTURA GENERAL ***")
    print(f"Número de filas: {data_frame_limpio.shape[0]}")
    print(f"Número de columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {(data_frame_limpio.columns)}")

#Funcion para describir estadisticas del data frame
def describir_estadisticas(data_frame_limpio):
    print("\n***ESTADISTICAS***")
    print(f"{data_frame_limpio[['id', 'fecha_contratacion']].describe()}")

#Funcion para medir las columnas categoricas
def describir_categoricas(data_frame_limpio):
    print("\n*** FRECUENCIAS CATEGORICAS ***")
    print("Departamentos:")
    print(f"{data_frame_limpio['departamento'].value_counts()}")
    print()
    print("Puestos:")
    print(f"{data_frame_limpio['puesto'].value_counts()}")
    print()
    print("Estados de empleados:")
    print(f"{data_frame_limpio['estado_empleado'].value_counts()}")

#Funcion para describir los rangos de fechas
def describir_fechas(data_frame_limpio):
    print("\n*** RANGOS DE FECHAS ***")
    print(f"Fecha mínima: {data_frame_limpio['fecha_contratacion'].min()}")
    print(f"Fecha máxima: {data_frame_limpio['fecha_contratacion'].max()}")