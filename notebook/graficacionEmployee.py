import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from transformacionEmployee import transformar_datos_empleado

RUTA_PUBLIC_FRONT = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-front", "public", "graficos"
)
RUTA_CSV_BACKEND = os.path.join(
    os.path.dirname(__file__), "..", "..", "hrm-system-borrador", "training", "analytics-data"
)

# Ruta por defecto para guardar imágenes
RUTA_ASSETS = RUTA_PUBLIC_FRONT

def crear_ruta_si_no_existe(ruta_destino):
    # Se crea la carpeta destino en caso de que aún no exista
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_lineas(datos_agrupados, columna_eje_x, columna_eje_y,
                    titulo="Gráfico de líneas", color_linea="#2196F3",
                    nombre_archivo="lineas.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.plot(
        datos_agrupados[columna_eje_x],
        datos_agrupados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2
    )

    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)
    area_dibujo.grid(True, linestyle="--", alpha=0.6)

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico de líneas guardado en: {ruta_completa}")


def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Gráfico de barras", color_barras="#4CAF50",
                    nombre_archivo="barras.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )

    area_dibujo.set_title(titulo, fontsize=14)
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)
    area_dibujo.set_ylabel(columna_valores, fontsize=12)

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico de barras guardado en: {ruta_completa}")


def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Gráfico de torta", lista_colores=None,
                   nombre_archivo="torta.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0"]

    figura, area_dibujo = plt.subplots(figsize=(8, 8))

    cantidad_categorias = len(datos_agrupados)

    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )

    area_dibujo.set_title(titulo, fontsize=14)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico de torta guardado en: {ruta_completa}")


def graficar_mapa_calor(datos_agrupados, columna_filas, columna_columnas, columna_valores,
                        titulo="Mapa de calor", paleta_color="YlOrRd",
                        nombre_archivo="mapa_calor.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    tabla_pivote = datos_agrupados.pivot_table(
        index=columna_filas,
        columns=columna_columnas,
        values=columna_valores,
        aggfunc="sum",
        fill_value=0
    )

    figura, area_dibujo = plt.subplots(figsize=(10, 6))

    sns.heatmap(
        tabla_pivote,
        annot=True,
        fmt=".0f",
        cmap=paleta_color,
        ax=area_dibujo,
        linewidths=0.5,
        linecolor="gray"
    )

    area_dibujo.set_title(titulo, fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Mapa de calor guardado en: {ruta_completa}")


# ============================================================
# EJECUCIÓN: GRAFICAR TODO CON DATOS REALES
# ============================================================
def generar_graficos_empleados(data_frame_limpio):

    resultados = transformar_datos_empleado(data_frame_limpio)

    # 1. Contrataciones por fecha
    graficar_lineas(
        resultados["agrupacion_1Empleado"],
        "fecha_contratacion",
        "cantidad_empleados",
        "Contrataciones por fecha",
        nombre_archivo="contrataciones_por_fecha.png"
    )

    # 2. Empleados por departamento
    graficar_barras(
        resultados["agrupacion_2Empleado"],
        "departamento",
        "total_empleados",
        "Empleados por departamento",
        nombre_archivo="empleados_por_departamento.png"
    )

    # 3. Empleados por estado
    graficar_barras(
        resultados["agrupacion_3Empleado"],
        "estado_empleado",
        "cantidad",
        "Empleados por estado",
        nombre_archivo="empleados_por_estado.png"
    )

    # 4. Tipo de contrato
    graficar_torta(
        resultados["agrupacion_4Empleado"],
        "tipo_contrato",
        "cantidad_contratos",
        "Distribución por tipo de contrato",
        nombre_archivo="empleados_por_contrato.png"
    )

    # 5. Nivel educativo
    graficar_torta(
        resultados["agrupacion_5Empleado"],
        "nivel_educativo",
        "cantidad_personas",
        "Distribución por nivel educativo",
        nombre_archivo="nivel_educativo.png"
    )

    # 6. Empleados activos por departamento
    graficar_barras(
        resultados["agrupacion_extraEmpleado"],
        "departamento",
        "empleados_activos",
        "Empleados activos por departamento",
        nombre_archivo="empleados_activos_departamento.png"
    )

    # 7. Empleados indefinidos por puesto
    graficar_barras(
        resultados["agrupacion_indefinidoEmpleado"],
        "puesto",
        "cantidad",
        "Empleados indefinidos por puesto",
        nombre_archivo="empleados_indefinidos_puesto.png"
    )

    print("Todos los gráficos fueron generados correctamente.")