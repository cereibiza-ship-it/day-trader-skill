import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "trader" / "watchlist.json"

def cargar_acciones():
    with RUTA.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    resultados = []
    for accion in datos.get("hits", []):
        resultados.append({
            "activo": accion.get("symbol", ""),
            "mercado": "EE. UU.",
            "senal": ", ".join(accion.get("setups", [])),
            "riesgo": "Pendiente de evaluar"
        })

    return resultados
