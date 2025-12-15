print("vamos adivinhar o número que você está pensando!")

try:
    numero = int(input("Digite um número entre 1 e 10: "))
    if numero <= 10:
        print(f'o numero que você pensou foi {numero}, correto?')
except ValueError:
    print("Digite um número válido entre 1 e 10.")
