## 24. Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.

numeros = [5, 12, 8, 20, 3, 15]
contador_maiores_que_10 = 0

for numero in numeros:
    if numero > 10:
        contador_maiores_que_10 += 1

print(f"Quantidade de itens maiores que 10: {contador_maiores_que_10}")