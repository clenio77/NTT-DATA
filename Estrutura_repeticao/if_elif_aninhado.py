conta_normal = True
conta_universitaria = False
saldo = 100
cheque_especial = 100
saque = int(input('Digite o valor do saque: '))


if conta_normal:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	elif saque <= (saldo + cheque_especial):
		print("Saque realizado com uso do cheque especial!")
    else:
        print('Não foi possível realizar o saque, saldo insuficiente!s')
elif conta_universitaria:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	else:
		print("Saldo insuficiente!")
else:
    print('Sistema não reconheceu o tipo de conta"')