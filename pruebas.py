Lista_a_descomponer = "Temperaturas de 4000 ºC a -252 ºC"

# Numeros
numericos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Signos
simbolos_operativos = ["+", "-", "/", "*"]

Lista_Temperaturas_Estado_Gaseoso = []

Lista_Nueva = ['4', '0', '0', '0', '-', '2', '5', '2']

tempera_mas_alta_gas = ""

tempera_mas_baja_gas = ""


def pruebas_descomponer():
    for cadaletra in Lista_a_descomponer:
        for nume in numericos:
            if cadaletra == nume:
                Lista_Temperaturas_Estado_Gaseoso.append(cadaletra)
                break
        for sim in simbolos_operativos:
            if cadaletra == sim:
                Lista_Temperaturas_Estado_Gaseoso.append(cadaletra)
                break
    return Lista_Temperaturas_Estado_Gaseoso


def prueba_decomposision_parte():
    global tempera_mas_alta_gas
    global tempera_mas_baja_gas
    for num in range(len(Lista_Nueva)):
        if Lista_Nueva[num-1] == "-":
            tempera_mas_baja_gas += Lista_Nueva[num]
        elif Lista_Nueva[num] != "4":
            print(Lista_Nueva[num] != "4")
            tempera_mas_baja_gas += Lista_Nueva[num]


prueba_decomposision_parte()

#guarda = pruebas_descomponer()

tempera_mas_alta_gas = ""

tempera_mas_baja_gas = ""

'''for cifras in range(len(Lista_Nueva)):
    if Lista_Nueva[cifras+1] == "-":
        tempera_mas_alta_gas += Lista_Nueva[cifras]
    else:
        for restantes in range(len(Lista_Nueva)):
            if Lista_Nueva[restantes] == "-":
                break
            elif Lista_Nueva[restantes-1] == "-":
                tempera_mas_baja_gas += Lista_Nueva[restantes+1]
                break
            elif Lista_Nueva[cifras] != Lista_Nueva[restantes]:
                tempera_mas_baja_gas += Lista_Nueva[restantes]
                break
        tempera_mas_alta_gas += Lista_Nueva[cifras]'''


def prueba_decomposision_parte():
    for cifras in range(len(Lista_Nueva)):
        if Lista_Nueva[cifras+1] == "-":
            break
        else:
            tempera_mas_alta_gas += Lista_Nueva[cifras]
