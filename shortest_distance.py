def menor_distancia(matriz):
  pontos = []
  for line in matriz:
    for x in line:
      if x != '0':
        pontos.append(matriz.index(line))
        pontos.append(line.index(x))
  # if pontos[0] > pontos[2]:
  #   soma1 = pontos[0] - pontos[2]
  # else:
  #   soma1 = pontos[2] - pontos[0]
    
  # if pontos[1] > pontos[3]:
  #   soma2 = pontos[1] - pontos[3]
  # else:
  #   soma2 = pontos[3] - pontos[1]
  soma1 = abs(pontos[0] - pontos[2])
  soma2 = abs(pontos[1] - pontos[3])
  soma_total = soma1 + soma2
  return soma_total

lista = []
matriz = open('matrix.txt', 'r')
for line in matriz: 
  linha = []
  for x in line:
    if (x != ' ') and (x != '\n'):
      linha.append(x)
  lista.append(linha)

print(menor_distancia(lista))
matriz.close()
