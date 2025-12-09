class ModelTrainer:
    def __init__(self, model_name, hyperparams):
        # O underline (_) indica: "Isso é para uso interno da classe, não mexa!"
        self.model_name = model_name
        self._config = hyperparams

    def train(self):
        # Aqui simulamos o uso dessas configs protegidas
        print(f"--> Iniciando treinamento do modelo: {self.model_name}")
        print(f"--> Carregando hiperparâmetros: {self._config}")
        print("--> Treinamento finalizado (Simulação).")

"""
# --- USO ---

# Configuração que definimos no início (Isso é muito comum em MLOps)
params = {"learning_rate": 0.01, "epochs": 10}

# Instanciando o treinador
meu_treinador = ModelTrainer("RandomForest_v1", params)

# Executando
meu_treinador.train()
"""