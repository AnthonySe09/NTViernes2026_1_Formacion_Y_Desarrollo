#SIMULANDO DATOS DE UNA TABLA EN PYTHON

import random
from datetime import datetime, timedelta

def generar_evaluaciones(numeroEvaluaciones):

    EvaluationTypes = ["Evaluacion", "Projecto", "Quiz"]
    comments = ["Excelente trabajo", "Buen esfuerzo", "Necesita mejorar", "No cumplio con los requisitos", "Trabajo sobresaliente"]
    evaluations = []
    fechaInicio = datetime(2026, 1, 1)

    for i in range(numeroEvaluaciones):
        fecha = fechaInicio + timedelta(days=random.randint(0, 365))

        # Generando errores intencionales
        evaluation = {
            "evaluationId": random.randint(0, 8000) if random.random() > 0.1 else None,  # 10% valores nulos
            "employeeId": random.randint(0, 10000) if random.random() > 0.05 else "ID-ERR",  # 5% valores no numéricos
            "courseId": random.randint(0, 500),
            "score": random.randint(0, 5) if random.random() > 0.2 else random.randint(6, 10),  # 20% fuera de rango
            "evaluationType": random.choice(EvaluationTypes + ["TipoErroneo", "  Evaluacion  "]),  # Tipos inválidos o con espacios
            "comments": random.choice(comments + ["", "   ", None]),  # Comentarios vacíos o nulos
            "evaluationDate": fecha.strftime("%Y/%m/%d") if random.random() > 0.1 else "FechaErronea"  # 10% fechas inválidas
        }
        evaluations.append(evaluation)

    return evaluations