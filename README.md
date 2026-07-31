# Escáner SAST para Scripts Python

## Descripción

Este proyecto implementa un escáner **SAST (Static Application Security Testing)** desarrollado en Python como parte de un trabajo de investigación. La herramienta realiza análisis estático sobre scripts Python con el objetivo de detectar vulnerabilidades comunes antes de la ejecución del código.

El escáner utiliza dos técnicas de análisis:

- **Análisis mediante AST (Abstract Syntax Tree)** para identificar el uso de funciones potencialmente peligrosas.
- **Análisis mediante expresiones regulares (Regex)** para detectar credenciales o información sensible almacenada dentro del código fuente.

Los hallazgos encontrados son evaluados mediante un motor de reglas y posteriormente presentados en un reporte resumido.

---

## Características

- Análisis estático de código fuente.
- Detección basada en AST.
- Detección mediante expresiones regulares.
- Motor de reglas independiente.
- Clasificación por severidad.
- Generación de reportes en consola.
- Arquitectura modular.

---

## Estructura del proyecto

```
sast_escaner/
│
├── analyzers/
│   ├── ast_analyzer.py
│   └── regex_analyzer.py
│
├── core/
│   ├── finding.py
│   ├── result.py
│   ├── rule.py
│   └── rule_engine.py
│
├── reports/
│   └── report_generator.py
│
├── rules/
│   └── default_rules.py
│
├── tests/
│   └── scripts de prueba
│
└── main.py
```

---

## Vulnerabilidades detectadas

Actualmente el escáner es capaz de detectar:

| ID | Vulnerabilidad | Método |
|----|----------------|--------|
| R-01 | Uso de `eval()` | AST |
| R-02 | Uso de `exec()` | AST |
| R-03 | Uso de `pickle.loads()` | AST |
| R-04 | Uso de `subprocess` inseguro | AST |
| R-05 | Contraseña hardcodeada | Regex |
| R-06 | API Key hardcodeada | Regex |
| R-07 | Token hardcodeado | Regex |
| R-08 | Secret hardcodeado | Regex |

---

## Requisitos

- Python 3.10 o superior

---

## Instalación

Clonar el repositorio:

```bash
git clone <repositorio>
```

Entrar al proyecto:

```bash
cd sast_escaner
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar el escáner:

```bash
python -m sast_escaner.main
```

Ingresar la ruta del archivo Python que se desea analizar.

Ejemplo:

```text
C:\Users\Usuario\Desktop\archivo.py
```

---

## Salida

El sistema genera un reporte que incluye:

- Archivo analizado
- Número de hallazgos
- Tabla resumen
- Severidad
- Nivel de riesgo
- Conclusión del análisis

---

## Arquitectura

El sistema está dividido en módulos independientes:

```
Archivo Python
        │
        ▼
 AST Analyzer
        │
        ▼
 Regex Analyzer
        │
        ▼
 Rule Engine
        │
        ▼
 Report Generator
```

Esta arquitectura facilita la incorporación de nuevas reglas de análisis sin modificar el funcionamiento de los módulos existentes.

---

## Estado del proyecto

Versión actual: **1.0**

Funcionalidades implementadas:

- ✔ Motor de reglas
- ✔ AST Analyzer
- ✔ Regex Analyzer
- ✔ Reporte en consola

---

## Autor

Proyecto desarrollado como parte de una investigación para la implementación de un escáner SAST orientado al análisis estático de scripts Python.
