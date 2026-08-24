import pandas as pd

class ClassificadorOrcamentario:
    """
    Classifica despesas oficiais em blocos de monitoramento.
    """

    def __init__(self):
        self.termos_publicidade = [
            "publicidade",
            "propaganda",
            "comunicação institucional",
            "divulgação",
            "campanha publicitária",
            "mídia"
        ]

    def classificar_linha(self, row: pd.Series) -> str:
        acao = str(row.get("acao_nome", "")).lower()
        
        for termo in self.termos_publicidade:
            if termo in acao:
                return "PUBLICIDADE_INSTITUCIONAL"
        
        return "DESPESA_PRIMARIA"

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["bloco"] = df.apply(self.classificar_linha, axis=1)
        return df
