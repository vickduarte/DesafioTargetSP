def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# String a ser invertida
string = input("Digite a string para inverter: ")

# Inverter a string e exibir o resultado
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")