import ListaSimple 
import NodoListaSimple


from flask import Flask, request, Response
app = Flask("Practica2")


nodo = NodoListaSimple
nodo1 = nodo.NodoListaSimple("hola")
nodo2 = nodo.NodoListaSimple("adios")
print nodo1.getValor()
print nodo2.getValor()



lista1 = ListaSimple
lista = lista1.ListaSimple()
lista.add(1)
lista.add(2)
lista.add(3)
lista.listaPrint()

lista.add(4)







@app.route('/kateleen', methods = ['POST']) 
def hello():

	lista.add(str(request.form['dato']))

	return str(lista.inicio.getSiguiente().getSiguiente().getSiguiente().getSiguiente().getValor())

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.2')