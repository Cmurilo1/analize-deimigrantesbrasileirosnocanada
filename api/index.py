from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Pega o caminho absoluto da pasta onde este arquivo (index.py) está
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Se o CSV estiver na RAIZ do projeto e o index.py dentro de /api:
        csv_path = os.path.join(diretorio_atual, '..', 'imigrantes_canada.csv')

        
        # Caso o CSV esteja na MESMA PASTA que este index.py, use:
        # csv_path = os.path.join(diretorio_atual, 'imigrantes_canada.csv')

        if not os.path.exists(csv_path):
            return f"Erro: Arquivo não encontrado em: {csv_path}"
            
        # Lê o CSV especificando o encoding (evita erro de acentuação)
        df = pd.read_csv(csv_path)
        
        # Transforma os dados em HTML
        tabela = df.head().to_html(classes='table table-striped')
        
        return f"""
        <html>
            <head><title>Análise Canadá</title></head>
            <body>
                <h1>✅ Conectado com Sucesso!</h1>
                <p>Abaixo os primeiros 5 registros do arquivo:</p>
                {tabela}
            </body>
        </html>
        """
    except Exception as e:
        return f"<h1>❌ Erro no Servidor</h1><p>{str(e)}</p>"

# Importante para rodar localmente no VS Code
if __name__ == "__main__":
    app.run(debug=True)
