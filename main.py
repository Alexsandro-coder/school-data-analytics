import pandas as pd
df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Definir a nota de corte para recuperação
nota_corte = 6.0

# Filtrar apenas os alunos com nota abaixo da média
df_recuperacao = df[df['nota da fase'] < nota_corte]

# Organiza os nomes cadastrados
df_recuperacao['nome'] = df_recuperacao['nome'].str.title()
df_recuperacao = df_recuperacao.sort_values('nome')

# Filtro por bimestre
bimestre1 = df_recuperacao['fase de nota'] == '1 bimestre'
bimestre2 = df_recuperacao['fase de nota'] == '2 bimestre'

# Mostrar quantos alunos ficaram de recuperação
print(f'\nTotal de alunos em recuperação: {len(df_recuperacao['nome'].unique())}')
print('\n--- Lista de Alunos em Recuperação ---')
print(df_recuperacao[['matricula', 'nome', 'materia','fase de nota', 'nota da fase']])