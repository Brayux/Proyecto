import random
import os
import time
from colorama import Fore, Style, init

# Inicializa colorama para que los colores se reinicien automáticamente después de cada uso
init(autoreset=True)

# Diccionario que almacenará las palabras que se colocan en la sopa de letras
palabras_colocadas = {}


# Diccionarios de palabras con su puntaje correspondiente, divididos por dificultad
dificil = {
    'PROGRAMACION': 95, 
    'PYTHON': 90, 
    'WHILE': 85, 
    'FOR': 80, 
    'IF': 75, 
    'PRINT': 70, 
    'INPUT': 70, 
    'PIP': 90, 
    'TRUE': 75, 
    'FALSE': 75, 
    'RANGE': 85, 
    'ELSE': 75, 
    'FUNCIONES': 100, 
    'MATRIZ': 95, 
    'STR': 70, 
    'ELIF': 75, 
    'LENGUAJES': 95, 
    'INTERPRETE': 95, 
    'COMPUTADOR': 90, 
    'CLASES': 100,
    'HERENCIA': 100,
    'POLIMORFISMO': 100,
    'ALGORITMOS': 95,
    'RECURSIVIDAD': 95,
    'MODULOS': 90,
    'DECORADORES': 100,
    'OPTIMIZACION': 98,
    'ASINCRONISMO': 95,
    'MULTITHREADING': 110,
    'PARALELISMO': 105,
    'PROGRAMACIONFUNCIONAL': 120,
    'ANALISISDECOMPLEJIDAD': 130,
    'ORIENTACIONAOBJETOS': 110,
    'MANEJODEEXCEPCIONES': 115,
    'SOBRECARGADEOPERADORES': 120,
    'OPTIMIZACIONDEALGORITMOS': 130,
    'PROGRAMACIONCONCURRENTE': 125
}

medio = {
    'PYTHON': 70, 
    'WHILE': 65, 
    'RANGE': 65, 
    'MATRIZ': 65, 
    'LENGUAJES': 70, 
    'FOR': 60, 
    'IF': 55, 
    'TRUE': 55, 
    'FALSE': 55, 
    'ELSE': 55, 
    'PRINT': 50, 
    'INPUT': 50, 
    'STR': 50, 
    'ELIF': 55,
    'DICCIONARIOS': 65,
    'LISTAS': 65,
    'TUPLAS': 70,
    'SETS': 70,
    'EXCEPCIONES': 70,
    'BUCLES': 65,
    'ARREGLOS': 70,
    'ARCHIVOS': 70,
    'OBJETOS': 75,
    'METODOS': 75,
    'ITERADORES': 80,
    'GENERADORES': 80,
    'INSTANCIAS': 78,
    'FUNCIONALIDAD': 85,
    'SOBRECARGA': 80
}

facil = {
    'FOR': 40, 
    'IF': 30, 
    'TRUE': 30, 
    'FALSE': 30, 
    'ELSE': 30, 
    'PRINT': 20, 
    'INPUT': 20, 
    'STR': 20, 
    'ELIF': 30,
    'SUMA': 15,
    'RESTAR': 15,
    'VALORES': 25,
    'TIPOS': 25,
    'NUMEROS': 25,
    'LISTA': 20,
    'SET': 10,
    'TEST': 10,
    'NUM': 10,
    'MAP': 10,
    'SUM': 15,
    'ADD': 10
}

# Diccionarios adicionales para personalización de palabras
lista_palabras_usuario = {}

