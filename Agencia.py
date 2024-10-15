from random import randint

class Agencia():
  """
    Cria um objeto Agencia.

    Atributos:
        telefone (int): Telefone agência
        cnpj (int): CNPJ da agência
        numero (int): Número da agência
        clientes (List): Lista de clientes
        caixa (float): Caixa da agencia
        emprestimos (List): Lista de empréstimos da agência
       =
    """

    def __init__(self, telefone:int, cnpj:int, numero:int):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0.0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 100000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual {self.caixa}.")
        else:
            print(f"O valor de caixa está ok. Caixa atual {self.caixa}")

    def emprestar_dinheiro(self, valor:float, cpf:int, juros:float):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Emprestimo não e possivel. Dinheiro não disponível em caixa")
    
    def adicionar_cliente(self, nome:str, cpf:int, patrimonio:float):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    
    def __init__(self, telefone: int, cnpj: int, site:str):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    
    def __init__(self, telefone: int, cnpj: int):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 10000000
        

class AgenciaPremium(Agencia):

    def __init__(self, telefone: int, cnpj: int):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome: str, cpf: int, patrimonio: float):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o patrimônnio necessário.')
