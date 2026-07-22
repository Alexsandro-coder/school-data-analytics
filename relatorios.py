import pandas as pd
from filtros import definir_grau_alerta, visualizar_bimestres
def relatorio_pronto(bimestre_escolhido,df_recuperacao):
    # formatação do relatorio
    relatorio = df_recuperacao[df_recuperacao['fase de nota'] == bimestre_escolhido][
        ['matricula', 'nome', 'materia', 'fase de nota', 'nota da fase']]

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

def relatorio(bimestre_escolhido,df_recuperacao, gerar_criticidade=False):
    df_relatorio = relatorio_pronto(bimestre_escolhido,df_recuperacao)
    if gerar_criticidade == True:
        df_criticidade = relatorio_de_criticidade(df_relatorio)
        return df_relatorio, df_criticidade
    return df_relatorio



def situacao (relatorio,df,bimestre_de_comparacao):
    alunos_recuperacao = len(relatorio['matricula'].unique())
    percentual_recuperacao = alunos_recuperacao/len(df['matricula'].unique())*100
    media_materias_por_aluno= len(relatorio['materia'])/alunos_recuperacao
    bimestre = bimestre_de_comparacao
    df_situacao = pd.DataFrame({
        'bimestre': [bimestre],
        'alunos_recuperacao': [alunos_recuperacao],
        'percentual_recuperacao': [percentual_recuperacao],
        'media_materias_por_aluno': [media_materias_por_aluno]
    })
    return df_situacao
