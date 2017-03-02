#Clase de lista doblemente enlazada que usa nodos tipo nodo doble
import NodoDoble
nd = NodoDoble



class ListaDobleL():
	def __init__(self, tamanio = 0):
		self.inicio = None
		self.fin = None
		self.tamanio = tamanio

	def isEmpty(self):
		if self.tamanio == 0:
			return True
		else:
			return False

	def add(self, valor):
		nuevo = nd.NodoDoble(valor)

		if self.isEmpty()==True:

			self.inicio = nuevo
			self.fin = nuevo

		else:

			self.fin.setAbajo(nuevo)
			self.fin = nuevo
		self.tamanio = self.tamanio + 1


	def listaPrint(self):
		nodoAux = self.inicio
		while nodoAux != self.fin.getAbajo():
			print str(nodoAux.getValor())
			nodoAux = nodoAux.getAbajo()



	def agregarInicio(self,valor):
		nuevo = nd.NodoDoble(valor)
		if self.isEmpty() == True:
			self.inicio = nuevo
			self.fin = nuevo
		else:
			nuevo.setAbajo(self.inicio)
			self.inicio = nuevo
		self.tamanio = self.tamanio + 1


	def buscar(self,valor):
		if self.isEmpty()==False:
			nodoAux = self.inicio
			while nodoAux != self.fin.getAbajo():
				if nodoAux.getValor() == valor:
					return nodoAux
				else:
					nodoAux = nodoAux.getAbajo()
		return None