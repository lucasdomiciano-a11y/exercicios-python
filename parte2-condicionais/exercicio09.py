## 9. Peça a média de um estudante e classifique: 6 ou mais é Aprovado; de 4 a 5,9 é Recuperação; abaixo de 4 é Reprovado.

media = float(input("Digite a média do estudante: "))
if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")