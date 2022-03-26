vetor = ["a", 2, True, 2.1]
print(len(vetor))

# tamanho do vetor - len

print(vetor[3])
print(vetor[0])
print(vetor[1:2])
print(vetor[::-1]) # iltimo elemento do vetor
print(vetor[-2])

#Adicionar elementos
#outroVetor[0] = input ("Digite um valor")
#print(outroVetor)

#outroVetor.append(5) # add final 
#print(outoVetor)

#outroVetor.insert(1, 2) # add no inicio
#print(outroVetor)

#outroVetor.insert(0, 10)

outroVetor = [1, 2, 3]
outroVetor.insert(1, 10)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:   # para saber o indice usar =  for indice, numero in enumerate(numeros):
    print(numero)
    if numero % 2 == 0:
        print(f" o número {numero} é par")
    print(numero)


#for i in range(0, len(numeros)):
 #   print(numeros[i])

#pegar invetido  for numero in numeros[::-1]: 

for numero in numeros[::-1]:
    print(numero)


    frase = "Ola Mundo!"
    palavras = frase.split(" ")  # passar separador, exemplo virgula.. 
    for i, palavra in enumerate(palavras):
        palavras[i] = palavra[0].upper() + palavra[1::]
    print(palavra)


# join(palavras)  vai juntar a instring 















