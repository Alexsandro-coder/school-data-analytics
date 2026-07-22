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

def relatorio(bimestre_escolhido,df_recuperacao, gerar_criticidade=False):
    df_relatorio = rl.relatorio_pronto(bimestre_escolhido,df_recuperacao)
    if gerar_criticidade == True:
        df_criticidade = rl.relatorio_de_criticidade(df_relatorio)
        return df_relatorio, df_criticidade
    return df_relatorio

df = pd.read_csv('alunos_fake_projeto.csv')
# Visualização original dos dados
print(df.head())

# Chama a função de filtro definida para a recuperação
df_recuperacao = fl.preparar_dados_recuperacao(df)
try:
    print('Qual bimestre gostaria de gerar um relatorio?')
    # Chama a função de filtro definida para verificar os bimestres
    bimestre_escolhido = fl.visualizar_bimestres(df_recuperacao)
    while True:
        resp = str(input('Gostaria de um relatorio de criticidade do bimestre escolhido? [S/N]:')).upper().strip()
        if resp in ['S', 'N']:
            break
        print('Opção inválida! Digite S ou N.')
    if resp == 'S':
        gerar_criticidade = True
        # Guardamos os dois retornos da função!
        df_rel, df_crit = (relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade))
        print('\n--- Relatório principal ---')
        print(f'\nTotal de alunos em recuperação: {len(df_rel["nome"].unique())}')# Mostrar quantos alunos ficaram de recuperação
        print(df_rel)
        print('\n--- Relatório de criticidade ---')
        print(df_crit)
        while True:
            resp = str(input('Gostaria de comparar o relatorio de criticidade com outro bimestre ou gerar um grafico?'
                             '\n [1] Comparar bimestres'
                             '\n [2] Gerar um grafico'
                             'Digite a opção: ')).upper().strip()
            if resp in ['1', '2']:
                break
            print('Opção inválida!.')
        if resp == '1':
            gerar_criticidade = True
            bimestre_de_comparacao = fl.comparar_bimestres(bimestre_escolhido, df_recuperacao)
            # Buscamos o relatório do outro bimestre também com criticidade!
            df_rel_comp, df_crit_comp = relatorio(bimestre_de_comparacao, df_recuperacao, gerar_criticidade)
            print('\n--- Criticidade bimestre comparado ---')
            print(df_crit_comp)
        elif resp == '2':
            gf.grafico_de_criticidade(df_crit)

    else:
        gerar_criticidade = False
        df_rel = relatorio(bimestre_escolhido, df_recuperacao, gerar_criticidade)
        print('\n--- Relatório Principal ---')
        print(df_rel)
except Exception as e:
    print(f"Ocorreu um erro: {e}")