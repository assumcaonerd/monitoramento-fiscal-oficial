"""
Processador e agregador de despesas.
"""

import pandas as pd
from typing import Dict, List

class AgregadorDespesas:
    """
    Realiza agregações básicas para monitoramento fiscal.
    """

    def agregar_por_bloco(self, df: pd.DataFrame, coluna_valor: str = "Valor Pago") -> pd.DataFrame:
        """
        Agrega valores por bloco de classificação.
        """
        if "bloco" not in df.columns:
            raise ValueError("DataFrame precisa ter a coluna 'bloco'")
        
        resultado = (
            df.groupby("bloco")[coluna_valor]
            .sum()
            .reset_index()
            .sort_values(coluna_valor, ascending=False)
        )
        return resultado

    def agregar_por_funcao(self, df: pd.DataFrame, coluna_valor: str = "Valor Pago") -> pd.DataFrame:
        """
        Agrega por função de governo.
        """
        colunas = [c for c in ["funcao_codigo", "funcao_nome"] if c in df.columns]
        if not colunas:
            raise ValueError("Colunas de função não encontradas")
        
        resultado = (
            df.groupby(colunas)[coluna_valor]
            .sum()
            .reset_index()
            .sort_values(coluna_valor, ascending=False)
        )
        return resultado

    def agregar_por_orgao(self, df: pd.DataFrame, coluna_valor: str = "Valor Pago") -> pd.DataFrame:
        """
        Agrega por órgão.
        """
        colunas = [c for c in ["orgao_codigo", "orgao_nome"] if c in df.columns]
        if not colunas:
            raise ValueError("Colunas de órgão não encontradas")
        
        resultado = (
            df.groupby(colunas)[coluna_valor]
            .sum()
            .reset_index()
            .sort_values(coluna_valor, ascending=False)
        )
        return resultado

    def resumo_geral(self, df: pd.DataFrame, coluna_valor: str = "Valor Pago") -> Dict:
        """
        Gera um resumo executivo.
        """
        total = df[coluna_valor].sum()
        return {
            "total": total,
            "total_formatado": f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "quantidade_registros": len(df),
            "data_processamento": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")
        }