lista_palabras_personalizada = {
    'COMENTARIOS': 10,
    'SET': 10,
    'TEST': 10,
    'NUM': 10,
    'MAP': 10,
    'ADD': 10,
    'SUM': 15,
    'SUMA': 15,
    'RESTAR': 15,
    'ASIGNACION': 20,
    'PRINT': 20,
    'INPUT': 20,
    'STR': 20,
    'LISTA': 20,
    'FOR': 40,
    'ELIF': 30,
    'IF': 30,
    'TRUE': 30,
    'FALSE': 30,
    'ELSE': 30,
    'TIPOS': 25,
    'VALORES': 25,
    'NUMEROS': 25,
    'FUNCIONES': 40,
    'PYTHON': 70,
    'WHILE': 65,
    'RANGE': 65,
    'MATRIZ': 65,
    'LENGUAJES': 70,
    'FOR': 60,
    'IF': 55,
    'TRUE': 55,
    'FALSE': 55,
    'ELSE': 55,
    'PRINT': 50,
    'INPUT': 50,
    'STR': 50,
    'DICCIONARIOS': 65,
    'LISTAS': 65,
    'TUPLAS': 70,
    'SETS': 70,
    'EXCEPCIONES': 70,
    'BUCLES': 65,
    'ARREGLOS': 70,
    'ARCHIVOS': 70,
    'OBJETOS': 75,
    'METODOS': 75,
    'ITERADORES': 80,
    'GENERADORES': 80,
    'INSTANCIAS': 78,
    'FUNCIONALIDAD': 85,
    'SOBRECARGA': 80,
    'PIP': 90,
    'LENGUAJES': 95,
    'MODULOS': 90,
    'ALGORITMOS': 95,
    'RECURSIVIDAD': 95,
    'CLASES': 100,
    'HERENCIA': 100,
    'DECORADORES': 100,
    'POLIMORFISMO': 100,
    'ASINCRONISMO': 95,
    'OPTIMIZACION': 98,
    'MULTITHREADING': 110,
    'PARALELISMO': 105,
    'PROGRAMACIONFUNCIONAL': 120,
    'ANALISISDECOMPLEJIDAD': 130,
    'ORIENTACIONAOBJETOS': 110,
    'MANEJODEEXCEPCIONES': 115,
    'SOBRECARGADEOPERADORES': 120,
    'OPTIMIZACIONDEALGORITMOS': 130,
    'PROGRAMACIONCONCURRENTE': 125
}
lista_palabras = {}
palabras_buscar = []
palabras_encontradas = {}

# Diccionario que representa las direcciones posibles para colocar palabras en la sopa de letras
rotaciones = {
    1 : (0,1),
    2 : (0,-1),
    3 : (1,0),
    4 : (-1,0),
    5 : (1,1),
    6 : (-1, -1),
    7 : (1, -1),
    8 : (-1, 1)
}

# Diccionario con multiplicadores de puntaje según la dificultad elegida
multiplicadores_dificultad = {
    'FACIL': 1,
    'MEDIO': 1.5,
    'DIFICIL': 2
}

rotaciones_posibles = []

# --- FUNCIONES DE CONFIGURACIÓN Y UTILIDAD ---

# Limpia la pantalla de la terminal
def limpiar_pantalla():
    os.system('cls')

# Función que configura las características del juego según la dificultad elegida
def configurar_dificultad(dificultad):
    if dificultad == 'FACIL':
        return 10, 10, 5, [(0,1), (1,0)], facil
    if dificultad == 'MEDIO':
        return 15, 15, 10, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1)], medio
    if dificultad == 'DIFICIL':
        return 30, 30, 15, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], dificil
    return
    

# Prioriza las palabras personalizadas del usuario sobre las palabras por defecto
def priorizar_lista_usuario(lista_palabras, lista_palabras_usuario):
    for palabra in lista_palabras_usuario:
        lista_palabras[palabra] = lista_palabras_usuario[palabra]
    return lista_palabras

# --- FUNCIONES RELACIONADAS CON LA SOPA DE LETRAS ---

# Genera una sopa de letras vacía
def generar_sopa_de_letras(filas, columnas):
    sopa_de_letras = {}
    for fila in range(filas):
        for columna in range(columnas):
            sopa_de_letras[(fila, columna)] = '-'  # Inicializa cada posición con un guion
    return sopa_de_letras

