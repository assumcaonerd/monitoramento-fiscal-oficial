# Como usar a API do Portal da Transparência

## 1. Obter a chave de acesso

1. Acesse: https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email
2. Autentique com conta gov.br (nível Prata ou Ouro recomendado)
3. A chave será enviada para o e-mail da conta

## 2. Usar o coletor

```python
from src.collectors.api_portal import ColetorAPIPortal

coletor = ColetorAPIPortal(chave_api="SUA_CHAVE_AQUI")

# Testar conexão
if coletor.testar_conexao():
    print("Conexão OK")

# Buscar órgãos
orgaos = coletor.orgaos_siafi(pagina=1)
print(orgaos[:3])
```

## 3. Limites da API

- 00h às 06h: até 700 requisições por minuto
- Demais horários: 400 requisições por minuto
- Algumas rotas têm limite menor (180/min)

## Observação

Para volumes grandes, continue preferindo os arquivos CSV de download.
A API é excelente para consultas pontuais, testes e atualizações incrementais.
