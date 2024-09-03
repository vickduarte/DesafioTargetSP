import json

# Dados de faturamento diário
faturamento_json = '''
{
    "dias": [
        {"dia": "2024-01-01", "faturamento": 5000},
        {"dia": "2024-01-02", "faturamento": 7000},
        {"dia": "2024-01-03", "faturamento": 8000},
        {"dia": "2024-01-04", "faturamento": 6000},
        {"dia": "2024-01-05", "faturamento": 6500}
    ]
}
'''

# Carregar dados do JSON
dados = json.loads(faturamento_json)
faturamentos = [dia["faturamento"] for dia in dados["dias"] if "faturamento" in dia]

# Calcular o menor e maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcular a média mensal ignorando dias sem faturamento
total_faturamento = sum(faturamentos)
num_dias_com_faturamento = len(faturamentos)
media_mensal = total_faturamento / num_dias_com_faturamento

# Contar dias com faturamento superior à média mensal
dias_acima_media = len([f for f in faturamentos if f > media_mensal])

# Resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")