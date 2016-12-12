import math
from grafo import *

def tsp(g):
    caminhos = [[] for x in range(g.num_vertex)]
    for v in range(g.num_vertex):
        print(v)
        usados = [0 for x in range(g.num_vertex)]
        usados[v] = 1
        caminhos[v].append(v)
        while(sum(usados)!=g.num_vertex):
           
            if(len(caminhos[v])==1):
                candidatos = [caminhos[v][0]]
            else:
                candidatos = [caminhos[v][0],caminhos[v][-1]]
 
            custo = 99999999
            proximo = None
 
            for i in range(len(candidatos)):
                for u in range(g.num_vertex):
                    if(g.get_dist(candidatos[i],u)<=custo and candidatos[i]!=u and not usados[u]):
                        custo = g.get_dist(candidatos[i],u)
                        proximo = [i,u]
           
            usados[proximo[1]] = 1
 
            if(proximo != None):
                if(proximo[0]==0):
                    if(len(candidatos)==1):
                        caminhos[v].append(proximo[1])
                    else:
                        caminhos[v].insert(0,proximo[1])
                else:
                    caminhos[v].append(proximo[1])
   
    for i in range(len(caminhos)):
        for j in range(len(caminhos[i])):
           
            aux = caminhos[i][0]
            del caminhos[i][0]
            caminhos[i].insert(-1,aux)
            j = 0
 
            if(i == caminhos[i][j]):
                caminhos[i].append(i)
                break
           
 
    return caminhos

def menor_caminho(g,caminhos):
	custos = []
	aux = 0

	for i in range(g.num_vertex):
		for j in range(g.num_vertex):
			l = j + 1
			aux = aux + g.get_dist(caminhos[i][j],caminhos[i][l])
		custos.append(aux)
		aux = 0

	valor_min = min(custos)
	index_minimo = custos.index(valor_min)

	caminho_min = caminhos[index_minimo]

	return caminho_min, valor_min


