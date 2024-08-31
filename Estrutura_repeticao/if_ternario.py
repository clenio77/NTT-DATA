saldo = 100
saque = int(input('Digite o valor do saque: '))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")