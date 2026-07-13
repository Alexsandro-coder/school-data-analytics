import pandas as pd
from filtros import definir_grau_alerta
def relatorio_pronto(bimestre_escolhido,df_recuperacao):
    # formatação do relatorio
    relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][
        ['matricula', 'nome', 'materia', 'fase de nota', 'nota da fase']]

    # Mostrar quantos alunos ficaram de recuperação
    print(f'\nTotal de alunos em recuperação: {len(relatorio["nome"].unique())}')
    print('\n--- Lista de Alunos em Recuperação ---')
    return relatorio

def relatorio_de_criticidade(relatorio):
    # Agrupa por matrícula e nome, processa as matérias e conta o total
    df_criticidade = relatorio.groupby(['matricula', 'nome']).agg(
        materias=('materia', lambda x: ', '.join(x.unique())),
        total_materias=('materia', 'count')
    ).reset_index()
    # Cria um grau de riso com base na quantidade de matérias de recuperação
    df_criticidade['risco'] = df_criticidade['total_materias'].apply(definir_grau_alerta)

    colunas_desejadas = ['matricula', 'nome', 'materias', 'total_materias', 'risco']

    return df_criticidade[colunas_desejadas]