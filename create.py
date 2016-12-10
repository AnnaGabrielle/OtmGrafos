import random

def create_car_data(n_cars,n_vertex):
	out_file = str(n_vertex)+"V_"+str(n_cars)+"C_data.car"
	file = open(out_file,"w")
	for i in range(n_cars):
		kmpl = random.uniform(10.0,16.0)
		rent = []
		back = []
		file.write("%.2f" % kmpl +";")
		for j in range(n_vertex):
			if(j!=(n_vertex-1)):
				file.write("%.2f" % random.uniform(100,300)+" ")
			else:
				file.write("%.2f" % random.uniform(100,300)+";")
		for j in range(n_vertex):
			if(j!=(n_vertex-1)):
				file.write("%.2f" % random.uniform(100,300)+" ")
			else:
				file.write("%.2f" % random.uniform(100,300))
		if(i != n_vertex-1):
			file.write("\n")
	file.close()



def create_graph_data(n_vertex):
	out_file = str(n_vertex)+"_v.graph"
	file = open(out_file,"w")
	file.write(str(n_vertex)+"\n")
	for i in range(n_vertex):
		file.write("%.1f" % random.uniform(0,200) + " " + "%.2f" % random.uniform(0,200))
		if(i != n_vertex-1):
			file.write("\n")
	file.close()



create_graph_data(5)
create_car_data(3,5)