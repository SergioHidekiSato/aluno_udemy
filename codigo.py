import pandas as pd
import os

# Caminho para a pasta Downloads do usuário atual
caminho_downloads = os.path.expanduser('~/Downloads/dominios.csv')

# Carrega o CSV
df = pd.read_csv(caminho_downloads, sep=';', encoding='utf-8')

# Supondo que a coluna com o domínio se chama 'nome'
df['link'] = 'https://' + df['nome']

# Salva apenas a coluna de links em Parquet
df[['link']].to_parquet('sites_gov_br.parquet', index=False)
