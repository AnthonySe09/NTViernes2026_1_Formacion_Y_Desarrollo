import pandas as pd

from evaluation import generar_evaluaciones
from Inscription import generateRegistration

from notebook.limpiezaEvaluacion import limpiar_evaluacion
from notebook.limpiezaInscription import limpiar_inscription

evaluations=generar_evaluaciones(1000)
registrations=generateRegistration(10)


# evaluaciones_ordenadas=pd.DataFrame(evaluations)
# evaluaciones_ordenadas_limpias=limpiar_evaluacion(evaluaciones_ordenadas)
# print(evaluaciones_ordenadas_limpias)

inscripciones_ordenadas=pd.DataFrame(registrations)
inscripciones_ordenadas_limpias=limpiar_inscription(inscripciones_ordenadas)
print(inscripciones_ordenadas_limpias)




