
class Cliente:
	nome = ""

class Pessoa_fisica(Cliente):
	cpf = ""
	def __init__(self, nome, cpf):
		self.nome = nome		
		self.cpf = cpf

class Pessoa_juridica(Cliente):
	cnpj = ""
	def __init__(self, nome, cnpj):
		self.nome = nome
		self.cnpj = cnpj


class Conta:
	saldo = 0
	def __init__(self, saldo, cliente):
		self.saldo = saldo
		self.cliente = cliente
			
	def saque(self, valor):
		self.saldo-=valor

	def deposito(self, valor):
		self.saldo+=valor

class Corrente(Conta):
	def __init__(self,saldo,cliente):
		super().__init__(saldo,cliente)

class Poupanca(Conta):
	def __init__(self,saldo,cliente):
		super().__init__(saldo,cliente)




cliente1= Pessoa_fisica("luisa","12343234121232")
cliente2= Pessoa_juridica("joao","11213")

conta1 = Corrente(200, cliente1) 
conta2 = Poupanca(300, cliente2)

print(conta1.saldo)
print(conta1.cliente.nome)
