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


def get_all_points(tuple_points):
  points = []
  for x in tuple_points:
    if x[0] != 'R':
      points.append(x[0])
  
  return points


def shortest_distance(array_routes, tuple_points):
  tuple_routes = []

  for route in array_routes:
    valor_total = 0
    ponto_ordernados = []
    
    for point in route:
      for x in tuple_points:
        if point == x[0]:
          ponto_ordernados.append(x)
    
    for point in tuple_points:
      if point[0] == 'R':
        ponto_ordernados.insert(0, point)
        ponto_ordernados.append(point)

    for i in range(len(ponto_ordernados) - 1):
      soma1 = abs(ponto_ordernados[i][1] - ponto_ordernados[i + 1][1])
      soma2 = abs(ponto_ordernados[i][2] - ponto_ordernados[i + 1][2])
      distancia = soma1 + soma2
      valor_total += distancia
    
    tupla = (route, valor_total)
    tuple_routes.append(tupla)

  sorted_tuple_routes = sorted(tuple_routes,  key=lambda tuple_routes:tuple_routes[1], reverse=True)
  return sorted_tuple_routes

      
def Populations(points, tuple_points):
  initial_population = [] 
  for i in range(6):
    copia = points.copy()
    x = shuffled_points(copia)
    initial_population.append(copia)

  x = shortest_distance(initial_population, tuple_points)

  array = []
  for i in x:
    array.append(i[0])
  
  allroutes = []

  for i in range(len(points)):
    while len(array) > 0:
      index1 = random.randint(0, len(array) - 1)
      index2 = random.randint(0, len(array) - 1)
    
      if index1 != index2:
        mutation(array[index1], array[index2], allroutes)
        array.pop(index1)
        array.pop(index2 - 1)

    menor_distancia = shortest_distance(allroutes, tuple_points)
    menor_distancia = menor_distancia[len(menor_distancia) //2:]

    for i in menor_distancia:
      array.append(i[0])

    allroutes = []
    print(menor_distancia)
  
  return menor_distancia


def mutation(route1, route2, allroutes):
  route3 = []
  route4 = []

  route3.append(route2[0])
  for i in route1[1:]:
    if i == route3[0]:
      route3.append(route1[0])
    else:
      route3.append(i)

  route4.append(route1[0])
  for i in route2[1:]:
    if i == route4[0]:
      route4.append(route2[0])
    else:
      route4.append(i)


  allroutes.append(route1)
  allroutes.append(route2)
  allroutes.append(route3)
  allroutes.append(route4)
  return allroutes


def shuffled_points(array):
  random.shuffle(array)

  return array


matrix = open('matrix.txt', 'r')
matriz = get_matrix(matrix)
tuple_points = get_all_points_and_indexes(matriz)
points = get_all_points(tuple_points)


population = Populations(points, tuple_points)
print(population)
