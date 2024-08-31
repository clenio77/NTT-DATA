texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")

print()  # adiciona uma quebra de linha

# exemplo usando a função built-in range(inicio, fim, salto)
for numero in range(0,25, 2):
	print(numero, end=' ')