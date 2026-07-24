"""
Sistema de Análise e Diagnóstico de Desempenho Escolar
Projeto: school-data-analytics
Função principal: Processa dados de alunos, gera relatórios de recuperação,
criticidade, compara bimestres e cria visualizações.
"""
import pandas as pd
from src import filtros as fl, graficos as gf, relatorios as rl
from dados import config as con

def carregar_dados():
    df = pd.read_csv(con.ARQUIVO_DADOS)  # Visualização original dos dados
    pd.set_option('display.width', None)  # faz com que o csv apareça por completo
    print(df.head())
    return df

def perguntar_acao(pergunta = '',opcao1 = 'SIM', opcao2 = 'NAO'):
    while True:
        resp = str(input(f'{pergunta}: '
                         f'\n [1] {opcao1}'
                         f'\n [2] {opcao2}'
                         '\nDigite a opção: ')).strip()
        if resp in ['1', '2']:
            break
        print('Opção inválida!.')
    return resp

def exibir_relatorio_principal(df_rel, titulo="Relatório principal"):
    print(f'\n--- {titulo} ---')
    print(f'\nTotal de alunos em recuperação: {len(df_rel["matricula"].unique())}')  # Mostrar quantos alunos ficaram de recuperação
    print(df_rel)

def processar_comparacao(bimestre_escolhido, df_recuperacao, df_rel, df):
    gerar_criticidade = True
    bimestre_de_comparacao = fl.comparar_bimestres(bimestre_escolhido, df_recuperacao)
    # Buscamos o relatório do outro bimestre também com criticidade!
    df_rel_comp, df_crit_comp = rl.relatorio(bimestre_de_comparacao, df_recuperacao, gerar_criticidade)
    print('\n--- bimestre comparados ---')
    bimestre1 = rl.situacao(df_rel, df, bimestre_escolhido)
    bimestre2 = rl.situacao(df_rel_comp, df, bimestre_de_comparacao)
    df_comparacao = pd.concat([bimestre1, bimestre2], ignore_index=True)
    print(df_comparacao)

def iniciar():
    df = carregar_dados()
    # Chama a função de filtro definida para a recuperação
    df_recuperacao = fl.preparar_dados_recuperacao(df)
    try:
        print('Qual bimestre gostaria de gerar um relatorio?')
        # Chama a função de filtro definida para verificar os bimestres
        bimestre_escolhido = fl.visualizar_bimestres(df_recuperacao)
        resp = perguntar_acao('Gostaria de um relatorio de criticidade do bimestre escolhido?')
        if resp == '1':
            gerar_criticidade = True
            # Guardamos os dois retornos da função!
            df_rel, df_crit = (rl.relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade))
            exibir_relatorio_principal(df_rel)
            print('\n--- Relatório de criticidade ---')
            print(df_crit)
            resp = perguntar_acao('Gostaria de comparar esse bimestre com outro ou gerar um grafico?'
                                  ,'COMPARAR'
                                  ,'GERAR GRAFICO')
            if resp == '1':
                processar_comparacao(bimestre_escolhido, df_recuperacao, df_rel, df)
            elif resp == '2':
                gf.grafico_de_criticidade(df_crit)

        else:
            gerar_criticidade = False
            df_rel = rl.relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade)
            exibir_relatorio_principal(df_rel)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")