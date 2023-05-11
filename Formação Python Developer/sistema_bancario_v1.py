# Programa simulacro de um sistema bancário Versão 01

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("DEPÓSITO")

        print( f"Saldo Atual: {saldo:.2f}")

        deposito = float(input("Digite o valor do depósito: "))
        
        if deposito > 0:
            extrato += f"Depósito R${deposito:.2f}\n"
            saldo = saldo + deposito
        else:
            print("Valor do depósito inválido!")
            
        print( f"Saldo Atualizado: R${saldo:.2f}")
    
    elif opcao == "2":
        print("SAQUE")
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingido!")
        
        else:
            saque = float(input("Digite o valor do saque: "))
            if saque < saldo and saque <= 500:
                numero_saques += 1
                saldo = saldo - saque
                extrato += f"Saque R${saque:.2f}\n"
                print( f"Saldo Atualizado: R${saldo:.2f}")
            else:
                print("Saldo insuficiente na conta ou limite de saque de R$500,00 extrapolado!")
    
    elif opcao == "3":
        print("EXTRATO")
        print( f"Número de saques realizados: {numero_saques}")
        print(extrato)
        print( f"Saldo Atual: R${saldo:,.2f}")
    

    elif opcao == "4":
        print("SAIR")
        break
    
    else:
        print("Digite uma opção válida!")