from grafo import Grafo
from create import *
from heuristica import *
from backtracking import *
from forca_bruta import *
import itertools

#--------------- chamada do create, para criar os arquivos  ---------
#create_graph_data(5) # (numero de vertices)
#create_car_data(3,5) #(numero de carros, numero de vertices)

#---------------------necessario para Forca Bruta E Backtraking------
#g = Grafo("5_v.graph","5V_3C_data.car")

#--------------- chamada Forca Bruta -------------------------------- 
#custo_minimo, carro_usado,caminho_usado = forca_bruta(g)
#g.plot(caminho_usado, "plotandoResultado_forcaBruta.html")

#--------------- chamada heuristica ---------------------------------
#exec_heurica("5_v.graph","5V_3C_data.car")

# -------------- chamada do backtracking, só tem o tsp --------------
#caminho, car, calculo = exec_heurica("5_v.graph","5V_3C_data.car")
#distOpt = calcularDistancia(g, caminho)
#vertices = montando_vertices(g)
#custoback = tsp_backtracking(g, vertices, 1, 0, distOpt)
#print("Custo caminho backtracking: ", custoback)
