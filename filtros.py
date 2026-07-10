def preparar_dados_recuperacao(df, nota_corte=6.0):
    # Filtrar apenas os alunos com nota abaixo da média
    df_recuperacao = df[df['nota da fase'] < nota_corte].copy()
    # Organiza os nomes cadastrados
    df_recuperacao['nome'] = df_recuperacao['nome'].str.title()
    df_recuperacao = df_recuperacao.sort_values('nome')
    return df_recuperacao