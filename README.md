# Monitoramento Fiscal Oficial

Ferramenta aberta de acompanhamento de despesas do Governo Federal com base exclusiva em fontes oficiais.

## Objetivo
Monitorar de forma transparente e rastreável as despesas primárias, benefícios sociais, renúncias fiscais e publicidade institucional do Governo Federal, com metodologia clara e dados oficiais.

## Princípios
- Toda informação deve ser rastreável até a fonte oficial
- Separação rigorosa entre despesa realizada, renúncia e crédito
- Preferência pela fase de **Pagamento**
- Metodologia pública e auditável

## Estrutura do projeto
- `src/collectors` → Coleta de dados (CSV + API)
- `src/classifiers` → Classificação orçamentária
- `src/processors` → Tratamento e agregação
- `docs` → Metodologia e guias
- `data` → Dados brutos e processados
- `scripts` → Scripts de atualização

## Fontes principais
- Portal da Transparência (CSVs diários de despesas)
- Portal da Transparência (API de dados)
- Portal da Transparência (arquivos de benefícios)
- Receita Federal (Demonstrativo de Gastos Tributários)

## Como começar

### Opção 1 – API (mais leve)
1. Obtenha a chave em: https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email
2. Use o coletor em `src/collectors/api_portal.py`
3. Veja o guia em `docs/como-usar-api.md`

### Opção 2 – Arquivos CSV
1. Baixe em: https://portaldatransparencia.gov.br/download-de-dados/despesas
2. Coloque o arquivo de Pagamento em `data/raw/`
3. Use o coletor em `src/collectors/despesas_portal.py`

## Status atual
Fase 1 em construção: despesas primárias + publicidade institucional.
Coletor via API e processador de agregação já disponíveis.
