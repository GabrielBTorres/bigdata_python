import pandas as pd
import plotly.express as px

arquivo_excel = "/content/controle2.xlsx"
df = pd.read_excel(arquivo_excel)

df["Desconto"] = df["Preço de Venda"] - df["Preço de Venda Atacado"]

dados_ordenados = df.sort_values(by="Desconto", ascending=False)

novo_arquivo_excel = "dados_tratados.xlsx"
dados_ordenados.to_excel(novo_arquivo_excel, index=False)

top_10_produtos = dados_ordenados.head(10)

fig = px.bar(top_10_produtos, x="Produtos", y="Desconto", title="Top 10 Produtos com Maiores Descontos no Atacado")
fig.show()


fig.write_html("grafico.html")