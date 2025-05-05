preço = float(input("digite o preço do produto: R$ ")) #Leia preço do produto

#Cálcula 5% de desconto
desconto = preço * 0.05

#Aplica o desconto
preco_com_desconto = preço - desconto

#Exibição de resultados

print(f"O preço com 5% de desconto é: R$ {preco_com_desconto:.2f}")

#Fim do programa