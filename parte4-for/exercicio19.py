## 19. Peça um número e calcule seu fatorial. O fatorial de 5 é 5 × 4 × 3 × 2 × 1 = 120.

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")