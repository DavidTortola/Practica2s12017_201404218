import NodoListaSimple

class ListaSimple(object):
	def __init__(self):
		self.inicio = None

	def isEmpty(self):
		if self.inicio==None:
			return True
		else:
			return False

	def listaPrint(self):
		if self.isEmpty()==True:
			nodoAux = NodoListaSimple
			nodoAux = self.inicio
			while (nodoAux.getSiguiente() != None) :
				print(nodoAux.getValor())
				nodoAux = nodoAux.getSiguiente()
		else:
			print "aaa"


	def add(self, valorAux):

		nuevo = NodoListaSimple().setValor(valorAux)

		if self.isEmpty()==True:

			self.inicio = nuevo

		else:

			nodoAux=NodoListaSimple

			nodoAux = self.inicio

			while (nodoAux.getSiguiente() != None ):
				nodoAux = nodoAux.getSiguiente()

			nodoAux.setSiguiente(nuevo)
			self.inicio=nuevo
