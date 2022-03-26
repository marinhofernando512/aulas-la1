#1) Leia um vetor de 10 posições. Calcule e escreva quantos valores pares ele possui

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
conta_pares = 0
for numero in numeros:   
    if numero % 2 == 0:
        conta_pares += 1
    
print(conta_pares)







