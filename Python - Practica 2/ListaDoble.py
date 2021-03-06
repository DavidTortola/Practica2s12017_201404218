#Clase de lista doblemente enlazada que usa nodos tipo nodo doble, es de modo horizontal (Siguiente, anterior)
#Creado por Osmel David Tortola Tistoj, Carne: 201404218

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
		#Crea el nodo a insertar
		nuevo = nd.NodoDoble(valor)

		#Si es la primera insercion
		if self.isEmpty()==True:
			self.inicio = nuevo
			self.fin = nuevo

		#Si no es la primera insercion compara alfabeticamente antes de insertar
		else:

			#Obtiene la letra inicial del valor a insertar como cabecera
			letraInsertar = valor[:1]
			letraInsertar = ord(letraInsertar)

			#Crea un booleano para saber si se inserto en el while o si se salio sin insertar
			insertado = False

			#Inicia el auxiliar en el inicio de la lista
			nodoAux = self.inicio

			#Ciclo mientras no llegue al final de la lista
			while nodoAux != None:

				#Obtiene la letra inicial del nodo actual para comparar con la que se va a insertar
				letraComparar = nodoAux.getValor()[:1]
				letraComparar = ord(letraComparar)

				#Si la letra a insertar es mayor que la actual avanza al siguiente nodo
				if letraInsertar > letraComparar:
					nodoAux = nodoAux.getSiguiente()

				#Si la letra a insertar es menor que la actual
				else:

					#Si el nodo actual es el primero de la lista
					if nodoAux == self.inicio:

						#Ingresa el nodo actual como nuevo primero en la lista
						nuevo.setSiguiente(nodoAux)
						nodoAux.setAnterior(nuevo)
						self.inicio=nuevo
						insertado = True
						break
					#Si el nodo actual no es el primero de la lista
					else:

							#Ingresa el nuevo al medio de la lista
							nuevo.setAnterior(nodoAux.getAnterior())
							nodoAux.getAnterior().setSiguiente(nuevo)

							nuevo.setSiguiente(nodoAux)
							nodoAux.setAnterior(nuevo)
							insertado=True
							break
							
			#Si sale del whilel sin que insertado sea true es porque hay que insertar al final
			if insertado == False:
				self.fin.setSiguiente(nuevo)
				nuevo.setAnterior(self.fin)
				self.fin = nuevo

		#Aumenta el tamanio de la lista
		self.tamanio = self.tamanio + 1


	def getInicio(self):
		return self.inicio

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

	def eliminarPorValor(self,valor):

		if self.isEmpty()==False:
			nodoAux=self.inicio

			while nodoAux!=self.fin.getSiguiente():
				if nodoAux.getValor() == valor:

					#Eliminar
					#Si es el primer nodo en la lista
					if nodoAux == self.inicio:

						#Si existe un nodo siguiente
						if nodoAux.getSiguiente() != None:

							self.inicio = nodoAux.getSiguiente()

							nodoAux.getSiguiente().setAnterior(None)
							self.tamanio = self.tamanio - 1

							break

						#Si es el unico nodo en la lista
						else:
							self.inicio = None
							self.fin = None
							self.tamanio = 0

							break
					#Si es el ultimo nodo en la lista
					elif nodoAux == self.fin:

						#Si existe un nodo anterior (no es el unico nodo en la lista)
						if nodoAux.getAnterior() != None:
							self.fin = nodoAux.getAnterior()
							nodoAux.getAnterior().setSiguiente(None)
							self.tamanio = self.tamanio - 1
							break
						#Si no existe un nodo anterior
						else:
							self.inicio = None
							self.fin = None
							self.tamanio = 0
							break
					#Si no es ni el primero ni el ultimo
					else:
						nodoAux.getAnterior().setSiguiente(nodoAux.getSiguiente())
						nodoAux.getSiguiente().setAnterior(nodoAux.getAnterior())
						self.tamanio=self.tamanio - 1
						break
				else:
					nodoAux = nodoAux.getSiguiente()