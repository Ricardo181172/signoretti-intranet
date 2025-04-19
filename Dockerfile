# Use a imagem oficial do Python
FROM python:3.11.4  

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o container
COPY . /app/

# Expõe a porta 8000, onde o Django vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
