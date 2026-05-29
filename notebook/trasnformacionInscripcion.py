import pandas as pd

def transformar_datos_inscripciones(data_frame_limpio):

    resultados = {}

    # =====================================================
    # FILTRO 1
    # Inscripciones aprobadas
    # =====================================================
    filtro1 = data_frame_limpio.query("status == 'Aprobado'")

    agrupacion1 = (
        filtro1
        .groupby("courseId")["registrationId"]
        .count()
        .reset_index(name="cantidad_aprobados")
    )

    resultados["aprobados_por_curso"] = agrupacion1

    # =====================================================
    # FILTRO 2
    # Cursos con ID mayor a 10
    # =====================================================
    filtro2 = data_frame_limpio.query("courseId > 10")

    agrupacion2 = (
        filtro2
        .groupby("status")["registrationId"]
        .count()
        .reset_index(name="cantidad_inscripciones")
    )

    resultados["cursos_mayores_10"] = agrupacion2

    # =====================================================
    # FILTRO 3
    # Empleados con ID menor a 50
    # =====================================================
    filtro3 = data_frame_limpio.query("employeeId < 50")

    agrupacion3 = (
        filtro3
        .groupby("employeeId")["registrationId"]
        .count()
        .reset_index(name="cantidad_registros")
    )

    resultados["empleados_menores_50"] = agrupacion3

    # =====================================================
    # FILTRO 4
    # Inscripciones pendientes
    # =====================================================
    filtro4 = data_frame_limpio.query("status == 'Pendiente'")

    agrupacion4 = (
        filtro4
        .groupby("registrationDate")["registrationId"]
        .count()
        .reset_index(name="cantidad_pendientes")
    )

    resultados["pendientes_por_fecha"] = agrupacion4

    # =====================================================
    # FILTRO 5
    # Inscripciones rechazadas
    # =====================================================
    filtro5 = data_frame_limpio.query("status == 'Rechazado'")

    agrupacion5 = (
        filtro5
        .groupby("courseId")["employeeId"]
        .nunique()
        .reset_index(name="empleados_unicos")
    )

    resultados["rechazados_por_curso"] = agrupacion5

    return resultados