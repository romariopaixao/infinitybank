from operacoes.consulta import *
from operacoes.saque import *
from operacoes.transferencia import *
from operacoes.deposito import *
from banco import *
from time import sleep

def menu():
    while True:
        print('''
        ---- BEM VINDO ----
        1 - Adicionar conta
        2 - Editar nome
        3 - Consultar conta
        4 - Excluir conta
        5 - Listar todos
        6 - Realizar saque
        7 - Realizar deposito
        8 - Realizar transferência
        9 - Consultar saldo
        10 - Sair
        ''')
        sleep(2)
        opcao = int(input('Digite um numero da opção desejada: '))

        if opcao == 1:
            sleep(1)
            nome = input('Digite o nome do cleinte: ')
            saldo = float(input('Digite o saldo: '))
            adicionarConta(nome, saldo)
            sleep(1)
        elif opcao == 2:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            nome = input('Digite o novo nome do cliente: ')
            editarNome(conta, nome)
            sleep(1)
        elif opcao == 3:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            buscarCliente(conta)
            sleep(1)
        elif opcao == 4:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            removerConta(conta)
            sleep(1)
        elif opcao == 5:
            sleep(1)
            listarTodos()
            sleep(1)
        elif opcao == 6:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            valor = float(input('Digite o valor de saque: '))
            sacar(conta, valor)
            sleep(1)
        elif opcao == 7:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            valor = float(input('Digite o valor de saque: '))
            depositar(conta, valor)
            sleep(1)
        elif opcao == 8:
            sleep(1)
            contaOrigem = int(input('Digite o numero da conta de origem: '))
            contaDestino = int(input('Digite o numero da conta de destino: '))
            valor = float(input('Digite o valor que deseja transferir: '))
            transferir(contaOrigem, contaDestino, valor)
            sleep(1)
        elif opcao == 9:
            sleep(1)
            conta = int(input('Digite o numero da conta: '))
            consultarSaldo(conta)
            sleep(1)
        elif opcao == 10:
            sleep(1)
            print('Voce saiu do programa! Ate mais.')
            break
        else:
            sleep(1)
            print('Comando inválido! Tente novamente')
            sleep(1)

menu()