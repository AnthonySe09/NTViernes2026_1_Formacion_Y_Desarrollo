import pandas as pd

def transformar_datos_evaluacion(data_frame_limpio):
    #5 filtros por tabla y 5 agrupaciones por tabla

    filtro=data_frame_limpio.query("evaluacion==''")
    agrupacion=filtro.groupby("fecha")["id"].count().reset_index(name="cuenta")