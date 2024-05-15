from flask import Flask, render_template, json, url_for

app = Flask(__name__)

# Cargar datos del archivo JSON
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view_data')
def view_data():
    return render_template('view_data.html', data=data)

@app.route('/detail/<int:item_id>')
def detail(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    return render_template('detail.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)