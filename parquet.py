import pandas as pd

# Substitua pelo caminho do seu arquivo Parquet
caminho_arquivo = '~/Downloads/sites_gov_br.parquet'

# Lê o arquivo Parquet em um DataFrame
df = pd.read_parquet(caminho_arquivo)

# Exibe o conteúdo na tela
print(df)