#Clase nodo para lista doblemente enlazada
class NodoDoble(object):

	def __init__(self, valor = None, letra = None, dominio = None, siguiente = None, anterior = None, arriba = None, abajo = None):
		self.siguiente = siguiente
		self.anterior = anterior
		self.arriba = arriba
		self.abajo = abajo
		self.valor = valor
		self.letra = letra
		self.dominio = dominio

	def getValor(self):
		return self.valor

	def setValor(self, valorAux):
		self.valor = valorAux

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self, valorAux):
		self.siguiente = valorAux

	def getAnterior(self):
		return self.anterior

	def setAnterior(self, valorAux):
		self.anterior = valorAux

	def getArriba(self):
		return self.arriba

	def setArriba(self, valorAux):
		self.arriba = valorAux

	def getAbajo(self):
		return self.abajo

	def setAbajo(self, valorAux):
		self.abajo = valorAux

	def getLetra(self):
		return self.letra

	def setLetra(self, valorAux):
		self.letra = valorAux

	def getDominio(self):
		return self.dominio

	def setDominio(self, valorAux):
		self.dominio = valorAux