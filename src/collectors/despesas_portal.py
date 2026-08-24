"""
Coletor de despesas do Portal da Transparência.
Versão atualizada com base no schema do projeto turicas/transparencia-gov-br
e adaptada para 2026.
"""

from pathlib import Path
from datetime import date
from typing import Optional
import pandas as pd


class ColetorDespesasPortal:
    """
    Coletor de arquivos de Pagamento do Portal da Transparência.
    """

    BASE_DOWNLOAD = "https://portaldatransparencia.gov.br/download-de-dados/despesas"

    def __init__(self, data_dir: str = "data/raw"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def url_arquivo(self, ano: int, mes: int, dia: int) -> str:
        """
        Monta a URL de download do pacote diário.
        Exemplo: 20260820
        """
        return f"{self.BASE_DOWNLOAD}/{ano}{mes:02d}{dia:02d}"

    def carregar_pagamento(self, caminho_arquivo: str) -> pd.DataFrame:
        """
        Carrega e normaliza o arquivo de Pagamento.
        Aceita CSV com separador ; e encoding latin1.
        """
        caminho = Path(caminho_arquivo)
        if not caminho.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        df = pd.read_csv(
            caminho,
            sep=";",
            encoding="latin1",
            dtype=str,
            low_memory=False,
        )

        # Normalização do valor pago
        colunas_valor = [c for c in df.columns if "valor" in c.lower() and "pago" in c.lower()]
        if not colunas_valor:
            colunas_valor = [c for c in df.columns if "valor" in c.lower()]

        if colunas_valor:
            col = colunas_valor[0]
            df["valor_pago"] = (
                df[col]
                .astype(str)
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .str.replace(r"[^0-9\.]", "", regex=True)
            )
            df["valor_pago"] = pd.to_numeric(df["valor_pago"], errors="coerce").fillna(0.0)

        # Padronização de nomes de colunas mais comuns
        mapeamento = {
            "Código Órgão Superior": "codigo_orgao_superior",
            "Nome Órgão Superior": "orgao_superior",
            "Código Órgão": "codigo_orgao",
            "Nome Órgão": "orgao",
            "Código Unidade Gestora": "codigo_unidade_gestora",
            "Nome Unidade Gestora": "unidade_gestora",
            "Código Favorecido": "codigo_favorecido",
            "Nome Favorecido": "favorecido",
            "Código Função": "codigo_funcao",
            "Nome Função": "funcao",
            "Código Subfunção": "codigo_subfuncao",
            "Nome Subfunção": "subfuncao",
            "Código Programa": "codigo_programa",
            "Nome Programa": "programa",
            "Código Ação": "codigo_acao",
            "Nome Ação": "acao",
            "Data Emissão": "data_emissao",
            "Código Pagamento": "codigo_pagamento",
        }

        df = df.rename(columns={k: v for k, v in mapeamento.items() if k in df.columns})

        return df

    def listar_instrucoes(self) -> None:
        print("=" * 60)
        print("Como baixar o arquivo de Pagamento")
        print("=" * 60)
        print("1. Acesse: https://portaldatransparencia.gov.br/download-de-dados/despesas")
        print("2. Selecione o exercício e o mês")
        print("3. Baixe o pacote")
        print("4. Extraia o arquivo que termina com _Despesas_Pagamento.csv")
        print("5. Coloque em data/raw/")
        print("=" * 60)
