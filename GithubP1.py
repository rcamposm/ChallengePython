******************* PARTE I *******************************
#Instalamos git en la terminal de VSC
$sudo apt-get install git -y

#Revisamos la versión del Git que hemos instalado
$git --version

# Podemos ver también un resumen de las principales funcionalidades de Git
$git

#Creamos una carpeta
$mkdir ChallengePython
#Accedemos a la carpeta
$cd ChallengePython/

******************* PARTE II *******************************

$git init //inicializar el repositorio

#Con el `$git init`  se crean dos áreas.
- Un área en memoria RAM llamada `Staging`
- Un área llamada repositorio `/.git/`

#Conectare a GitHub
#Configurar como variable global tu usuario
$git config --global user.name "rcamposm" //(nombre de github , sino tiene crear)
#Configurar como variable global tu correo
$git config --global user.email "raquelcamposm@gmail.com"

$git config --global color.ul true

$git config --list


******************* PARTE III *******************************
1. Nos logueamos a GitHub
2. Creamos un repositorio: "PythonChallenge"
    - Public Mode
    - Add a README File
    - Choose a license: MIT License

# En la consola del VSC luego de abrir la carpeta donde queremos guardar el proyecto
$git clone https://github.com/rcamposm/ChallengePython.git
******************* PARTE IV *******************************

#Lista el contenido~
$ls -ltr

$git status // visualizar cambios
# Los archivos que salen en rojo se encuentran en el Working Directory.
# Los archivos que salen en verde se encuentran en el Staging Area.

# Crear el archivo HelloPython.py con un print("Hola Immuners!)

$git status // visualizar cambios

#Con el git add  se pasa el archivo al staging área y espera que lo pases al repositorio o que lo remuevas con rm.
$git add HelloPython.py //Agregamos el archivo al repositorio

$git add . // Agregar los cambios de la carpeta en la que nos encontramos agregar todo

$git commit -m "First python program" HelloPython.py// Agregamos los cambios para el repositorio

$git log nombre_de_archivos.extensión //histórico de cambios con detalles
$git log HelloPython.py 

$git log #muestra el hostorial de los registros (Commits) del proyecto con sus respectivos autores, hora específica y descripciones.

$git show archivo.extensión //Muestra todos los cambios

******************* PARTE V *******************************
#Subimos al repositorio Remoto
$ git push -u origin main
   Username raquelcamposm@gmail.com
   pass:
# Got push envía los commits al repositorio remoto de GitHub

#Verificamos que los archivos se hayan subido al  repositorio remoto (GitHub)

$ git push //envia a otro repositorio remoto lo que estamos haciendo
$ git pull //traer repositorio remoto


******************* PARTE VI *******************************
#git branch + name: Crear una rama.
#git branch: Lista de ramas y saber en que ramas estamos.
#git checkout + branch: Para movernos entre ramas.


#Para verificar donde estamos posicionados
$ git log --oneline
$ git branch

#Para crear una rama
$ git branch ramaParrafo

# Modificamos el archivo HelloPython.py --> print("Hola Immuners! hoy estamos 22/11")

$git add HelloPython.py //Agregamos el archivo al repositorio

$git commit -m "Actualizamos el párrafo" HelloPython.py// Agregamos los cambios para el repositorio

#Luego nos movemos a la rama master para poder copiar los cambios de la rama al master
$ git checkout main
   
#Agregamos los cambios de la rama al master
# Merge para fusionar las ramas
$ git merge ramaParrafo
 
#Subimos al repositorio remoto
$ git push

# Verificamos que el archivo HelloPython.py está actualizado también en el Github
******************* PARTE VII *******************************
# Subir la rama al repositorio remoto (GitHub)
$ git branch
$ git checkout ramaParrafo
$ git push
$ git push --set-upstream origin ramaParrafo

******************* MÁS ************************************
Git reset vs. Git rm
*********************************************************************************************


