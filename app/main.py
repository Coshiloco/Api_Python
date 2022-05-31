from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
# Para asignar un id a los elementos quimicos
from random import randrange
# Importacion de la libreria de la abse de datos
# Importamos la libreria del tiempo
import psycopg
# Importamos la libreria que me hace los hilos
import concurrent.futures
import threading

app = FastAPI()

'''Crearemos una clase que
va a definir lo que puede introducir el
usuario'''


class Post(BaseModel):
    id_elemento_quimico: Optional[int]
    Nombre_Elemento_Quimico: str
    Estados_fisicos: dict
    Peso_Atomico: float
    Niveles_de_Energia: int
    Electronegatividad: float
    Punto_De_Fusion: float
    Punto_de_Ebullicion: float
    Afinidad_Electronica: float
    Energia_de_Ionizacion: dict
    Radio: dict
    Dureza: dict
    Modulo: dict
    Densidad: dict
    Conductividad: dict
    calor: dict
    Abundancia: dict
    Descubierto: int


'''Creamos la clase que nos permite meter los datos de los estados 
fisicos para meterlo en la otra tabla'''

# Vamos a guardar un abecedario
abecedario = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k",
              "l", "ñ", "z", "x", "c", "v", "b", "n", "m"]
abecedario_mayusculas = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                         "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ",
                         "Z", "X", "C", "V", "B", "N", "M"]
# Numeros
numericos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Signos
simbolos_operativos = ["+", "-", "/", "*"]


class EstadosFisicos():
    Temperatura_Mas_Alta = None
    Temperatura_Mas_Baja = None
    Estados = None

    # Constructor
    def __init__(self, temperatura_baja, temperatura_alta, estados):
        self.Temperatura_Mas_Alta = temperatura_alta
        self.Temperatura_Mas_Baja = temperatura_baja
        self.Estados = estados

# La clase de Energia de Ionizacion


class EnergiaIonizacion():
    ConUnSoloAtomo = None
    DeDosATreinta = None

    # COnstructor
    def __init__(self, soloatomo, dedosatreinta):
        self.ConUnSoloAtomo = soloatomo
        self.DeDosATreinta = dedosatreinta


# tabla del radio

class RadioTabla():
    calculated = None
    empirical = None
    covalent = None
    van_de_Waals = None

# tabla de dureza


class Dureza():
    Brinell = None
    Mohs = None
    Vickers = None

# tabla del modulo


class Modulo():
    bulk = None
    shear = None
    Young = None

# Tabla de densidad


class DensidadTabla():
    STP = None
    Liquido = None

# Tabla Conductividad


class Conductividad():
    thermal = None
    electric = None

# tabla calor


class Calor():
    specific = None
    vaporization = None
    fusion = None

# Tabla Abundancia


class Abundancia():
    universe = None
    solar = None
    meteor = None
    crust = None
    ocean = None
    human = None


'''Cremaos la funcion que nos permite obtener el diccionario y asi 
poder meter cada campo en la tabla'''

Lista_Texto_Temperaturas_Estado_Gaseoso = []
Lista_Texto_Temperaturas_Estado_Liquido = []
Lista_Texto_Temperaturas_Estado_Solido = []


Lista_Temperaturas_Estado_Gaseoso = []
Lista_Temperaturas_Estado_Liquido = []
Lista_Temperaturas_Estado_Solido = []

conversion_a_numero_tmp_alta = 0

conversion_anumero_tmp_baja = 0

valores_estados_fisicos_lista = []

llaves_estados_fisicos_lista = []

# Para hacer el String
tempera_mas_alta_gas = ""
# Para la temperatura mas baja
tempera_mas_baja_gas = ""
# Alta del liquido
tempera_mas_alta_liquido = ""
# Baja del liquido
tempera_mas_baja_liquido = ""
# Alta del solido
tempera_mas_alta_solido = ""
# Baja del solido
tempera_mas_baja_solido = ""

# Ahora hay que meter los estados fisicos es decir gas ,liquido y solido
Estados_Gas_Valor = ""
Estados_Liquido_Valor = ""
Estados_Solidos_Valor = ""


contador_ceros = 0

# Contador del simbolo menos
contador_simbolos = 0
'''Variable bandera para saber si la cifra de la temperatura es negativa '''
contador_negativos = 0


