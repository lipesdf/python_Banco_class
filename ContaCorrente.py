from datetime import datetime
import pytz
from random import randint


class ContaCorrente():

    """
    Cria um objeto ContaConrrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome cliente
        cpf (str): CPF do cliente
        agencia (int): Agencia Responsacel pela conta do cliente
        num_conta (int): Número da Conta Corrente do cliente
        saldo (float): Saldo dísponivel na conta do cliente
        limite (float): Limite do Cheque especial do cliente
        transacoes (list): Historico de transações do cliente
    """
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome:str, cpf:str, agencia:int, num_conta:int):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self._saldo:,.2f}")

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def depositar(self, valor:float):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
    
    def sacar_dinheiro(self, valor:float):
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor.")
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_limite_chequeespecial(self):
        print(f"Seu Limte de Cheque Especial é de R${self._limite_conta():,.2f}")
    
    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self._transacoes:
            print(transacao)
    
    def transferir(self, valor:float, conta_destino:object):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular:str, conta_corrente:object):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova Senha Inválida')

