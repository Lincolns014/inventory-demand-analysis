import pandas as pd

def calcular_pedido_mensal(df, meses):

    df_filtrado = df[
        df['Hora de início'].dt.to_period('M').astype(str).isin(meses)
    ].copy()

    colunas_para_somar = [
    'Bateria AA (UNID.)','Bateria AAA (UNID.)','Bateria recarregável AA (UNID.)','Cabo adaptador displayport M/DVI F (UND.)',
    'Cabo de rede (METRO)','Carregador USB de pilhas (UNID.)','Fone headset P2 (UNID.)','Mouse pad c/ apoio em gel (UNID.)',
    'Itens de A a Z.Pen drive 16/32/64GB (UNID.)','Webcam soho (UNID.)','Mouse (UNID.)','Teclado (UNID.)','WEBCAM HD USB intelbras 1080P',
    'Webcam Go Tech HD 720P','Agenda 2024 (UNID.)','Alfinete para mapa/quadro (UNID.)','Apagador p/ quadro branco (UNID.)',
    'Apontador (UNID.)','Barbante (METRO)','Bloco adesivo POST-IT - 75x100mm (UNID)','Bloco de papel p/ cavalete (UNID.)',
    'Borracha (UNID.)','Caderno de protocolo (UNID.)','Caixa arquivo (UNID.)','Caixa p/ correio (UNID.)','Caneta - azul (UNID.)',
    'Caneta - preta (UNID.)','Caneta - verde (UNID.)','Caneta - vermelha (UNID.)','Capa p/ encadernar - transparente (UNID.)',
    'Clips 2/0 (CX 100 UNID.)','Clips 3/0 (CX 50 UNID.)','Clips 4.0 (CX 50 UNID.)','Clips 6.0 (CX 50 UNID.)','Clips 8.0 (CX 25 UNID.)',
    'Cola bastão (UNID.)','Cola líquida 90g (UNID.)','Cola super bonder (UNID.)','Colchetes N° 3 (CX 100 UNID.)','Colchetes N° 8 (CX 100 UNID.)',
    'Colchetes N° 11 (CX 100 UNID.)','Colchetes N° 12 (CX 100 UNID.)','Colchetes N° 15 (CX 100 UNID.)','Contra capa p/ encadernar - preta (UNID.)',
    'Cordão p/ crachá (UNID.)','Display acrílico p/ mesa (UNID.)','Elático amarelo p/ dinheiro (UNID.)','Envelope A3 - pardo (UNID.)','Envelope A4 - pardo (UNID.)',
    'Envelope A5 - branco (UNID.)','Envelope Ofício - branco (UNID.)','Espiral p/ encadernar (UNID.)','Estilete (UNID.)','Etiqueta autoadesiva N° 1 (FOLHA)',
    'Etiqueta autoadesiva N° 8 (FOLHA)','Etiqueta autoadesiva N° 10 (FOLHA)','Etiqueta autoadesiva N° 20 (FOLHA)','Etiqueta autoadesiva N° 21 (FOLHA)',
    'Etiqueta autoadesiva N° 39 (FOLHA)','Extrator de Grampo (UNID.)','Filme adesivo p/ encadernar (METRO)','Fita adesiva - transparente 18mm X 50m (UNID.)',
    'Fita adesiva - transparente 48mm X 50m (UNID.)','Fita crepe 18mm X 50m (UNID.)','Fita crepe 48mm X 50m (UNID.)','Fita dupla face 18mm X 30m (UNID.)',
    'Fita dupla face 19mm X 30m (UNID.)','Furador tam. G (UNID.)','Furador tam. P (UNID.)','Grampeador tam. G (UNID.)','Grampeador tam. P (UNID.)','Grampo 9/14 (CX 1000 UNID)',
    'Grampo 9/14 (CX 5000 UNID)','Grampo 26/6 (CX 1000 UNID)','Grampo 26/6 (CX 5000 UNID)','Grampo Trilho Dello Estendido 300x9x112mm Branco PCT 50UN','Lâmina p/ estilete (UNID.)',
    'Lápis HB2 (UNID.)','Lápis HB5 (UNID.)','Marca texto - amarelo (UNID.)','Marca texto - azul (UNID.)','Marca texto - laranja (UNID.)','Marca texto - rosa (UNID.)',
    'Marca texto - verde (UNID.)','Marcador p/ quadro branco - azul (UNID.)','Marcador p/ quadro branco - preto (UNID.)','Marcador p/ quadro branco - verde (UNID.)',
    'Marcador p/ quadro branco - vermelho (UNID.)','Marcador permanente - azul (UNID.)','Marcador permanente - verde (UNID.)','Marcador permanente - vermelho (UNID.)',
    'Molha dedos (UNID.)','Papel vergê (FOLHA)','Pasta ABA c/ elástico (UNID.)','Pasta L (UNID.)','Pasta sanfonada (UNID.)','Pasta suspensa (UNID.)','Percevejos (UNID)',
    'Pincel atômico - preto (UNID.)','Porta caneta (UNID.)','Prendendor de papel 8mm (UNID.)','Prendendor de papel 25mm (UNID.)','Prendendor de papel 41mm (UNID.)',
    'Prendendor de papel 51mm (UNID.)','Régua 30cm (UNID.)','Régua 50cm (UNID.)','Resma A3 (UNID.)','Resma A4 (UNID.)','Tesoura tam. G (UNID.)'
    ]

    # 🔥 evita erro se alguma coluna não existir
    colunas_existentes = [
        col for col in colunas_para_somar if col in df_filtrado.columns
    ]

    # 🔥 converte para número
    df_filtrado[colunas_existentes] = df_filtrado[colunas_existentes].apply(
        pd.to_numeric, errors='coerce'
    )

    soma = df_filtrado[colunas_existentes].sum()

    pedido = pd.DataFrame(soma).reset_index()
    pedido.columns = ['Produto', 'Quantidade']

    return pedido