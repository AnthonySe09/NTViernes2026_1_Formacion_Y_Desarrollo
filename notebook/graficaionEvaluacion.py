# Rutina de graficacion para EVALUACIONES
# Genera PNG (para frontend) y CSV (para analitica/backend) para cada transformacion
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Carpeta destino del frontend (public) para que vite los sirva
RUTA_PUBLIC_FRONT = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-front", "public", "graficos"
)

# Carpeta destino para CSV de analitica (la sirve el backend)
RUTA_CSV_BACKEND = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-borrador", "training", "analytics-data"
)


def crear_ruta_si_no_existe(ruta_destino):
    os.makedirs(ruta_destino, exist_ok=True)


def exportar_csv(dataframe, nombre_archivo, ruta_destino=RUTA_CSV_BACKEND):
    # Exporta un dataframe a CSV en la carpeta de analitica
    crear_ruta_si_no_existe(ruta_destino)
    ruta_csv = os.path.join(ruta_destino, nombre_archivo)
    dataframe.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"CSV guardado en: {ruta_csv}")
    return ruta_csv


def graficar_scores_invalidos_por_tipo(agrupacion_1, ruta_destino=RUTA_PUBLIC_FRONT):
    # FILTRO 1 - Scores fuera del rango 0-5 agrupados por tipo de evaluacion
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion_1.empty:
        print("Sin datos para graficar scores invalidos.")
        return

    figura, area_dibujo = plt.subplots(figsize=(10, 5))
    area_dibujo.bar(
        agrupacion_1["evaluationType"].astype(str),
        agrupacion_1["cantidad_scores_invalidos"],
        color="#E53935",
        edgecolor="black"
    )
    area_dibujo.set_title("Evaluaciones con scores invalidos por tipo", fontsize=14)
    area_dibujo.set_xlabel("Tipo de evaluacion", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de scores invalidos", fontsize=12)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "ev1_scores_invalidos_por_tipo.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico evaluaciones 1 guardado en: {ruta_png}")

    exportar_csv(agrupacion_1, "ev1_scores_invalidos_por_tipo.csv")


def graficar_comentarios_vacios(agrupacion_2, ruta_destino=RUTA_PUBLIC_FRONT):
    # FILTRO 2 - Comentarios vacios por tipo de evaluacion
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion_2.empty:
        print("Sin datos para graficar comentarios vacios.")
        return

    figura, area_dibujo = plt.subplots(figsize=(8, 8))
    area_dibujo.pie(
        agrupacion_2["comentarios_vacios"],
        labels=agrupacion_2["evaluationType"].astype(str),
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("pastel")
    )
    area_dibujo.set_title("Proporcion de comentarios vacios por tipo", fontsize=14)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "ev2_comentarios_vacios.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico evaluaciones 2 guardado en: {ruta_png}")

    exportar_csv(agrupacion_2, "ev2_comentarios_vacios.csv")


