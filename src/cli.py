from src.enlace import remetente, destinatario

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Enviar uma mensagem")
        print("2 - Processar um frame recebido")
        print("3 - Sair")
        escolha = input("Digite sua escolha: ")
        
        if escolha == "1":
            mensagem = input("Digite a mensagem em bits para envio: ")
            frame = remetente(mensagem)
            print("Frame gerado:", frame)
        elif escolha == "2":
            frame = input("Digite o frame recebido: ")
            resultado = destinatario(frame)
            print(resultado)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
