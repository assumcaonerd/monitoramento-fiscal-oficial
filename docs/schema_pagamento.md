# Schema do Arquivo de Pagamento

Baseado no repositório turicas/transparencia-gov-br e nos arquivos oficiais do Portal da Transparência.

## Campos principais mapeados

| Nome Original | Nome Interno | Tipo |
|---------------|--------------|------|
| Código Órgão Superior | codigo_orgao_superior | integer |
| Nome Órgão Superior | orgao_superior | text |
| Código Órgão | codigo_orgao | integer |
| Nome Órgão | orgao | text |
| Código Unidade Gestora | codigo_unidade_gestora | integer |
| Unidade Gestora | unidade_gestora | text |
| Código Gestão | codigo_gestao | integer |
| Gestão | gestao | text |
| Código Favorecido | codigo_favorecido | text |
| Favorecido | favorecido | text |
| Código Pagamento | codigo_pagamento | text |
| Data Emissão | data_emissao | date |
| Valor Original do Pagamento | valor_original | decimal |
| Valor do Pagamento Convertido pra R$ | valor_pago | decimal |
| Código Grupo de Despesa | codigo_grupo_de_despesa | text |
| Grupo de Despesa | grupo_de_despesa | text |
| Código Elemento de Despesa | codigo_elemento_de_despesa | text |
| Elemento de Despesa | elemento_de_despesa | text |
| Código Modalidade de Aplicação | codigo_modalidade_de_aplicacao | text |
| Modalidade de Aplicação | modalidade_de_aplicacao | text |
| Observação | observacao | text |
| Processo | processo | text |

## Observação

O arquivo oficial usa separador `;` e encoding `latin1` (ou `ISO-8859-1`).
O valor monetário vem com ponto como separador de milhar e vírgula como decimal.