def graficar_ids_invalidos_por_curso(agrupacion_3, ruta_destino=RUTA_PUBLIC_FRONT):
    # FILTRO 3 - employeeId no numerico agrupado por curso
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion_3.empty:
        print("Sin datos para graficar IDs invalidos.")
        return

    datos = agrupacion_3.sort_values("empleados_id_error", ascending=False).head(15)

    figura, area_dibujo = plt.subplots(figsize=(12, 5))
    area_dibujo.plot(
        datos["courseId"].astype(str),
        datos["empleados_id_error"],
        marker="o",
        linewidth=2,
        color="#3949AB"
    )
    area_dibujo.set_title("Cursos con employeeId no numerico (top 15)", fontsize=14)
    area_dibujo.set_xlabel("courseId", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de IDs invalidos", fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "ev3_ids_invalidos_por_curso.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico evaluaciones 3 guardado en: {ruta_png}")

    exportar_csv(agrupacion_3, "ev3_ids_invalidos_por_curso.csv")


def graficar_tipos_invalidos(agrupacion_4, ruta_destino=RUTA_PUBLIC_FRONT):
    # FILTRO 4 - Tipos de evaluacion invalidos
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion_4.empty:
        print("Sin datos para graficar tipos invalidos.")
        return

    figura, area_dibujo = plt.subplots(figsize=(10, 6))
    barras = area_dibujo.barh(
        agrupacion_4["evaluationType"].astype(str),
        agrupacion_4["tipos_invalidos"],
        color="#FB8C00",
        edgecolor="black"
    )
    for barra, valor in zip(barras, agrupacion_4["tipos_invalidos"]):
        area_dibujo.text(
            valor + 0.1,
            barra.get_y() + barra.get_height() / 2,
            str(int(valor)),
            va="center",
            fontsize=9
        )

    area_dibujo.set_title("Tipos de evaluacion invalidos", fontsize=14)
    area_dibujo.set_xlabel("Cantidad de registros", fontsize=12)
    area_dibujo.set_ylabel("Tipo de evaluacion", fontsize=12)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "ev4_tipos_invalidos.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico evaluaciones 4 guardado en: {ruta_png}")

    exportar_csv(agrupacion_4, "ev4_tipos_invalidos.csv")


def graficar_fechas_erroneas(agrupacion_5, ruta_destino=RUTA_PUBLIC_FRONT):
    # FILTRO 5 - Mapa de calor de fechas erroneas por curso
    crear_ruta_si_no_existe(ruta_destino)

    if agrupacion_5.empty:
        print("Sin datos para graficar fechas erroneas.")
        return

    datos = agrupacion_5.sort_values("fechas_erroneas", ascending=False).head(20).copy()
    datos["courseId"] = datos["courseId"].astype(str)
    datos["categoria"] = "fechas_erroneas"

    tabla_pivote = datos.pivot_table(
        index="courseId",
        columns="categoria",
        values="fechas_erroneas",
        fill_value=0
    )

    figura, area_dibujo = plt.subplots(figsize=(8, 10))
    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap="Reds",
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )
    area_dibujo.set_title("Fechas erroneas por curso (top 20)", fontsize=14)
    plt.tight_layout()

    ruta_png = os.path.join(ruta_destino, "ev5_fechas_erroneas.png")
    figura.savefig(ruta_png)
    plt.close(figura)
    print(f"Grafico evaluaciones 5 guardado en: {ruta_png}")

    exportar_csv(agrupacion_5, "ev5_fechas_erroneas.csv")


def graficar_todas_evaluaciones(transformaciones, ruta_destino=RUTA_PUBLIC_FRONT):
    # Funcion principal que genera todos los graficos de evaluaciones
    # Recibe el diccionario retornado por transformar_datos_evaluacion()
    graficar_scores_invalidos_por_tipo(transformaciones["agrupacion_1"], ruta_destino)
    graficar_comentarios_vacios(transformaciones["agrupacion_2"], ruta_destino)
    graficar_ids_invalidos_por_curso(transformaciones["agrupacion_3"], ruta_destino)
    graficar_tipos_invalidos(transformaciones["agrupacion_4"], ruta_destino)
    graficar_fechas_erroneas(transformaciones["agrupacion_5"], ruta_destino)

    print("\nTodos los graficos de evaluaciones fueron generados correctamente.")


# Ejecucion directa: simula evaluaciones, limpia, transforma y grafica
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

    from utils.evaluation import generar_evaluaciones
    from notebook.limpiezaEvaluacion import limpiar_evaluacion
    from notebook.transformacionEvaluacion import transformar_datos_evaluacion

    print("=" * 80)
    print("SIMULACION + GRAFICACION DE EVALUACIONES")
    print("=" * 80)

    evaluaciones_simuladas = generar_evaluaciones(200)
    df_evaluaciones = pd.DataFrame(evaluaciones_simuladas)
    df_limpio = limpiar_evaluacion(df_evaluaciones)
    transformaciones = transformar_datos_evaluacion(df_limpio)

    graficar_todas_evaluaciones(transformaciones)
