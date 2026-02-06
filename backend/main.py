from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path

app = FastAPI(title="MallaClientes API", description="API para segmentación y scoring de clientes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = Path(__file__).parent.parent / 'MallaClientes.xlsx'

def load_clientes():
    if DATA_PATH.exists():
        df = pd.read_excel(DATA_PATH)
        # Solo columnas clave para demo
        cols = [c for c in df.columns if 'nit' in c.lower() or 'nombre' in c.lower() or 'rutero' in c.lower() or 'cupo' in c.lower() or 'clasific' in c.lower() or 'cartera' in c.lower()]
        return df[cols].head(50).to_dict(orient='records')
    return []

@app.get("/")
def read_root():
    return {"message": "API de MallaClientes funcionando"}

@app.get("/clientes")
def get_clientes():
    """Devuelve una muestra de clientes con columnas clave"""
    return {"clientes": load_clientes()}
