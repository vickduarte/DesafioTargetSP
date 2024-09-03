# Valores de faturamento por estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o valor total
total_faturamento = sum(faturamento_estado.values())

# Calcular e exibir o percentual de representação
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estado.items()}

for estado, percentual in percentuais.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")