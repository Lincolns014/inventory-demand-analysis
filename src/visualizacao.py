import matplotlib.pyplot as plt
import os

def gerar_grafico(pedido):

    os.makedirs("outputs", exist_ok=True)

    pedido = pedido[pedido['Quantidade'] != 0]

    if pedido.empty:
        print("Nenhum dado para plotar")
        return

    plt.figure(figsize=(10, 20))
    barras = plt.barh(pedido['Produto'], pedido['Quantidade'])

    plt.bar_label(barras)
    plt.title("Distribuição de Produtos")
    plt.tight_layout()

    caminho = "outputs/distribuicao_produtos.png"
    plt.savefig(caminho)

    print(f"📊 Gráfico salvo em {caminho}")