# Llena la sopa de letras con caracteres aleatorios en las posiciones vacías
def llenar_con_aleatorias(sopa_de_letras, filas, columnas):
    letras_posibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for fila in range(filas):
        for columna in range(columnas):
            if sopa_de_letras[(fila, columna)] == '-':
                sopa_de_letras[(fila, columna)] = random.choice(letras_posibles)

#Verifica si la palabra cabe en la sopa dependiendo de la dirección (rotación) que se utilice
def palabra_cabe_en_sopa(letras_palabra, filas, columnas, direccion_fila, direccion_columna):
    if direccion_fila == 0:
        return len(letras_palabra) <= columnas
    elif direccion_columna == 0:
        return len(letras_palabra) <= filas
    else:
        return len(letras_palabra) <= min(filas, columnas)

# Coloca las palabras en la sopa de letras en la dirección especificada , si no lo consigue intenta cambiar la rotacion
def colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas):
    if ''.join(letras_palabra) in palabras_colocadas:
        return False  # La palabra ya está colocada, no la agregues de nuevo
    while True:
        random.shuffle(rotaciones_posibles)
        for direccion_fila, direccion_columna in rotaciones_posibles:
            if not palabra_cabe_en_sopa(letras_palabra, filas, columnas, direccion_fila, direccion_columna):
                continue
            inicio_fila = random.randint(0, filas - 1)
            inicio_columna = random.randint(0, columnas - 1)
            if validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
                for posicion, letra in enumerate(letras_palabra):
                    nueva_fila = inicio_fila + posicion * direccion_fila
                    nueva_columna = inicio_columna + posicion * direccion_columna
                    reemplazar_letra(sopa_de_letras, nueva_fila, nueva_columna, letra)
                palabras_colocadas[''.join(letras_palabra)] = ((inicio_fila, inicio_columna), (direccion_fila, direccion_columna))
                return True
            
# Función que selecciona una palabra al azar de la lista de palabras, la separa en letras y la elimina de la lista
def escoger_separar_en_lista(letras_palabra):
    while True:
        palabra = random.choice(list(lista_palabras.keys()))
        if palabra not in palabras_colocadas:  # Verifica si la palabra ya ha sido colocada
            palabras_buscar.append(palabra)
            letras_palabra = list(palabra)
            del lista_palabras[palabra]
            return palabra, letras_palabra


# Valida si hay suficiente espacio para colocar una palabra
def validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
    contador = 0
    for letra in letras_palabra:
        nueva_fila = inicio_fila + contador * direccion_fila
        nueva_columna = inicio_columna + contador * direccion_columna
        if nueva_fila < 0 or nueva_fila >= filas or nueva_columna < 0 or nueva_columna >= columnas:
            return False
        if sopa_de_letras[(nueva_fila, nueva_columna)] != '-' and sopa_de_letras[(nueva_fila, nueva_columna)] != letra:
            return False
        contador += 1
    return True

# Imprime la sopa de letras de manera organizada
def imprimir_sopa_de_letras(sopa_de_letras, filas, columnas):
    print("   ", end='')
    for i in range(columnas):
        print(f" {i:02d} ", end=' ')
    print()
    print("   +" + "----+" * columnas)
    for fila in range(filas):
        print(f"{fila:02d} |", end=' ')
        for columna in range(columnas):
            letra = sopa_de_letras[(fila, columna)]
            print(f' {letra} |', end=' ')
        print()
        print("   +" + "----+" * columnas)

# Función para reemplazar una letra en la sopa de letras
def reemplazar_letra(sopa_de_letras, fila, columna, nueva_letra):
    sopa_de_letras[(fila, columna)] = nueva_letra.lower()

