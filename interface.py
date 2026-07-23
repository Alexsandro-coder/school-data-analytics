"""
Sistema de Análise e Diagnóstico de Desempenho Escolar
Projeto: school-data-analytics
Função principal: Processa dados de alunos, gera relatórios de recuperação,
criticidade, compara bimestres e cria visualizações.
"""
import pandas as pd
import filtros as fl
import relatorios as rl
import graficos as gf

def carregar_dados():
    df = pd.read_csv('alunos_fake_projeto_atualizado.csv')  # Visualização original dos dados
    pd.set_option('display.width', None)  # faz com que o csv apareça por completo
    print(df.head())
    return df

def iniciar():
    df = carregar_dados()

    # Chama a função de filtro definida para a recuperação
    df_recuperacao = fl.preparar_dados_recuperacao(df)
    try:
        print('Qual bimestre gostaria de gerar um relatorio?')
        # Chama a função de filtro definida para verificar os bimestres
        bimestre_escolhido = fl.visualizar_bimestres(df_recuperacao)
        while True:
            resp = str(input('Gostaria de um relatorio de criticidade do bimestre escolhido?'
                             '\n [1] SIM'
                             '\n [2] NÃO'
                             '\nDigite a opção:')).upper().strip()
            if resp in ['1', '2']:
                break
            print('Opção inválida!.')
        if resp == '1':
            gerar_criticidade = True
            # Guardamos os dois retornos da função!
            df_rel, df_crit = (rl.relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade))
            print('\n--- Relatório principal ---')
            print(f'\nTotal de alunos em recuperação: {len(df_rel["matricula"].unique())}')# Mostrar quantos alunos ficaram de recuperação
            print(df_rel)
            print('\n--- Relatório de criticidade ---')
            print(df_crit)
            while True:
                resp = str(input('Gostaria de comparar esse bimestre com outro ou gerar um grafico?'
                                 '\n [1] Comparar bimestres'
                                 '\n [2] Gerar um grafico'
                                 '\nDigite a opção: ')).upper().strip()
                if resp in ['1', '2']:
                    break
                print('Opção inválida!.')
            if resp == '1':
                gerar_criticidade = True
                bimestre_de_comparacao = fl.comparar_bimestres(bimestre_escolhido, df_recuperacao)
                # Buscamos o relatório do outro bimestre também com criticidade!
                df_rel_comp, df_crit_comp = rl.relatorio(bimestre_de_comparacao, df_recuperacao, gerar_criticidade)
                print('\n--- bimestre comparados ---')
                bimestre1 = rl.situacao(df_rel,df, bimestre_escolhido)
                bimestre2 = rl.situacao(df_rel_comp,df, bimestre_de_comparacao)
                df_comparacao = pd.concat([bimestre1, bimestre2], ignore_index=True)
                print(df_comparacao)
            elif resp == '2':
                gf.grafico_de_criticidade(df_crit)

        else:
            gerar_criticidade = False
            df_rel = rl.relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade)
            print('\n--- Relatório Principal ---')
            print(f'\nTotal de alunos em recuperação: {len(df_rel["matricula"].unique())}')# Mostrar quantos alunos ficaram de recuperação
            print(df_rel)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")