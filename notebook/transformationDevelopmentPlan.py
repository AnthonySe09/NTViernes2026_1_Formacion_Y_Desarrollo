# Routine to transform and group development plan data
import pandas as pd


def transformDevelopmentPlans(cleanOrganizedDevelopmentPlans):

    # Trabajar sobre una copia para no mutar el DataFrame original
    df = cleanOrganizedDevelopmentPlans.copy()

    # Asegurar que startDate sea datetime desde el inicio
    df["startDate"] = pd.to_datetime(df["startDate"], errors="coerce")
    df["yearMonth"] = df["startDate"].dt.to_period("M")
    df["month"] = df["startDate"].dt.month


    # TRANSFORMACIÓN 1 — Planes completados por mes
    # Pregunta de negocio:
    # ¿En qué meses se completaron la mayoría de los planes?

    grouping1 = (
        df.query("status == 'Completado'")
        .groupby("yearMonth")["idPlan"]
        .count()
        .reset_index(name="planCount")
        .sort_values(by="planCount", ascending=False)
    )


    # TRANSFORMACIÓN 2 — Objetivos más comunes
    # Pregunta de negocio:
    # ¿En qué objetivos se trabaja con mayor frecuencia?

    grouping2 = (
        df.query("objective.notnull()", engine="python")
        .groupby("objective")["idPlan"]
        .count()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )


    # TRANSFORMACIÓN 3 — Objetivos con retrasos o cancelaciones
    # Pregunta de negocio:
    # ¿Qué objetivos presentan más problemas de ejecución?

    grouping3 = (
        df.query("status == 'Atrasado' or status == 'Cancelado'")
        .groupby(["objective", "status"])["idPlan"]
        .count()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )


    # TRANSFORMACIÓN 4 — Planes por mes
    # Pregunta de negocio:
    # ¿Qué meses registraron la mayor actividad de formación?

    grouping4 = (
        df.groupby("month")["idPlan"]
        .count()
        .reset_index(name="planCount")
        .sort_values(by="planCount", ascending=False)
    )


    # TRANSFORMACIÓN 5 — Mapa de calor Objetivo vs Estado (excluyendo completados)
    # Pregunta de negocio:
    # ¿Qué objetivos presentan más problemas operativos?

    grouping5 = (
        df.query("status != 'Completado'")
        .groupby(["objective", "status"])["idPlan"]
        .count()
        .reset_index(name="count")
    )


    # TRANSFORMACIÓN 6 — Tasa de completitud por objetivo
    # Pregunta de negocio:
    # ¿Qué objetivos se logran completar con mayor éxito?

    total_by_objective = (
        df.groupby("objective")["idPlan"]
        .count()
    )

    completed_by_objective = (
        df.query("status == 'Completado'")
        .groupby("objective")["idPlan"]
        .count()
    )

    grouping6 = (
        (completed_by_objective / total_by_objective * 100)
        .round(1)
        .reset_index(name="completionPct")
        .sort_values(by="completionPct", ascending=False)
    )


    # RESUMEN DE AGRUPACIONES

    groupedDevelopmentPlans = {
        "grouping1_completed_plans_by_month":   grouping1,
        "grouping2_most_common_objectives":      grouping2,
        "grouping3_objectives_with_issues":      grouping3,
        "grouping4_plans_by_month":              grouping4,
        "grouping5_objective_status_heatmap":    grouping5,
        "grouping6_completion_rate_by_objective": grouping6,
    }

    return groupedDevelopmentPlans