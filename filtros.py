def preparar_dados_recuperacao(df, nota_corte=6.0):
    # Filtrar apenas os alunos com nota abaixo da média
    df_recuperacao = df[df['nota da fase'] < nota_corte].copy()
    # Organiza os nomes cadastrados
    df_recuperacao['nome'] = df_recuperacao['nome'].str.title()
    df_recuperacao = df_recuperacao.sort_values('nome')
    return df_recuperacao

def visualizar_bimestres_disponiveis(df_recuperacao):
    # Filtro por bimestre
    bimestres = df_recuperacao['fase de nota'].unique()
    print('Bimestres disponíveis:')
    for i, b in enumerate(bimestres, 1):
        print(f"[{i}] {b}")
    bimestre_escolhido = ''
    while True:
        try:
            escolha = int(input('Qual bimestre deseja ver? '))
            if escolha <= len(bimestres):
                bimestre_escolhido = bimestres[escolha - 1]
                break
            else:
                print(f"Opção inválida. Digite um número entre 1 e {len(bimestres)}.")
        except ValueError:
            'Digite apenas o numero correspondente'
    return bimestre_escolhido

def relatorio_pronto(bimestre_escolhido,df_recuperacao):
    # formatação do relatorio
    relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][
        ['matricula', 'nome', 'materia', 'fase de nota', 'nota da fase']]

    # Mostrar quantos alunos ficaram de recuperação
    print(f'\nTotal de alunos em recuperação: {len(relatorio["nome"].unique())}')
    print('\n--- Lista de Alunos em Recuperação ---')
    return relatorio

# Função Auxiliar
def definir_grau_alerta(total):
    if total <= 2:
        return "Básico"
    elif total <= 4:
        return "Intermediário"
    else:
        return "Crítico"

def relatorio_de_risco(relatorio):
    # Agrupa por aluno, junta as matérias em texto e conta o total delas
    df_risco = (relatorio.groupby('nome').agg(
        materias=('materia', lambda x: ', '.join(x.unique())),
        total_materias=('materia', 'count')).reset_index())
    df_risco['risco'] = df_risco['total_materias'].apply(definir_grau_alerta)
    return df_risco