curso = "    python "

print(curso.strip())

print('Remove espaços da esquerda')
print(curso.lstrip()+'.')

print('Remove espaços da direita')
print(curso.rstrip()+'.')

cursos = "python"
print('Center', cursos.center(10, "#"))

print(".".join(cursos))
