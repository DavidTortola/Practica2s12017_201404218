#Clase MatrizDispersa, que utiliza listas dobles como cabeceras

import ListaDoble
import NodoDoble
import ListaDobleL
nd = NodoDoble
ld = ListaDoble
ldl = ListaDobleL

class MatrizDispersa(object):

	def __init__(self):
		self.listaLetras = None
		self.listaDominios = None
		self.tamanio = 0

	#Insertar un valor en la matriz
	def insertar(self, letra, dominio, valor):

		#Si es el primer valor en insertarse
		if self.tamanio == 0:

			#Se instancian las cabeceras
			self.listaLetras = ldl.ListaDobleL()
			self.listaDominios = ld.ListaDoble()

			#Se crea el nodo a insertar en la matriz
			nodoNuevo = nd.NodoDoble(valor)

			#Se agrega los nodos respectivos en las cabeceras
			self.listaLetras.add(letra)
			self.listaDominios.add(dominio)

			#Se crean nodos auxiliares para colocar los apuntadores
			nodoAuxiliarDominio = nd.NodoDoble()
			nodoAuxiliarLetra = nd.NodoDoble()

			#Se crean los apuntadores
			NodoAuxiliarLetra = self.listaLetras.buscar(letra)
			NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

			NodoAuxiliarLetra.setSiguiente(nodoNuevo)
			NodoAuxiliarDominio.setAbajo(nodoNuevo)

			nodoNuevo.setArriba(NodoAuxiliarDominio)
			nodoNuevo.setAnterior(NodoAuxiliarLetra)

			#Se aumenta el tamanio de la matriz
			self.tamanio = self.tamanio + 1

		#Si ya existe un nodo en la matriz
		elif self.tamanio > 0:



















			#Si ya existe la cabecera de letra y de dominio
			if self.listaLetras.buscar(letra) != None and self.listaDominios.buscar(dominio) != None:




				#Se crean los apuntadores
				NodoAuxiliarDominio = self.listaDominios.inicio
				NodoAuxiliarLetras = self.listaLetras.inicio

				posicionL = self.recorrerCabeceraL(letra)
				posicionD = self.recorrerCabeceraD(dominio)

				print str(posicionD)
				i=0
				while i <= posicionL:
					NodoAuxiliarDominio = NodoAuxiliarDominio.getAbajo()
					i = i+1

				i=0
				while i <= posicionD:
					NodoAuxiliarLetra = NodoAuxiliarLetra.getSiguiente()
					i = i+1

				print NodoAuxiliarLetra.getValor() +" asdfasdfasd"

				#Se crea el nodo a insertar en la matriz
				nodoNuevo = nd.NodoDoble(valor)
				

				nodoNuevo.setAbajo(NodoAuxiliarDominio.getAbajo())
				NodoAuxiliarDominio.getAbajo().setArriba(nodoNuevo)
				nodoNuevo.setArriba(NodoAuxiliarDominio)
				NodoAuxiliarDominio.setAbajo(nodoNuevo)

				nodoNuevo.setSiguiente(NodoAuxiliarLetra.getSiguiente())
				NodoAuxiliarLetra.getSiguiente().setAnterior(nodoNuevo)
				nodoNuevo.setAnterior(NodoAuxiliarLetra)
				NodoAuxiliarLetra.setSiguiente(nodoNuevo)

				#Se aumenta el tamanio de la matriz
				self.tamanio = self.tamanio + 1


			#Si no existe la cabecera letra pero si existe el dominio
			elif self.listaLetras.buscar(letra) == None and self.listaDominios.buscar(dominio) != None:

				#Se agrega la cabecera letra
				self.listaLetras.add(letra)

				#Se crean los apuntadores
				NodoAuxiliarLetra = self.listaLetras.buscar(letra)
				NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

				#Se crea el nodo a insertar en la matriz
				nodoNuevo = nd.NodoDoble(valor)
				NodoAuxiliarLetra.setSiguiente(nodoNuevo)

				#Recorre y agrega al final del dominio el nuevo nodo
				while NodoAuxiliarDominio.getAbajo() != None:
					NodoAuxiliarDominio = NodoAuxiliarDominio.getAbajo()

				NodoAuxiliarDominio.setAbajo(nodoNuevo)

				nodoNuevo.setArriba(NodoAuxiliarDominio)
				nodoNuevo.setAnterior(NodoAuxiliarLetra)

				#Se aumenta el tamanio de la matriz
				self.tamanio = self.tamanio + 1

			#Si la letra ya existe y la cabecera dominio no
			elif self.listaLetras.buscar(letra) != None and self.listaDominios.buscar(dominio) == None:

				#Se agrega la cabecera a la lista
				self.listaDominios.add(dominio)

				#Se crean los apuntadores
				NodoAuxiliarLetra = self.listaLetras.buscar(letra)
				NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

				#Se crea el nodo a insertar en la matriz
				nodoNuevo = nd.NodoDoble(valor)
				NodoAuxiliarDominio.setAbajo(nodoNuevo)

				#Recorre y agrega al final de la cabecera letra el nuevo nodo
				while NodoAuxiliarLetra.getSiguiente() != None:
					NodoAuxiliarLetra = NodoAuxiliarLetra.getSiguiente()
				NodoAuxiliarLetra.setSiguiente(nodoNuevo)

				nodoNuevo.setArriba(NodoAuxiliarDominio)
				nodoNuevo.setAnterior(NodoAuxiliarLetra)

				#Se aumenta el tamanio de la matriz
				self.tamanio = self.tamanio + 1

			#No existe ni la cabecera de letra ni la de dominio
			elif self.listaLetras.buscar(letra) == None and self.listaDominios.buscar(dominio) == None:

				#Se agrega la cabecera a la lista
				self.listaDominios.add(dominio)
				self.listaLetras.add(letra)

				#Se crean los apuntadores
				NodoAuxiliarLetra = self.listaLetras.buscar(letra)
				NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

				#Se crea el nodo a insertar en la matriz
				nodoNuevo = nd.NodoDoble(valor)
				NodoAuxiliarLetra.setSiguiente(nodoNuevo)
				NodoAuxiliarDominio.setAbajo(nodoNuevo)

				nodoNuevo.setArriba(NodoAuxiliarDominio)
				nodoNuevo.setAnterior(NodoAuxiliarLetra)

				#Se aumenta el tamanio de la matriz
				self.tamanio = self.tamanio + 1

	def imprimirMatriz(self):
		nodoAux = self.listaDominios.inicio
		actual = nodoAux
		while nodoAux != None:
			nodoAux2 = self.listaLetras.inicio
			while nodoAux2 != None:
				if actual != None:
					print actual.getValor()
					actual = actual.getAbajo()
				nodoAux2 = nodoAux2.getAbajo()
				
			print "  ----   "
			nodoAux = nodoAux.getSiguiente()
			actual = nodoAux


	def recorrerCabeceraL(self, valor):
		nodoAux = self.listaLetras.inicio
		contador = 0
		while nodoAux != None:
			if nodoAux.getValor() == valor:
				return contador
			else:
				nodoAux = nodoAux.getAbajo()
				contador = contador + 1
		return -1


	def recorrerCabeceraD(self, valor):
		nodoAux = self.listaDominios.inicio
		contador = 0
		while nodoAux != None:
			if nodoAux.getValor() == valor:
				return contador
			else:
				nodoAux = nodoAux.getSiguiente()
				contador = contador + 1
		return -1

