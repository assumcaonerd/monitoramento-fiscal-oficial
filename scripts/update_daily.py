from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from src.collectors.despesas_portal import ColetorDespesasPortal
from src.classifiers.classificador import ClassificadorOrcamentario

def main():
    coletor = ColetorDespesasPortal()
    classificador = ClassificadorOrcamentario()

    print("=== Monitoramento Fiscal Oficial ===")
    print("1. Baixe os arquivos de Pagamento do Portal da Transparência")
    print("2. Coloque-os em data/raw/")
    print("3. Execute o processamento")

    # Exemplo de uso (após baixar o arquivo):
    # df = coletor.carregar_pagamento("data/raw/20260823_Despesas_Pagamento.csv")
    # df = classificador.aplicar(df)
    # print(df.groupby("bloco")["Valor Pago"].sum())

if __name__ == "__main__":
    main()
