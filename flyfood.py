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
      if (x != '0') and (x != 'R'):
        point_tuple = (x, matrix.index(line), line.index(x))
        points.append(point_tuple)

  return points

def all_routes(matrix):

  return

def shortest_distance(array, points):
  
  return


print(get_all_points(lista)) 
matrix.close()
