# Librerias que necesitamos
import threading
# Importamos la libreria de ThreadPoll
import concurrent.futures
# Libreria del tiempo
import time

# Medimos el tiempor pro el que empieza
start = time.perf_counter()

'''Vamos a probar a pasarle una funcion'''


def do_something(seconds, añadido):
    print(f"Sleeping {seconds + añadido} second...")
    time.sleep(seconds + añadido)
    return f"Done Sleeping...{seconds}"


'''Vamos a usar el Thread poll'''

with concurrent.futures.ThreadPoolExecutor() as executor:
    '''Tambien podemos pasar listas en el submit 
    y de igual manera en la porpia funcion dentro de los argumentos del submit'''
    secs = [5, 4, 3, 2, 1]
    a = [0]
    '''El metod submit llama a la funcion que le estamos pasado
    y como argumento tiene la funcion que le estamos pasando 
    que se llama do_something y los otros dos parametros que son
    los argumentos de la funcion pero en la funcion necesitamos hacer un return
    '''
    # Si queremos ahora ejecutar esto diez veces
    '''La pecularidad del map es que los elementos que le apsamos como argumento
    as su funcino son objetos iterables es decir valen variables convencionales
    tienen que ser estructuras de datos'''
    # Returns an iterator equivalent to map(fn, iter).
    mapeados = executor.map(do_something, secs, a)
    #sts = [executor.submit(do_something, sec, 0) for sec in secs]
    #results = [executor.submit(do_something, 1, 2) for _ in range(10)]
    '''Podemos guardarlo en una lista de sa forma tan curiosa como si fiera un elemento
    el submit que es como si fuera una tarea y lo que vamos a utilizar es una lista 
    convergente que basicamente es una lista con un elemento en el que podemos meter el bucle
    para recorrenos ese mismo elemento todas las veces que queramos supongo que esto
    es una modalidad de python es decir es una estructura y te permite utilizar bucles como
    se ve dentro de una lista'''
    '''for f in concurrent.futures.as_completed(results):
        print(f.result())'''
    # Se puede hacer tantos executor con listas comprimidas como quieras
    '''for s in concurrent.futures.as_completed(sts):
        print(s.result())'''
    # as completed An iterator over the given futures that yields each as it completes.
    # for mapas in mapeados:
    # print(mapas)
    '''Podemos ejecutar todos los submits que queramos'''
    # Return the result of the call that the future represents que en nuestro caso el future es funcion1
    # print(funcion1.result())
    '''Y hay que hacer un print del otro'''
    # print(funcion2.result())
    '''Lo curioso es que el tiempo que tarda todo el programa estas funciones responde 
    a como si ejecutara una sola funcion es decir si nuestra hipotesis es que se duplicase el
    tiempo a 6 segundos dado que estamos durmiendo el programa 6 segundos tan solo tarda 3 segundos
    bastante interesante y mucho mas facil el pool que en java'''
    '''Otra cosa a destacar es que el pool de Threads tiene automatica la rutina es decir 
    no tenemso necesidad de poenrle join hasta que no termina entera las tareas a ejecutar no se termina
    tampoco el hilo main'''


'''Aqui es cuando pasamos a crear los hilos que es tremendamente ams facil que java
dentro del Thread tenemos que pasar una serie de parametros el primero de ellos es
el target = funcion que queremos que ejecute ese hilo en concreto, como en java tenemso que coger
esos objetos que hemos creado y ejecutar con el metodo .start()
'''

#hilo1 = threading.Thread(target=do_something)
#hilo2 = threading.Thread(target=do_something)

# hilo1.start()
# hilo2.start()

'''Al igual que en java tenemos el metodo .join() que se ejecuta cada hilo 
y lo que hace igual que en java es esperar a que se termienen de ejecutar 
las instrucciones de cada hilo antes de que siga ejecutandose el hilo main
Wait until the thread terminates. tal como dice la descripcion del metodo
por lo que ahora si que podemos calcular con precision el tiempo que 
tarda en ejecutar el programa en concreto con los dos hilos secundarios y el main'''

# hilo1.join()
# hilo2.join()

'''Segunda forma y sintaxis interesante la _ en python siginifica y se utiliza para 
los bucles que es una variable no definida es decir que no queremos hacer nada
con ella que no guardara ningun valor y se puede utilizar como veremos en el bucle
for en combinacion con in range porque no queremos obtener los numeros sino simplemente crear
10 hilos'''

'''Como ya hemos hecho en java otras veces podemos crear una lista de hilos para hacer
una corrutina es decir que el hilo main no termine Wait until the thread terminates. hasta 
que todos los hilos hayan terminado sus sentencia asi ver el conteo
de tiempo y ver que tan eficiente es'''

# Creamos una lista en python de hilos
#threads = []

'''COn el argumento args=[] le pasamos los parametros a la funcion 
lo que nos permite añadir mas complejidad si cabe y mayor riqueza de pruebas
lo curioso de este argumento que podemos añadir a la funcion 
que se añade tanto a la funcion de python pasando como argumento como al objeto 
hilso y en el constrctor Thread es que es un Iterable es decir una lista que permite recorreserla
por lo que tiene sentido he incluso me atraveria a suponer que sigue el orden establecido de pasada
de parametros y efectivamente es asi el orden importa el primer elemento de nuestra lista del campo
args= del constrcutor Thread() es el primer argumento por orden que cogera nuestra funcion clasica 
de python con def'''

'''for _ in range(10):
    hilos = threading.Thread(target=do_something, args=[1.5, 2])
    hilos.start()
    threads.append(hilos)'''

# Establecemos la corrutina con el metodo join que su descripcion es Wait until the thread terminates.
# Para cada hilo

'''for hilo in threads:
    hilo.join()'''


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")
