# 1. Imagem Base: Começamos com um Linux leve que já tem Python instalado
FROM python:3.9-slim

# 2. Diretório de Trabalho: Criamos uma pasta '/app' dentro do container
WORKDIR /app

# 3. Copiar Arquivos: Pegamos tudo da pasta atual (.) e jogamos na pasta do container (.)
COPY . .

# --- A CORREÇÃO ESTÁ AQUI ---
# Manda o Python ler o arquivo e instalar as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# O comando padrão (será substituído pelo docker-compose, mas é bom ter)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]