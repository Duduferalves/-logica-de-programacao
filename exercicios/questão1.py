def mostrar_mensagem_numero(msg, numero):
    print("Mensagem recebida:", msg)
    print("Número recebido:", numero)

if __name__ == '__main__':
    print("Este programa mostra uma mensagem e um número\n")

    mensagem = input("Digite uma mensagem: ")
    numero = int(input("Agora digite um número: "))

    print("\nChamando a função...\n")
    mostrar_mensagem_numero(mensagem, numero)

    print("\nPrograma finalizado")

