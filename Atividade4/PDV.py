#Função para mostrar o menu e solicitar qual operação será utilizada
def menu():
    print("\n===============================");
    print("\t Caixa Eletrônico");
    print("===============================");
    print("1 - Consultar Saldo");
    print("2 - Depositar");
    print("3 - Sacar");
    print("4 - Sair");
    print("===============================");
    
    op = int(input("Escolha uma opção (1~4): "))
    return op

def consultar_saldo(saldo):
    print(f"\nSeu saldo é: R$ {saldo:.2f}")
    input("Press Enter to continue...")
    
def depositar(saldo):
    saldo += float(input("\nDiigite o valor a ser deposito: "))
    print("\nO valor foi depositado com sucesso!")
    return saldo

def sacar(saldo):
    
    valor_sacar = float(input("\nDigite o valor a ser sacado: "))

    if(valor_sacar <= saldo):
        print("\nSaque realizado com sucesso")
        return (saldo - valor_sacar)
    else:
        print("\n Valor indisponivel para saque")
        return saldo
    
saldo = 0

while True: 
    opcao = menu()
    
    match opcao:
        case 1:
            consultar_saldo(saldo)
        case 2:
            saldo = depositar(saldo)
        case 3:
            saldo = sacar(saldo)
        case 4:
            print("Finalizando apliação...\n\n")
            break
        case _:
            print("Valor invalido, por favor selecione uma opção válida (1~4).")
