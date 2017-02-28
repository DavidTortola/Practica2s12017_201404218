import NodoListaSimple
lista = NodoListaSimple



class ListaSimple():
	def __init__(self):
		self.inicio = None
		self.dato=None

	def isEmpty(self):
		if self.inicio==None:
			return True
		else:
			return False

	def listaPrint(self):
			nodoAux = self.inicio
			while nodoAux != None :
				print str(nodoAux.getValor())
				nodoAux = nodoAux.getSiguiente()



	def add(self, valorAux):

		nuevo = lista.NodoListaSimple(valorAux)

		if self.inicio==None:

			self.inicio = nuevo
		else:
			
			nodoAux = self.inicio

			while (nodoAux.getSiguiente() != None ):
				nodoAux = nodoAux.getSiguiente()

			nodoAux.setSiguiente(nuevo)