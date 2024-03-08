#En esta linea importamos las librerias necesarias para 
from flask import Flask,jsonify 

app= Flask(__name__)

@app.route('/personas', methods=['GET'])
def index():
    lista_personas=[
	    {'nombre': 'Andres Lopez Ascanio'},
	    {'nombre': 'Juan Giraldo'},
	    {'nombre': 'Manuel Perez'},
	    {'nombre': 'Martha Ariza'},
	    {'nombre': 'Andres Lozano'},
	    {'nombre': 'Matin De la Rosa'},
	    {'nombre': 'Argelina Hoyos'},
	    {'nombre': 'Maria Martinez'},
	    {'nombre': 'Daniel Gonzales'},
	    {'nombre': 'Juancho Pelaez'}
    ]
    return jsonify(lista_personas)

if __name__ == '__main__':
     app.run(debug=True)