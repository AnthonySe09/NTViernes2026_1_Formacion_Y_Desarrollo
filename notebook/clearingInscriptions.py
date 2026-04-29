import pandas as pd

def limpiar_inscripcion(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()

    #Rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y eliminar espacios en blanco y convertir a minusculas
    columnas_texto=["empleadoId","estado"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()

    #limpiar los textos solo con valores esperados
    estados_esperados=["inscrito", "en_curso", "completado", "cancelado"]
    data_frame_limpio["estado"]=data_frame_limpio["estado"].where(
          data_frame_limpio["estado"].isin(estados_esperados),
     pd.NA
    )

    #rutina para evaluar numeros
    #evaluar que las columnas numericas si son numeros
    data_frame_limpio["inscripcionId"]=pd.to_numeric(data_frame_limpio["inscripcionId"])
    data_frame_limpio["programaId"]=pd.to_numeric(data_frame_limpio["programaId"])

    #evaluar solo valores numericos permitidos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["inscripcionId"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["programaId"]>0]


    #rutina para evaluar fechas
    #evaluemos que una fecha si es una fecha
    data_frame_limpio["fechaInscripcion"]=pd.to_datetime(data_frame_limpio["fechaInscripcion"])

    #remplazar una fecha por defecto si el campo esta vacio
    fecha_default=pd.to_datetime("1998-05-28")
    data_frame_limpio["fechaInscripcion"]=data_frame_limpio["fechaInscripcion"].fillna(fecha_default)


    #rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["inscripcionId","empleadoId","programaId","estado"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio
