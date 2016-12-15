import time
import math
from grafo import *

def montando_vertices(g):
	vertices=[]
	for i in range(g.num_vertex):
		vertices.append(i)
	return vertices

def tsp_backtracking(g, vertices, l, val, mincost):  # 1<=l <= n, parâmetro
	n = len(vertices)
	varaux = 0
	if l == n:
		mincost = min(mincost, val+g.get_dist(vertices[n],vertices[1]))
	else:
		for i in range(l+1, n):
			varaux = vertices[l+1]
			vertices[l+1] = vertices[i]
			vertices[i] = varaux
			newLength = val + g.get_dist(vertices[l], vertices[l+1])
			if newLength >= mincost:
				continue 
			else:
				mincost = min(mincost, tsp_backtracking(g, vertices, l+1, newLength, mincost))
			vertices[i] = vertices[l+1]
			vertices[l+1] = varaux
	return mincost

