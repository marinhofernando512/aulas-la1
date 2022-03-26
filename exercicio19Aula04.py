# exercicio 19


while True: 
    codigo = int(input("Digite o código do aluno"))

    if not codigo:
        break

    nota01 = float(input("Digite a nota1:"))
    nota02 = float(input("Digite a nota2:"))
    nota03 = float(input("Digite a nota3:"))

    media = (nota01 + nota02 + nota03) / 3

    print(f"A media do aluno com o código {codigo} é: {media :.2f}")

print("Programa finalizado...")











