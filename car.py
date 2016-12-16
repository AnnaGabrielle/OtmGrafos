
class Car(object):

	def __init__(self,id,gas_price,rent_price,back_price):
		self.id = id
		self.gas_price = gas_price
		self.rent_price = rent_price
		self.back_price = back_price

	def kmpl(self):
		return self.gas_price

	def rent(self,vertex):
		return self.rent_price[vertex]

	def back(self,vertex):
		return self.back_price[vertex]

	def __repr__(self):
		return "Id: "+str(self.id)+" - Km/L: "+str(self.gas_price)