# Elimina palabras de la lista personalizada que exceden la longitud permitida
def eliminar_palabras_por_longitud(max_longitud, lista_palabras_personalizada):
    palabras_a_eliminar = [palabra for palabra in lista_palabras_personalizada if len(palabra) > max_longitud]
    for palabra in palabras_a_eliminar:
        if palabra in lista_palabras_personalizada:
            del lista_palabras_personalizada[palabra]

# Función que limpia la pantalla, resalta la palabra encontrada u omitida en la sopa de letras y la imprime actualizada
def imprimir_sopa_de_letras_coloreada_y_actualizar(sopa_de_letras, palabra, coordenadas, direccion, filas, columnas):
    limpiar_pantalla()
    fila_inicial, columna_inicial = coordenadas
    direccion_fila, direccion_columna = direccion
    for i in range(len(palabra)):
        fila_actual = fila_inicial + i * direccion_fila
        columna_actual = columna_inicial + i * direccion_columna
        if palabra in palabras_encontradas:
            if palabras_encontradas[palabra] == "encontrada":
                sopa_de_letras[(fila_actual, columna_actual)] = Fore.GREEN + sopa_de_letras[(fila_actual, columna_actual)] + Style.RESET_ALL
            else:
                sopa_de_letras[(fila_actual, columna_actual)] = Fore.RED + sopa_de_letras[(fila_actual, columna_actual)] + Style.RESET_ALL
    imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)
    mostrar_lista_palabras(palabras_buscar)

# --- FUNCIONES DE INTERACCIÓN DEL JUGADOR ---

# Función que pide al jugador las coordenadas para buscar una palabra en la sopa
def verificar_coordenadas(sopa_de_letras, palabra):
    while True:
        coords = input(f"Ingrese las coordenadas (fila, columna) para la palabra '{palabra}': ")
        try:
            fila, columna = map(int, coords.split(","))
            if (fila, columna) in sopa_de_letras:
                return fila, columna
            else:
                print("Coordenadas fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar dos números separados por una coma.")

# Muestra la lista de palabras, resaltando en verde las encontradas y en rojo las omitidas
def mostrar_lista_palabras(palabras_buscar):
    palabras_mostradas = []
    for palabra in palabras_buscar:
        if palabra in palabras_encontradas:
            if palabras_encontradas[palabra] == "encontrada":
                palabras_mostradas.append(Fore.GREEN + palabra + Style.RESET_ALL)
            else:
                palabras_mostradas.append(Fore.RED + palabra + Style.RESET_ALL)
        else:
            palabras_mostradas.append(palabra)
    print("\nPalabras a encontrar:", " ".join(palabras_mostradas))
    print()

# Muestra las instrucciones del juego
def mostrar_instrucciones():
    print("\nInstrucciones:")
    print("1. Tienes que encontrar las palabras ocultas en la sopa de letras.")
    print("2. Puedes ingresar manualmente las coordenadas para cada palabra o pedir que se resalte automáticamente.")
    print("3. Si fallas 3 veces en buscar una palabra, se te dará la opción de resaltarla automáticamente.")
    print("4. Cada vez que encuentres o resaltes una palabra, se limpiará la pantalla y se actualizará la sopa.")
    print("5. Puedes salir del juego en cualquier momento escribiendo 'salir'.\n")

# --- FUNCIONES DE PUNTUACIÓN Y VERIFICACIÓN ---

# Función que penaliza al jugador por errores cometidos
def penalizar_por_errores(intentos):
    if intentos == 1:
        return 10
    elif intentos == 2:
        return 20
    elif intentos >= 3:
        return 50  

# Calcula un bono adicional por el tamaño de la sopa de letras
def calcular_bono_tamano(filas, columnas, cantidad_palabras):
    return (filas * columnas) * (cantidad_palabras / 10)

# Verifica si todas las palabras han sido encontradas
def verificar_palabras_encontradas():
    for palabra in palabras_buscar:
        if palabra not in palabras_encontradas or palabras_encontradas[palabra] == "omitida":
            return False
    return True

