# CAR RENTER SALESMAN PROBLEMA

###### Engenharia de Computação e Informação - UFRJ

###### Disciplina: Otimização em Grafos - EEL857

###### Aluna: Anna Gabrielle Lamellas Pinto Homem

## Gerais

- grafo
- car
- edge
- create
- graph 

## de Resolução

- heuristica
- forca_bruta
- backtracking -> não terminado, apenas o backtracking do TSP retornando o custo do caminho mínimo

## Informações Importantes

Os algoritmos podem ser executados a partir do graph.py, tirando os comentários da parte em que se quer executar:

Inicie executando a chamada do create, para criar os grafos e as iformações dos carros:
		create_graph_data(numero de vertices)
		create_car_data(numero de carros,numero de vertices)

Antes de executar a Força Bruta ou o Backtracking, é necessário definir o grafo g:
	 g = Grafo("nome do arquivo de grafo.graph","nome do arquivo de carro.car")

Para a heuristica, basta apenas chamar:
	exec_heurica("nome do arquivo de grafo.graph","nome do arquivo de carro.car")
