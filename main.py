from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# Dados simulados (você substituirá por dados reais via scraping ou APIs)
concursos = [
    {"id": 1, "cargo": "Analista", "estado": "SP", "salario": 5000, "orgao": "TRE-SP"},
    {"id": 2, "cargo": "Técnico", "estado": "RJ", "salario": 3000, "orgao": "TRE-RJ"},
    {"id": 3, "cargo": "Fiscal", "estado": "MG", "salario": 7000, "orgao": "Prefeitura de BH"},
    # Adicione mais concursos aqui...
]

@app.get("/concursos")
def listar_concursos(
    estado: Optional[str] = Query(None, description="Filtrar por estado"),
    cargo: Optional[str] = Query(None, description="Filtrar por cargo"),
    salario_min: Optional[float] = Query(None, description="Filtrar por salário mínimo"),
    orgao: Optional[str] = Query(None, description="Filtrar por órgão")
):
    resultados = concursos
    
    # Filtros
    if estado:
        resultados = [c for c in resultados if c['estado'].lower() == estado.lower()]
    if cargo:
        resultados = [c for c in resultados if cargo.lower() in c['cargo'].lower()]
    if salario_min:
        resultados = [c for c in resultados if c['salario'] >= salario_min]
    if orgao:
        resultados = [c for c in resultados if orgao.lower() in c['orgao'].lower()]
    
    return resultados

