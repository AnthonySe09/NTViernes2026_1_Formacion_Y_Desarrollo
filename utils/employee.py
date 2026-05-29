#Simulando datos de una tabla en PYTHON

import random
from datetime import datetime, timedelta


def generar_empleados(numeroEmpleados):
    
    listaNombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía"]
    listaApellidos = ["García", "López", "Martínez", "Sánchez", "Pérez", "Gómez"]
    listaDepartamentos = ["Ventas", "Recursos Humanos", "Finanzas", "Marketing", "Tecnología", "Operaciones"]
    listaPuestos = ["Gerente", "Analista", "Asistente", "Coordinador", "Especialista", "Director"]
    listaEstadoEmpleado = ["Activo", "Inactivo", "En Permiso", "En Vacaciones", "En Capacitación", "En Prueba"]
    listaTipoContrato = ["Tiempo Completo", "Medio Tiempo", "Contrato Temporal", "Freelance"]
    listaNivelEducativo = ["Licenciatura", "Maestría", "Doctorado", "Técnico", "Bachillerato"]
    listaFechaContratacion = datetime(2019, 1, 1)
    
    empleados=[]
    for _ in range(numeroEmpleados):
        
        fecha=listaFechaContratacion + timedelta(days=random.randint(0, 1800))
        
        empleado = {
            "id":random.randint(0,200),
            "nombre": random.choice(listaNombres),
            "apellido": random.choice(listaApellidos),
            "fecha_contratacion": fecha.strftime("%Y-%m-%d"),
            "departamento": random.choice(listaDepartamentos),
            "puesto": random.choice(listaPuestos),
            "estado_empleado": random.choice(listaEstadoEmpleado),
            "tipo_contrato": random.choice(listaTipoContrato),
            "nivel_educativo": random.choice(listaNivelEducativo)
        }
        
        # Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.1:
            empleado["nombre"] = " " + empleado["nombre"] + " "
        elif probabilidadError < 0.2:
            empleado["apellido"] = empleado["apellido"].lower()
        elif probabilidadError < 0.3:
            empleado["fecha_contratacion"] = fecha.strftime("%Y/%m/%d")
        elif probabilidadError < 0.4:
            empleado["departamento"] = None
        elif probabilidadError < 0.5:
            empleado["tipo_contrato"] = ""
            
    
        empleados.append(empleado)
    return empleados    