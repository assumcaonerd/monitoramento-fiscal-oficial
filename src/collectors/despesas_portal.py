from pathlib import Path
import pandas as pd
from typing import Optional

class ColetorDespesasPortal:
    """
    Coletor de despesas do Portal da Transparência.
    Prioriza arquivos CSV diários de Pagamento.
    """

    def __init__(self, data_dir: str = "data/raw"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def listar_arquivos_disponiveis(self) -> None:
        """
        Orienta o usuário sobre onde baixar os arquivos.
        O Portal disponibiliza os CSVs por mês em:
        https://portaldatransparencia.gov.br/download-de-dados/despesas
        """
        print("Acesse: https://portaldatransparencia.gov.br/download-de-dados/despesas")
        print("Baixe o pacote do mês desejado e coloque os arquivos em data/raw/")

    def carregar_pagamento(self, caminho_arquivo: str) -> pd.DataFrame:
        """
        Carrega e normaliza o arquivo de Pagamento.
        """
        caminho = Path(caminho_arquivo)
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        df = pd.read_csv(
            caminho,
            sep=";",
            encoding="latin1",
            dtype=str,
            low_memory=False
        )

        # Normalização do valor
        if "Valor Pago" in df.columns:
            df["Valor Pago"] = (
                df["Valor Pago"]
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float)
            )
        elif "Valor" in df.columns:
            df["Valor Pago"] = (
                df["Valor"]
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float)
            )

        # Padronização de nomes de colunas mais comuns
        mapeamento = {
            "Código Órgão Superior": "orgao_superior_codigo",
            "Nome Órgão Superior": "orgao_superior_nome",
            "Código Órgão": "orgao_codigo",
            "Nome Órgão": "orgao_nome",
            "Código Função": "funcao_codigo",
            "Nome Função": "funcao_nome",
            "Código Subfunção": "subfuncao_codigo",
            "Nome Subfunção": "subfuncao_nome",
            "Código Programa": "programa_codigo",
            "Nome Programa": "programa_nome",
            "Código Ação": "acao_codigo",
            "Nome Ação": "acao_nome",
        }

        df = df.rename(columns={k: v for k, v in mapeamento.items() if k in df.columns})
        
        return df
