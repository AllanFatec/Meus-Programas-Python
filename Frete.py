distância = float(input("Digite a distância da entrega (km):"))
peso = float(input("Digite o peso do produto (kg): "))

if distância < 100:
    frete = 10
elif distância <= 500:
    frete = 20
else:
    frete = 50

if peso > 10:
    frete+=15 # Adiciona taxa por peso extra

print(f"O valor do frete é R${frete:.2f}")