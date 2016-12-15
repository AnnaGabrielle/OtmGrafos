from edge import Edge
from car import Car
import math

class Grafo(object):

	def __init__(self, file_name,car_file):
		
		file = open(file_name,"r")
		
		self.num_vertex = int(file.readline())
		
		self.car_list = []

		self.vertex = [[] for i in range(self.num_vertex)]

		self.distance_matrix = [[None]*self.num_vertex for i in range(self.num_vertex)]
		
		id = 0
		for line in file:
			point = list(map(float,line.split(" ")))
			self.add_vertex(id,point[0],point[1])
			id+=1

		file.close()

		file = open(car_file,"r")
		cars = []
		id = 0
		for line in file:
			info = line.split(";")
			if(len(info)>1):
			    kmpl = float(info[0])
			    rent = list(map(float,info[1].split(" ")))
			    back = list(map(float,info[2].split(" ")))
			    c = Car(id,kmpl,rent,back)
			    self.car_list.append(c)
			    id+=1

		self.calc_dist()

	def add_vertex(self,id,x,y):
		self.vertex[id]=[round(x,2),round(y,2)]


	def get_dist(self,i,j):
		"""retorna a distancia de ir do vertice I para o vertice J"""
		return self.distance_matrix[i][j]


	def calc_dist(self): 
		"""Calcula a distancia euclidiana entre todos os vertices"""
		for i in range(self.num_vertex):
			for j in range(self.num_vertex):
				self.distance_matrix[i][j] = round(math.sqrt(((self.vertex[i][0]-self.vertex[j][0])**2)+((self.vertex[i][1]-self.vertex[j][1])**2)),2)

	def __repr__(self):
		"""print(g) -> Printa os vertices e a matriz de distancia"""
		string = "------------| Vertices |------------\n\n"
		for i in range(self.num_vertex):
			string +=str(i)+" ["+str(self.vertex[i][0])+","+str(self.vertex[i][1])+"]\n"
		string += "\n------------| Matriz |------------\n\n"
		for i in range(self.num_vertex):
			for j in range(self.num_vertex):
				string+=str(self.distance_matrix[i][j])+" "
			string+="\n"
		string+="\n------------| END |------------"
		return string



	def plot(self,caminho, path,carro = None):
		
		file = open(path,"w")
		start = " <!DOCTYPE html><html><body><svg height=\"800\" width=\"800\"><polyline points=\""
		middle = ""
		for i in caminho:
			x = self.vertex[i]
			middle += " "+str(x[0]*2.5)+","+str(x[1]*2.5)
		middle +="\"style=\"fill:none;stroke:black;stroke-width:1\"/>"
		middle2=""
		for i in caminho:
			x = self.vertex[i]
			middle2+= "<circle cx=\""+str(x[0]*2.5)+"\" cy=\""+str(x[1]*2.5)+"\" r=\"3\"  fill=\"red\" />"

		end = "</svg></body></html>"
		string_write= start+middle+middle2+end
		file.write(string_write)


