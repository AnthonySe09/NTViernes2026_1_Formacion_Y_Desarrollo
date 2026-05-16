import pandas as pd

def transformar_datos_empleados(data_frame_limpio):

    resultados = {}

    # =====================================================
    # FILTRO 1
    # Empleados activos
    # =====================================================
    filtro1 = data_frame_limpio[
        data_frame_limpio["estado_empleado"] == "Activo"
    ]

    agrupacion1 = (
        filtro1
        .groupby("departamento")
        .size()
        .reset_index(name="cantidad_empleados")
    )

    resultados["empleados_activos_departamento"] = agrupacion1

    # =====================================================
    # FILTRO 2
    # Contrato indefinido
    # =====================================================
    filtro2 = data_frame_limpio[
        data_frame_limpio["tipo_contrato"] == "Indefinido"
    ]

    agrupacion2 = (
        filtro2
        .groupby("puesto")
        .size()
        .reset_index(name="cantidad_empleados")
    )

    resultados["contrato_indefinido_puesto"] = agrupacion2

    # =====================================================
    # FILTRO 3
    # Nivel educativo universitario
    # =====================================================
    filtro3 = data_frame_limpio[
        data_frame_limpio["nivel_educativo"] == "Universitario"
    ]

    agrupacion3 = (
        filtro3
        .groupby("departamento")
        .size()
        .reset_index(name="cantidad_profesionales")
    )

    resultados["universitarios_departamento"] = agrupacion3

    # =====================================================
    # FILTRO 4
    # Empleados retirados
    # =====================================================
    filtro4 = data_frame_limpio[
        data_frame_limpio["estado_empleado"] == "Retirado"
    ]

    agrupacion4 = (
        filtro4
        .groupby("tipo_contrato")
        .size()
        .reset_index(name="cantidad_retirados")
    )

    resultados["retirados_tipo_contrato"] = agrupacion4

    # =====================================================
    # FILTRO 5
    # Empleados del departamento TI
    # =====================================================
    filtro5 = data_frame_limpio[
        data_frame_limpio["departamento"] == "TI"
    ]

    agrupacion5 = (
        filtro5
        .groupby("fecha_contratacion")
        .size()
        .reset_index(name="cantidad_contrataciones")
    )

    resultados["contrataciones_ti_fecha"] = agrupacion5

    return resultados