#Clase de lista doblemente enlazada que usa nodos tipo nodo doble
import NodoDoble
nd = NodoDoble



class ListaDoble():
	def __init__(self, tamanio = 0):
		self.inicio = None
		self.fin = None
		self.tamanio = tamanio

	#Devuelve true si el tamanio es 0 y false si es mayor que cero
	def isEmpty(self):
		if self.tamanio == 0:
			return True
		else:
			return False

	#Agrega un nodo con el valor que recibe al final de la lista
	def add(self, valor):
		nuevo = nd.NodoDoble(valor)

		if self.isEmpty()==True:

			self.inicio = nuevo
			self.fin = nuevo

		else:

			self.fin.setSiguiente(nuevo)
			self.fin = nuevo
		self.tamanio = self.tamanio + 1


	#Imprime los valores de la lista
	def listaPrint(self):
		nodoAux = self.inicio
		while nodoAux != self.fin.getSiguiente():
			print str(nodoAux.getValor())
			nodoAux = nodoAux.getSiguiente()



	#Agrega al inicio de la lista
	def agregarInicio(self,valor):
		nuevo = nd.NodoDoble(valor)
		if self.isEmpty() == True:
			self.inicio = nuevo
			self.fin = nuevo
		else:
			nuevo.setSiguiente(self.inicio)
			self.inicio = nuevo
		self.tamanio = self.tamanio + 1

	#Devuelve un nodo que cumple con tener el mismo valor
	def buscar(self,valor):
		if self.isEmpty()==False:
			nodoAux = self.inicio
			while nodoAux != self.fin.getSiguiente():
				if nodoAux.getValor() == valor:
					return nodoAux
				else:
					nodoAux = nodoAux.getSiguiente()
		return None