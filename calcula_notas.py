# Programa que calcula a média ponderada de três avaliações

# Entrada de dados
print()
print("Cálculo da média ponderada de três avaliações")
print()
nota1 = float(input("Digite a nota da 1ª avaliação (peso 2): "))
print()
nota2 = float(input("Digite a nota da 2ª avaliação (peso 3): "))
print()
nota3 = float(input("Digite a nota da 3ª avaliação (peso 5): "))
print()

# Processamento
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

# Saída de dados
print(f"A média ponderada das três avaliações é: {media:.2f}")
print()