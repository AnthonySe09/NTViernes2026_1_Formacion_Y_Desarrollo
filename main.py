import pandas as pd
#IMPORTAR SIMULACIONES
from utils.evaluation import generar_evaluaciones
from utils.Inscription import generateRegistration
from utils.DevelopmentPlan import generateDevelopmentPlans
#from utils. employee import generar_empleados

#ZONA PARA IMPORTAR LIMPIEZAS
from notebook.limpiezaEvaluacion import limpiar_evaluacion
from notebook.limpiezaInscription import limpiar_inscription
from notebook.cleaningDevelopmentPlan import cleanDevelopmentPlan
#from notebook.limpiezaEmployee import limpiar_simulacion_empleados

#ZONA PARA IMPORTAR DESCRIPCIOENS
from notebook.descripcionEvaluacion import describirEstructura, describirEstadisticas, describirCategoricas, describirFechas
from notebook.describingDevelopmentPlan import describeStructure, describeStatistics, describeCategories, describeDates
from notebook.descripcion_Inscripcion import describir_estructura, describir_estadisticas, describir_categoricas, describir_fechas
#from notebook.descripcionEmployee import describir_estructura, describir_estadisticas, describir_categoricas, describir_fechas

#IMPORTAR TRANSFORMACIONES
from notebook.transformacionEvaluacion import transformar_datos_evaluacion
from notebook.trasnformacionInscripcion import transformar_datos_inscripciones

#CREANDO SIMULACIONES
evaluations=generar_evaluaciones(100)
registrations=generateRegistration(10)
developmentPlans=generateDevelopmentPlans(10)
#empleados = generar_empleados(10)

#CREANDO LIMPIEZA DE DATOS
evaluaciones_ordenadas=pd.DataFrame(evaluations)
evaluaciones_ordenadas_limpias=limpiar_evaluacion(evaluaciones_ordenadas)
print(evaluaciones_ordenadas_limpias)


inscripciones_ordenadas=pd.DataFrame(registrations)
inscripciones_ordenadas_limpias=limpiar_inscription(inscripciones_ordenadas)
print(inscripciones_ordenadas_limpias)


planDesarrollo_ordenadas = pd.DataFrame(developmentPlans)  
planDesarrollo_ordenadas_limpias = cleanDevelopmentPlan(planDesarrollo_ordenadas)  # limpiar
print(planDesarrollo_ordenadas_limpias)

#empleados_ordenadas = pd.DataFrame(empleados)
#empleados_ordenadas_limpias = limpiar_simulacion_empleados(empleados_ordenadas)
#print(empleados_ordenadas_limpias)

#DESCRIBIENDO EL SET DE DATOS 

describirEstructura(evaluaciones_ordenadas_limpias)
describirEstadisticas(evaluaciones_ordenadas_limpias)
describirCategoricas(evaluaciones_ordenadas_limpias)
describirFechas(evaluaciones_ordenadas_limpias)

describeStructure(planDesarrollo_ordenadas_limpias)
describeStatistics(planDesarrollo_ordenadas_limpias)
describeCategories(planDesarrollo_ordenadas_limpias)
describeDates(planDesarrollo_ordenadas_limpias)

describir_estructura(inscripciones_ordenadas_limpias)
describir_estadisticas(inscripciones_ordenadas_limpias)
describir_categoricas(inscripciones_ordenadas_limpias)
describir_fechas(inscripciones_ordenadas_limpias)

#describir_estructura(empleados_ordenadas_limpias)
#describir_estadisticas(empleados_ordenadas_limpias)
#describir_categoricas(empleados_ordenadas_limpias)
#describir_fechas(empleados_ordenadas_limpias)

# TRANSFORMACIONES
print("\n" + "="*80)
print("TRANSFORMACIÓN DE EVALUACIONES")
print("="*80)

transformacion_evaluaciones = transformar_datos_evaluacion(evaluaciones_ordenadas_limpias)

print("\nFiltro 1 - Scores inválidos (fuera del rango 0-5):")
print(transformacion_evaluaciones["filtro_1"])
print("\nAgrupación por tipo de evaluación:")
print(transformacion_evaluaciones["agrupacion_1"])

print("\nFiltro 2 - Comentarios vacíos:")
print(transformacion_evaluaciones["filtro_2"])
print("\nAgrupación de comentarios vacíos:")
print(transformacion_evaluaciones["agrupacion_2"])

print("\nFiltro 3 - EmpleadoIDs no numéricos:")
print(transformacion_evaluaciones["filtro_3"])
print("\nAgrupación de IDs erróneos por curso:")
print(transformacion_evaluaciones["agrupacion_3"])

print("\nFiltro 4 - Tipos de evaluación inválidos:")
print(transformacion_evaluaciones["filtro_4"])
print("\nAgrupación de tipos inválidos:")
print(transformacion_evaluaciones["agrupacion_4"])

print("\nFiltro 5 - Fechas erróneas:")
print(transformacion_evaluaciones["filtro_5"])
print("\nAgrupación de fechas erróneas por curso:")
print(transformacion_evaluaciones["agrupacion_5"])

print("\n" + "="*80)
print("TRANSFORMACIÓN DE INSCRIPCIONES")
print("="*80)

transformacion_inscripciones = transformar_datos_inscripciones(inscripciones_ordenadas_limpias)

print("\nAprobados por curso:")
print(transformacion_inscripciones["aprobados_por_curso"])

print("\nCursos con ID mayor a 10 - Inscripciones por estado:")
print(transformacion_inscripciones["cursos_mayores_10"])

print("\nEmpleados con ID menor a 50 - Cantidad de registros:")
print(transformacion_inscripciones["empleados_menores_50"])

print("\nInscripciones pendientes por fecha:")
print(transformacion_inscripciones["pendientes_por_fecha"])

print("\nInscripciones rechazadas - Empleados únicos por curso:")
print(transformacion_inscripciones["rechazados_por_curso"])