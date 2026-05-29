# Routine to transform and group development plan data
import pandas as pd

def transformDevelopmentPlans(cleanOrganizedDevelopmentPlans):
    
    # TRANSFORMACIÓN 1 Planes completados por fecha
    # Pregunta de negocio:
    # ¿En qué fechas se completaron la mayoría de los planes?

    filter1 = cleanOrganizedDevelopmentPlans.query(
        "status == 'Completado'"
    )

    grouping1 = (
        filter1
        .groupby("startDate")["idPlan"]
        .count()
        .reset_index(name="planCount")
        .sort_values(by="planCount", ascending=False)
    )


    # TRANSFORMACIÓN 2 Objetivos más comunes
    # Pregunta empresarial:
    # ¿En qué objetivos se trabaja con mayor frecuencia?

    filter2 = cleanOrganizedDevelopmentPlans.query(
        "objective.notnull()",
        engine="python"
    )

    grouping2 = (
        filter2
        .groupby("objective")["idPlan"]
        .count()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )


    # TRANSFORMACIÓN 3 Objetivos con retrasos o cancelaciones
    # Pregunta de negocio:
    # ¿Qué objetivos presentan más problemas de ejecución?

    filter3 = cleanOrganizedDevelopmentPlans.query(
        "status == 'Atrasado' or status == 'Cancelado'"
    )

    grouping3 = (
        filter3
        .groupby(["objective", "status"])["idPlan"]
        .count()
        .reset_index(name="count")
        .sort_values(by="count", ascending=False)
    )


    # TRANSFORMACIÓN 4 Planes por mes
    # Pregunta de negocio:
    # ¿Qué meses registraron la mayor actividad de formación?

    cleanOrganizedDevelopmentPlans["startDate"] = pd.to_datetime(
        cleanOrganizedDevelopmentPlans["startDate"]
    )

    cleanOrganizedDevelopmentPlans["month"] = (
        cleanOrganizedDevelopmentPlans["startDate"]
        .dt.month
    )

    grouping4 = (
        cleanOrganizedDevelopmentPlans
        .groupby("month")["idPlan"]
        .count()
        .reset_index(name="planCount")
        .sort_values(by="planCount", ascending=False)
    )


    # TRANSFORMACIÓN 5
    # Análisis de mapa de calor Objetivo vs Estado
    # Pregunta de negocio:
    # ¿Qué objetivos presentan más problemas operativos?

    filter5 = cleanOrganizedDevelopmentPlans.query(
        "status != 'Completado'"
    )

    grouping5 = (
        filter5
        .groupby(["objective", "status"])["idPlan"]
        .count()
        .reset_index(name="count")
    )


    # RESUMEN DE AGRUPACIONES

    groupedDevelopmentPlans = {
        "grouping1_completed_plans_by_date": grouping1,
        "grouping2_most_common_objectives": grouping2,
        "grouping3_objectives_with_issues": grouping3,
        "grouping4_plans_by_month": grouping4,
        "grouping5_objective_status_heatmap": grouping5
    }

    return groupedDevelopmentPlans