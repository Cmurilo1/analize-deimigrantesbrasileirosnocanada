from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Caminho para o seu arquivo CSV que está na raiz
    csv_path = os.path.join(os.getcwd(), 'imigrantes_canada.csv')
    
    try:
        df = pd.read_csv(csv_path)
        # Retorna as 5 primeiras linhas como HTML
        return f"<h1>Análise de Imigrantes</h1> {df.head().to_html()}"
    except Exception as e:
        return f"Erro ao ler o arquivo: {str(e)}"

# A Vercel precisa que a variável seja 'app'