#Clase nodo para la lista simple, con valor y siguiente.
class NodoListaSimple(object):

	def __init__(self, dato = None, siguiente = None):
		self.valor = dato
		self.siguiente = siguiente

	def getValor(self):
		return self.valor

	def setValor(self, valorAux):
		self.valor = valorAux

	def getSiguiente(self):
		return self.siguiente

	def setSiguiente(self, valorAux):
		self.siguiente = valorAux
