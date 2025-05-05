preço = float(input("digite o valor do produto: R$ ")) #Leia preço do produto
precof = float(input("digite o valor do produto com desconto: R$ ")) #Leia preço do produto com desconto

#Cálculo

desc = (preço - precof)/preço * 100

#Exibição de resultados

print(f"a porcentagem do desconto foi: {desc:.2f}%")

#Fim do programa