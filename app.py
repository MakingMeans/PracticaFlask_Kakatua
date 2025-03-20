from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta adicional
@app.route('/about')
def about():
    return "Página de información"

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
