import ListaSimple 
import ListaDoble
import MatrizDispersa


from flask import Flask, request, Response
app = Flask("Practica2")




lista1 = ListaSimple
lista = lista1.ListaSimple()

matrizD = MatrizDispersa
matriz1 = matrizD.MatrizDispersa()

matriz1.add("amy@1")
matriz1.add("ana@4")
matriz1.add("cici@2")
matriz1.add("beto@5")
matriz1.add("toro@2")
matriz1.add("triciclo@2")
matriz1.add("casa@9")
matriz1.add("comida@2")
matriz1.add("kaka@8")

matriz1.graficarMatriz()

@app.route('/listaSimple', methods = ['POST']) 
def hello():
	if str(request.form['tipo'])=="agregar":
		lista.add(str(request.form['informacion']))

	elif str(request.form['tipo'])=="borrar":
		indice = int(request.form['informacion'])
		lista.borrar(indice)

	elif str(request.form['tipo'])=="buscar":
		
		return str(lista.buscar(str(request.form['informacion']))) 

#if __name__ == "__main__":
 # app.run(debug=True, host='127.0.0.2')