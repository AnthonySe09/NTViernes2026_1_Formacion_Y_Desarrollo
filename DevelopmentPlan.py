import random
from datetime import datetime, timedelta
developmentPlans = []

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
    for _ in range (planNumbers):
        date = simulatedDate + timedelta(days=random.randint(0,365))
        developmentPlan = {
            "idPlan" : random.randint(100,200),
            "startDate" : date.strftime("%y/%m/%d"),
            "objective" : random.choice(listObjectives),
            "status" : random.choice (listStatus)
        }
        developmentPlans.append(developmentPlan)
    return developmentPlans

def printDevelopmentPlans(plans):
    print("\n📋 DEVELOPMENT PLANS\n")
    print(f"{'ID':<10}{'START DATE':<15}{'STATUS':<15}OBJECTIVE")
    print("-" * 70)

    for plan in plans:
        print(f"{plan['idPlan']:<10}{plan['startDate']:<15}{plan['status']:<15}{plan['objective']}")


plans = generateDevelopmentPlans(10)
printDevelopmentPlans(plans)