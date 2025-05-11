ct = 0
soma = 0
maior_que_20 = 0
print("Digite [-1] para sair")
while True:
    valor = float(input("Digite um valor: "))
    if valor == -1:
        break
    ct = ct + 1
    soma = soma + valor
    if valor > 20:
        maior_que_20 = maior_que_20 + 1
if ct > 0:
    media = soma / ct
    print(f"Quantidade de valores digitados: {ct}")
    print(f"Soma dos valores digitados: {soma:.2f}")
    print(f"Média aritmética: {media:.2f}")
    print(f"Quantidade de valores maiores que 20: {maior_que_20}")
else:
    print("Nenhum valor válido foi digitado.")
