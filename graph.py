from grafo import Grafo
from heuristica import *

g = Grafo("10_v.graph","10V_10C_data.car")
caminhos = tsp(g)

#print(g)
for caminho in caminhos:
	print(caminho)

caminho, valor = menor_caminho(g, caminhos)	

print (caminho, valor)

g.plot(caminho)