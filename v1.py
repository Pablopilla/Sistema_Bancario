saldo = 50.0  # Saldo teste
opcao = -1
usuario = 'Pablo'
contador_deposito = 0
contador_saque = 0
limite= 500
print('===== Ph-Bank ===== \n') 
print(f'{usuario}, seja muito bem-vindo ao Ph-Bank \n')
print('===== Ph-Bank ===== ')

while opcao != 0:
    try:
        opcao = int(input('\n[1] Sacar \n[2] Depositar \n[3] Extrato \n[0] Sair\nSelecione uma opção:' ))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        continue  

    if opcao == 1:        
        if contador_saque >= 3:
            print ('Limite de saques diários atingido!')
        else:
            saque = float(input('Digite valor de saque :R$ '))
            if saldo < saque:
                print ('Falha ao sacar por falta de saldo. ')
            elif saque > limite:
                print ('Erro ! Seu limite por saque é de R$500,00')
            else:
                contador_saque += 1
                saldo = saldo - saque
                print('Sacando...')

    elif opcao == 2:
        while True:
            try:
                deposito = float(input('Qual valor deseja depositar? '))
                if deposito > 0:
                    print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
                    contador_deposito += 1 
                    saldo = saldo + deposito
                    break  # Sai do loop de depósito
                else:
                    print("O valor precisa ser maior que zero!")
            except ValueError:
                print('Não foi digitado um número válido, tente novamente!')

    elif opcao == 3:
        print('\nExibindo extrato...')
        print(f'Foram feitos {contador_saque} Saques')
        print(f'Foram feitos {contador_deposito} depositos ')
        print(f'Seu saldo atual é de: R$ {saldo:.2f}')

    elif opcao == 0:
        print('\nObrigado por usar nosso Banco!')
        print('Teste') 
        print('Teste')    
        print('Teste')    
        print('Teste')    
        print('Teste')       
        
    else:
        print('\nOpção inválida! Tente novamente.')