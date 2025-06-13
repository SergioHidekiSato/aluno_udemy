import pandas as pd
import requests

# URL do CSV de domínios do governo brasileiro
url = 'https://dominios.governo.gov.br/dados-abertos/dominios.csv'

# Baixa o arquivo CSV
response = requests.get(url)
with open('dominios_gov_br.csv', 'wb') as f:
    f.write(response.content)

# Carrega o CSV
df = pd.read_csv('dominios_gov_br.csv', sep=';', encoding='utf-8')

# Supondo que a coluna com o domínio se chama 'nome'
df['link'] = 'https://' + df['nome']

# Salva apenas a coluna de links em Parquet
df[['link']].to_parquet('sites_gov_br.parquet', index=False)