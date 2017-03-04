#Clase MatrizDispersa, que utiliza listas dobles como cabeceras

import ListaDoble
import NodoDoble
import ListaDobleL
import subprocess
nd = NodoDoble
ld = ListaDoble
ldl = ListaDobleL

class MatrizDispersa(object):

	def __init__(self):
		self.listaLetras = None
		self.listaDominios = None
		self.tamanio = 0

	def add(self,correo):
		valores = correo.split("@")
		valor = valores[0]
		dominio = valores[1]
		letra = valor[:1]

		self.insertar(letra,dominio,valor)
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


				#Se crean los apuntadores
				NodoAuxiliarLetra = self.listaLetras.buscar(letra)

				NodoAuxiliarLetra.setSiguiente(nodoNuevo)

				nodoNuevo.setAnterior(NodoAuxiliarLetra)

				#Se aumenta el tamanio de la matriz
				self.tamanio = self.tamanio + 1						

			#Si la letra ya existe y la cabecera dominio no
			elif self.listaLetras.buscar(letra) != None and self.listaDominios.buscar(dominio) == None:

				#Se agrega la cabecera a la lista
				self.listaDominios.add(dominio)

				#Se colocan los apuntadores horizontales (desde la cabecera letra)
				NodoAuxiliarLetra = self.listaLetras.buscar(letra)

				#Se crea el nodo a insertar en la matriz
				nodoNuevo = nd.NodoDoble(valor, letra, dominio)

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

				#Se crean los apuntadores
				NodoAuxiliarDominio = self.listaDominios.buscar(dominio)

				NodoAuxiliarDominio.setAbajo(nodoNuevo)
				nodoNuevo.setArriba(NodoAuxiliarDominio)

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

	def buscarMatch(self, letra, dominio):
		nodoAux = self.listaDominios.buscar(dominio)
		while nodoAux != None:
			if nodoAux.getLetra() == letra:
				return True
			else:
				nodoAux = nodoAux.getAbajo()
		return False

	def graficarMatriz(self):

		file=open("Graficas\MatrizDispersa.txt","w")
		file.write("digraph Matriz{ \n")

		auxDominio = self.listaDominios.inicio
		actual = auxDominio
		contador = 1

		file.write("i[style =\"filled\"; label=\" \";pos = \"0,0!\"] \n")

		#Se obtienen las cabeceras de dominio

		while auxDominio != None:
			file.write(actual.getValor()+"[style=\"filled\"; label=" +actual.getValor() +";pos=\""+str(contador)+",0!\"]\n")
			contador = contador+1

			auxDominio=auxDominio.getSiguiente()
			actual=auxDominio

		#Se obtienen las cabeceras de letra inicial
		contador=1

		auxLetra = self.listaLetras.inicio
		actual=auxLetra

		while auxLetra != None:
			file.write(actual.getValor()+"[style =\"filled\"; label="+actual.getValor()+";pos= \"0,"+str(contador)+"!\"]\n")
			contador=contador+1
			auxLetra = auxLetra.getAbajo()
			actual=auxLetra

		#Obtener los nodos
		auxDominio = self.listaDominios.inicio
		actual = auxDominio
		auxiliar = self.listaLetras.inicio

		while auxDominio != None:
			auxLetra = self.listaLetras.inicio
			while auxLetra != None :
				if actual.getAbajo() != None :
					actual = actual.getAbajo()
					file.write(actual.getValor()+"[style =\"filled\"; label="+actual.getValor()+";pos= \""+str(self.posX(auxDominio.getValor()))+","+str(self.posY(actual.getLetra()))+"!\"]\n")
				auxLetra = auxLetra.getAbajo()
			auxDominio=auxDominio.getSiguiente()
			actual = auxDominio

		#Se enlazan las cabeceras hacia la derecha
		auxDominio = self.listaDominios.inicio
		auxLetra = self.listaLetras.inicio

		file.write("\n i->"+auxDominio.getValor()+"->i->"+auxLetra.getValor()+"->i;\n")

		first = True
		actual = auxDominio
		while auxDominio!=None:
			if first==True:
				file.write(str(actual.getValor()))
				first=False
			else:
				file.write("->" +actual.getValor())

			auxDominio=auxDominio.getSiguiente()
			actual=auxDominio
		file.write(";")

		#Enlazar las cabeceras de letra inicial hacia abajo

		auxDominioFin = self.listaDominios.fin
		ultimo = True
		actual = auxDominioFin

		while auxDominioFin != None:
			
			if ultimo==True:
				file.write(str(actual.getValor()))
				ultimo=False
				
			else:
				file.write("->"+actual.getValor())

			auxDominioFin=auxDominioFin.getAnterior()
			actual=auxDominioFin

		file.write(";\n")

		#Enlzaca cabeceras hacia la izquierda

		primero=True
		actual=auxLetra
		while auxLetra!=None:
			if primero==True:
				file.write(str(actual.getValor()))
				primero=False
			else:
				file.write("->"+actual.getValor())
			auxLetra=auxLetra.getAbajo()
			actual=auxLetra
		file.write(";\n")

		#Enlazar cabeceras hacia arriba

		ultimo = True
		auxLetraFin = self.listaLetras.fin
		actual=auxLetraFin
		while auxLetraFin!=None:
			if ultimo == True:
				file.write(str(actual.getValor()))
				ultimo=False
			else:
				file.write("->"+actual.getValor())
			auxLetraFin=auxLetraFin.getArriba()
			actual=auxLetraFin
		file.write(";\n")


		#Enlazar los valores hacia la derecha

		auxDominio=self.listaDominios.inicio
		actual=auxDominio

		while auxDominio!= None:
			auxLetra= self.listaLetras.inicio
			file.write(auxDominio.getValor())
			while auxLetra!=None: 
				if actual.getAbajo()!=None:
					actual=actual.getAbajo() 
					file.write("->"+actual.getValor())
				auxLetra=auxLetra.getAbajo()
			file.write(";\n")
			auxDominio=auxDominio.getSiguiente() 
			actual=auxDominio
		file.write("\n\n")

		#Enlazar valores hacia abajo

		auxLetra=self.listaLetras.inicio
		actual=auxLetra
		while auxLetra!=None:
			auxDominio=self.listaDominios.inicio
			file.write(auxLetra.getValor())
			while auxDominio!=None:
				if actual.getSiguiente()!=None:
					actual=actual.getSiguiente()
					file.write("->"+actual.getValor())
				auxDominio=auxDominio.getSiguiente()
			file.write(";\n")
			auxLetra=auxLetra.getAbajo()
			actual=auxLetra
		file.write("\n\n")



		auxDominio=self.listaDominios.inicio
		auxiliar=auxDominio

		while auxDominio != None:

			while auxiliar.getAbajo()!=None:
				auxiliar=auxiliar.getAbajo()
			while auxiliar.getArriba()!=None:
				file.write(auxiliar.getValor()+"->")
				auxiliar=auxiliar.getArriba()
			
			file.write(auxDominio.getValor())
			file.write(";\n")
			auxDominio=auxDominio.getSiguiente()
			auxiliar=auxDominio

		auxLetra=self.listaLetras.inicio
		auxiliar=auxLetra

		while auxLetra!=None:
			while auxiliar.getSiguiente()!=None:
				auxiliar=auxiliar.getSiguiente()
			while auxiliar.getAnterior()!=None:
				file.write(auxiliar.getValor()+"->")
				auxiliar=auxiliar.getAnterior()
			file.write( auxLetra.getValor())
			file.write(";\n")
			auxLetra=auxLetra.getAbajo()
			auxiliar=auxLetra

		file.write("}")
		subprocess.Popen("fdp -Tpng Graficas\MatrizDispersa.txt -o Graficas\MatrizDispersa.png")

	def posX(self,nodo):
		x=1
		auxDominio=self.listaDominios.inicio

		while auxDominio != None:
			if auxDominio.getValor() == nodo:
				return x 
			else:
				x=x+1
				auxDominio=auxDominio.getSiguiente()

	def posY(self,nodo):
		y=1
		auxLetra = self.listaLetras.inicio
		while auxLetra!=None:
			if auxLetra.getValor()==nodo:
				return y
			else:
				y=y+1
				auxLetra=auxLetra.getAbajo()