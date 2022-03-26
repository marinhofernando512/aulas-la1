#  Escreva um programa que leia 5 numeros e os armazene em um vetor. Mostre o vetor, o 
# maior elemento e a posição que ele se encontra.


numeros = []

maior_valor = None
posicao = 0 
for i in range(5):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

    if i == 0:
        maior_valor = numero
    elif numero > maior_valor:
        maior_valor = numero
        posicao = i

print(numeros)
print(maior_valor)
print(posicao)




