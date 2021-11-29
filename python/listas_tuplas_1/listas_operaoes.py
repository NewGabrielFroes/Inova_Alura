idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

type(idades)

len(idades)

print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)

for idade in idades:
  print(idade)

idades.remove(30)

idades.append(15)

idades.remove(15)

idades.append(27)
idades.remove(27)

if 15 in idades:
  idades.remove(15)

if 28 in idades:
  idades.remove(28)

idades.append(19)

idades.insert(0, 20)


idades = [20, 39, 18]

idades.append([27, 19])

for elemento in idades:
  print("Recebi o elemento", elemento)

idades = [20, 39, 18]
idades.extend([27, 19])

for idade in idades:
  print(idade + 1)

idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)

idades_no_ano_que_vem = [idade+1 for idade in idades]

print([idade for idade in idades if idade > 21])


def proximo_ano(idade):
  return idade+1

[proximo_ano(idade) for idade in idades if idade > 21]

def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)

def faz_processamento_de_visualizacao(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()