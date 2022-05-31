Para crear un entorno virtual
en python es decir como un proyecto en java
separado tenemos
py -3 -m venv <nombre>

Una vez creado se nos genera un entorni
de trabajo vacio virgen donde podemos
instalar todas las librerias que nosotros queremos

Para que el cmd de windows
se nos posicione dodne nosotrs queremos ejecutar
los comandos del proyecto necesitamos la ruta
venv\Scripts\activate.bat

Para hacer la instalacion de FastAPI
utilizamos el comando
pip install "fastapi[all]"

Si queremos ver todo lo que hemos instalado en la carpeta
de la libreria de nuestor proyecto
lo que tenemos que hacer es ejecutar en la consola
del entorno virtual que recordemos que lleva una (venv) a la
izquierda
pip freeze

#Pasos que seguimos en el codigo de main.py

1 - Para importar todo lo que es la api
utilizamos la conocida forma
de form desd ela libreria que queremos
import todas esas librerias de la libreria

2- Creamos el tipico objeto al que llamaremos app
El objeto app contiene una superclase que pertenece
a FastAPI

3- COjeremos la ruta absoluta
y como ya conocemos mediante los protocolos
de http
lo que le diremos es el tipico HEllo
world de las apis
donde retornaremos el Hello World

Para levantar el servidor hay que correr
un comando que pertenece a los paquetes
que nos hemos instalado a la libreria uvicorn
donde con un comando en la consola correremos el servidor
uvicorn main:app
O por si se ha producido algun cambio en el codigo o en alguna funcionalidad
hay que ejecutar en la consola que a su izquierda
este situada en el entorno virtual con (venv) con el comando
uvicorn main:app --reload, en windows vale con el --reload
este te monitoriza el codigo en tiempo real por si tienes que hacer algun cambio

Donde main es el archivo en python que funciona como putno de entrada, mientras que app
funciona como ese objeto que mos creamos con todas las propiedades de FastAPI con su conjunto
de librerias

#Hello world de la api

En cuanto a la funcion su nombre es anecdotico
la palabra reservada async como en javascript hace referencia a una funcion
que va a tener un cierto retardo en su ejecucion es decir se ejecuta mas tarde que una funcion
por ejemplo para cosas como para conectarse a una base de datos u ese tipo de operaciones
que requieren una respuesta por parte del servidor y que conllevan un tiempo de espera

Como hemos comprobado el nombre de la funcion es anecdotico
y nos retorna el mensaje sin problemas por lo que la hemos llamado como seria
mas logico Hello World APi y es una llamada de tipo GET por lo qye hace precisamnete
el servidor que somos nostros es MANDAR UNA PETICION PARA OBTENER CIERTA INFORMACIÓN

Como hemos podido comprobar si le quitamos la palabra reservada async no afecta te sigue corriendo lo que es la api es decir la llamada con el mensaje que nos tiene que devolver

Otra comprobacion que queremos hacer es si podemos retornar todo tipo de datos
como hemos comporbado si que puede devolver todo tipo de datos

Importanto en cuanto a la funcion despues de la linea @app.get("/")

- Es una funcion normal de python
- Puede contener cualquier logica dentro
- Al ser de tipo get
- Todo lo que vaya al return es lo que se va a enviar al servidor y lo que va a poder consultar el usuario

Es decir en esta funcion async def HelloWorldAPI():
return [("Pelota", True, 4)]

- Es el primer GET
- Va a devolver al suario el return
- puede no necesariamente contener la palabra reservada async
- Todo ese return lo que va ha hacer la api es automaticamente convertirlo en un JSON

@app.get("/") Esta linea es fundamental y es lo que lo convierte en api
porque si no la funcion a continuación no tendría sentido y no funcionaria

- @ es parte de la sintaxis hay que aprenderselo si no no hace el proceso de la API
- app es el objeto que pertenece a FastAPI que es la libreria que instanciamos y lo creamos de la siguiente manera app = FastAPI()
- El .get es un metodo HTTP y es el que utiliza el servidor para mandar los datos al servidro y poder ,ostrarselos al usuario
- "/" es la ruta que tiene que seguir que en este caso es la absoluta la de todo el proyecto pero es la ruta donde esta ubicada nuestro servidor que es en local es como decirle que de donde nos tiene que obtener la información es de nuestro servidor local que esta representada por esta ip http://127.0.0.1:8000

