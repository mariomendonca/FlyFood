import random 

def get_matrix(matrix_txt):
  lista = []
  for line in matrix: 
    linha = []
    for x in line:
      if (x != ' ') and (x != '\n'):
        linha.append(x)
    lista.append(linha)
  return lista

def get_all_points_and_indexes(matrix):
  array = []
  for line in matrix:
    for x in line:
      if (x != '0'):
        point_tuple = (x, matrix.index(line), line.index(x))
        array.append(point_tuple)
  return array 


# fazer a adaptacao em relacao as rota

def get_all_points(matrix):
  points = []
  for line in matrix:
    for x in line:
      if (x != '0') and (x != 'R'):
        points.append(x)
  
  return points

def shuffled_points(array):
  random.shuffle(array)
  return array

def fatorial(n):
  if n <= 1: 
    return 1
  else: 
    return n * fatorial(n - 1)


def shortest_distance(route, points):
  melhor_rota = None
  melhor_rota_distancia = 0
  maximo_de_vezes = fatorial(int(len(route))) // 2
  minimo_de_vezes = fatorial(int(len(route))) // 5
  contador_minimo = 1
  contador_maximo = 1
  
  while contador_minimo <  minimo_de_vezes and contador_maximo <= maximo_de_vezes:
    valor_total = 0 
    ponto_ordernados = []
    route = shuffled_points(route)
    for point in route:
      for x in points:
        if point == x[0]:      
          ponto_ordernados.append(x)
    # ponto de partida e chegada (estabelecimento)
    for point in points:
      if point[0] == 'R':
        ponto_ordernados.insert(0, point)
        ponto_ordernados.append(point)

    for i in range(len(ponto_ordernados) - 1):
      soma1 = abs(ponto_ordernados[i][1] - ponto_ordernados[i + 1][1])
      soma2 = abs(ponto_ordernados[i][2] - ponto_ordernados[i + 1][2])
      distancia = soma1 + soma2
      valor_total += distancia
    
    if melhor_rota_distancia == 0:
      melhor_rota_distancia = valor_total
    if valor_total <= melhor_rota_distancia:
      melhor_rota_distancia = valor_total
      melhor_rota = route
      contador_minimo += 1

    contador_maximo += 1

  return melhor_rota, melhor_rota_distancia



matrix = open('matrix.txt', 'r')

matriz = get_matrix(matrix)
points = get_all_points(matriz)
tuple_points = get_all_points_and_indexes(matriz)


testing = shortest_distance(points, tuple_points)
print(testing)