# Ahora tenemos que hacer la funcion que queremos que nos ejecute el hilo


def Insertar_estadps_Fisicos(tmp_baja_gas, tmp_alta_gas, tmp_baja_liquido, tmp_alta_liquido, tmp_baja_solido, tmp_alta_solido, Estado_Gaseoso, Estado_Liquido, Estado_Solido):
    with psycopg.connect("dbname=fastapi user=postgres password=PeneFlaciszon76") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO estados_fisicos (estado, temeperatura_mas_baja, temperatura_mas_alta) VALUES (%s, %s, %s)",
                (Estado_Gaseoso, tmp_baja_gas, tmp_alta_gas))
            cur.execute("SELECT * FROM estados_fisicos")
            consulta = cur.fetchall()
            print(consulta)


def Insertar_Campos_Tabla(postusuario):
    global Lista_Texto_Temperaturas_Estado_Gaseoso
    global Lista_Texto_Temperaturas_Estado_Liquido
    global Lista_Texto_Temperaturas_Estado_Solido
    global Lista_Temperaturas_Estado_Gaseoso
    global Lista_Temperaturas_Estado_Liquido
    global Lista_Temperaturas_Estado_Solido
    global valores_estados_fisicos_lista
    global llaves_estados_fisicos_lista
    global tempera_mas_alta_gas
    global tempera_mas_baja_gas
    global tempera_mas_alta_liquido
    global tempera_mas_baja_liquido
    global tempera_mas_alta_solido
    global tempera_mas_baja_solido
    global Estados_Gas_Valor
    global Estados_Liquido_Valor
    global Estados_Solidos_Valor
    for p in postusuario:
        if p["Estados_fisicos"]:
            values = p["Estados_fisicos"]
            valores_estados_fisicos = values.values()
            llaves_estados_fisicos = values.keys()
            for ele in llaves_estados_fisicos:
                llaves_estados_fisicos_lista.append(ele)
            for elem in valores_estados_fisicos:
                valores_estados_fisicos_lista.append(elem)
            for elemento in range(len(llaves_estados_fisicos_lista)):
                if elemento == 0:
                    Lista_Texto_Temperaturas_Estado_Gaseoso.append(
                        llaves_estados_fisicos_lista[elemento])
                elif elemento == 1:
                    Lista_Texto_Temperaturas_Estado_Liquido.append(
                        llaves_estados_fisicos_lista[elemento])
                elif elemento == 2:
                    Lista_Texto_Temperaturas_Estado_Solido.append(
                        llaves_estados_fisicos_lista[elemento])
            for cadauno in range(len(valores_estados_fisicos_lista)):
                if cadauno == 0:
                    Estados_Gas_Valor = valores_estados_fisicos_lista[cadauno]
                elif cadauno == 1:
                    Estados_Liquido_Valor = valores_estados_fisicos_lista[cadauno]
                elif cadauno == 2:
                    Estados_Solidos_Valor = valores_estados_fisicos_lista[cadauno]
            Descomponer_Temperaturas(Lista_Texto_Temperaturas_Estado_Gaseoso,
                                     Lista_Texto_Temperaturas_Estado_Liquido, Lista_Texto_Temperaturas_Estado_Solido)
            pasarlo_a_numero(Lista_Temperaturas_Estado_Gaseoso,
                             Lista_Temperaturas_Estado_Liquido, Lista_Temperaturas_Estado_Solido)
            print(Estados_Gas_Valor)
            print(Estados_Liquido_Valor)
            print(Estados_Solidos_Valor)
            # Funcion que descompone las temperaturas ()
            hilo_Estados_FIsicos = threading.Thread(target=Insertar_estadps_Fisicos, args=[tempera_mas_baja_gas, tempera_mas_alta_gas,
                                                                                           tempera_mas_baja_liquido, tempera_mas_alta_liquido,
                                                                                           tempera_mas_baja_solido, tempera_mas_alta_solido, Estados_Gas_Valor, Estados_Liquido_Valor,
                                                                                           Estados_Solidos_Valor])
            hilo_Estados_FIsicos.start()


