def calcula_idade(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade

if __name__ == '__main__':
    print("Este programa calcula a sua idade\n")

    nascimento = int(input("Digite seu ano de nascimento: "))
    idade = calcula_idade(nascimento)

    print("Você tem", idade, "anos")

    print("Cálculo concluído")
