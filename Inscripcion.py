import random
from datetime import datetime, timedelta 


def generar_inscripcion(numeroServicios):

    listaEstado = ["Inscrito", "Por inscribir"]
    fechaInicio = datetime(2026, 1, 1) 

    inscripcions = []

    for _ in range(numeroServicios):

        fecha = fechaInicio + timedelta(days=random.randint(0, 60)) 

        inscripcion = {
            "registrationId": random.randint(0, 100),
            "employeeId": random.randint(0, 100),
            "courseId": random.randint(0, 20),
            "registrationDate": fecha.strftime("%y/%m/%d"),
            "status": random.choice(listaEstado),
        }

        inscripcions.append(inscripcion)

    return inscripcions  


def mostrar_tabla(lista):

    headers = ["registrationId", "employeeId", "courseId", "registrationDate", "status"]

    print(f"{headers[0]:<15} {headers[1]:<12} {headers[2]:<10} {headers[3]:<18} {headers[4]:<15}")
    print("-" * 70)

    for item in lista:
        print(f"{item['registrationId']:<15} {item['employeeId']:<12} {item['courseId']:<10} {item['registrationDate']:<18} {item['status']:<15}")


# Uso
datos = generar_inscripcion(3)
mostrar_tabla(datos)    