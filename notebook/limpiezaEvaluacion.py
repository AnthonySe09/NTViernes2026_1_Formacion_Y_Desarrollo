#LIMPIEZA CREADA POR ANTHONY
import pandas as pd
def limpiar_evaluacion(data_frame):
    data_frame_limpio=data_frame.copy()
    #1.LIMPIAR ESPACIOS EN BLANCO
    datos_texto=["evaluationTypes", "comments"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. definir valores esperados
    evaluaciones_validas=["Excelente trabajo", "Buen esfuerzo", "Necesita mejorar", "No cumplio con los requisitos", "Trabajo sobresaliente"]
    data_frame_limpio["evaluationTypes"]=data_frame_limpio["evaluationTypes"].where(
        data_frame_limpio["evaluationTypes"].isin(evaluaciones_validas),pd.NA
    )
    #3.convertir columnas numericas 
    data_frame_limpio["evaluationId"]=pd.to_numeric(data_frame_limpio["evaluationId"])
    data_frame_limpio["employeeId"]=pd.to_numeric(data_frame_limpio["employeeId"])

    #4. convertir columnas de tipo fecha
    data_frame_limpio["evaluationDate"] = pd.to_datetime(data_frame_limpio["evaluationDate"])

    #5. Reemplazar fechas Nulas por fecha por defecto
    fecha_defecto=pd.to_datetime("2026-01-01")
    data_frame_limpio["evaluationDate"]=data_frame_limpio["evaluationDate"].fillna(fecha_defecto)

    #6. Eliminar filas que traen datos obligatorios vacios
    columnas_obligatorias=["evaluationId", "employeeId", "courseId"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #7 eliminar valores invalidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["evaluationId"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["employeexId"]>0]

    #8. Eliminar datos duplicados

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
