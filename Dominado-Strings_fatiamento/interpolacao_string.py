
nome = "Clenio"
idade = 45
profissao = "Programador"
bootcamp = "bootcamp NTT DATA"
escola = "Dio Innovation"
linguagem = "Python"

'''METODO'''
print("Nome:  %s Idade: %d "%(nome,idade))


'''METODO STRINGS'''
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}, Profissão: {profissao}, ".format(nome=nome,idade=idade,profissao=profissao))

'''METODO F STRING'''
print(f"Nome: {nome} Idade: {idade}")
