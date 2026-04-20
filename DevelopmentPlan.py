import random
from datetime import datetime, timedelta

listObjectives = [
    "Induccion a nuevos trabajadores",
    "Capacitar a trabajadores antiguos",
    "Mejorar el clima laboral",
    "Aumentar la productividad del equipo",
    "Fortalecer habilidades de liderazgo",
    "Optimizar procesos internos",
    "Reducir la rotacion de personal",
    "Fomentar el trabajo en equipo",
    "Actualizar conocimientos tecnicos",
    "Mejorar la comunicacion organizacional",
    "Desarrollar habilidades blandas",
    "Implementar nuevas tecnologias",
    "Mejorar la atencion al cliente",
    "Aumentar la eficiencia operativa",
    "Promover la innovacion",
    "Fortalecer la cultura organizacional",
    "Reducir errores en procesos",
    "Capacitar en seguridad laboral",
    "Mejorar la gestion del tiempo",
    "Desarrollar planes de carrera"
]

listStatus = [
    "Pendiente",
    "En proceso",
    "Completado",
    "Cancelado",
    "Atrasado"
]

simulatedDate = datetime(2026,1,1)

def generateDevelopmentPlans (planNumbers):

    developmentPlans = []
    
    for _ in range (planNumbers):
        date = simulatedDate + timedelta(days=random.randint(0,365))
        developmentPlan = {
            "idPlan" : random.randint(1,1000),
            "startDate" : date.strftime("%y/%m/%d"),
            "objective" : random.choice(listObjectives),
            "status" : random.choice (listStatus)
        }

        # Agregar un solo error al registro segun probabilidad
        probabilityError = random.random()
        # Agg valores nulos
        if probabilityError < 0.2:
            developmentPlan["idPlan"] = None
        # Agg incoherencias en objetivo
        elif probabilityError < 0.35:
            developmentPlan["objective"] = random.choice(["Clase para jugar COD Warzone", "Clase de como robarle a la empresa", "Clase de como ser una peor persona"])
        # Agg texto fecha_invalida
        elif probabilityError < 0.5:
            developmentPlan["startDate"] = "fecha_invalida"
        # Agg incoherencias en estado
        elif probabilityError < 0.65:
            developmentPlan["status"] = random.choice(["procccecso", "done", ""])
        # Agg valores fuera de rango
        elif probabilityError < 0.75:
            developmentPlan["idPlan"] = -random.randint(1, 50)

        # Agregar errores adicionales en un mismo registro
        # Nulos adicionales
        if random.random() < 0.05:
            developmentPlan["objective"] = None
        # Texto con espacios y en mayuscula
        if random.random() < 0.1 and developmentPlan["objective"]:
            developmentPlan["objective"] = "  " + developmentPlan["objective"].upper() + "  "
        # Fecha con formato distinto
        if random.random() < 0.1:
            developmentPlan["startDate"] = date.strftime("%d-%m-%Y")
        # Poner todo en minuscula
        if random.random() < 0.1:
            developmentPlan["status"] = developmentPlan["status"].lower()
        # Duplicar registro
        if random.random() < 0.1:
            developmentPlans.append(developmentPlan.copy())

        developmentPlans.append(developmentPlan)
    return developmentPlans

# Esto solo lo utilizo para visualizar si los datos quedaron cargados correctamente antes de realizar la limpieza
def printDevelopmentPlans(plans):
    print("\n📋 DEVELOPMENT PLANS\n")
    print(f"{'ID':<10}{'START DATE':<15}{'STATUS':<15}OBJECTIVE")
    print("-" * 70)

    for plan in plans:
        idPlan = str(plan.get("idPlan"))
        startDate = str(plan.get("startDate"))
        status = str(plan.get("status"))
        objective = str(plan.get("objective"))

        print(f"{idPlan:<10}{startDate:<15}{status:<15}{objective}")

plans = generateDevelopmentPlans(1000)
printDevelopmentPlans(plans)