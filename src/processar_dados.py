import pandas as pd

def carregar_dados(caminho):

    df = pd.read_excel(caminho, sheet_name='Base auxiliar')

    df['Hora de início'] = pd.to_datetime(
        df['Hora de início'], format='%d-%m-%Y'
    )

    return df