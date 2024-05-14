from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la vista de publicación
@app.route('/post_view')
def post_view():
    return render_template('post_view.html')

if __name__ == '__main__':
    app.run(debug=True)