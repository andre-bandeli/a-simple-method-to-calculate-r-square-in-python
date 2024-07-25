import pandas as pd
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados da planilha (alterar o nome)
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Extrair os dados dados_observados e dados_previstos
dados_observados = df['estacao']
dados_previstos = df['eta']

# Calcular o R-squared
r2 = r2_score(dados_observados, dados_previstos)

# Gerar o gráfico de regressão
plt.figure(figsize=(10, 6))
sns.regplot(x=dados_observados, y=dados_previstos, line_kws={'color': 'red'}, ci=None)

# Adicionar títulos, labels e valor de R² no título
plt.title(f'Gráfico de Regressão: Dados dados_Observados vs dados_Previstos (R² = {r2:.2f})')
plt.xlabel('Dados dados_Observados (Estação)')
plt.ylabel('Dados dados_Previstos (ETA)')
plt.grid(True)

# Mostrar o gráfico
plt.show()