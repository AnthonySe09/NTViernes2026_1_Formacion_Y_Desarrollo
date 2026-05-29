# Rutina de graficacion para INSCRIPCIONES
# Genera PNG (para frontend) y CSV (para analitica/backend) para cada transformacion
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

RUTA_PUBLIC_FRONT = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-front", "public", "graficos"
)
RUTA_CSV_BACKEND = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-borrador", "training", "analytics-data"
)


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def exportar_csv(dataframe, nombre_archivo, ruta_destino=RUTA_CSV_BACKEND):
    crear_ruta_si_no_existe(ruta_destino)
    ruta_csv = os.path.join(ruta_destino, nombre_archivo)
    dataframe.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"CSV guardado en: {ruta_csv}")
    return ruta_csv


def graficar_aprobados_por_curso(agrupacion1, ruta_destino=RUTA_PUBLIC_FRONT):
    # TRANSFORMACION 1 - Inscripciones aprobadas por curso
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion1.empty:
        print("Sin datos para graficar aprobados por curso.")
        return

    datos = agrupacion1.sort_values("cantidad_aprobados", ascending=False).head(15)

    figura, area_dibujo = plt.subplots(figsize=(12, 5))
    area_dibujo.plot(
        datos["courseId"].astype(str),
        datos["cantidad_aprobados"],
        marker="o",
        linewidth=2,
        color="#2196F3"
    )
    area_dibujo.set_title("Inscripciones aprobadas por curso (top 15)", fontsize=14)
    area_dibujo.set_xlabel("courseId", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de aprobados", fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "in1_aprobados_por_curso.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico inscripciones 1 guardado en: {ruta_png}")

    exportar_csv(agrupacion1, "in1_aprobados_por_curso.csv")


def graficar_cursos_mayores_10(agrupacion2, ruta_destino=RUTA_PUBLIC_FRONT):
    # TRANSFORMACION 2 - Cursos con ID mayor a 10 agrupados por estado
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion2.empty:
        print("Sin datos para graficar cursos > 10.")
        return

    figura, area_dibujo = plt.subplots(figsize=(8, 5))
    area_dibujo.bar(
        agrupacion2["status"].astype(str),
        agrupacion2["cantidad_inscripciones"],
        color="#4CAF50",
        edgecolor="black"
    )
    area_dibujo.set_title("Inscripciones en cursos con ID > 10 por estado", fontsize=14)
    area_dibujo.set_xlabel("Estado", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de inscripciones", fontsize=12)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "in2_cursos_mayores_10.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico inscripciones 2 guardado en: {ruta_png}")

    exportar_csv(agrupacion2, "in2_cursos_mayores_10.csv")


def graficar_empleados_menores_50(agrupacion3, ruta_destino=RUTA_PUBLIC_FRONT):
    # TRANSFORMACION 3 - Empleados con ID < 50 y cantidad de registros
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion3.empty:
        print("Sin datos para graficar empleados menores a 50.")
        return

    datos = agrupacion3.sort_values("cantidad_registros", ascending=False).head(20)

    figura, area_dibujo = plt.subplots(figsize=(12, 5))
    area_dibujo.bar(
        datos["employeeId"].astype(str),
        datos["cantidad_registros"],
        color="#9C27B0",
        edgecolor="black"
    )
    area_dibujo.set_title("Registros por empleado (employeeId < 50, top 20)", fontsize=14)
    area_dibujo.set_xlabel("employeeId", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de registros", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "in3_empleados_menores_50.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico inscripciones 3 guardado en: {ruta_png}")

    exportar_csv(agrupacion3, "in3_empleados_menores_50.csv")


def graficar_pendientes_por_fecha(agrupacion4, ruta_destino=RUTA_PUBLIC_FRONT):
    # TRANSFORMACION 4 - Inscripciones pendientes por fecha
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion4.empty:
        print("Sin datos para graficar pendientes por fecha.")
        return

    datos = agrupacion4.copy()
    datos["registrationDate"] = datos["registrationDate"].astype(str)
    datos = datos.sort_values("registrationDate")

    figura, area_dibujo = plt.subplots(figsize=(12, 5))
    area_dibujo.plot(
        datos["registrationDate"],
        datos["cantidad_pendientes"],
        marker="o",
        linewidth=2,
        color="#FF9800"
    )
    area_dibujo.set_title("Inscripciones pendientes por fecha", fontsize=14)
    area_dibujo.set_xlabel("Fecha de inscripcion", fontsize=12)
    area_dibujo.set_ylabel("Cantidad pendientes", fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "in4_pendientes_por_fecha.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico inscripciones 4 guardado en: {ruta_png}")

    exportar_csv(agrupacion4, "in4_pendientes_por_fecha.csv")


def graficar_rechazados_por_curso(agrupacion5, ruta_destino=RUTA_PUBLIC_FRONT):
    # TRANSFORMACION 5 - Rechazados por curso, empleados unicos
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion5.empty:
        print("Sin datos para graficar rechazados por curso.")
        return

    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    area_dibujo.pie(
        agrupacion5["empleados_unicos"],
        labels=agrupacion5["courseId"].astype(str),
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("Set2", n_colors=max(1, len(agrupacion5)))
    )
    area_dibujo.set_title("Empleados rechazados unicos por curso", fontsize=14)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "in5_rechazados_por_curso.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico inscripciones 5 guardado en: {ruta_png}")

    exportar_csv(agrupacion5, "in5_rechazados_por_curso.csv")


def graficar_todas_inscripciones(transformaciones, ruta_destino=RUTA_PUBLIC_FRONT):
    # Recibe el diccionario retornado por transformar_datos_inscripciones()
    graficar_aprobados_por_curso(transformaciones["aprobados_por_curso"], ruta_destino)
    graficar_cursos_mayores_10(transformaciones["cursos_mayores_10"], ruta_destino)
    graficar_empleados_menores_50(transformaciones["empleados_menores_50"], ruta_destino)
    graficar_pendientes_por_fecha(transformaciones["pendientes_por_fecha"], ruta_destino)
    graficar_rechazados_por_curso(transformaciones["rechazados_por_curso"], ruta_destino)

    print("\nTodos los graficos de inscripciones fueron generados correctamente.")
