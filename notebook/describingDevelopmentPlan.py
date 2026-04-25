import pandas as pd

# Describir la estructura general del dataset
def describeStructure(cleanDataFrame):
    print("--- Estructura general ---")
    print(f"Numero de filas: {cleanDataFrame.shape[0]}")
    print(f"Numero de columnas: {cleanDataFrame.shape[1]}")
    print(f"Columnas disponibles: {list(cleanDataFrame)}")
# Describir estadisticas del data frame
def describeStatistics(cleanDataFrame):
    print(f"\n?---Estadisticas---")
    print(f"{cleanDataFrame[["idPlan"]].describe()}")
# Medir columnas categoricas
def describeCategories(cleanDataFrame):
    print(f"\n?---Frecuencias categoricas---")
    print(f"\n?Servicios ofrecidos")
    print(f"{cleanDataFrame["objective"].value_counts()}")
    print("")
    print(f"{cleanDataFrame["status"].value_counts()}")
# Describir rangos de fechas
def describeDates(cleanDataFrame):
    print(f"\n---Rangos de fechas---")
    print(f"\n fecha minima: {cleanDataFrame["startDate"].min()}")
    print(f"\n fecha minima: {cleanDataFrame["startDate"].max()}")