''' Insertar_estadps_Fisicos(tempera_mas_baja_gas, tempera_mas_alta_gas,
                                     tempera_mas_baja_liquido, tempera_mas_alta_liquido,
                                     tempera_mas_baja_solido, tempera_mas_alta_solido, Estados_Gas_Valor, Estados_Liquido_Valor,
                                     Estados_Solidos_Valor)'''


def Descomponer_Temperaturas(Lista_texto_Gaseoso, Lista_texto_Liquido, Lista_texto_solido):
    global Lista_Temperaturas_Estado_Gaseoso
    global Lista_Temperaturas_Estado_Liquido
    global Lista_Temperaturas_Estado_Solido
    global numericos
    global simbolos_operativos
    global contador_ceros
    for cadaletra in Lista_texto_Gaseoso[0]:
        for nume in numericos:
            if cadaletra == nume:
                Lista_Temperaturas_Estado_Gaseoso.append(cadaletra)
                break
        for sim in simbolos_operativos:
            if cadaletra == sim:
                Lista_Temperaturas_Estado_Gaseoso.append(cadaletra)
                break
    for cadale in Lista_texto_Liquido[0]:
        for num in numericos:
            if cadale == num:
                Lista_Temperaturas_Estado_Liquido.append(cadale)
                break
        for si in simbolos_operativos:
            if cadale == si:
                Lista_Temperaturas_Estado_Liquido.append(cadale)
                break
    for letra in Lista_texto_solido[0]:
        for nm in numericos:
            if letra == nm:
                Lista_Temperaturas_Estado_Solido.append(letra)
                break
        for simbo in simbolos_operativos:
            if letra == simbo:
                Lista_Temperaturas_Estado_Solido.append(letra)
                break
    print(Lista_texto_Gaseoso)
    print(Lista_Temperaturas_Estado_Gaseoso)
    print(Lista_texto_Liquido)
    print(Lista_Temperaturas_Estado_Liquido)
    print(Lista_texto_solido)
    print(Lista_Temperaturas_Estado_Solido)


def pasarlo_a_numero(Gas, Liquido, Solido):
    global tempera_mas_alta_gas
    global tempera_mas_baja_gas
    global tempera_mas_alta_liquido
    global tempera_mas_baja_liquido
    global tempera_mas_alta_solido
    global tempera_mas_baja_solido
    global contador_simbolos
    for cifras in range(len(Gas)):
        if Gas[cifras+1] == "-":
            tempera_mas_alta_gas += Gas[cifras]
            break
        else:
            tempera_mas_alta_gas += Gas[cifras]
    for num in range(len(Gas)):
        if Gas[num-1] == "-":
            tempera_mas_baja_gas += Gas[num]
        elif not(Gas[num] == "4" or Gas[num] == "0"):
            tempera_mas_baja_gas += Gas[num]
    for liqui in range(len(Liquido)):
        if liqui == 0:
            tempera_mas_alta_liquido += Liquido[liqui]
        elif liqui <= 3:
            tempera_mas_alta_liquido += Liquido[liqui]
        elif liqui > 3:
            tempera_mas_baja_liquido += Liquido[liqui]
    for soli in range(len(Solido)):
        if soli == 0:
            tempera_mas_alta_solido += Solido[soli]
        elif soli <= 3:
            tempera_mas_alta_solido += Solido[soli]
        else:
            tempera_mas_baja_solido += Solido[soli]
    print(tempera_mas_alta_gas)
    print(tempera_mas_baja_gas)
    print(tempera_mas_alta_liquido)
    print(tempera_mas_baja_liquido)
    print(tempera_mas_alta_solido)
    print(tempera_mas_baja_solido)


'''No me hace fakta porque el break se queda en el punto
por tanto mal porque se quedaria en el menos aunque ya pasaria asi que si ahora
tiempo'''


@app.get("/")
async def HelloWorldAPI():
    return [("Pedrerol", True, 4)]

# Prueba con el metodo post

# ObtencionLementos

# Guardamos tenporalmente en memoria con una variable los elementos quimicos
alamacen_elementos_quimicos_temporal = []

# Para asiganr un id a los elementos quimicos
Conteo_elementos_quimicos = 0

# Funcion de buscar por el momento

