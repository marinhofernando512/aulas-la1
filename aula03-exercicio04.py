while (True): # Loop infinito
    valor: int = int(input("Digite um número: ") or 0)

    if not valor:
        break

    soma += valor

print(f"Soma: {soma}")


for i in range(2):
    for j in range(2):
        valor: int = i + j
        print(valor)
