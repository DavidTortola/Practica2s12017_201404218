import ListaSimple 
import ListaDoble
import MatrizDispersa


from flask import Flask, request, Response
app = Flask("Practica2")

lista1 = ListaSimple
lista = lista1.ListaSimple()

matrizD = MatrizDispersa
matriz1 = matrizD.MatrizDispersa()

@app.route('/listaSimple', methods = ['POST']) 
def hola():
	if str(request.form['tipo'])=="agregar":
		matriz1.add(str(request.form['informacion']))
		matriz1.graficarMatriz()

	elif str(request.form['tipo'])=="borrar":
		matriz1.borrar(str(request.form['informacion']))
		matriz1.graficarMatriz()

	elif str(request.form['tipo'])=="buscar":
		
		return str(lista.buscar(str(request.form['informacion']))) 


@app.route('/matrizDispersa', methods = ['POST']) 
def hello():
	if str(request.form['tipo'])=="agregar":
		lista.add(str(request.form['informacion']))

	elif str(request.form['tipo'])=="borrar":
		indice = int(request.form['informacion'])
		lista.borrar(indice)

	elif str(request.form['tipo'])=="buscar":
		
		return str(lista.buscar(str(request.form['informacion']))) 


if __name__ == "__main__":
 app.run(debug=True, host='0.0.0.0')