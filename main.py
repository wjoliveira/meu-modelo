from trainer import ModelTrainer

# --- USO ---

# Configuração que definimos no início (Isso é muito comum em MLOps)
params = {"learning_rate": 0.01, "epochs": 10}

# Instanciando o treinador
meu_treinador = ModelTrainer("RandomForest_v1", params)

# Executando
meu_treinador.train()