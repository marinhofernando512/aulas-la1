# Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 4 alunos.
#a) a média de cada aluno será fornecida pelo usuário.
#b) a tabela de conceitos se encontra abaixo:

#Nota	Conceito
#de 0.0 à 4.9	D
#de 5.0 à 6.9	C
#de 7.0 à 8.9	B
#de 9.0 à 10.0	A



for i in range(4):
    media = float(input(f"Digite a média do aluno {i + 1}:"))
    conceito = ""
    if media < 0:
        conceito = "Media inválida"
    elif media <= 4.0:
        conceito = "D"
    elif media <= 6.9:
        conceito = "C"
    elif media <= 8.9:
        conceito = "B"
    else:
        conceito = "A"

        print(conceito)




