import pandas as pd

def transformar_datos_empleado(data_frame_limpio):

# =========================================
# FILTRO 1:
# Cantidad de empleados contratados por fecha
# =========================================

    filtro1=data_frame_limpio

    agrupacion1Empleado = (
        filtro1
        .groupby("fecha_contratacion")["id"]
        .count()
        .reset_index(name="cantidad_empleados")
    )

# =========================================
# FILTRO 2:
# Cantidad de empleados por departamento
# =========================================

    filtro2 = data_frame_limpio

    agrupacion2Empleado = (
        filtro2
        .groupby("departamento")["id"]
        .count()
        .reset_index(name="total_empleados")
    )


# =========================================
# FILTRO 3:
# Cantidad de empleados por estado
# =========================================

    filtro3 = data_frame_limpio

    agrupacion3Empleado = (
        filtro3
        .groupby("estado_empleado")["id"]
        .count()
        .reset_index(name="cantidad")
    )


# =========================================
# FILTRO 4:
# Cantidad de empleados por tipo de contrato
# =========================================

    filtro4 = data_frame_limpio

    agrupacion4Empleado = (
        filtro4
        .groupby("tipo_contrato")["id"]
        .count()
        .reset_index(name="cantidad_contratos")
    )


# =========================================
# FILTRO 5:
# Cantidad de empleados por nivel educativo
# =========================================

    filtro5 = data_frame_limpio

    agrupacion5Empleado = (
        filtro5
        .groupby("nivel_educativo")["id"]
        .count()
        .reset_index(name="cantidad_personas")
    )

    
# =========================================
# FILTRO extra:
# =========================================

    filtro_extra = data_frame_limpio.query("estado_empleado == 'Activo'")

    agrupacion_extraEmpleado = (
        filtro_extra
        .groupby("departamento")["id"]
        .count()
        .reset_index(name="empleados_activos")
    )

    
# =========================================
# FILTRO extra:
# =========================================

    filtro_indefinido = data_frame_limpio.query("tipo_contrato == 'Indefinido'")

    agrupacion_indefinidoEmpleado = (
        filtro_indefinido
        .groupby("puesto")["id"]
        .count()
        .reset_index(name="cantidad")
    )

    return {
        "filtro_1": filtro1,
        "agrupacion_1Empleado": agrupacion1Empleado,

        "filtro_2": filtro2,
        "agrupacion_2Empleado": agrupacion2Empleado,

        "filtro_3": filtro3,
        "agrupacion_3Empleado": agrupacion3Empleado,

        "filtro_4": filtro4,
        "agrupacion_4Empleado": agrupacion4Empleado,

        "filtro_5": filtro5,
        "agrupacion_5Empleado": agrupacion5Empleado,

        "filtro_extra": filtro_extra,
        "agrupacion_extraEmpleado": agrupacion_extraEmpleado,

        "filtro_indefinido": filtro_indefinido,
        "agrupacion_indefinidoEmpleado": agrupacion_indefinidoEmpleado
    }
