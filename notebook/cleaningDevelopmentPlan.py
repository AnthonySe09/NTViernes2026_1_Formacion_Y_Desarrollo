# Limpieza de plan de desarrollo realizada por Adriano Jimenez Arboleda
import pandas as pd
from utils.DevelopmentPlan import listObjectives, listStatus
# definir funcion de limpieza
def cleanDevelopmentPlan (dataFrame):

    # Crear una copia de los datos y trabajar en ella
    cleanDataFrame = dataFrame.copy()

    # Estandarizarizacion y normalizacion de los id
    cleanDataFrame["idPlan"] = (pd.to_numeric(cleanDataFrame["idPlan"]
                                               .astype("string")
                                               .str.strip()))
    cleanDataFrame.loc[cleanDataFrame["idPlan"] < 0, "idPlan"] = pd.NA

    # Estandarizarizacion y normalizacion de fechas
    cleanDataFrame["startDate"] = (pd.to_datetime(cleanDataFrame["startDate"].astype("string").str.strip(), errors="coerce")
                                    .fillna(pd.to_datetime("2026-01-01")))

    # Convertir columnas a String, eliminar espacios en blanco y empezar primera letra en mayuscula y el resto minuscula, 
    # ademas definir registros validos 
    validValues = {
        "objective" : listObjectives,
        "status" : listStatus
    }
    textColumns =["objective", "status"]
    for column in textColumns:
        cleaned = (cleanDataFrame[column]
                                  .astype("string")
                                  .str.strip()
                                  .str.capitalize())
        cleanDataFrame[column] = cleaned.where(
            cleaned.isin(validValues[column]),pd.NA)
        
    # Definir columnas obligatorias y eliminar aquellas que tengan cualquier registro en NaN
    requiredColumns = ["idPlan", "startDate", "objective", "status"]
    cleanDataFrame = cleanDataFrame.dropna(subset=requiredColumns)

    # Eliminar duplicados
    cleanDataFrame = cleanDataFrame.drop_duplicates(subset=["idPlan"])
    
    # Retornar data frame con datos limpios
    return cleanDataFrame