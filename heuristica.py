import math
import time
from grafo import *

def tsp(g): #heurisca inicial do tsp
    print("Start TSP")
    start = time.time()
    caminhos = [[] for x in range(g.num_vertex)] 
    step = 1
    v = 0 
    soma = 1
    while v < g.num_vertex: #todos os vertices serao iniciais em algum momento 
        if v > g.num_vertex:
        	break
        usados = [0 for x in range(g.num_vertex)] #marcado todos os vertices como usados
        usados[v] = 1 #vertice inicial marcado como usado
        caminhos[v].append(v) 
        while(sum(usados)!=g.num_vertex): #se todos os vertices ainda nao foram usados
           
            if(len(caminhos[v])==1): #candidatos sao os extremos da lista, para poder acrescentar vizinhos
                candidatos = [caminhos[v][0]]
            else:
                candidatos = [caminhos[v][0],caminhos[v][-1]]
 
            custo = 99999999
            proximo = None
 
            for i in range(len(candidatos)):
                for u in range(g.num_vertex):
                    if(g.get_dist(candidatos[i],u)<=custo and candidatos[i]!=u and not usados[u]): #pegando os candidatos e vendo a distancia com todos os outros, sendo nao usados
                        custo = g.get_dist(candidatos[i],u)
                        proximo = [i,u]
           
            usados[proximo[1]] = 1 #marcando u como usado
 
            if(proximo != None): 
                if(proximo[0]==0): #se o candidato estava na primeira posicao
                    if(len(candidatos)==1): 
                        caminhos[v].append(proximo[1])
                    else: 
                        caminhos[v].insert(0,proximo[1])
                else:
                    caminhos[v].append(proximo[1])
        soma+=0.2
        v+= 1 if g.num_vertex <= 250 else int(soma) #se numero de vertices for maior que 250, o passo dele aumenta. 
   
    for i in range(len(caminhos)): #reorganiza a lista para o inicial ficar certo
        for j in range(len(caminhos[i])):
           
            aux = caminhos[i][0]
            del caminhos[i][0]
            caminhos[i].insert(-1,aux)
            j = 0
 
            if(i == caminhos[i][j]):
                caminhos[i].append(i)
                break
           
    print("TSP time: "+str(time.time()-start)+" segundos")
    return caminhos

def menor_caminho(g,caminhos): #qual das opcoes de caminho é o menor
	custos = []
	aux = 0

	for i in range(len(caminhos)):
		if len(caminhos[i])== 0:
			break
		for j in range(g.num_vertex):
			l = j + 1
			aux = aux + g.get_dist(caminhos[i][j],caminhos[i][l])
		custos.append(aux)
		aux = 0

	valor_min = min(custos)
	index_minimo = custos.index(valor_min)

	caminho_min = caminhos[index_minimo]

	return caminho_min, valor_min

def calcularDistancia(g, caminho): #calculo da distancia
	aux = 0
	for i in range(g.num_vertex):
		l = i +1
		aux += g.get_dist(caminho[i], caminho[l])
	return aux



def twoOptSwap(caminho, i, k):
	novo_caminho = caminho[:]
	inicio = novo_caminho[0:i] 
	meio = novo_caminho[i:k]
	meio = meio[::-1]
	final = novo_caminho[k:]

	novo_caminho = inicio + meio + final
	return novo_caminho

def twoOpt(g,caminho):  #2opt para melhorar o caminho
	print("Start 2-OPT")
	start = time.time()
	mudou = True 
	distancia_atual = calcularDistancia(g,caminho)
	caminho_atual = caminho[:-1]
	itt = 1
	mudanca = 0 
	while mudou and itt<999999 and mudanca <= 150: #limita o número de mudanças 
		
		mudou = False
		for i in range(g.num_vertex-1):
			for k in range(i+1, g.num_vertex):
				itt+=1
				novo_caminho = twoOptSwap(caminho_atual, i, k)
				nova_distancia = calcularDistancia(g, novo_caminho+[novo_caminho[0]])
				if nova_distancia < distancia_atual:
					mudou = True
					mudanca += 1
					distancia_atual = nova_distancia
					caminho_atual = novo_caminho[:]
	print("2-opt time: "+ str(time.time()-start)+ " segundos \nNumero de iteracoes: "+str(itt)+"\nNumero de mudancas: "+str(mudanca))
	return caminho_atual+[caminho_atual[0]]
		
