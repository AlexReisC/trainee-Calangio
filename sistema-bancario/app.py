contas = {}

while(True):
    escolha = int(input("Escolha uma opção:" + 
                    "\n1. Criar nova conta" +
                    "\n2. Depositar" +
                    "\n3. Retirar" +
                    "\n4. Verificar saldo" +
                    "\n5. Sair\n"))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do titular da conta: ")
            if nome not in contas:
                contas.setdefault(nome, 0.0)
                print(f"Conta criada para {nome}.\n")
            else:
                print("O titular ja tem conta\n")
        case 2:
            nome = input("Digite o nome do titular da conta: ")
            quantia = float(input("Digite a quantia a ser depositada: "))
            if quantia > 0:
                contas.setdefault(nome, quantia)
                print(f"Depósito de R${quantia} realizado com sucesso.\n")
            else:
                print("Digite um valor maior que 0\n")
        case 3:
            nome = input("Digite o nome do titular da conta: ")
            quantia = float(input("Digite a quantia a ser retirada: "))
            if quantia < contas.get(nome) and contas.get(nome) > 0:
                valorFinal = contas.get(nome) - quantia
                contas.setdefault(nome, valorFinal)
                print(f"Saque de R${quantia} realizado com sucesso.\n")
            else:
                print("Não é possível sacar este valor, verifique o saldo.\n")
        case 4:
            nome = input("Digite o nome do titular da conta: ")
            quantia = contas.get(nome)
            print(f"Saldo atual: R$ {quantia}\n")
        case 5:
            print("Obrigado por usar o sistema bancário.")
            break
