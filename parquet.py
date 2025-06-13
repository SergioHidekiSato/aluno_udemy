import pandas as pd
import os

# Caminho para o arquivo Parquet (expande ~ para o diretório do usuário)
caminho_arquivo = os.path.expanduser('~/Downloads/sites_gov_br.parquet')

# Lê o arquivo Parquet em um DataFrame
df = pd.read_parquet(caminho_arquivo)

# Exibe todas as linhas do DataFrame
pd.set_option('display.max_rows', None)
print(df.to_string())
