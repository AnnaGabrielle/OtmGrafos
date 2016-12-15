import math
import time
import itertools 
from grafo import *

def montando_vertices(g):
	vertices=[]
	for i in range(g.num_vertex):
		vertices.append(i)
	return vertices

def forca_bruta(g):
	print("Start Força Bruta")
	start = time.time()
	vertices = montando_vertices(g)
	
	caminhos_vertices=[]
	caminhos_car = []
	lista_del = []
	
	custo_minimo = 999999999
	carro_usado = []
	caminho_usado = []


	for i in itertools.permutations(range(len(vertices))): #todas as combinacoes possíveis de caminho
		lista = list(i)
		lista.append(lista[0])
		tamanho_lista = len(lista)
		caminhos_vertices.append(lista)
		cars = len(g.car_list)

	for j in itertools.product(range(len(g.car_list)), repeat = len(vertices)): #todas as combinacoes possiveis de carros
		lista_carros = list(j)
		caminhos_car.append(lista_carros)
		#print(caminhos_car, j)

	for k in caminhos_car: #retirando as combinacoes invalidas
		lista_observando = k
		indice = caminhos_car.index(k)
		for w in range(len(vertices)):
			for z in range(w+1, len(vertices)):
				if (lista_observando[w] == lista_observando[z]) and (lista_observando[w] != lista_observando[w+1]):
					if indice not in lista_del:
						lista_del.append(indice)
			if w == ((len(vertices))-1):
				w_valor = lista_observando[w]
				indice_da_info = lista_observando.index(w_valor)
				if (indice_da_info != w) and (indice_da_info != w-1) and (lista_observando[w]!=lista_observando[w-1]): #se acha outro index diferente de w com o mesmo valor de w
					if indice not in lista_del:
						lista_del.append(indice)
				else: break

	car_minhos_viaveis = deletando_da_lista(lista_del, caminhos_car)
	#print(car_minhos_viaveis)

	for caminho in caminhos_vertices:
		for carros in car_minhos_viaveis:
			valor = calculando_custo(g, caminho, carros)
			if custo_minimo > valor: 
				custo_minimo = valor
				carro_usado = carros
				caminho_usado = caminho

	print("custo: "+ str(custo_minimo),"\nOrdem dos carros: ", carro_usado,"\nCaminho percorrido: ", caminho_usado)
	print("Forca Bruta time: "+str(time.time()-start)+" segundos")
	return custo_minimo, carro_usado, caminho_usado


def deletando_da_lista(lista_del, lista_paradeletar):
	lista_indices = lista_del
	lista_indices.sort(reverse=True)
	lista_para_deletar = lista_paradeletar
	for i in lista_indices:
		del lista_para_deletar[i]
	return lista_para_deletar



def calculando_custo(g, caminho_tsp, car_minho):  #Custo total da viagem com a troca de carros

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


g = Grafo("8_v.graph","8V_6C_data.car")
custo_minimo, carro_usado,caminho_usado = forca_bruta(g)
print(carro_usado)
g.plot(caminho_usado, "plotando_54.html")