# Calcula el puntaje final basado en la dificultad y tiempo transcurrido
def calcular_puntaje(dificultad, tiempo_transcurrido):
    if dificultad == 'DIFICIL':
        if tiempo_transcurrido < 3:
            return 1000, "Eres una bestia"
        elif 3 <= tiempo_transcurrido <= 5:
            return 500, "Buen trabajo"
        elif 5 < tiempo_transcurrido <= 8:
            return 250, "Puedes mejorar"
        else:
            return 100, "Te falta nivel"
    elif dificultad == 'MEDIO':
        if tiempo_transcurrido < 3:
            return 500, "Eres bueno, prueba la dificultad difícil"
        elif 3 <= tiempo_transcurrido <= 5:
            return 250, "Buen trabajo"
        elif 5 < tiempo_transcurrido <= 8:
            return 100, "Puedes mejorar"
        else:
            return 50, "Tienes que mejorar"
    elif dificultad == 'FACIL':
        if tiempo_transcurrido < 3:
            return 250, "Prueba la dificultad media"
        elif 3 <= tiempo_transcurrido <= 5:
            return 100, "Buen trabajo"
        elif 5 < tiempo_transcurrido <= 8:
            return 50, "Puedes mejorar"
        else:
            return 10, "Eres muy malo, dedícate a otra cosa"
        
