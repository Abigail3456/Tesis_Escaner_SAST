from sast_escaner.core.rule import Rule

DEFAULT_RULES = [

    Rule(
        id="R-01",
        name="Uso de eval()",
        method="AST",
        pattern="eval",
        severity="Crítica",
        description="Uso de ejecución dinámica de código.",
        recommendation="Evitar eval() y utilizar alternativas seguras."
    ),

    Rule(
        id="R-02",
        name="Uso de exec()",
        method="AST",
        pattern="exec",
        severity="Crítica",
        description="Ejecución dinámica de código.",
        recommendation="Evitar exec()."
    ),

    Rule(
        id="R-03",
        name="Uso de os.system()",
        method="AST",
        pattern="os.system",
        severity="Alta",
        description="Ejecución de comandos del sistema.",
        recommendation="Utilizar subprocess de forma segura."
    ),

    Rule(
        id="R-04",
        name="Contraseña hardcodeada",
        method="REGEX",
        pattern="password",
        severity="Media",
        description="Credencial almacenada directamente.",
        recommendation="Utilizar variables de entorno."
    ),
    Rule(
    id="R-05",
    name="Contraseña hardcodeada",
    method="REGEX",
    pattern="password",
    severity="Media",
    description="Se detectó una contraseña almacenada directamente en el código fuente.",
    recommendation="Utilizar variables de entorno o mecanismos seguros para gestionar credenciales."
    ),

    Rule(
    id="R-06",
    name="API Key hardcodeada",
    method="REGEX",
    pattern="api_key",
    severity="Alta",
    description="Se detectó una API Key almacenada directamente en el código fuente.",
    recommendation="Almacenar las API Keys en variables de entorno o servicios seguros."
    ),

    Rule(
    id="R-07",
    name="Token hardcodeado",
    method="REGEX",
    pattern="token",
    severity="Alta",
    description="Se detectó un token almacenado directamente en el código fuente.",
    recommendation="Evitar almacenar tokens dentro del código fuente."
    ),

    Rule(
    id="R-08",
    name="Secret hardcodeado",
    method="REGEX",
    pattern="secret",
    severity="Alta",
    description="Se detectó un valor secreto almacenado directamente en el código fuente.",
    recommendation="Gestionar los secretos mediante variables de entorno o gestores de secretos."
    ),

]