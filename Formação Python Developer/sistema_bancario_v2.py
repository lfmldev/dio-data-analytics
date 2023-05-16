# Programa simulacro de um sistema bancário Versão 01

# Definir uma função para o menu:
def menu():

    menu = """
    Escolha a operação desejada

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Criar conta
    [6] Listar contas
    [7] Sair

    => """
    print(menu)
    escolha = input()
    return escolha

# Função com parâmetros por posição , a contrabarra define que todos os parâmetros
# a esquerda são posicionais, ele não aceita por exemplo "saldo="

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        extrato += f"Depósito R${valor:.2f}\n"
        saldo = saldo + valor
    else:
        print("Valor do depósito inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # Aqui os argumentos devem ser passados por chave, nomeada, por exemplo: "saque="
    if numero_saques >= limite_saques:
        print("Limite de saques atingido!")
            
    else:
        if valor < saldo and valor <= 500:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"

        elif valor > 500:
            print("limite de saque de R$500,00 extrapolado!")

        else:
            print("Saldo insuficiente na conta")
    
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("========== EXTRATO ==========")
    print(extrato)
    print()
    print( f"Saldo Atual: R${saldo:,.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Já existe um usuário com este CPF!")
        return
  
    nome = input("Informe o nome completo: ")
    data_nascimento= input("informe a data de nascimento(dd-mm=aaaa): ")
    endereco = input(" Digite o seu endereço completo : (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print( "Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print( "Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
    print("=" * 100)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "1":
            
            valor = float(input("Informe o valor do depósito: ")) # Recebe o valor que será usado na função

            saldo, extrato = depositar(saldo, valor, extrato) # A função terá dois retornos         
                               
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato = extrato, 
                limite = limite,
                numero_saques= numero_saques, 
                limite_saques = LIMITE_SAQUES,
            )           
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato= extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta) 

        elif opcao == "6":
            listar_contas(contas)       

        elif opcao == "7":
            print("SAIR")
            break
        
        else:
            print("Digite uma opção válida!")

main()