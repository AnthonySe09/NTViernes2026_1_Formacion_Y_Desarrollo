import pandas as pd
from utils.evaluation import generar_evaluaciones
from notebook.limpiezaEvaluacion import limpiar_evaluacion

evaluations=generar_evaluaciones(1000)

evaluaciones_ordenadas=pd.DataFrame(evaluations)
evaluaciones_ordenadas_limpias=limpiar_evaluacion(evaluaciones_ordenadas)
print(evaluaciones_ordenadas)

