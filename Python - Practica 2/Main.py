#Clase principal para la practica 2 del curso Estructuras De Datos
#Creado por Osmel David Tortola Tistoj, Carne: 201404218

import ListaSimple 
import MatrizDispersa
import Pila
import Cola

from flask import Flask, request, Response
app = Flask("Practica2s1_201404218")

lista1 = ListaSimple
lista = lista1.ListaSimple()

pila1 = Pila
pila = pila1.Pila()

cola1 = Cola
cola = cola1.Cola()

matriz1 = MatrizDispersa
matriz = matriz1.MatrizDispersa()

@app.route('/listaSimple', methods = ['POST']) 
def mListaSimple():
	if str(request.form['tipo'])=="agregar":
		lista.add(str(request.form['informacion']))
		lista.graficarLista()

	elif str(request.form['tipo'])=="borrar":
		indice = int(request.form['informacion'])
		lista.borrar(indice)
		lista.graficarLista()

	elif str(request.form['tipo'])=="buscar":
		return str(lista.buscar(str(request.form['informacion']))) 
		
@app.route('/cola', methods = ['POST']) 
def mCola():
	if str(request.form['tipo'])=="queue":
		cola.queue(str(request.form['informacion']))
		cola.graficarCola()

	elif str(request.form['tipo'])=="dequeue":
		temp = cola.dequeue()
		cola.graficarCola()
		return temp

@app.route('/pila', methods = ['POST']) 
def mPila():
	if str(request.form['tipo'])=="push":
		pila.push(str(request.form['informacion']))
		pila.graficarPila()

	elif str(request.form['tipo'])=="pop":
		temp = pila.pop()
		pila.graficarPila()
		return temp

@app.route('/matrizDispersa', methods = ['POST']) 
def mMatrizD():
	if str(request.form['tipo'])=="agregar":
		matriz.add(str(request.form['informacion']))
		matriz.graficarMatriz()

	elif str(request.form['tipo'])=="borrar":
	
		matriz.borrar(str(request.form['informacion']))
		matriz.graficarMatriz()

	elif str(request.form['tipo'])=="buscarDominio":
		
		return matriz.buscarDominio(str(request.form['informacion']))
	elif str(request.form['tipo'])=="buscarLetra":
		
		return matriz.buscarLetra(str(request.form['informacion']))

if __name__ == "__main__":
 app.run(debug=True, host='0.0.0.0')