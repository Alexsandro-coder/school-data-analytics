import pandas as pd
import filtros as fl
df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Chama a função de filtro definida para a recuperação
df_recuperacao = fl.preparar_dados_recuperacao(df)

# Chama a função de filtro definida para verificar os bimestres
bimestre_escolhido = fl.visualizar_bimestres_disponiveis(df_recuperacao)

# formatação do relatorio
relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][['matricula', 'nome', 'materia','fase de nota', 'nota da fase']]

# Mostrar quantos alunos ficaram de recuperação
print(f'\nTotal de alunos em recuperação: {len(relatorio["nome"].unique())}')
print('\n--- Lista de Alunos em Recuperação ---')
print(relatorio)