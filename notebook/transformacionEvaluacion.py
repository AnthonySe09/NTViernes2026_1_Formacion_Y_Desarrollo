import pandas as pd

def transformar_datos_evaluacion(data_frame_limpio):

    # =========================================================
    # FILTRO 1:
    # Evaluaciones con score fuera del rango permitido (0-5)
    # =========================================================
    filtro_1 = data_frame_limpio.query("score > 5 or score < 0")

    agrupacion_1 = (
        filtro_1.groupby("evaluationType")["score"]
        .count()
        .reset_index(name="cantidad_scores_invalidos")
    )

    # =========================================================
    # FILTRO 2:
    # Comentarios vacíos, nulos o con espacios
    # =========================================================
    filtro_2 = data_frame_limpio[
        data_frame_limpio["comments"].isna() |
        (data_frame_limpio["comments"].str.strip() == "")
    ]

    agrupacion_2 = (
        filtro_2.groupby("evaluationType")["comments"]
        .count()
        .reset_index(name="comentarios_vacios")
    )

    # =========================================================
    # FILTRO 3:
    # employeeId no numérico
    # =========================================================
    filtro_3 = data_frame_limpio[
        pd.to_numeric(data_frame_limpio["employeeId"], errors="coerce").isna()
    ]

    agrupacion_3 = (
        filtro_3.groupby("courseId")["employeeId"]
        .count()
        .reset_index(name="empleados_id_error")
    )

    # =========================================================
    # FILTRO 4:
    # evaluationType inválido o con espacios
    # =========================================================
    tipos_validos = [
        "Autoevaluacion",
        "EvaluacionJefe",
        "EvaluacionPar"
    ]

    filtro_4 = data_frame_limpio[
        ~data_frame_limpio["evaluationType"].str.strip().isin(tipos_validos)
    ]

    agrupacion_4 = (
        filtro_4.groupby("evaluationType")["evaluationId"]
        .count()
        .reset_index(name="tipos_invalidos")
    )

    # =========================================================
    # FILTRO 5:
    # Fechas erróneas
    # =========================================================
    filtro_5 = data_frame_limpio[
        pd.to_datetime(
            data_frame_limpio["evaluationDate"],
            format="%Y/%m/%d",
            errors="coerce"
        ).isna()
    ]

    agrupacion_5 = (
        filtro_5.groupby("courseId")["evaluationDate"]
        .count()
        .reset_index(name="fechas_erroneas")
    )

    return {
        "filtro_1": filtro_1,
        "agrupacion_1": agrupacion_1,

        "filtro_2": filtro_2,
        "agrupacion_2": agrupacion_2,

        "filtro_3": filtro_3,
        "agrupacion_3": agrupacion_3,

        "filtro_4": filtro_4,
        "agrupacion_4": agrupacion_4,

        "filtro_5": filtro_5,
        "agrupacion_5": agrupacion_5
    }