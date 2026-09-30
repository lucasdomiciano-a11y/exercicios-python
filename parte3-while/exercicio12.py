## 12. Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    soma += numero