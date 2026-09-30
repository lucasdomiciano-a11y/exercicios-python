## 25. Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.

numeros = [3, 7, 1, 9, 4]
numeros_invertidos = numeros[::-1]
print("Itens na ordem inversa:")
for numero in numeros_invertidos:
    print(numero)