Por ejemplo si hacemos la prueba y le cambiamos la ruta @app.get("/login") si accedemos solo por asi decirlo a nuestra ruta del servidor que es nuestra ip porque esta en local que seria esta http://127.0.0.1:8000/ con el slash o sin el ambas valen pero por eso le tenemos que indicar el camino al metodo get y ponerle el slash para que sepa donde tiene que ir con el /login si accedemos a nuestro servidor nuestra ip en local nos va ha decir que no hay datos es decir todo lo que le enviamos en el return
ya no esta

CTRL + C para cerrar el servidor

Importabte como funciona FastAPI es que buscar la primera coincidencia en cuanto al path
o ruta de las sentencias de estilo @app.get("/") donde encontrara la primera coincidencia
de los que esta entre comillas que es el path y ejecutara tan solo el codigo que esta en la funcion
de esa coincidencia

Es decir lo que hace la API en concreto FastAPI() es solicitar un get methos busca todos los que haya
GET request method url: "/"
primero todos los que ocntengan el metodo get en el codigo una vez encontrada la primera coincidencia
valora la url y ejecuta el codigo

#Recuperar datos con la peticion POST del metodo de HTTP del servidor

- Poner el metodo en post de la linea @app.post("/createpost")
- En la funcion de cabecera pasarle un argumento para que se almacene la información pasada
- def create_post(body): como vemos de argumento tiene el body pero es lo que el usuario envia
  return {"message": "post creado con exito"}, el return es siempre como en una peticion get lo que el servidro recibe y te envia pero de forma que solo el programador lo hace por tanto hay un doble envio por un lado lo que pueda introducir el usuario y lo que tu como programador quieres que te devuleva el servidor con el return para mostrarlo o hacer cualquier cosa con el

def create_post(body : dict = Body(...)):

Lo que le estamos diciendo es que en esa petición POST dodne toda la información
esta en el Body de esa clase que me lo pase a un diccionario de python que se hace con la clase dict y que te lo genera vacio que es la siguiente linea a la izquierda y que me lo guarde en la variable que se va a llamar body que seria la clave y el dict su valor que sera un diccionario en python que contendra todos los datos de la peticion POST y los tres puntos porque no sabes el nuemro determinado de caracteres que va a ocupar body es decir que seran enviados pro el usuario.

Por eso cuando llamamos a body que es la clave nos inprime los valores alamacenados de dict

pydentic es uan libreria que tiene FIrstAPi que sirve
para cuando nostros hacemos una petición POST que es un metodo del protocolo HTTP
lo que sirve es para que mandemos los datos de la forma en el que el desarrollador
de la API quiere es decir prepara al frontend para decirle al usuario que tipo de entrada
queremos que haga exactamente

TRas esto crearemos una clas en nuestro
programa de Python que se va a llamar
Post que es donde se le va a decir
que tipo de entrada va a poder
Meter el usuario

En el metodo de crear el post lo qeu estamos haciendo es decirle me vas a guardar lo que te pase
el usuario en la clase Post que esta parametrizada de acuerdo al patron de inserccion
de dato que queremos que meta el usuario

#Metodo pytdentic

Pydentic tiene un metodo que se llama dict() por el cual todo los datos enviados
te los pasa a un diccionario de python por lo que asi seria mas facil para tratarlos con una logica

Para obtener los elementos de forma real lo que hariamos
seria guardar la peticion post que ha hehco el usuario y los datos que ha mandado
los guardariamos en una base de datos pero temporalmente
lo que vamos ha hacer es guardarlos en memeroia para recuperarlos con un get de peticion
con una ruta diferente pero para que podamos entender el proceso

