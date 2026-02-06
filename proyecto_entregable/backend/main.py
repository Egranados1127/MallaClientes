from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

# Datos de ejemplo simulados
clientes_demo = [
    {
        "NIT": "900123456",
        "Nombre Comercial": "Cliente Ejemplo S.A.S.",
        "Rutero": "Centro",
        "Cupo": 20000000,
        "Clasificación": "MADUREZ",
        "Calificación Cartera": "BUENA",
        "Score Importancia": 92.5,
        "Score Ubicación": 90,
        "Cluster 3x3": "Alta-Alta",
        "Ciudad": "Medellín",
        "Vendedor": "Juan Pérez"
    },
    {
        "NIT": "800654321",
        "Nombre Comercial": "Distribuciones XYZ",
        "Rutero": "Sur",
        "Cupo": 15000000,
        "Clasificación": "OPORTUNIDAD",
        "Calificación Cartera": "REGULAR",
        "Score Importancia": 78.2,
        "Score Ubicación": 100,
        "Cluster 3x3": "Media-Alta",
        "Ciudad": "Bogotá",
        "Vendedor": "Ana Gómez"
    },
    {
        "NIT": "901112233",
        "Nombre Comercial": "Comercializadora ABC",
        "Rutero": "Oriente",
        "Cupo": 8000000,
        "Clasificación": "DECLIVE",
        "Calificación Cartera": "RIESGO",
        "Score Importancia": 54.7,
        "Score Ubicación": 80,
        "Cluster 3x3": "Baja-Media",
        "Ciudad": "Cali",
        "Vendedor": "Carlos Ruiz"
    }
]

class Cliente(BaseModel):
    NIT: str
    Nombre_Comercial: str
    Rutero: str
    Cupo: int
    Clasificación: str
    Calificación_Cartera: str
    Score_Importancia: float
    Score_Ubicación: int
    Cluster_3x3: str
    Ciudad: str
    Vendedor: str

app = FastAPI(title="MallaClientes API", description="API demo para segmentación y scoring de clientes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/clientes", response_model=List[dict])
def get_clientes():
    return clientes_demo