if __name__ == "__main__":
    # Solicita al usuario si quiere una sopa de letras predefinida o personalizada
    personalizacion = input("¿Quiere jugar en una dificultad predefinida o desearía que la sopa de letras fuera personalizada bajo ciertos criterios? Responda con 'predefinida' o 'personalizada' según sea su caso: ").lower()

    if personalizacion == 'predefinida':
        print("Las dificultades disponibles son las siguientes: \n FACIL:\n - Sopa de letras de 10 X 10 \n - Solo orientaciones vertical y horizontal \n - Solo 5 palabras \n - Palabras cortas \n MEDIO: \n - Sopa de letras de 15 X 15 \n - Orientaciones verticales, horizontales y diagonales en una dirección \n - 10 palabras \n - Palabras de longitud moderada \n DIFICIL: \n - Sopa de letras 30 X 30 \n - Todas las orientaciones posibles \n - 15 palabras \n - Todo tipo de palabras")
        dificultad = input("Seleccione la dificultad bajo la cual le gustaría establecer la sopa de letras: ").upper()
        filas, columnas, cantidad_palabras_sopa, rotaciones_posibles, lista_palabras = configurar_dificultad(dificultad)

    elif personalizacion == 'personalizada':
        dificultad = input("¿Qué nivel de dificultad te gustaría asignar a la sopa personalizada (FACIL, MEDIO, DIFICIL)?: ").upper()
            # Solicitar al usuario las dimensiones de la sopa de letras personalizada
        cantidad_palabras_sopa = 0
        print("Ingrese el tamaño de la sopa de letras, debe ser mínimo de dimensiones 10 X 10 y máximo 30 X 30")
        filas = int(input("Ingrese el número de filas: "))
        while not (10 <= filas <= 30):
            print("El número de filas debe estar entre 10 y 30.")
            filas = int(input("Ingrese de nuevo el número de filas: "))

        columnas = int(input("Ingrese el número de columnas: "))
        while not (10 <= columnas <= 30):
            print("El número de columnas debe estar entre 10 y 30.")
            columnas = int(input("Ingrese de nuevo el número de columnas: "))

        # Solicita cuántas palabras quiere en la sopa de letras
        cantidad = int(input("¿Cuántas palabras quiere en la sopa? "))

        # Elimina palabras de mayor longitud según las dimensiones de la sopa
        if columnas == 10 or filas == 10:
            eliminar_palabras_por_longitud(10, lista_palabras_personalizada)
        elif columnas == 11 or filas == 11 or 10 < filas < 11 or 10 < columnas < 11:
            eliminar_palabras_por_longitud(11, lista_palabras_personalizada)
        elif columnas == 12 or filas == 12:
            eliminar_palabras_por_longitud(12, lista_palabras_personalizada)
        elif columnas == 13 or filas == 13:
            eliminar_palabras_por_longitud(13, lista_palabras_personalizada)
        elif columnas == 14 or filas == 14:
            eliminar_palabras_por_longitud(14, lista_palabras_personalizada)
        elif columnas == 15 or filas == 15:
            eliminar_palabras_por_longitud(15, lista_palabras_personalizada)
        elif columnas == 16 or filas == 16:
            eliminar_palabras_por_longitud(16, lista_palabras_personalizada)
        elif columnas == 17 or filas == 17:
            eliminar_palabras_por_longitud(17, lista_palabras_personalizada)
        elif columnas == 18 or filas == 18:
            eliminar_palabras_por_longitud(18, lista_palabras_personalizada)

        # Solicitar las rotaciones que el jugador desea usar
        print("¿Con cuáles rotaciones quiere jugar en la sopa? Las rotaciones posibles son: \n 1. Horizontal (izquierda-derecha) \n 2. Horizontal (derecha-izquierda) \n 3. Vertical (arriba-abajo) \n 4. Vertical (abajo-arriba) \n 5. Diagonal descendente (de arriba a la izquierda hacia abajo a la derecha) \n 6. Diagonal ascendente (de abajo a la derecha hacia arriba a la izquierda) \n 7. Diagonal descendente (de arriba a la derecha hacia abajo a la izquierda) \n 8. Diagonal ascendente (de abajo a la izquierda hacia arriba a la derecha) \n Ponga un numero entre 1 y 8, apartir del numero que acompaña a las orientaciones que se ven arriba:")
        primera_rotacion_elegida = int(input("Número de la rotación: "))

        # Añadir la rotación seleccionada a las rotaciones posibles
        for clave, valor in rotaciones.items():
            if clave == primera_rotacion_elegida:
                rotaciones_posibles.append(valor)

        del rotaciones[primera_rotacion_elegida]
        cantidad_rotaciones = 7

        # Bucle para añadir más rotaciones si el usuario lo desea
        while True:
            rotaciones_siguientes = input("¿Quiere añadir más rotaciones? Responda con 'SI' o 'NO': ").upper()
            if rotaciones_siguientes == 'NO':
                print("Se jugará con las rotaciones elegidas.")
                break
            elif rotaciones_siguientes == "SI":
                cantidad_rotaciones -= 1
                if cantidad_rotaciones > 0:
                    while True:
                        rotaciones_sig = input("¿Qué otra rotación quiere usar? (ingrese un número): ")
                        es_numero = True
                        for caracter in rotaciones_sig:
                            if caracter < '0' or caracter > '9':
                                es_numero = False
                                break
                        if es_numero:
                            rotaciones_sig = int(rotaciones_sig)
                            if rotaciones_sig in rotaciones:
                                rotaciones_posibles.append(rotaciones[rotaciones_sig])
                                del rotaciones[rotaciones_sig]
                                break
                            else:
                                print("Por favor, ingrese un número de rotación válido que esté disponible.")
                        else:
                            print("Entrada inválida. Por favor, ingrese un número válido.")
                else:
                    print("No hay más rotaciones posibles.")
                    break
            else:
                print("Por favor, responda 'SI' o 'NO'.")

        # Mostrar las palabras disponibles
        palabras_disponibles = list(lista_palabras_personalizada.keys())
        print("Palabras disponibles: " + str(palabras_disponibles))

        # Solicitar al usuario si quiere usar palabras aleatorias o seleccionadas
        while True:
            palabras = input('¿Quiere jugar con palabras aleatorias o prefiere elegir sus propias palabras? Escriba "ALEATORIO" o "ELEGIR" según su preferencia: ').upper()
            if palabras == "ALEATORIO":
                while cantidad > 0:
                    palabra_azar, palabra_al = random.choice(list(lista_palabras_personalizada.items()))
                    lista_palabras[palabra_azar] = palabra_al
                    del lista_palabras_personalizada[palabra_azar]
                    cantidad -= 1
                    cantidad_palabras_sopa += 1
                print("Se jugará con palabras aleatorias.")
                break
            elif palabras == "ELEGIR":
                while True:
                    añadir_palabra = input("¿Qué palabra quiere añadir? ").upper()
                    if añadir_palabra in lista_palabras_personalizada:
                        lista_palabras[añadir_palabra] = lista_palabras_personalizada[añadir_palabra]
                        cantidad_palabras_sopa += 1
                        del lista_palabras_personalizada[añadir_palabra]
                        cantidad -= 1
                        if cantidad <= 0:
                            break
                    else:
                        print("La palabra no está en la lista o ya fue añadida.")
                break
            else:
                print("Entrada inválida. Por favor, responda con 'ALEATORIO' o 'ELEGIR'.")

        # Opción de agregar palabras personalizadas
        adicionar_elementos = input("¿Quiere añadir palabras personalizadas a la sopa? (responda con 'SI' o 'NO'). La sopa de letras iniciará con las palabras que el programa ya tiene definidas. Las palabras que añada se añadirán junto con las palabras definidas por el programa, siempre y cuando la cantidad de palabras añadidas sea suficiente para completar la sopa de letras. La cantidad de letras de las palabras añadidas no puede ser superior a las dimensiones de la sopa de letras: ").upper()
        if adicionar_elementos == "SI":
            cantidad_elementos_añadir = int(input("¿Cuántas palabras quiere añadir a la sopa? "))
            while cantidad_elementos_añadir > 0:
                añadir_palabra = input("¿Qué palabra quiere añadir?: ").upper()
                cantidad_letras_palabra = len(añadir_palabra)
                if cantidad_letras_palabra > filas or cantidad_letras_palabra > columnas:
                    print("La palabra es demasiado larga para las dimensiones de la sopa.")
                    continue
                lista_palabras_usuario[añadir_palabra] = list(añadir_palabra)
                cantidad_elementos_añadir -= 1
                cantidad -= 1
                cantidad_palabras_sopa += 1
        elif adicionar_elementos == "NO":
            print("No se añadirán palabras personalizadas.")

    # Prioriza las palabras del usuario y genera la sopa
    lista_palabras = priorizar_lista_usuario(lista_palabras, lista_palabras_usuario)
    sopa_de_letras = generar_sopa_de_letras(filas, columnas)

    # Coloca las palabras en la sopa de letras, intentando en las rotaciones disponibles
    for _ in range(cantidad_palabras_sopa):
        palabra, letras_palabra = escoger_separar_en_lista(lista_palabras)
        colocada = colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas)
        if colocada and palabra in lista_palabras:
            del lista_palabras[palabra]
        for direccion_fila, direccion_columna in rotaciones_posibles:
            inicio_fila = random.randint(0, filas - 1)
            inicio_columna = random.randint(0, columnas - 1)
            if validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
                colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas)
                colocada = True
                break

    # Rellena las posiciones vacías de la sopa de letras con letras aleatorias
    llenar_con_aleatorias(sopa_de_letras, filas, columnas)
    limpiar_pantalla()

    puntaje_total = 0
    errores_totales = 0
    tiempo_inicio = time.time()

    juego_terminado = False
    # Inicia el juego, preguntando por cada palabra
    for palabra in palabras_buscar:
        intentos = 0
        while True:
            mostrar_instrucciones()
            imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)
            mostrar_lista_palabras(palabras_buscar)

            # Si el jugador falla más de 3 veces, se penaliza y se resalta la palabra
            if intentos >= 3:
                penalizacion = penalizar_por_errores(intentos)
                puntaje_total -= penalizacion
                print(f"Cometiste {intentos} errores y perdiste {penalizacion} puntos.")
                print(f"Resaltando la palabra '{palabra}' automáticamente...")
                palabras_encontradas[palabra] = "omitida"
                if palabra in palabras_colocadas:
                    coordenadas_iniciales, direccion = palabras_colocadas[palabra]
                    imprimir_sopa_de_letras_coloreada_y_actualizar(sopa_de_letras, palabra, coordenadas_iniciales, direccion, filas, columnas)
                break

            opcion = input(f"¿Quieres buscar la palabra '{palabra}' manualmente, resaltar automáticamente o salir del juego? (Escribe 'buscar', 'resaltar' o 'salir'): ").lower()

            if opcion == 'salir':
                juego_terminado = True
                break

            # Si elige buscar la palabra manualmente, se verifica su respuesta
            if opcion == 'buscar':
                fila, columna = verificar_coordenadas(sopa_de_letras, palabra)
                if palabra in palabras_colocadas:
                    coordenadas_correctas, direccion_correcta = palabras_colocadas[palabra]
                    if (fila, columna) == coordenadas_correctas:

                        # Asegúrate de que el puntaje se está sumando correctamente
                        palabras_encontradas[palabra] = "encontrada"
                        imprimir_sopa_de_letras_coloreada_y_actualizar(sopa_de_letras, palabra, coordenadas_correctas, direccion_correcta, filas, columnas)
                        break
                    else:
                        print(f"No se encontró la palabra '{palabra}' en las coordenadas ingresadas.")
                        intentos += 1
                        errores_totales += 1  # Incrementa el contador de errores
                        print(f"Errores cometidos: {intentos}")  # Mostrar la cantidad de errores
                else:
                    print(f"No se pudo buscar la palabra '{palabra}' porque no está colocada en la sopa.")

            elif opcion == 'resaltar':
                print(f"Resaltando automáticamente la palabra '{palabra}'...")
                palabras_encontradas[palabra] = "omitida"
                penalizacion_resaltado = 30  # Definir penalización por resaltar
                puntaje_total -= penalizacion_resaltado  # Restar puntos por resaltar
                if palabra in palabras_colocadas:
                    coordenadas_iniciales, direccion = palabras_colocadas[palabra]
                    imprimir_sopa_de_letras_coloreada_y_actualizar(sopa_de_letras, palabra, coordenadas_iniciales, direccion, filas, columnas)
                break
            else:
                print("Opción no válida. Por favor, escribe 'buscar', 'resaltar' o 'salir'.")
    tiempo_final = time.time()
    tiempo_transcurrido = (tiempo_final - tiempo_inicio) / 60

    # Al final del juego, muestra el total de errores cometidos
    if juego_terminado:
        print("\nHas decidido salir del juego. ¡Hasta la próxima!")
    else:
        if verificar_palabras_encontradas():
            print("\n¡Felicidades! Has encontrado todas las palabras correctamente.")
        else:
            print("\nHas completado la sopa de letras, pero algunas palabras fueron omitidas.")

    # Muestra los errores cometidos al final
    print(f"Cometiste un total de {errores_totales} errores.")
    # Calcula el puntaje final basado en el tiempo y muestra el resultado
    puntos, mensaje = calcular_puntaje(dificultad, tiempo_transcurrido)
    print(f"¡Has terminado en {tiempo_transcurrido:.2f} minutos!")
    print(f"Puntos obtenidos: {puntos} - {mensaje}")    

    puntaje_total += puntos  # Sumar el puntaje obtenido por tiempo al total
    bono_tamano = calcular_bono_tamano(filas, columnas, cantidad_palabras_sopa)
    puntaje_total += bono_tamano  # Sumar el bono por el tamaño de la sopa

    print(f"Has ganado {bono_tamano} puntos adicionales por el tamaño de la sopa.")
    print(f"Puntaje total acumulado: {puntaje_total}")