from grafo import *
from create import *
from heuristica import *
import time

#create_graph_data(8) # (numero de vertices)
#create_car_data(3,8) #(numero de carros, numero de vertices)


g = Grafo("8_v.graph","8V_6C_data.car")
melhor_sol = None
carros = []

def backtracking_carro(carro,possiveis_carros):
	global carros

	if is_solution(carro):
		carros.append(carro)
	else:
		for i in range(len(possiveis_carros)):
			novo_carro = list(list(carro)+[possiveis_carros[i]])
			novo_possiveis_carros = list(possiveis_carros)
			if(carro!=[]):
				if(carro[-1]!=novo_carro[-1]):
					del novo_possiveis_carros[novo_possiveis_carros.index(carro[-1])]
			backtracking_carro(novo_carro,novo_possiveis_carros)


def backtracking(caminho,vertices):
	global melhor_sol
	global carros
	if is_solution(caminho):
		caminho.append(caminho[0])
		for carro in carros:
			val_atual = calculando_custo(caminho,carro)
			if(melhor_sol==None):
				melhor_sol = list([[caminho,carro],val_atual])
			elif val_atual<melhor_sol[1]:
				melhor_sol = list([[caminho,carro],val_atual])
	else:
		for i in range(len(vertices)):
			for c in carros:
				novo_caminho = list(list(caminho) + [vertices[i]])
				novo_vertices = list(vertices)
				del novo_vertices[i]
	
				if(calculando_custo_parcial(novo_caminho,c[:len(novo_caminho)]) > melhor_sol[1]):
					continue
				else:
					backtracking(novo_caminho,novo_vertices)
					break

def is_solution(c):
	global g
	return True if len(c) == g.num_vertex else False

def calculando_custo(caminho_tsp, car_minho):  #Custo total da viagem com a troca de carros, feito da mesma forma que na heuristica
	global g
	valor_caminho = 0
	numero_carros = 1
	vaux_carro = 0
	vaux_vertice = 0
	caminho_tuple = []
	for i in range(len(caminho_tsp)-1):
		caminho_tuple.append(tuple([caminho_tsp[i],caminho_tsp[i+1]]))

	for i in range(len(car_minho)):
		vaux_carro = car_minho[i]
		path = caminho_tuple[i]
		valor_caminho += g.get_dist(path[0],path[1])/g.car_list[vaux_carro].kmpl()
		

	for j in range(len(car_minho)):
		vaux_carro = car_minho[j]
		vaux_vertice = caminho_tsp[j]
		if (caminho_tsp[0] == caminho_tsp[j+1]):
			valor_caminho = valor_caminho + g.car_list[vaux_carro].back(caminho_tsp[0])
			break
		elif j < 1: 
			valor_caminho = valor_caminho + g.car_list[vaux_carro].rent(caminho_tsp[0])
		else:
			if car_minho[j] != car_minho[j-1]:
				valor_caminho= valor_caminho + g.car_list[car_minho[j-1]].back(caminho_tsp[j]) + g.car_list[vaux_carro].rent(caminho_tsp[j])		
		
		if(car_minho[j] != car_minho[j+1]):
			numero_carros+=1

	return valor_caminho

def calculando_custo_parcial(caminho_tsp, car_minho):  #Custo total da viagem com a troca de carros, feito da mesma forma que na heuristica
	global g
	valor_caminho = 0
	numero_carros = 1
	vaux_carro = 0
	vaux_vertice = 0
	caminho_tuple = []
	for i in range(len(caminho_tsp)-1):
		caminho_tuple.append(tuple([caminho_tsp[i],caminho_tsp[i+1]]))

	for i in range(len(car_minho)-1):
		vaux_carro = car_minho[i]
		path = caminho_tuple[i]
		valor_caminho += g.get_dist(path[0],path[1])/g.car_list[vaux_carro].kmpl()
		

	for j in range(len(car_minho)-1):
		vaux_carro = car_minho[j]
		vaux_vertice = caminho_tsp[j]
		if (caminho_tsp[0] == caminho_tsp[j+1]):
			valor_caminho = valor_caminho + g.car_list[vaux_carro].back(caminho_tsp[0])
			break
		elif j < 1: 
			valor_caminho = valor_caminho + g.car_list[vaux_carro].rent(caminho_tsp[0])
		else:
			if car_minho[j] != car_minho[j-1]:
				valor_caminho= valor_caminho + g.car_list[car_minho[j-1]].back(caminho_tsp[j]) + g.car_list[vaux_carro].rent(caminho_tsp[j])		
		
		if(car_minho[j] != car_minho[j+1]):
			numero_carros+=1

	return valor_caminho



if __name__ == '__main__':
	path = []
	vertices = [i for i in range(g.num_vertex)]
	car = []
	p_car = [i for i in range(len(g.car_list))]
	s  = time.time()
	p,c,v = exec_heurica("8_v.graph","8V_6C_data.car")
	melhor_sol=[[p,c],v]
	print(melhor_sol)
	#a = input()
	backtracking_carro(car,p_car)
	backtracking(path,vertices)
	print(melhor_sol)

	print(time.time()-s)
