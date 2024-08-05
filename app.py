from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Lista para almacenar tareas
tareas = []

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/add', methods=['POST'])
def add_tarea():
    tarea = request.form.get('tarea')
    tareas.append(tarea)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_tarea(index):
    tareas.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