def carroh(g,caminho): #heurisca para o carro
	start = time.time()
	carros_usados = [-1 for i in range(len(g.car_list))]  #-1 significa que o carro pode ser pego ainda
	custo = 99999999
	carro = None
	
	for car in range(len(g.car_list)): #decisao do primeiro carro, carro com menor custo para ir para a proxima cidade
		novo_custo = g.car_list[car].rent(caminho[0]) + g.get_dist(caminho[0],caminho[1])/g.car_list[car].kmpl()
		if(custo>=novo_custo):
			custo = novo_custo
			carro = car

	car_minho = []   #caminho de carros, cada carro usado para ir do vértice atual para o próximo
	car_minho.append(carro)
	carros_usados[carro] = 0  #carro marcado como sendo usado

	for i in range(1,len(caminho)-1): #dist(v,v+1) -> impossivel, por isso v-1,v.  Decidindo o próximo carro
		custo = 99999999
		for x in range(len(carros_usados)):
			if(carros_usados[x]==0):
				carro_atual = x  #qual o carro atual
		for car in range(len(g.car_list)):
			if(carros_usados[car]==1): #colocar um custo muito grande para ser impossivel pegar carro ja devolvido
				custo_c = 2*custo
				custo_aluguel = 0
				custo_devol = 0				
			else: #os carros que ainda podem ser pegos
				if(carro_atual == car): #info se continuar com o carro atual
					custo_aluguel = 0
					custo_devol = 0
					for v in range(i+1,len(caminho)-1): #pega a media do custo de devolução dessa carro nos vertices futuros
						custo_devol += g.car_list[car].back(v)
						if(v==len(caminho)-2):
							custo_devol/=v
				else: #custo de pegar outro carro para ir
					custo_devol = g.car_list[carro_atual].back(caminho[i])
					custo_aluguel = g.car_list[car].rent(caminho[i])
				
				custo_c =  g.get_dist(caminho[i], caminho[i+1])/g.car_list[car].kmpl() #custo do caminho

			custo_t = custo_aluguel + custo_devol + custo_c			#custo total
			
			if(custo >= custo_t): #decisao do carro
				custo = custo_t
				carro_novo = car
		carros_usados[carro_atual]=1   #nao deixa mais pegar esse carro
		carros_usados[carro_novo]=0    #carro usando no momento
		car_minho.append(carro_novo)   #acrescenta o carro no caminho de carros
	print("heuristica carro: "+ str(time.time()-start)+ " segundos")
	return car_minho

def calculando_valor(g, caminho_tsp, car_minho):  #Custo total da viagem com a troca de carros

	valor_caminho = 0
	numero_carros = 1
	vaux_carro = 0
	vaux_vertice = 0
	caminho_tuple = []
	for i in range(len(caminho_tsp)-1): #para o caminho ter o mesmo tamanho do car_minho
		caminho_tuple.append(tuple([caminho_tsp[i],caminho_tsp[i+1]]))

	for i in range(len(car_minho)): #pegando o gasto de uma cidade para a outra no caminho_tsp, usando a ordem dos carros de car_minho
		vaux_carro = car_minho[i]
		path = caminho_tuple[i]
		valor_caminho += g.get_dist(path[0],path[1])/g.car_list[vaux_carro].kmpl() #preco considerado km/l, dividindo acha-se litro, considerou-se 1l = 1 valor para o gasto
		

	for j in range(len(car_minho)):  #custo de pegar e devolver os carros nesse caminho_tsp
		vaux_carro = car_minho[j]
		vaux_vertice = caminho_tsp[j]
		if (caminho_tsp[0] == caminho_tsp[j+1]): #terminando a viagem, devolvendo o ultimo carro 
			valor_caminho = valor_caminho + g.car_list[vaux_carro].back(caminho_tsp[0])
			break
		elif j < 1: #iniciando a viagem, alugando o primeiro carro
			valor_caminho = valor_caminho + g.car_list[vaux_carro].rent(caminho_tsp[0])
		else:
			if car_minho[j] != car_minho[j-1]: #se carro no vertice atual e diferente do anterior: Devolve o carro anterior no vertice atual e aluga o carro atual neste mesmo vertice 
				valor_caminho= valor_caminho + g.car_list[car_minho[j-1]].back(caminho_tsp[j]) + g.car_list[vaux_carro].rent(caminho_tsp[j])		
		
		if(car_minho[j] != car_minho[j+1]): #contando o número de carros usados
			numero_carros+=1

	return valor_caminho, numero_carros

def exec_heurica(grafo, carro): #chamada da heuristica. (grafo.graph, carro.car)
	g = Grafo(grafo,carro) #info dos arquivos
	caminhos = tsp(g) #rodando a tsp

	caminho, valor = menor_caminho(g, caminhos)	
	g.plot(caminho,	"antes.html") #plotando o grafo antes das melhorias

	caminho = twoOpt(g, caminho) #2opt
	car = carroh(g,caminho) #rodando a heurisica do carro
	print("Caminho a ser seguido: ")
	print(caminho)
	print("Ordem dos carros:")
	print(car)
	g.plot(caminho, "depois.html") #plotando o grafo depois da melhoria do 2opt
	calculo,car = calculando_valor(g, caminho, car)
	print("Custo da viagem: ", calculo,"\nQuantidade de carros usados: ", car)
	return caminho, car, calculo