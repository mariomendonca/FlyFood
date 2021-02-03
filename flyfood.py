lista = []
matrix = open('matrix.txt', 'r')
for line in matrix: 
  linha = []
  for x in line:
    if (x != ' ') and (x != '\n'):
      linha.append(x)
  lista.append(linha)


def get_all_points(matrix):
  points = []
  for line in matrix:
    for x in line:
      if (x != '0'):
        point_tuple = (x, matrix.index(line), line.index(x))
        points.append(point_tuple)

  return points

def all_routes(matrix):

  return

rotas = [ 'ABCD', 'DCBA', 'DBAC']
# rotas = ['ABCD', 'ACBD']

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
    print(valor_total)

    if melhor_rota_distancia == 0:
      melhor_rota_distancia = valor_total
    if valor_total <= melhor_rota_distancia:
      melhor_rota_distancia = valor_total
      melhor_rota = route

  return melhor_rota, melhor_rota_distancia



# fazer a msm logica de colocar numa lista e dps soma lo



# shortest_distance(rotas, get_all_points(lista))
print(shortest_distance(rotas, get_all_points(lista)))
# print(get_all_points(lista)) 
matrix.close()
