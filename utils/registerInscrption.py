import random

from datetime import datetime, timedelta

def generar_inscripciones(numero_inscripciones):

    estados_validos = ["inscrito", "en_curso", "completado", "cancelado"]
    fecha_inicio = datetime(2026, 1, 1)

    inscripciones = []
    for _ in range(numero_inscripciones):


        inscripcion = {
            "inscripcionId": random.randint(1, 5000),
            "empleadoId": random.randint(1, 1000),
            "programaId": random.randint(1, 200),
            "estado": random.choice(estados_validos),
            "fechaInscripcion": fecha_inicio + timedelta(days=random.randint(0, 30))
        }





#Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            inscripcion["inscripcionId"]=None
        elif(probabilidadError<0.4):
            inscripcion["empleadoId"]=random.choice(["clase de baile","clase de cocina"])
        elif(probabilidadError<0.5):
            inscripcion["programaId"]=random.choice([0,-10000,None])
        elif(probabilidadError<0.8):
            inscripcion["estado"]=" "+inscripcion["estado"].upper()
        elif(probabilidadError<0.9):
            inscripcion["fechaInscripcion"]=None

        inscripciones.append(inscripcion)
    return inscripciones