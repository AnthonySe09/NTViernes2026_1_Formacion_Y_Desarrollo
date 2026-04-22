import random

from datetime import datetime, timedelta 


def generateRegistration(numberRegistrations):

    statusList = ["Inscrito", "Por inscribir"]
    sytartDate = datetime(2026, 1, 1) 

    inscripcions = []

    for _ in range(numberRegistrations):

        date = sytartDate + timedelta(days=random.randint(0, 60)) 

        inscripcion = {
            "registrationId": random.randint(0, 100),
            "employeeId": random.randint(0, 100),
            "courseId": random.randint(0, 20),
            "registrationDate": date.strftime("%y/%m/%d"),
            "status": random.choice(statusList),
        }

        #inyectando errores controlados
        probabilidadError = random.random()
        if(probabilidadError < 0.2):  
            inscripcion["registrationId"] = None
        elif (probabilidadError <0.4):
            inscripcion["employeeId"] = random.choice([-1,None])
        elif (probabilidadError <0.6):
            inscripcion["courseId"] = random.choice([0,-10000,None])
        elif (probabilidadError <0.8):
            inscripcion["registrationDate"] = None
        elif(probabilidadError <0.9):
            inscripcion["status"] = random.choice([" nose","aveces ", " "]).upper()

        inscripcions.append(inscripcion)

    return inscripcions  




# def showTables(list):
#      headers = ["registrationId", "employeeId", "courseId", "registrationDate", "status"]

#      print(f"{headers[0]:<15} {headers[1]:<12} {headers[2]:<10} {headers[3]:<18} {headers[4]:<15}")
#      print("-" * 70)

#      for item in list:
#          print(f"{item['registrationId']:<15} {item['employeeId']:<12} {item['courseId']:<10} {item['registrationDate']:<18} {item['status']:<15}")


# # Uso
#      data = generateRegistration(5)
#      showTables(data)    