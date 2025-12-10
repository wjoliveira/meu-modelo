from trainer import ModelTrainer
# Teste simples: treina com poucas épocas só para ver se o código não quebra
try:
    treinador = ModelTrainer("Modelo_Teste_Github", {"epochs": 1})
    treinador.train()
    print("Sucesso: O modelo treinou sem erros!")
except Exception as e:
    print(f"Erro crítico: {e}")
    exit(1) # Avisa o GitHub que falhou