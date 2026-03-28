#SIMULANDO DATOS DE UNA TABLA EN PYTHON

import random
from datetime import datetime, timedelta
def generar_evaluaciones(numeroEvaluaciones):


    EvaluationTypes = ["Evaluacion", "Projecto", "Quiz"]
    comments = ["Excelente trabajo", "Buen esfuerzo", "Necesita mejorar", "No cumplio con los requisitos", "Trabajo sobresaliente"]
    evaluations=[]
    fechaInicio = datetime(2026, 1, 1)

    for i in range(numeroEvaluaciones):

        
        fecha=fechaInicio+timedelta(days=random.randint(0, 365))

        evaluation={
            "evaluationId": random.randint(0, 8000),
            "employeeId": random.randint(0, 10000),
            "courseId": random.randint(0, 500),
            "score": random.randint(0,5),
            "evaluationType": random.choice(EvaluationTypes),
            "comments": random.choice(comments),
            "evaluationDate": fecha.strftime("%Y/%m/%d")
        }
        evaluations.append(evaluation)
    return evaluations


