import matplotlib.pyplot as plt
def grafico_de_criticidade(df_criticidade):
    # grafico pro pycharm

    # Contamos quantos alunos caíram em cada nível de risco
    contagem_risco = df_criticidade['risco'].value_counts()

    # janela do gráfico de barras com cores
    plt.figure(figsize=(8, 5))
    contagem_risco.plot(
        kind='bar',
        color=['green', 'yellow', 'red'],
        edgecolor='black'
    )

    # Customização estética
    plt.title('Quantidade de Alunos por Grau de Risco (Recuperação)', fontsize=14)
    plt.xlabel('Grau de Alerta / Risco', fontsize=12)
    plt.ylabel('Total de Alunos', fontsize=12)
    plt.xticks(rotation=0)  # Deixa os nomes na horizontal
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Linhas de grade ao fundo

    # Para o grafico aparecer
    plt.tight_layout()
    plt.show()