'''Vamos a meter ya aqui la base de datos
con la libreria de psycopg3 que es para python y que se conecta
con POstesgrestSQL de la linea 58 a la 64 es como se conecta
lo metemos en un bucle infinito para que lo vargue hasta que la conexion
sea satisfactoria'''
# Connect to an existing database
with psycopg.connect("dbname=fastapi user=postgres password=PeneFlaciszon76") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        print("Conexion con la base de datos satisfactoria")
        cur.execute("SELECT * FROM elementos_quimicos")
        consulta = cur.fetchone()
        print(consulta)


def buscar_elementos_quimicos(id_elemento):
    for i in alamacen_elementos_quimicos_temporal:
        if (i["id_elemento_quimico"] == id_elemento):
            return i


# Buscar los indices por el post
'''Tenemos que hacer la funcion que nos eprmita buscar por el indice de toda la lista
no que nos devuelva el objeto en si que es lo que hacemos con el metodo de arriba
que nos devuelve el objeto y nosotros solo queremos los indices'''


def find_index_post(id):
    for i, p in enumerate(alamacen_elementos_quimicos_temporal):
        '''El enumerato lo que hace y por eso tenemos dos indices en el for
        es que va recorriendo todos los post en nuestra variable al almacen entonces
        nos devuleve dos cosas una el indice de ese elemento quimico y otra todo lo que son
        todos los valores del elemento quimico a nosotros lo que nos interesa es la i el indice'''
        if p["id_elemento_quimico"] == id:
            return i
            '''Lo que se recorre es cada elemento hasta que encuentre el que coincida con nuestra
            id una vez coincida el indice es decir un valro entero int lo devolvera en la variable
            i de index'''


@app.get("/obtenerelementos")
async def obtener_elementos():
    return {"Elemento de Nombre": alamacen_elementos_quimicos_temporal}

# Para pasarle un codigo de HTTP por ejemplo el de creado solo le tenemos que añadir otro argumento
# A la linea de post aparte de la ruta que se llama status code

# Para el administrador osea yo


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
async def create_post(new_post: Post):
    global Conteo_elementos_quimicos
    post_dict = new_post.dict()
    post_dict["id_elemento_quimico"] = Conteo_elementos_quimicos + 1
    Conteo_elementos_quimicos = post_dict["id_elemento_quimico"]
    alamacen_elementos_quimicos_temporal.append(post_dict)
    Insertar_Campos_Tabla(alamacen_elementos_quimicos_temporal)
    return {"data": post_dict}
# NombreElemento string, Estados fisicos String, Niveles de Energia int, etc

# Obtenemos el elemento quimico que queremos mediante el id en la delcaracion de la ruta


'''Ha este metodo de obetener un elemento que nosotros le digamos
tenemos que añadirle una respuesta personalizada al usuario
para que peuda saber que esta haciendo mal'''


@app.get("/obtenerelementos/{id}")
async def get_elemento_quimico(id: int, response: Response):
    print(id)
    elemento_seleccionado = buscar_elementos_quimicos(id)
    if not elemento_seleccionado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ha introducido una id de un elemento que no existe en la API")
        '''response.status_code = status.HTTP_404_NOT_FOUND
        # Para el informar al usuario mas claramente con un texto escrito por nosotros de lo que esta pasando
        return {"Detalles del error": "Ha introducido una id de un elemento que no existe en la API"}
        Vamos a lanzar una excepcion de manera mas eficiente'''
    return {"Elemento quimico seleccionado": elemento_seleccionado}

# Vamos a crear el metodo de la pai que te permite modficar elemento en este caso solo para el administrador


@app.put("/modificarelemento/{id}")
async def modificar_elemento(id: int, post: Post):
    indice_elmento = find_index_post(id)
    if indice_elmento == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Ha introducido una id de un elemento que no existe en la API")
    post_dict = post.dict()
    post_dict["id_elemento_quimico"] = id
    alamacen_elementos_quimicos_temporal[indice_elmento] = post_dict
    return {"Informacion servidor": post_dict}


'''En el metodo put hay dos parametros uno es el de la id del elemento quimico a maodificar
y el otro parametro es el nuevo elemento que nosotros introduciremos con la plantilla
y que vamos a modificar es decir el que sustituira al que originalmente etsaba que es 
lo que es una modificación'''
