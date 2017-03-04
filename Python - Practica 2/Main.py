import ListaSimple 
import ListaDoble
import MatrizDispersa


from flask import Flask, request, Response
app = Flask("Practica2")

lista1 = ListaSimple
lista = lista1.ListaSimple()

matrizD = MatrizDispersa
matriz1 = matrizD.MatrizDispersa()

matriz1.add("davidtortola_@hotmailcom")
matriz1.add("elefante@imagina")
matriz1.add("elemental@imagina")
matriz1.add("elemental2@imagina")
matriz1.add("jklef@kfej")
matriz1.add("julio@kfej")
matriz1.add("asdf@yahoo")

#matriz1.graficarMatriz()
matriz1.graficarMatriz()

matriz1.eliminar("a","yahoo","asdf")

@app.route('/listaSimple', methods = ['POST']) 
def hello():
	if str(request.form['tipo'])=="agregar":
		lista.add(str(request.form['informacion']))

	elif str(request.form['tipo'])=="borrar":
		indice = int(request.form['informacion'])
		lista.borrar(indice)

	elif str(request.form['tipo'])=="buscar":
		
		return str(lista.buscar(str(request.form['informacion']))) 

"""
if __name__ == "__main__":
 app.run(debug=True, host='127.0.0.2')

 """