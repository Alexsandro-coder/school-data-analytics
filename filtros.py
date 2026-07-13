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
            # Proteção contra o usuário
            if 1 <= escolha <= len(bimestres):
                bimestre_escolhido = bimestres[escolha - 1]
                break
            else:
                print(f"Opção inválida. Digite um número entre 1 e {len(bimestres)}.")
        except ValueError:
            print('Digite apenas o numero correspondente')
    return bimestre_escolhido

def definir_grau_alerta(total):
    if total <= 2:
        return 'LEVE'
    elif total <= 4:
        return 'ATENÇÃO'
    else:
        return 'CRÍTICO'

def comparar_bimestres(bimestre_escolhido, df_recuperacao):
    print(f'O {bimestre_escolhido} foi escolhido')

    bimestres = df_recuperacao['fase de nota'].unique()

    bimestre_disponiveis = [b for b in bimestres if b != bimestre_escolhido]

    print('Bimestres disponíveis:')
    for i, b in enumerate(bimestre_disponiveis, 1):
        if b == bimestre_escolhido:
            continue
        print(f"[{i}] {b}")

    bimestre_escolhido2 = ''
    while True:
        try:
            escolha = int(input('Qual bimestre deseja comparar? '))
            # Proteção contra o usuário
            if 1 <= escolha <= len(bimestre_disponiveis):
                bimestre_escolhido2 = bimestre_disponiveis[escolha - 1]
                break
            else:
                print(f"Opção inválida. Digite um número entre 1 e {len(bimestre_disponiveis)}.")
        except ValueError:
            print('Digite apenas o numero correspondente')
    return bimestre_escolhido2