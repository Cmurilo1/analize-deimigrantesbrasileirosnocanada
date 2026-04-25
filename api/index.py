from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Isso busca o arquivo independente de onde a Vercel coloque a pasta api
    base_path = os.path.dirname(os.path.abspath(file))
    # Sobe um nível para sair da pasta 'api' e achar o CSV na raiz
    csv_path = os.path.join(base_path, '..', 'imigrantes_canada.csv')
    
    try:
        if not os.path.exists(csv_path):
            return f"Erro: Arquivo CSV não encontrado no caminho: {csv_path}"
            
        df = pd.read_csv(csv_path)
        return f"<h1>Análise de Imigrantes</h1> {df.head().to_html()}"
    except Exception as e:
        return f"Erro ao processar os dados: {str(e)}"