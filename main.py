from fastapi import FastAPI
from trainer import ModelTrainer
from pymongo import MongoClient

app = FastAPI()

# Conexão com o Banco (Global)
# Em produção real, usamos variáveis de ambiente para a URL
client = MongoClient("mongodb://banco-dados:27017/")
db = client["mlops_db"]
collection = db["historico_api"]

@app.get("/")
def home():
    return {"mensagem": "API de MLOps está Online! 🚀"}

@app.post("/treinar")
def treinar_modelo():
    # 1. Configurar e Treinar
    params = {"learning_rate": 0.05, "epochs": 20}
    treinador = ModelTrainer("Modelo_API_v1", params)
    treinador.train()
    
    # 2. Salvar log no MongoDB
    registro = {
        "acao": "treinamento",
        "modelo": "Modelo_API_v1",
        "status": "sucesso"
    }
    collection.insert_one(registro)
    
    return {"status": "Modelo treinado e registrado no MongoDB!"}