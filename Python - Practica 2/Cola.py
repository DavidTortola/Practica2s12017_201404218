#Clase Cola que utiliza nodos de un simple enlace
#Creado por Osmel David Tortola Tistoj, Carne: 201404218

import NodoListaSimple
import subprocess
ns = NodoListaSimple



class Cola():
	def __init__(self):
		self.inicio = None
		self.fin = None
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

	def queue(self, valorAux):

		nuevo = ns.NodoListaSimple(valorAux)

		if self.inicio==None:

			self.inicio = nuevo
			self.fin = nuevo

		else:
			
			self.fin.setSiguiente(nuevo)
			self.fin = nuevo

		self.tamano=self.tamano+1

	def dequeue(self):
		if self.inicio!=None:
			if self.inicio.getSiguiente()!=None:
				temp = self.inicio
				self.inicio = self.inicio.getSiguiente()
				return temp.getValor()
			else:
				temp = self.inicio
				self.inicio = None
				self.fin = None
				self.tamano=0
				return temp.getValor()
		else:
			return "empty"
		
	
	def graficarCola(self):

		if self.inicio!=None:
			file=open("Graficas\Cola.txt","w")
			file.write("digraph Matriz{ bgcolor=red node[fontcolor=black, color=white] [shape=box]\n")
			nodoAux=self.inicio
			file.write(nodoAux.getValor())
			nodoAux = nodoAux.getSiguiente()
			while nodoAux!=None:

					file.write("->" +nodoAux.getValor())
					nodoAux=nodoAux.getSiguiente()
			file.write("}")
			subprocess.Popen("dot -Tpng Graficas\Cola.txt -o Graficas\Cola.png")