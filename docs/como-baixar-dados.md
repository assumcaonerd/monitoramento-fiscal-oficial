# Como baixar os dados de Pagamento

## Passo a passo

1. Acesse: https://portaldatransparencia.gov.br/download-de-dados/despesas
2. Selecione o **Exercício** (2026)
3. Selecione o **Mês** desejado
4. Clique em **Baixar**
5. O Portal gerará um pacote com vários arquivos CSV, incluindo:
   - `AAAAMMDD_Despesas_Pagamento.csv`
   - Outros arquivos de empenho e liquidação

6. Coloque o arquivo `*_Despesas_Pagamento.csv` dentro da pasta `data/raw/` do repositório.

## Observação importante

Os arquivos são grandes. Recomenda-se começar com um ou dois meses recentes para testar o processamento.

Após baixar, execute o script de processamento para gerar as primeiras agregações.