Problema que nos hemos encontrado
El código que he escrito arriba, genera el mismo error. El problema está en que en python cuando defines (o sea asignas valor) una variable local (a la función foobar en este caso) con un mismo nombre que una variable preexistente en un ámbito superior, ésta última variable deja de existir dentro de la función. Por tanto, dentro de foobar "a" no existe antes de que hagas: hay que declarar la variable
con la palabra reservada delante global

Es lo que nos pasa al hacer un contador que se autoincremente
solo de los POST o datos que el usuario envia al servidor
que lo que queremos es que la id del elemento quimico que es un campo int en la API
se incremento de forma que cuando añadamos otro elemento este autoincrementado siguiendo un orden
para una posterior inserccion en una base de datos

Importante
@app.get("/obtenerelementos/{id}")
def get_elemento_quimico(id: int):
En esa funcion si queremos conusltar por el id La funcion tiene que tener como argumento exactamente
el mismo nombre que tiene entre los corchetes por lo que si no es asi nos dara un error de
que no puede encontrar lo que le estamos diciendo
Porque la explicacion es cuando nosotros le pasamos el id que lo declaramos la ruta en el get
la funcino lo que hace es guardar xactamente ese id que es el valor que se situa entre los corchetes
y con ese id podemos delvolver al usuario el elemento que quiere

Aunque tambien podria ser el identificador el simbolo quimico epro necesitariamos
una lista predefinida ocn todos ellos

(id: int): lo que hace esta parte es decirle pydemic que convierta automaticamente el dato
que recibe de la url mediante el protocolo de HTTP que lo convierta a un entero
para poder ser procesado pro la logica

Vamos a mandar repsuestas a los usuarios para que se les informe
de lo que estan haciendo mal

def get_elemento_quimico(id: int, response: Response): en este parametro de la funcion nos estamos guardando la respuesta que nos da el servidor por lo que si cumple una cierta condicion la desencadenamos la repsuesta que queremos en este caso es de recurso no encontrado 404 not found
con esta linea
if not elemento_seleccionado:
response.status_code = status.HTTP_404_NOT_FOUND
donde sin necesidad de sabenros el codigo de memoria con la libreria status le estamos diciendo que le saque al usuario status code 404 not found es decir introdujo mal el id

COmo hemos creado la carpeta de app ahora hay que cambiar la ruta donde ejecutamos el servidor
de la siguiente manera

uvicorn app.main:app --reload para que no tengamos que estar reiniciandolo todo el rato

Una palabra reservada bastante clave es
SELECT \* FROM products ORDER BY id LIMIT 5 OFFSET 2;
El OFFSET lo que hace es que descarta los dos primeros resultados

INSERT INTO tabla VALUES () () () returning con toda la id para que te devuelva toda la consulta
es decir con el returning te decuelve el campo que tu quieras

DELETE FROM la tabla que quieres elminar WHERE id SE PUEDE USAR LA CLAUSULA RETURNING EN TODAS LAS CONULTAS DE ESTE ESTILO IMAGINO QUE EN LA DE MODIFICACION TAMBIEN de la fila con el id que quieres borrar

No se porque razon la libreria de psycopg al buscar una tabla que tiene caracteres en mayusculas
no lo coje sin embargos cambiando los caracteres si que te deja y extrae perfectamente los datos
y funciona todo correctamente

Segunda forma y sintaxis interesante la \_ en python siginifica y se utiliza para
los bucles que es una variable no definida es decir que no queremos hacer nada
con ella que no guardara ningun valor y se puede utilizar como veremos en el bucle
for

In PostgreSQL unquoted names are case-insensitive. Thus SELECT _ FROM hello and SELECT _ FROM HELLO are equivalent.

However, quoted names are case-sensitive. SELECT _ FROM "hello" is not equivalent to SELECT _ FROM "HELLO".

To make a "bridge" between quoted names and unquoted names, unquoted names are implicitly lowercased, thus hello, HELLO and HeLLo are equivalent to "hello", but not to "HELLO" or "HeLLo" (OOPS!).

Thus, when creating entities (tables, views, procedures, etc) in PostgreSQL, you should specify them either unquoted, or quoted-but-lowercased.
