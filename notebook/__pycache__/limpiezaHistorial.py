import pandas as pd

def limpiar_inscripcion(registros):

    # convertir lista de diccionarios a DataFrame para limpieza
    data_frame_sucio = pd.DataFrame(registros)
    data_frame_limpio = data_frame_sucio.copy()

    # =========================
    # LIMPIEZA DE TEXTOS 
    # =========================
    columnas_texto = ["estado"]

    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # estados válidos (alineado a TU generador)
    estados_esperados = ["inscrito", "en_curso", "completado", "reprobado"]

    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(estados_esperados),
        pd.NA
    )

    # =========================
    # LIMPIEZA DE NUMEROS
    # =========================
    columnas_numericas = ["inscripcionId", "empleadoId", "programaId", "avance", "nota"]

    for columna in columnas_numericas:
        data_frame_limpio[columna] = pd.to_numeric(data_frame_limpio[columna], errors="coerce")

    # eliminar valores inválidos
    data_frame_limpio = data_frame_limpio[
        (data_frame_limpio["inscripcionId"] > 0) &
        (data_frame_limpio["empleadoId"] > 0) &
        (data_frame_limpio["programaId"] > 0)
    ]

    # =========================
    # LIMPIEZA DE FECHAS
    # =========================
    data_frame_limpio["fechaInscripcion"] = pd.to_datetime(
        data_frame_limpio["fechaInscripcion"],
        errors="coerce"
    )

    fecha_default = pd.to_datetime("1998-05-28")

    data_frame_limpio["fechaInscripcion"] = data_frame_limpio["fechaInscripcion"].fillna(fecha_default)

    # =========================
    # CAMPOS OBLIGATORIOS
    # =========================
    columnas_obligatorias = ["inscripcionId", "empleadoId", "programaId", "estado"]

    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio