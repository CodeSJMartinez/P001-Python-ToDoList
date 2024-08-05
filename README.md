# Presentación del Proyecto
## Propósito del Proyecto:

Vamos a crear una aplicación web simple que sirva como lista de tareas o to-do list. La aplicación permitirá a los usuarios agregar, eliminar y ver tareas. El propósito principal de esta aplicación es ayudar a los usuarios a organizar su trabajo o actividades diarias de manera sencilla y eficiente.

## Por qué crearlo:

Decidí crear este proyecto porque la organización personal es un desafío común, y tener una herramienta simple que te ayude a recordar y priorizar tareas puede ser muy útil. Además, desarrollar una aplicación web como esta es un excelente ejercicio para aprender los conceptos básicos de programación web, manejo de datos y despliegue en la nube.

## Conceptos Básicos
### Conceptos de Python Utilizados:

*Flask:* Flask es un marco de desarrollo web para Python. Piensa en Flask como el esqueleto de nuestra aplicación. Nos proporciona las herramientas necesarias para manejar peticiones y respuestas web, como las puertas y pasillos que permiten a los visitantes entrar y moverse dentro de un edificio.

*Listas y Diccionarios:* En Python, una lista es como una lista de compras donde almacenas elementos en orden. Un diccionario es como un libro de contactos, donde cada nombre tiene un número asociado.

*Funciones:* Las funciones son como recetas en un libro de cocina. Te dicen cómo realizar una tarea específica cuando las llamas.

*Variables:* Las variables son cajas donde guardas información que necesitas usar más tarde. Por ejemplo, puedes tener una variable llamada tarea que guarde la descripción de una tarea.

## Proceso de Desarrollo
### Paso 1: Configuración del Entorno

Primero, necesitamos configurar nuestro entorno de desarrollo. Esto implica instalar Python y Flask en nuestra computadora.

Instalación de Python: Si no lo tienes instalado, descárgalo e instálalo desde python.org.

Instalación de Flask: Abre la terminal o línea de comandos y ejecuta pip install flask. Esto instala Flask en tu sistema.

### Paso 2: Crear la Estructura del Proyecto

Crea una carpeta para tu proyecto y dentro de ella, crea un archivo llamado app.py. Este archivo será el corazón de nuestra aplicación.

### Paso 3: Configurar Flask

Dentro de app.py, configuramos nuestra aplicación Flask:

```python
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
```

Explicación del Código:

*from flask import Flask, request, render_template, redirect:* Importamos las herramientas de Flask necesarias para nuestra aplicación.

*app = Flask(__name__):* Creamos una instancia de nuestra aplicación Flask.

*tareas = []:* Creamos una lista vacía para almacenar las tareas.

Las funciones index, add_tarea, y delete_tarea definen cómo nuestra aplicación responderá a diferentes acciones de los usuarios.

### Paso 4: Crear la Interfaz de Usuario

Crea una carpeta llamada templates dentro de tu proyecto y añade un archivo index.html. Este archivo definirá cómo se verá nuestra aplicación en el navegador.


```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Tareas</title>
</head>
<body>
    <h1>Mi Lista de Tareas</h1>
    <form action="/add" method="post">
        <input type="text" name="tarea" placeholder="Nueva tarea">
        <button type="submit">Añadir</button>
    </form>
    <ul>
        {% for tarea in tareas %}
            <li>{{ tarea }} <a href="/delete/{{ loop.index0 }}">Eliminar</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Paso 5: Ejecutar la Aplicación Localmente

Para ver cómo funciona nuestra aplicación, abre la terminal, navega a la carpeta de tu proyecto y ejecuta python app.py. Luego, abre tu navegador y ve a http://127.0.0.1:5000 para ver tu lista de tareas en acción.

### Paso 6: Despliegue en la Nube

Una vez que nuestra aplicación funciona localmente, podemos desplegarla en la nube para que esté disponible en cualquier parte. Utilizaremos un servicio como Heroku para hacer esto.

Configurar Heroku: Regístrate y crea una nueva aplicación en el panel de Heroku.
Instalar Heroku CLI: Sigue las instrucciones de instalación en devcenter.heroku.com/articles/heroku-cli.
Subir la Aplicación: Desde la terminal, ejecuta los comandos:

```bash
heroku login
git init
heroku git:remote -a tu-nombre-de-aplicacion
git add .
git commit -m "Primer despliegue"
git push heroku master
```

## Resultados y Uso
### Funcionamiento del Proyecto:

Una vez terminado, el proyecto permite a los usuarios:

Añadir Tareas: Escribir una tarea en el campo de texto y hacer clic en "Añadir".
Ver Tareas: Todas las tareas se listan debajo del formulario.
Eliminar Tareas: Hacer clic en "Eliminar" junto a cualquier tarea para quitarla de la lista.
Ejemplo Práctico:

Imagina que necesitas organizar tu día. Abres la aplicación, escribes "Comprar pan", "Llamar al dentista", y "Estudiar Python" en la lista. A medida que completas cada tarea, haces clic en "Eliminar" para mantener la lista actualizada.

## Conclusión

### Aprendizajes Clave:

Manejo de Datos: Aprendimos cómo manejar y modificar listas en Python.
Interacción Usuario-Servidor: Entendimos cómo Flask facilita la comunicación entre el navegador y el servidor.

### Mejoras Potenciales:

Autenticación de Usuario: Agregar funcionalidad para que cada usuario tenga su propia lista de tareas.
Base de Datos: Usar una base de datos para almacenar tareas de forma persistente.
Interfaz Mejorada: Mejorar la interfaz con CSS y JavaScript para una experiencia de usuario más atractiva.
Este proyecto es una excelente manera de comenzar a desarrollar aplicaciones web usando Python y Flask, y con cada paso, hemos aprendido algo nuevo sobre cómo funcionan las aplicaciones web. ¡Espero que te animes a seguir explorando y mejorando este proyecto!
