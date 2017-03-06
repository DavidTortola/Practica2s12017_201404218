#Clase Lista Simple, utiliza nodos tipo simples con un enlace
#Creado por Osmel David Tortola Tistoj, Carne: 201404218

import NodoListaSimple
import subprocess
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

	def graficarLista(self):

		if self.inicio!=None:
			file=open("Graficas\ListaSimple.txt","w")
			file.write("digraph Matriz{ bgcolor=red node[fontcolor=black, color=white] [shape=box]\n")
			nodoAux=self.inicio
			file.write(nodoAux.getValor())
			nodoAux = nodoAux.getSiguiente()
			while nodoAux!=None:

					file.write("->" +nodoAux.getValor())
					nodoAux=nodoAux.ge
					tSiguiente()
			file.write("}")
			subprocess.Popen("dot -Tpng Graficas\ListaSimple.txt -o Graficas\ListaSimple.png")