"""
Coletor via API do Portal da Transparência.
Mais leve e controlável que os CSVs diários completos.
"""

import requests
from typing import Optional, Dict, Any, List
from datetime import datetime

class ColetorAPIPortal:
    """
    Coletor de dados via API oficial do Portal da Transparência.
    Documentação: https://api.portaldatransparencia.gov.br/
    """

    BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"

    def __init__(self, chave_api: str):
        self.chave = chave_api
        self.headers = {
            "Accept": "application/json",
            "chave-api-dados": self.chave
        }

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def despesas_por_orgao(self, ano: int = 2026, pagina: int = 1) -> List[Dict]:
        """
        Consulta despesas agregadas por órgão.
        """
        params = {
            "ano": ano,
            "pagina": pagina
        }
        return self._get("despesas/por-orgao", params)

    def despesas_por_funcao(self, ano: int = 2026, pagina: int = 1) -> List[Dict]:
        """
        Consulta despesas por função de governo.
        """
        params = {
            "ano": ano,
            "pagina": pagina
        }
        return self._get("despesas/por-funcao", params)

    def orgaos_siafi(self, pagina: int = 1) -> List[Dict]:
        """
        Lista órgãos cadastrados no SIAFI.
        """
        return self._get("orgaos-siafi", {"pagina": pagina})

    def testar_conexao(self) -> bool:
        """
        Testa se a chave da API está funcionando.
        """
        try:
            self.orgaos_siafi(pagina=1)
            return True
        except Exception as e:
            print(f"Erro na conexão: {e}")
            return False


if __name__ == "__main__":
    print("Coletor API Portal da Transparência")
    print("Para usar, informe a chave obtida em:")
    print("https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email")
