import pandas as pd
df = pd.read_csv('alunos_fake_projeto.csv')
# 1. Visualização original dos dados
print(df.head())

# 2. Definir a nota de corte para recuperação
nota_corte = 6.0

# 3. Filtrar apenas os alunos com nota abaixo da média
df_recuperacao = df[df["nota da fase"] < nota_corte]

# 4. Mostrar quantos alunos ficaram de recuperação
print(f"\nTotal de alunos em recuperação: {len(df_recuperacao)}")
print("\n--- Lista de Alunos em Recuperação ---")
print(df_recuperacao[["matricula", "nome", "materia", "nota da fase"]])