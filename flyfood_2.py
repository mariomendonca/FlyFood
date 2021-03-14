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
def shortest_distance(routes, points):
  melhor_rota_distancia = 0
  melhor_rota = None
  # cada rota
  for route in routes:
    valor_total = 0 
    # cada ponto
    ponto_ordernados = []
    for point in route:
      # print(route, point)
      for x in points:
        if point == x[0]:
          ponto_ordernados.append(x)
    # ponto de partida e chegada (estabelecimento)
    for point in points:
      if point[0] == 'R':
        ponto_ordernados.insert(0, point)
        ponto_ordernados.append(point)

    # print(ponto_ordernados)
    for i in range(len(ponto_ordernados) - 1):
      soma1 = abs(ponto_ordernados[i][1] - ponto_ordernados[i + 1][1])
      soma2 = abs(ponto_ordernados[i][2] - ponto_ordernados[i + 1][2])
      distancia = soma1 + soma2
      valor_total += distancia
    # print(valor_total)

    if melhor_rota_distancia == 0:
      melhor_rota_distancia = valor_total
    if valor_total <= melhor_rota_distancia:
      melhor_rota_distancia = valor_total
      melhor_rota = route

  return melhor_rota, melhor_rota_distancia

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

def get_some_routes(points):
  qnt_de_rotas = fatorial(int(len(points))) // 2
  routes = []
  for i in range(qnt_de_rotas):
    test = points.copy()
    x = shuffled_points(test)
    routes.append(x)

  return routes


matrix = open('matrix.txt', 'r')

matriz = get_matrix(matrix)
points = get_all_points(matriz)
routes = get_some_routes(points)
tuple_points = get_all_points_and_indexes(matriz)
menor_distancia = shortest_distance(routes, tuple_points)
print(menor_distancia)
