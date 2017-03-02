import NodoListaSimple
lista = NodoListaSimple



class ListaSimple():
	def __init__(self):
		self.inicio = None
		self.tamano=0

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

		self.tamano=self.tamano+1

	def borrar(self, indiceAux):


		indice = int(indiceAux)


		if indice == 0:

			if self.inicio!=None:
				self.inicio = self.inicio.getSiguiente()
			else:
				self.inicio=None

		elif indice > 0:
			if indice<=self.tamano-1:
				if self.inicio!=None:
					nodoAux = self.inicio
					final = indice-1
					for i in range(0,final):
						if nodoAux.getSiguiente()!= None:
							nodoAux=nodoAux.getSiguiente()
						else:
							nodoAux

					if nodoAux.getSiguiente() != None:
						nodoAux.setSiguiente(nodoAux.getSiguiente().getSiguiente())

	def buscar(self,informacion):
		contador = 0
		if self.inicio!=None:
			nodoAux=self.inicio
			while(nodoAux!=None):
				if(str(nodoAux.getValor())==str(informacion)):
					return	contador
				else:
					contador = contador+1
					nodoAux=nodoAux.getSiguiente()
		return -1

