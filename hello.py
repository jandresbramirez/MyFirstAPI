from flask import Flask

app = Flask(__name__)

@app.route("/")

@app.route("/Espanol/")
@app.route("/Espanol/<nombre>")
def saludo_espanol(nombre = "andres"):
    return f"Hola mundo {nombre}"

@app.route("/Ingles/")
@app.route("/Ingles/<nombre>")
def saludo_ingles(nombre= "andres"):
    return f"Hola mundo {nombre}"

@app.route("/Frances/")
@app.route("/Frances/<nombre>")
def saludo_frances(nombre = "andres"):
    return f"Hola mundo {nombre}"

@app.route("/Portugues/")
@app.route("/Portugues/<nombre>")
def saludo_portugues(nombre = "andres"):
    return f"Hola mundo {nombre}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
    
    
    
    
    
