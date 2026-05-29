# Rutina de graficacion para planes de desarrollo
# Realizado por Adriano Jimenez Arboleda
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta de la carpeta assets en un proyecto React con Vite
RUTA_ASSETS = os.path.join(os.path.dirname(__file__), "..", "..", "mi-app-react", "src", "assets", "graficos")


def crear_ruta_si_no_existe(ruta_destino):
    # Se crea la carpeta destino en caso de que aún no exista
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_planes_completados_por_mes(grouping1, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 1 — Planes completados por mes
    # Muestra en qué meses se completaron la mayoría de los planes
    # Columnas esperadas: yearMonth, planCount

    crear_ruta_si_no_existe(ruta_destino)

    # Convertir Period a string para que matplotlib pueda graficarlo
    datos = grouping1.copy()
    datos["yearMonth"] = datos["yearMonth"].astype(str)
    datos = datos.sort_values("yearMonth")

    figura, area_dibujo = plt.subplots(figsize=(12, 5))

    area_dibujo.plot(
        datos["yearMonth"],
        datos["planCount"],
        marker="o",
        color="#2196F3",
        linewidth=2
    )

    area_dibujo.set_title("Planes completados por mes", fontsize=14)
    area_dibujo.set_xlabel("Mes", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de planes", fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g1_planes_completados_por_mes.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 1 guardado en: {ruta_completa}")


def graficar_objetivos_mas_comunes(grouping2, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 2 — Objetivos más comunes
    # Muestra en qué objetivos se trabaja con mayor frecuencia
    # Columnas esperadas: objective, count

    crear_ruta_si_no_existe(ruta_destino)

    figura, area_dibujo = plt.subplots(figsize=(14, 6))

    area_dibujo.bar(
        grouping2["objective"],
        grouping2["count"],
        color="#4CAF50",
        edgecolor="black"
    )

    area_dibujo.set_title("Objetivos más comunes", fontsize=14)
    area_dibujo.set_xlabel("Objetivo", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de planes", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g2_objetivos_mas_comunes.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 2 guardado en: {ruta_completa}")


def graficar_objetivos_con_problemas(grouping3, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 3 — Objetivos con retrasos o cancelaciones
    # Muestra qué objetivos presentan más problemas de ejecución
    # Columnas esperadas: objective, status, count

    crear_ruta_si_no_existe(ruta_destino)

    tabla_pivote = grouping3.pivot_table(
        index="objective",
        columns="status",
        values="count",
        aggfunc="sum",
        fill_value=0
    )

    figura, area_dibujo = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap="OrRd",
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )

    area_dibujo.set_title("Objetivos con retrasos o cancelaciones", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g3_objetivos_con_problemas.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 3 guardado en: {ruta_completa}")


def graficar_planes_por_mes(grouping4, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 4 — Actividad total por mes
    # Muestra qué meses registraron la mayor actividad de formación
    # Columnas esperadas: month, planCount

    crear_ruta_si_no_existe(ruta_destino)

    datos = grouping4.sort_values("month")

    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.bar(
        datos["month"].astype(str),
        datos["planCount"],
        color="#FF9800",
        edgecolor="black"
    )

    area_dibujo.set_title("Actividad de formación por mes", fontsize=14)
    area_dibujo.set_xlabel("Mes", fontsize=12)
    area_dibujo.set_ylabel("Cantidad de planes", fontsize=12)
    plt.xticks(rotation=0)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g4_planes_por_mes.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 4 guardado en: {ruta_completa}")


def graficar_mapa_calor_objetivo_estado(grouping5, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 5 — Mapa de calor Objetivo vs Estado
    # Muestra qué objetivos presentan más problemas operativos (excluye Completado)
    # Columnas esperadas: objective, status, count

    crear_ruta_si_no_existe(ruta_destino)

    tabla_pivote = grouping5.pivot_table(
        index="objective",
        columns="status",
        values="count",
        aggfunc="sum",
        fill_value=0
    )

    figura, area_dibujo = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap="YlOrRd",
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )

    area_dibujo.set_title("Mapa de calor: Objetivo vs Estado (sin Completado)", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g5_mapa_calor_objetivo_estado.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 5 guardado en: {ruta_completa}")


def graficar_tasa_completitud(grouping6, ruta_destino=RUTA_ASSETS):
    # TRANSFORMACIÓN 6 — Tasa de completitud por objetivo
    # Muestra qué objetivos se logran completar con mayor éxito
    # Columnas esperadas: objective, completionPct

    crear_ruta_si_no_existe(ruta_destino)

    figura, area_dibujo = plt.subplots(figsize=(14, 6))

    barras = area_dibujo.barh(
        grouping6["objective"],
        grouping6["completionPct"],
        color="#9C27B0",
        edgecolor="black"
    )

    # Agregar etiquetas de porcentaje al final de cada barra
    for barra, valor in zip(barras, grouping6["completionPct"]):
        area_dibujo.text(
            valor + 0.5,
            barra.get_y() + barra.get_height() / 2,
            f"{valor}%",
            va="center",
            fontsize=9
        )

    area_dibujo.set_title("Tasa de completitud por objetivo", fontsize=14)
    area_dibujo.set_xlabel("% Completado", fontsize=12)
    area_dibujo.set_ylabel("Objetivo", fontsize=12)
    area_dibujo.set_xlim(0, 110)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, "g6_tasa_completitud_por_objetivo.png")
    figura.savefig(ruta_completa)
    plt.close(figura)
    print(f"Gráfico 6 guardado en: {ruta_completa}")


def graficar_todos(groupedDevelopmentPlans, ruta_destino=RUTA_ASSETS):
    # Función principal que genera todos los gráficos de una sola vez
    # Recibe el diccionario retornado por transformDevelopmentPlans()

    graficar_planes_completados_por_mes(groupedDevelopmentPlans["grouping1_completed_plans_by_month"],  ruta_destino)
    graficar_objetivos_mas_comunes(     groupedDevelopmentPlans["grouping2_most_common_objectives"],     ruta_destino)
    graficar_objetivos_con_problemas(   groupedDevelopmentPlans["grouping3_objectives_with_issues"],     ruta_destino)
    graficar_planes_por_mes(            groupedDevelopmentPlans["grouping4_plans_by_month"],             ruta_destino)
    graficar_mapa_calor_objetivo_estado(groupedDevelopmentPlans["grouping5_objective_status_heatmap"],   ruta_destino)
    graficar_tasa_completitud(          groupedDevelopmentPlans["grouping6_completion_rate_by_objective"], ruta_destino)

    print("\nTodos los gráficos fueron generados correctamente.")