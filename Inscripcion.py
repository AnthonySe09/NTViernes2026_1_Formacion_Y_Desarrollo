#simulando datos de una tabla en python  

#solo con los string que tengo en la tabla, tengo que mirar cuales son con string en la tabla
import random
from datetime import datetime, timedelta #para generar fechas aleatorias

def generar_inscripciones(numeroIncripciones):

    listaNombres=["Corte de uñas","Operacion de calculos","Cambio e pulmun","inividor","corte de cola"]

    listasCodigos=["AN012","AN233","AN489","AN001","AN777"]

    listaCostos=["25000","3000000","750000","40000","500000"] 

    fechaInicio=datetime(2026,1,1) #fecha de inicio para generar fechas aleatorias


    servicios =[]
    for _ in range(numeroServicios):

        fecha=fechaInicio+timedelta(days=random.randint(0,60)) #generar una fecha aleatoria dentro de un año

        servicios={
            "id":random.randint(0,5000),
            "nombre":random.choice(listaNombres),
            "codigo":random.choice(listasCodigos),
            "costo":random.choice(listaCostos),
            "id_cliente":random.randint(0,100),
            "fecha":fecha.strftime("%y/%m/%d")
        }
        servicios.append(servicios)
    return servicios    