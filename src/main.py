import os
from processar_dados import carregar_dados
from analise import calcular_pedido_mensal
from visualizacao import gerar_grafico

def main():

    print("📥 Carregando dados...")
    df = carregar_dados("data/BD_07_2025.xlsx")

    print("📊 Calculando pedido mensal...")
    pedido = calcular_pedido_mensal(df, ["2025-07","2025-06"])

    os.makedirs("outputs", exist_ok=True)

    caminho = "outputs/pedidos.xlsx"
    pedido.to_excel(caminho, index=False)

    print(f"📁 Pedido salvo em {caminho}")

    print("📈 Gerando gráfico...")
    gerar_grafico(pedido)

    print("✅ Processo finalizado!")


if __name__ == "__main__":
    main()