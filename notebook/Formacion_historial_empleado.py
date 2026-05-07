
import random
from datetime import datetime, timedelta

def historial_empleados(cantidad_registros):

    estados_validos = ["inscrito", "en_curso", "completado", "reprobado"]
    fecha_inicio = datetime(2026, 1, 1)

    registros = []

    for _ in range(cantidad_registros):

        inscripcion = {
            "inscripcionId": random.randint(1, 250),
            "empleadoId": random.randint(1, 500),
            "programaId": random.randint(1, 200),
            "estado": random.choice(estados_validos),
            "avance": random.randint(0, 100),
            "nota": random.randint(0, 100),
            "fechaInscripcion": fecha_inicio + timedelta(days=random.randint(0, 30))
        }

        # Inyectando errores controlados en los datos
        probabilidad_Error = random.random()

        if probabilidad_Error < 0.2:
            inscripcion["inscripcionId"] = None
        elif probabilidad_Error < 0.4:
            inscripcion["empleadoId"] = random.choice(["texto", "error"])
        elif probabilidad_Error < 0.5:
            inscripcion["programaId"] = random.choice([0, -10000, None])
        elif probabilidad_Error < 0.8:
            inscripcion["estado"] = " " + inscripcion["estado"].upper()
        elif probabilidad_Error < 0.9:
            inscripcion["fechaInscripcion"] = None

        registros.append(inscripcion)

    return registros