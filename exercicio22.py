# Escreva um algoritmo que peça o salário de uma pessoa e imprima o salário líquido, segunda a tabela a seguir:

#Menor ou igual a R$ 600.00	                        Isento
#Maior que R$ 600.00 e menor ou igual a R$ 1200.00	20%
#Maior que R$ 1200.00 e menor ou igual a R$ 2000.00	25%
#Maior que R$ 2000.00	                            30%

# INPUT - PROCESSAMENTO - OUTPUT

salario = float(input("Digite o seu salário")) # str

salario_liquido = 0
if salario <= 0:
    salario_liquido = "Salário inválido"
elif salario <= 600:
    salario_liquido = salario
elif salario <= 1200:
    salario_liquido = salario * .8
elif salario <= 2000:
    salario_liquido = salario * .75
else:
    salario_liquido = salario * .70

print(salario_liquido)

