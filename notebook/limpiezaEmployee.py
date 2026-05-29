import pandas as pd

def limpiar_simulacion_empleados(data_frame):
    data_frame_limpio = data_frame.copy()
    
    #1. Limpiar espacios en blanco en columnas de texto
    datos_texto = ['nombre', 'apellido', 'departamento', 'puesto', 'estado_empleado', 'tipo_contrato', 'nivel_educativo']
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()
    
    #2. Definir valores esperados 
    departamentos_validos = ["Ventas", "Recursos Humanos", "Finanzas", "Marketing", "Tecnología"]
    puestos_validos = ["Gerente", "Analista", "Asistente", "Coordinador", "Especialista"]
    estados_validos = ["Activo", "Inactivo", "En Permiso", "En Vacaciones", "En Capacitación", "En Prueba"]
    
    
    data_frame_limpio["departamento"] = data_frame_limpio["departamento"].where(
        data_frame_limpio["departamento"].isin(departamentos_validos),
        pd.NA
    )
    data_frame_limpio["puesto"] = data_frame_limpio["puesto"].where(
        data_frame_limpio["puesto"].isin(puestos_validos),
        pd.NA
    )
    data_frame_limpio["estado_empleado"] = data_frame_limpio["estado_empleado"].where(
        data_frame_limpio["estado_empleado"].isin(estados_validos),
        pd.NA
    )
    
    #3. Convertir columnas numericas
    data_frame_limpio["id"]= pd.to_numeric(data_frame_limpio["id"])

    #4. Convertir columna a fecha válida 
    data_frame_limpio["fecha_contratacion"] = pd.to_datetime(data_frame_limpio["fecha_contratacion"])
      
    #5. Reemplazar fechas nulas por una fecha por defecto
    fecha_defecto = pd.to_datetime("2019-01-01") 
    data_frame_limpio["fecha_contratacion"] = data_frame_limpio["fecha_contratacion"].fillna(fecha_defecto)
    
    #6. Eliminar filas que tienen datos obligatorios vacíos
    columnas_obligatorias = ["nombre", "apellido", "departamento", "puesto", "fecha_contratacion", "estado_empleado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    
    #7. Eliminar valores inválidos
    # Solo mantener empleados contratados entre 2010 y 2025
    data_frame_limpio = data_frame_limpio[
        (data_frame_limpio["fecha_contratacion"] >= pd.to_datetime("2010-01-01")) &
        (data_frame_limpio["fecha_contratacion"] <= pd.to_datetime("2025-12-31"))
    ]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    
    #8. Eliminar datos duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates(subset=['nombre', 'apellido'])
    
    #9. columnas de tipo string a mayuscula 
    columnas_texto = data_frame_limpio.select_dtypes(include=["object", "string"]).columns
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].str.upper()
    
    return data_frame_limpio