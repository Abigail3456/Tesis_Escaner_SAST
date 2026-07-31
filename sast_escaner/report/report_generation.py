"""
=========================================================
Report Generator
---------------------------------------------------------
Genera un reporte resumido de los resultados obtenidos
durante el análisis SAST.

Responsabilidad:
    - Mostrar los resultados del análisis.
    - Calcular el nivel de riesgo.
    - Presentar un resumen estadístico.

El módulo NO:
    - Analiza código.
    - Detecta vulnerabilidades.
    - Asigna severidades.
=========================================================
"""
from fileinput import filename
import os

class ReportGenerator:

    # =====================================================
    # Método principal
    # =====================================================

    def generate(self, results):

        self._print_header(results)

        self._print_table(results)

        self._print_summary(results)

        self._print_footer(results)

    # =====================================================

    def _print_header(self, results):

        print("=" * 78)
        print("                     REPORTE DE ANÁLISIS SAST")
        print("=" * 78)

        if results:

            filename = os.path.basename(results[0].file)

            print(f"Archivo analizado : {filename}")

        print(f"Hallazgos         : {len(results)}")

        print()

    # =====================================================

    def _print_table(self, results):

        print("+------+-------+-----------+----------------------------+--------------------------------------+")
        print("| ID   | Línea | Severidad | Vulnerabilidad             | Fragmento                            |")
        print("+------+-------+-----------+----------------------------+--------------------------------------+")

        for result in results:

            fragment = result.code

            # Limita el fragmento para que la tabla no se rompa
            if len(fragment) > 36:
                fragment = fragment[:33] + "..."

            print(
                f"| {result.id:<4} "
                f"| {result.line:^5} "
                f"| {result.severity:<9} "
                f"| {result.name:<26} "
                f"| {fragment:<36} |"
            )

        print("+------+-------+-----------+----------------------------+--------------------------------------+")

    # =====================================================

    def _print_summary(self, results):

        severity_score = {

            "Crítica": 4,
            "Alta": 3,
            "Media": 2,
            "Baja": 1

        }

        score = 0

        counters = {
            "Crítica": 0,
            "Alta": 0,
            "Media": 0,
            "Baja": 0
        }

        for result in results:

            counters[result.severity] += 1

            score += severity_score[result.severity]

        # -----------------------------
        # Clasificación del riesgo
        # -----------------------------

        if counters["Crítica"] > 0:

            level = "CRÍTICO"

        elif score >= 10:

            level = "ALTO"

        elif score >= 5:

            level = "MEDIO"

        else:

            level = "BAJO"

        
        print()

        print("Resumen del análisis")

        print("--------------------")

        print(f"Críticas : {counters['Crítica']}")

        print(f"Altas    : {counters['Alta']}")

        print(f"Medias   : {counters['Media']}")

        print(f"Bajas    : {counters['Baja']}")

        print()

        print(f"Puntuación de riesgo : {score}")

        print(f"Nivel de riesgo      : [{level}]")

    # =====================================================

    def _print_footer(self, results):

        severity_order = {

            "Crítica": 4,
            "Alta": 3,
            "Media": 2,
            "Baja": 1

        }

        if not results:

            print("\nNo se detectaron vulnerabilidades.")
            return

        highest = max(
            results,
            key=lambda r: severity_order[r.severity]
        )

        print()

        print("Conclusión")

        print("----------")

        print(
            f"Se recomienda atender primero las vulnerabilidades "
            f"de severidad {highest.severity} antes de desplegar "
            f"la aplicación."
        )

        print()

        print("=" * 78)

        print("Fin del reporte.")

        print("=" * 78)