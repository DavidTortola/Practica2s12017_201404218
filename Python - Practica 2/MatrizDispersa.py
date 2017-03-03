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
			nodoNuevo = nd.NodoDoble(valor, letra, dominio)

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

				#Caso 1: Ya existe un nodo que une a las dos cabeceras, el valor se agrega en la lista del nodo.
				if self.buscarMatch(letra, dominio) == True:

					NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

					nodoAux = NodoAuxiliarDominio

					while nodoAux != None:

						if nodoAux.getLetra() == letra:
							NodoAuxiliarDominio = nodoAux
							nodoAux = nodoAux.getAbajo()
						else:
							nodoAux = nodoAux.getAbajo()

					NodoAuxiliarDominio.setValor(valor)	# ------------------> AQUI SE DEBE AGREGAR A LA FUTURA LISTA DEL NODO

				#Caso 2: No existe un nodo en comun entre las cabeceras, se debe crear el nodo en medio.
				else:

					NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

					nodoAux = NodoAuxiliarDominio.getAbajo()

					#Se crea el nodo a insertar en la matriz
					nodoNuevo = nd.NodoDoble(valor, letra, dominio)

					letraInsertar = letra[:1]
					letraInsertar = ord(letraInsertar)

					insertado = False
					while nodoAux != None:
						letraComparar = nodoAux.getLetra()[:1]
						letraComparar = ord(letraComparar)
						
						if letraInsertar>letraComparar:
							nodoAux = nodoAux.getAbajo()
						else:

							nodoNuevo.setAbajo(nodoAux)
							nodoNuevo.setArriba(nodoAux.getArriba())
							nodoAux.getArriba().setAbajo(nodoNuevo)
							nodoAux.setArriba(nodoNuevo)
							insertado = True
							break
					if insertado == False:
						nodoAux = NodoAuxiliarDominio.getAbajo()
						while nodoAux.getAbajo() != None:
							nodoAux = nodoAux.getAbajo()

						nodoNuevo.setArriba(nodoAux)
						nodoAux.setAbajo(nodoNuevo)

					#Se colocan los apuntadores horizontales (desde la cabecera letra)
					NodoAuxiliarLetra = self.listaLetras.buscar(letra)

					nodoAux2 = NodoAuxiliarLetra.getSiguiente()

					letraInsertar = dominio[:1]
					letraInsertar = ord(letraInsertar)

					insertado = False
					while nodoAux2 != None:
						letraComparar = nodoAux2.getDominio()[:1]
						letraComparar = ord(letraComparar)
						
						if letraInsertar>letraComparar:
							nodoAux2 = nodoAux2.getSiguiente()
						else:

							nodoNuevo.setSiguiente(nodoAux2)
							nodoNuevo.setAnterior(nodoAux2.getAnterior())
							nodoAux2.getAnterior().setSiguiente(nodoNuevo)
							nodoAux2.setAnterior(nodoNuevo)
							insertado = True
							break
					if insertado == False:
						nodoAux2 = NodoAuxiliarLetra.getSiguiente()
						while nodoAux2.getSiguiente() != None:
							nodoAux2 = nodoAux2.getSiguiente()

						nodoNuevo.setAnterior(nodoAux2)
						nodoAux2.setSiguiente(nodoNuevo)

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
				nodoNuevo = nd.NodoDoble(valor, letra, dominio)

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
				nodoNuevo = nd.NodoDoble(valor, letra, dominio)


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
				nodoNuevo = nd.NodoDoble(valor, letra, dominio)
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
				if actual.getAbajo() != None:
					actual = actual.getAbajo()
					if(actual.getLetra() != None and actual.getDominio() != None):
						print actual.getValor() +" - " +actual.getLetra() +" - " +actual.getDominio()
					else:
						print actual.getValor() 

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

	def buscarMatch(self, letra, dominio):
		nodoAux = self.listaDominios.buscar(dominio)
		while nodoAux != None:
			if nodoAux.getLetra() == letra:
				return True
			else:
				nodoAux = nodoAux.getAbajo()
		return False
