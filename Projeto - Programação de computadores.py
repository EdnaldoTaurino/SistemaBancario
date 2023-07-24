# Controle bancário
from time import sleep

print('-' * 40, 'CONTROLE BANCÁRIO', '-' * 40)

codigos = []
saldo = []


for i in range(1, 11):
    while True:
        codigo = int(input(f'Digite o {i}º código da conta: '))
        if codigo in codigos:
            print(f'Já existe uma conta com esse codigo {codigo} cadastrada tente novamente.')
            sleep(1)
        else:
            codigos.append(codigo)
            break
    valor = float(input(f'Conta codigo {codigo} digite o saldo: R$ '))
    saldo.append(valor)

while True:
    print('-' * 40, 'Controle bancário MENU', '-' * 40)
    print('''
    1. Realizar Depósito
    2. Realizar Saque
    3. Consultar o ativo bancário, ou seja, o somatório dos saldos de todos os clientes
    4. Finalizar Programa 
    ''')
    print('-' * 40, 'Controle bancário MENU', '-' * 40)
    opcao = input('Digite uma opção: ')


    if opcao == '1':
        inputCodigo = int(input('Digite o codigo da conta: '))
        if inputCodigo in codigos:
            indice = codigos.index(inputCodigo)
            depositar = float(input(f'Conta {inputCodigo} Digite o valor a ser depositado: '))
            saldo[indice] += depositar
            sleep(1)
            print('Realizando seu depósito, aguarde um instante...')
            sleep(1)
            print('1', end='', flush=True)  # end cancela a quebra de linha
            print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5)
            print('.', end='')
            sleep(1)
            print('2', end='', flush=True)  # flush = True evita o buffer e mostra os prints imediatamente
            print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5)
            print('.', end='')
            sleep(1)
            print('3', end='', flush=True)
            print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5), print('.', end=''), sleep(0.5)
            print('.',)
            sleep(1)
            print('Depósito realizado com SUCESSO!!!')
            sleep(2)
        else:
            print('Conta não encontrada!!! Tente novamente')


    elif opcao == '2':
        inputCodigo = int(input('Digite o codigo da conta: '))
        if inputCodigo in codigos:
            indice = codigos.index(inputCodigo)
            saldoConta = saldo[indice]
            saque = float(input('Digite o valor para saque: R$ '))
            if saque <= saldoConta:
                saldo[indice] -= saque
                sleep(1)
                print('Contando notas...')
                sleep(1.5)
                print('Separando dinheiro...')
                sleep(1.5)
                print(f'Saque realizado com Sucesso!!! novo saldo da conta codigo {inputCodigo} é de  R$ '
                      f'{saldo[indice]}')
                sleep(2)
            else:
                print(f'Valor não permitido a conta {inputCodigo} possui o valor de R$ {saldoConta} '
                      f'que é menor que o saque desejado de {saque}')
        else:
            print('Conta nao encontrada, tente novamente')


    elif opcao == '3':
        somaTotal = sum(saldo)
        print(f'Total de saldo dos clientes foi de {somaTotal}')

    elif opcao == '4':
        print('Programa finalizado!')
        break

    else:
        input('Digite uma opção válida, tente novamente.')
