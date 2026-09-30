## 15. Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos foram digitados.

contador_positivos = 0
while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero > 0:
        contador_positivos += 1
print(f"Quantidade de números positivos digitados: {contador_positivos}")