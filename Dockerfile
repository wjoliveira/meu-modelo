# 1. Imagem Base: Começamos com um Linux leve que já tem Python instalado
FROM python:3.9-slim

# 2. Diretório de Trabalho: Criamos uma pasta '/app' dentro do container
WORKDIR /app

# 3. Copiar Arquivos: Pegamos tudo da pasta atual (.) e jogamos na pasta do container (.)
COPY . .

# 4. Comando de Execução: O que acontece quando o container liga?
CMD ["python", "main.py"]