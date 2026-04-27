from flask import Flask
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Localização dinâmica do CSV
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(diretorio_atual, '..', 'imigrantes_canada.csv')

        # Processamento de Dados
        df = pd.read_csv(csv_path)
        df.set_index('País', inplace=True)
        anos = [str(ano) for ano in range(1980, 2005)]
        df_brasil = df.loc['Brasil', anos]
        
        # Criação do Gráfico Profissional
        fig = px.line(
            x=anos, 
            y=df_brasil.values, 
            title='📊 Evolução da Imigração: Brasil para o Canadá',
            labels={'x': 'Ano', 'y': 'Número de Imigrantes'},
            markers=True
        )
        fig.update_traces(line_color='#4169E1', line_width=3) # Azul Royal
        fig.update_layout(plot_bgcolor='white')
        
        grafico_html = pio.to_html(fig, full_html=False)
        tabela_html = df.head().to_html(classes='table table-striped table-hover border')

        # Retorno com HTML/Bootstrap
        return f"""
        <html>
            <head>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
                <title>Dashboard Imigração</title>
            </head>
            <body class="bg-light p-5">
                <div class="container bg-white p-4 shadow rounded">
                    <h1 class="text-center mb-4">Dashboard de Análise: Imigração</h1>
                    <div>{grafico_html}</div>
                    <hr class="my-5">
                    <h3>📌 Amostra do Dataset</h3>
                    <div class="table-responsive">{tabela_html}</div>
                </div>
            </body>
        </html>
        """
    except Exception as e:
        return f"<h1>Erro:</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)