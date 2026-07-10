import pandas as pd
import filtros as fl
df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Chama a função de filtro definida para a recuperação
df_recuperacao = fl.preparar_dados_recuperacao(df)

# Filtro por bimestre
bimestres = df_recuperacao['fase de nota'].unique()
print('Bimestres disponíveis:')
for i, b in enumerate(bimestres, 1):
    print(f"[{i}] {b}")

escolha = int(input('Qual bimestre deseja ver? '))
bimestre_escolhido = bimestres[escolha - 1]

# formatação do relatorio
relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][['matricula', 'nome', 'materia','fase de nota', 'nota da fase']]

# Mostrar quantos alunos ficaram de recuperação
print(f'\nTotal de alunos em recuperação: {len(relatorio["nome"].unique())}')
print('\n--- Lista de Alunos em Recuperação ---')
print(relatorio)