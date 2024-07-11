menu = """
    $$$$ PyBank - Sistema Bancário Pytonico $$$$
###################################################
 MENU:
 --------------------------------------------------
  - (E) para Extrato
  - (S) para Saque
  - (D) para Depósito
  - (Q) para sair do sistema

  Digite a opção desejada: """

saldo_cliente = 0.0
qte_saques = 3
saques_realizados = 0
limite_saque = 500.0
extrato_cliente = ""


def extrato():
	global extrato_cliente

	print("Extrato")
	print("-------------------------------")
	print(extrato_cliente)
	print("-------------------------------")
	saldo()

def saque():
	global saldo_cliente
	global extrato_cliente
	global saques_realizados

	valor_saque = float(input("Valor do saque: "))
	if valor_saque > 0 and  valor_saque <=  saldo_cliente and saques_realizados < qte_saques and valor_saque <= limite_saque:
		saldo_cliente -= valor_saque
		saques_realizados+=1
		extrato_cliente+= f"Saque de R$ {valor_saque:.2f}\n"
		print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
		saldo()
	elif valor_saque > saldo_cliente:
		print("Saque não realizado. Saldo insuficiente")
	elif valor_saque < 0:
		print("Saque não realizado. Digite um valor válido.")
	elif saques_realizados >= qte_saques:
		print("Você não tem mais saques disponíveis")
	elif valor_saque > limite_saque:
		print(f"O valor máximo permitido por saque é de R$ {limite_saque}")


def deposito():
	global saldo_cliente
	global extrato_cliente

	valor_deposito = float(input("Valor a ser depositado: "))
	print(valor_deposito)
	if valor_deposito > 0:
		saldo_cliente+= valor_deposito
		extrato_cliente+= f"Depósito de R$ {valor_deposito:.2f}\n"
		print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
		saldo()
	else:
		print("Depósito não realizado, por favor verifique o valor informado")

def saldo():
	print(f"Seu saldo é R$ {saldo_cliente:.2f}")

def sair():
	print("Sessão encerrada. Obrigado por utilizar nossos serviços")

while True:

	opcao = input(menu)

	if opcao in["e","E"]:
		extrato()
	elif opcao in["s","S"]:
		saque()
	elif opcao in["d","D"]:
		deposito()
	elif opcao in["q","Q"]:
		sair()
		break
	else:
		print("Operação inválida, por favor digite uma opção do menu")


