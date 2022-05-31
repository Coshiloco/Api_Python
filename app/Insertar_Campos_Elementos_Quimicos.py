
'''Nos tenemos que crear la clase con los elementos 
quimicos para introducir a la tabla geenral'''

# Importamos la libreria del tiempo
import psycopg
# Importamos la libreria que me hace los hilos
import concurrent.futures
import threading


class elementos_quimicos():
    id = None
    nombre = None
    estado_fisico = None
    peso_atomico = None
    niveles_de_energia = None
    electro_negatividad = None
    punto_de_fusion = None
    punto_de_ebullicion = None
    afinidad_electronica = None
    energia_de_ionizacion = None
    radio = None
    dureza = None
    modulo = None
    densidad = None
    conductividad = None
    calor = None
    abundancia = None
    descubierto = None

    '''
    COnstructor 
    que nso eprmite almacenar
    todos los parametros 
    necesarios
    
    '''

    def __init__(self, id, nombre, estado_fisico, peso_atomico,
                 niveles_de_energia, electro_negatividad, punto_de_fision,
                 punto_de_ebullicion, afinidad_electronica, energia_de_ionizacion,
                 radio, dureza, modulo, densidad, conductividad, calor, abundancia,
                 descubierto):
        self.id = id
        self.nombre = nombre
        self.estado_fisico = estado_fisico
        self.peso_atomico = peso_atomico
        self.niveles_de_energia = niveles_de_energia
        self.electro_negatividad = electro_negatividad
        self.punto_de_fusion = punto_de_fision
        self.punto_de_ebullicion = punto_de_ebullicion
        self.afinidad_electronica = afinidad_electronica
        self.energia_de_ionizacion = energia_de_ionizacion
        self.radio = radio
        self.dureza = dureza
        self.modulo = modulo
        self.densidad = densidad
        self.conductividad = conductividad
        self.calor = calor
        self.abundancia = abundancia
        self.descubierto = descubierto
