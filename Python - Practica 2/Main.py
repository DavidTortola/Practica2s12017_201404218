import ListaSimple 
import ListaDoble
import MatrizDispersa


from flask import Flask, request, Response
app = Flask("Practica2")




lista1 = ListaSimple
lista = lista1.ListaSimple()

matrizD = MatrizDispersa
matriz1 = matrizD.MatrizDispersa()



matriz1.insertar("a","gmail","andree")
matriz1.insertar("a","outlook","bruto")
matriz1.insertar("z","hotmail","asdfasfd")
matriz1.insertar("f","gmail","asdfasfd")
matriz1.insertar("g","hotmail","asdfasfd")
matriz1.insertar("y","gmail","asdfasfd")
matriz1.insertar("e","hotmail","asdfasfd")
matriz1.insertar("a","outlook","zebra")
matriz1.insertar("b","gmail","asdfasfd")



#matriz1.imprimirMatriz()

matriz1.listaLetras.listaPrint()
matriz1.listaDominios.listaPrint()


@app.route('/listaSimple', methods = ['POST']) 
def hello():
	if str(request.form['tipo'])=="agregar":
		lista.add(str(request.form['informacion']))

	elif str(request.form['tipo'])=="borrar":
		indice = int(request.form['informacion'])
		lista.borrar(indice)

	elif str(request.form['tipo'])=="buscar":
		
		return str(lista.buscar(str(request.form['informacion']))) 

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.2')