from http import client
from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('+++++++++++++++++++++++++++++++++++++++')
    print('++++++++++++++++ATM++++++++++++++++++++')
    print('++++++++++++Gaigher Bank+++++++++++++++')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')


    opcao: int = int(input())


    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe dados do cliente: ')

    nome: str= input('Nome: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('_______________')
    print(conta)
    sleep(2)
    menu()
    

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe numero da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Conta {numero} não encontada')
    else:
        print('Ainda não existem contas no sistema.')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor:float = float(input('Valor: '))

            conta.depositar(valor)
        else:
            print(f'A conta {numero} não foi encontrada')
    else:
        print('Ainda não existem contas no sistema')
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) >0:
        numero_o: int = int(input('Informe conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe conta destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe valor: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta {numero_d} não foi encontrada.')

        else:
            print(f'A conta {numero_o} não foi encontrada.')

    else:
        print('Não ha contas cadastradas')
        sleep(2)
        menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('__________')
            sleep(1)
    else:
        print('Não há contas no sistema')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
       for conta in contas:
           if conta.numero == numero:
               c = conta
    return c

if __name__ == '__main__':
    main()