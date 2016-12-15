from grafo import Grafo
from heuristica import *
from backtracking import *
import itertools

#g = Grafo("10V.graph","10V_3C_data.car")
#caminhos = tsp(g)
#caminho_antes, valor = menor_caminho(g, caminhos) 
#caminho= twoOpt(g, caminho_antes)
#distOpt = calcularDistancia(g, caminho)
#print(distOpt)

#vertices = montando_vertices(g)
#custoback = tsp_backtracking(g, vertices, 1, 0, distOpt)
#print(custoback)

exec_heurica("5_v.graph","5V_4C_data.car")
# g = Grafo("140_v.graph","140V_25C_data.car")
# caminhos = tsp(g)

# #print(g)

# caminho, valor = menor_caminho(g, caminhos)	

# g.plot(caminho,	"antes.html")
# caminho = twoOpt(g, caminho)
# print(len(caminho))
# print(caminho)
# car = carroh(g,caminho)
# print(len(car))
# print(car)
# g.plot(caminho, "depois.html")

# calculo,car = calculando_valor(g, caminho, car)
# print(calculo, car)