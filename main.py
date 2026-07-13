import pandas as pd
import filtros as fl
import relatorios as rl
df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Chama a função de filtro definida para a recuperação
df_recuperacao = fl.preparar_dados_recuperacao(df)

# Chama a função de filtro definida para verificar os bimestres
bimestre_escolhido = fl.visualizar_bimestres_disponiveis(df_recuperacao)

# Chama a função de filtro definida para retornar um relatorio pronto
relatorio = rl.relatorio_pronto(bimestre_escolhido,df_recuperacao)

df_criticidade = rl.relatorio_de_criticidade(relatorio)

print(relatorio)
print(df_criticidade)