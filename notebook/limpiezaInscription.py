import pandas as pd

def limpiar_inscription(data_frame):
    data_frame_limpio = data_frame.copy()

    #limpiando espacios en blanco
    dato_texto = ["status"]
    for columna in dato_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #definir valores esperados
    status_validos = ["Inscrito", "Por inscribir"]
    data_frame_limpio ["status"] = data_frame_limpio["status"].where(data_frame_limpio["status"].isin(status_validos), pd.NA) 

    #convertir columnas numericas
    data_frame_limpio["registrationId"] = pd.to_numeric(data_frame_limpio["registrationId"])

    data_frame_limpio["employeeId"] = pd.to_numeric(data_frame_limpio["employeeId"])

    data_frame_limpio["courseId"] = pd.to_numeric(data_frame_limpio["courseId"])

    # convertir columna a fecha valida
    data_frame_limpio["registrationDate"] = pd.to_datetime(data_frame_limpio["registrationDate"])

    #reemplazar fechas nulas por una fecha por defecto
    fecha_defecto = pd.to_datetime("2026-01-01")
    data_frame_limpio["registrationDate"] = data_frame_limpio["registrationDate"].fillna(fecha_defecto)

    # eliminar valores invalidos
    columnas_obligatorias = ["registrationId", "employeeId", "courseId","status"]
    data_frame_limpio = data_frame_limpio.dropna(subset = columnas_obligatorias)

    #elimar valores invalidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["registrationId"] >= 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["employeeId"] >= 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["courseId"] > 0]

    #convertirlos en enteros
    cols = ["registrationId", "employeeId", "courseId"]
    data_frame_limpio[cols] = data_frame_limpio[cols].astype("Int64")

    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
