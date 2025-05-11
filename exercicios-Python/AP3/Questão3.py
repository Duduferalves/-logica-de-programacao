pares = 0
impares = 0
soma_pares = 0
soma_impares = 0
print("Digite [0] para sair")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + numero
    else:
        impares = impares + 1
        soma_impares = soma_impares + numero
if pares > 0:
    media_pares = soma_pares / pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi digitado.")
if impares > 0:
    media_impares = soma_impares / impares
    print(f"Média dos números ímpares: {media_impares:.2f}")
else:
    print("Nenhum número ímpar foi digitado.")