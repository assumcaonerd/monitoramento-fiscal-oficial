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
- `src/collectors` → Coleta de dados
- `src/classifiers` → Classificação orçamentária
- `src/processors` → Tratamento e agregação
- `docs` → Metodologia e limitações
- `data` → Dados brutos e processados
- `scripts` → Scripts de atualização

## Fontes principais
- Portal da Transparência (CSVs diários de despesas)
- Portal da Transparência (arquivos de benefícios)
- Receita Federal (Demonstrativo de Gastos Tributários)

## Status atual
Fase 1 em construção: despesas primárias + publicidade institucional.
