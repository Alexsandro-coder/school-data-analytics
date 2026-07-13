def relatorio_pronto(bimestre_escolhido,df_recuperacao):
    # formatação do relatorio
    relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][
        ['matricula', 'nome', 'materia', 'fase de nota', 'nota da fase']]

    # Mostrar quantos alunos ficaram de recuperação
    print(f'\nTotal de alunos em recuperação: {len(relatorio["nome"].unique())}')
    print('\n--- Lista de Alunos em Recuperação ---')
    return relatorio