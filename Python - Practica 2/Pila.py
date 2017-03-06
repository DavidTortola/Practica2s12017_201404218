#Clase Pila que utiliza nodos de un enlace
#Creado por Osmel David Tortola Tistoj, Carne: 201404218

import NodoListaSimple
import subprocess
ns = NodoListaSimple



class Pila():
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

	def push(self, valorAux):

		nuevo = ns.NodoListaSimple(valorAux)

		if self.inicio==None:

			self.inicio = nuevo

		else:
			
			nuevo.setSiguiente(self.inicio)
			self.inicio = nuevo

		self.tamano=self.tamano+1

	def pop(self):
		if self.inicio!=None:
			if self.inicio.getSiguiente()!=None:
				temp = self.inicio
				self.inicio = self.inicio.getSiguiente()
				return temp.getValor()
			else:
				temp = self.inicio
				self.inicio = None
				self.tamano=0
				return temp.getValor()
		else:
			return "empty"
		
	
	def graficarPila(self):

		if self.inicio!=None:
			file=open("Graficas\Pila.txt","w")
			file.write("digraph Matriz{ bgcolor=red node[fontcolor=black, color=white] [shape=box]\n")
			nodoAux=self.inicio
			file.write(nodoAux.getValor())
			nodoAux = nodoAux.getSiguiente()
			while nodoAux!=None:

					file.write("->" +nodoAux.getValor())
					nodoAux=nodoAux.getSiguiente()
			file.write("}")
			subprocess.Popen("dot -Tpng Graficas\Pila.txt -o Graficas\Pila.png")