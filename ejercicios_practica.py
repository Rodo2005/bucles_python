#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuante cuantos números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    # inicio = ....
    # fin = ....

    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla
    inicio = 0
    fin = 0
    ultimo = 0
    cantidad_numeros = 0
    sumatoria = 0
    inicio = int(input("Ingrese el primer número de la secuencia\n"))
    ultimo = int(input("Ingrese el último numero de la secuencia\n"))
    fin = ultimo + 1
    j = inicio
    for i in range(inicio, fin):
        if i < fin + 1:
             cantidad_numeros = cantidad_numeros + 1
             sumatoria = sumatoria + j
             j = j + 1
    print("La cantidad de números es : ", cantidad_numeros)
    print("La suma de todos los numeros de la secuencia es: ", sumatoria)





def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''

    calculadora = ""
    while calculadora != "Fin" :
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        print("Ingrese que operacion desea realizar: ")
        print("Ingrese 's' para suma, 'r' para resta, 'm' para multiplicacion")
        print("'d' para division, 'p' para potencia")

        operacion = str(input())

        if operacion == 's':
            suma = numero_1 + numero_2
            print("La suma es: ", suma)
            print("Si no desea realizar ninguna operación escribe Fin")
            print("Si desea realizar otra operación aprete enter")
            calculadora = str(input())
            if calculadora != "" and calculadora != "Fin":
                print("Error en el operador ingresado")
                break

        elif operacion == 'r':
            resta = numero_1 - numero_2
            print("La resta es: ", resta)
            print("Si no desea realizar ninguna operación escribe Fin")
            print("Si desea realizar otra operación aprete enter")
            calculadora = str(input())
            if calculadora != "" and calculadora != "Fin":
                print("Error en el operador ingresado")
                break
            else:
                continue
        elif operacion == 'm':
            multiplicacion = numero_1 * numero_2
            print("La multiplicacion es:", multiplicacion)
            print("Si no desea realizar ninguna operación escribe Fin")
            print("Si desea realizar otra operación aprete enter")
            calculadora = str(input())
            if calculadora != "" and calculadora != "Fin":
                print("Error en el operador ingresado")
                break
        elif operacion == 'd':
            division = numero_1 / numero_2
            print("La division es:", division)
            print("Si no desea realizar ninguna operación escribe Fin")
            print("Si desea realizar otra operación aprete enter")
            calculadora = str(input())
            if calculadora != "" and calculadora != "Fin":
                print("Error en el operador ingresado")
                break
        elif operacion == 'p':
            potencia = numero_1 ** numero_2
            print("La potencia es:", potencia)
            print("Si no desea realizar ninguna operación escribe Fin")
            print("Si desea realizar otra operación aprete enter")
            calculadora = str(input())
            if calculadora != "" and calculadora != "Fin":
                print("Error en el operador ingresado")
                break



def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla la cantidad de ausentes
    
    # numeros = [1, 5, -1, 6, 10, 2, -5]

    suma = 0   # Variable ya inicializada, la suma arranca en cero
    # numero = 0

    # Verifique la calificación de un estudiante según su
    # promedio en un examen
    i = 0
    largo = len(notas)
    while i < largo:
        nota = notas[i]
        if nota >= 0:
            suma = suma + nota
            cantidad_notas += 1
            promedio = suma / cantidad_notas
            i += 1
        else:
            cantidad_ausentes += 1
            i += 1
    print("Notas válidas:", cantidad_notas)
    print("Días ausente:", cantidad_ausentes)
    # Si el promedio es mayor o igual a 90 --> imprimir A
    # Si el promedio es mayor o igual a 80 --> imprimir B
    # Si el promedio es mayor o igual a 70 --> imprimir C
    # Si el promedio es mayor o igual a 60 --> imprimir D
    # Si el promedio es manor a  60      --> imprimir F
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados
    if promedio >= 90:
        print("Calificación: A /", promedio)
    elif promedio >= 80:   # "and promedio < 90:"  esta parte de la sentencia no es necesaria
        print("Calificación: B /", promedio)        # aunque no modifica el resultado. Termina siendo redundante.
    elif promedio >= 70 and promedio < 80:
        print("Calificación: C /", promedio)
    elif promedio >= 60 and promedio < 70:
        print("Calificación: D /", promedio)
    elif promedio > 0 and promedio < 60:
        print("Calificación: F /", promedio)
    

def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted
    '''
    temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......
    temperatura_len = len(temp_dataloger)
    i = 0
    j = 0
    suma = 0
    while i < temperatura_len:
        valor = temp_dataloger[i]
        suma = suma + valor
        j += 1
        temperatura_promedio = suma / j
        i += 1

    #temperatura_1 = 0.0
    #temperatura_2 = 0.0
    #temperatura_3 = 0.0
    
    #temperatura_1 = float(input("Ingrese un valor de temperatura:\n"))
    #temperatura_2 = float(input("Ingrese un nuevo valor de temperatura:\n"))
    #temperatura_3 = float(input("Ingrse un ultimo valor de temperatura:\n"))
    #promedio = float(temperatura_1 + temperatura_2 + temperatura_3) / 3
    #lista = [temperatura_1, temperatura_2, temperatura_3]
    #lista.sort()
    k = i - 1
    temp_dataloger.sort()
    temperatura_min = temp_dataloger[0]
    temperatura_max = temp_dataloger[k]
    print("")
    print("La temperatura máxima es: ", temperatura_max, "ºC")
    print("")
    print("La temperatura mínima es: ", temperatura_min, "ºC")
    print("")
    print("El promedio de la temperatura es: ", "{0:.2f}".format(temperatura_promedio), "ºC")
    print("")

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp
    temperatura_min = min(temp_dataloger)
    print("La temperatura mìnima es:", temperatura_min)
    print("")
    temperatura_max = max(temp_dataloger)
    print("La temperatura máxima es:", temperatura_max)
    print("")
    suma = sum(temp_dataloger)
    print("La temperatura suma es:", suma)
    print("")
    temperatura_promedio = suma / j
    print("El promedio de la temperatura es: ", "{0:.2f}".format(temperatura_promedio))
    print("")

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    if temperatura_min >= 19 and temperatura_max <= 28:
        print("Verano")
    if temperatura_min >= 11 and temperatura_max <= 24:
        print("Otoño")
    if temperatura_min >= 8 and temperatura_max <= 14:
        print("Invierno")
    if temperatura_min >= 10 and temperatura_max <= 24:
        print("Primavera")

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
