#Declaração de variáveis

comprimento = float(input("Digite o comprimento da sala: ")) # Leitura do comprimento
largura = float(input("Digite a largura da sala: ")) # Leitura da Largura

# Cálculos

area = comprimento * largura # Cálculo da área
perimetro = 2 * (comprimento + largura) # Cálculo do perímetro

# Exibição dos resultados

print(f"A área da sala é: {area}")
print(f"O perímetro da sala é: {perimetro}")

# Fim do programa