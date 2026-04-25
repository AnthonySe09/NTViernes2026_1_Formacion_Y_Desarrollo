import pandas as pd

#Funcion para deacribir la estructura general del data set
def describir_estructura(data_frame_limpio):
    print("****** estructura*********")
    print(f"numero de filas:{data_frame_limpio.shape[0]}")
    print(f"numero de columnas:{data_frame_limpio.shape[1]}")
    print(f"columnas disponibles:{list(data_frame_limpio.columns)}")

##Funcion para describir estadisticas del data frame
def describir_estadisticas(data_frame_limpio):
    print("\n******* estadisticas********")
    print(data_frame_limpio[['registrationId', 'employeeId', 'courseId']].describe().astype(int))

#Funcion para medir las columnas categoricas
def describir_categoricas(data_frame_limpio):
    print("\n******* categorias********")
    print("******Estados de incripcion**********")
    print(data_frame_limpio['status'].value_counts())

# Funcion para describir los rangos de fechas 
def describir_fechas(data_frame_limpio):
    print("\n******* fechas********")
    print("******Fechas de inscripcion**********")
    print(f"fecha minima: {data_frame_limpio['registrationDate'].min()}")    
    print(f"fecha maxima: {data_frame_limpio['registrationDate'].max()}")   

    ##hola ya quedo el codigo de descripcion de inscripcion, saludos. 
    #hola
