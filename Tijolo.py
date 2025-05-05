CT = float(input("Digite o comprimento do tijolo: "))
LT = float(input("Digite a largura do tijolo: "))
CP = float(input("Digite a comprimento da parede: "))
LP = float(input("Digite a largura da sala: "))

QTD = ((CP*LP) / (CT*LT))

print(f"A quantidade de tijolos necessários para construir uma determinada parede é {QTD:.2f}")