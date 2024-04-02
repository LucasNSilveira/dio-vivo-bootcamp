import textwrap

def menu():
   menu =  """
    ===============MENU===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar
    [q] Sair

    => """
   return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato,/):
    if valor > 0 :
        saldo =+ valor
        extrato += f"Depósito: R${valor:.2f}"
        print("\n Depósito feito com suceso!")
    else:
        print("\n Depósito não foi realizado. A operação falhou!")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, num_saque, limite_saque): #Forma nomeada (keywords)
    excedido = valor > saldo
    maior_limite = valor > limite
    saques_max = num_saque > limite_saque
    if excedido:
        print("A operação falhou! Você não tem saldo suficiente!\nTente novamente.")
        
    elif maior_limite:
        print('Operação falhou! Valor de saque maior que o limite.')
    
    elif saques_max:
        print('Operação falhou! Número máximo de saques atingido.')
    
    elif valor > 0:
        saldo = saldo - valor
        extrato += f'Saque de: R$ {valor:.2f}\n'
        num_saque += 1
    
    else:
        print('Operação falhou! O valor informado é válido')
        
    return saldo, extrato

def extrato(saldo, /,*, extrato):
    print("\n===========EXTRATO===========")
    print("Não foram realizadas operações!" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=============================")
    return

def cadastro(usuarios):
    cpf = str(input('Informe o CPF: '))
    usuario = checar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nummero, bairro - cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data-nasc": data_nasc, "endereco": endereco})

def checar_usuario(cpf, usuarios):
    usuario_checado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_checado[0] if usuario_checado else None

def criar_conta(agencia, usuarios, numero_conta):
    cpf = input("Informe o CPF do usuário: ")
    usuario = checar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return({"agencia": agencia, "usuario": usuario, "numero_conta": numero_conta})
    
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    numero_saque = 0
    extrato = ""
    usuarios = []    
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            
            valor = float(input("Informe o valor do deposito: R$ "))
            
            saldo, extrato = deposito(saldo, valor, extrato)


        elif opcao == "s":
            valor = float(input('Informe o valor do saque: '))
            
            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                num_saque=numero_saque,
                limite_saque=LIMITE_SAQUE
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)
        
        elif opcao =="c":
            cadastro(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, usuarios, numero_conta)

            if conta:
                contas.append(conta)
                

        elif opcao == "q":
            break
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

        
main()