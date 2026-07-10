import pandas as pd
pd.set_option('display.max_columns', None)
import filtros as fl
df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Chama a função de filtro definida para a recuperação
df_recuperacao = fl.preparar_dados_recuperacao(df)

# Chama a função de filtro definida para verificar os bimestres
bimestre_escolhido = fl.visualizar_bimestres_disponiveis(df_recuperacao)

# Chama a função de filtro definida para retornar um relatorio pronto
relatorio = fl.relatorio_pronto(bimestre_escolhido,df_recuperacao)

print(relatorio)
print(fl.relatorio_de_risco(relatorio))
