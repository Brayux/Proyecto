# ¿Estas listo para ser parte del proyecto ProGreening?

| Nombre                       | Identificación |      Grupo      |      Carrera        |
|------------------------------|----------------|-----------------|---------------------|
| Brayan Andres Guerrero Cortés| 1011201494     |                 |                     |
| Daniel Santiago Barrera Rojas| 1031647812     |   ProGreening   | Ingeniería Agrícola |
| Pablo Mendoza Malagón        | 1072645448     |                 |                     |

# No olvides sonreir!!!
[![Imagen-de-Whats-App-2024-04-18-a-las-13-37-14-41369a78.jpg](https://i.postimg.cc/MKtYzt5J/Imagen-de-Whats-App-2024-04-18-a-las-13-37-14-41369a78.jpg)](https://postimg.cc/CzB8NG9c)
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>- ProGreening - </b></th>
  </tr>

## Introducción
[![Presentacion-Pro-Greening.png](https://i.postimg.cc/6pXfs0yZ/Presentacion-Pro-Greening.png)](https://postimg.cc/0bVwD7G5)
En este proyecto final, el equipo ProGreening ha desarrollado una sopa de letras en Python, utilizando un código original y creativo. La sopa de letras es un juego clásico que consiste en encontrar palabras ocultas en una cuadrícula de letras. Nuestro objetivo era crear una versión digital de este juego, utilizando las habilidades de programación adquiridas en esta materia abordada por el docente Felipe Gonzales.

## Descripción del Proyecto

Nuestro proyecto consiste en un programa en Python que genera una cuadrícula, con palabras ocultas en diferentes direcciones (horizontal, vertical y diagonal). El usuario puede ingresar una palabra para buscarla en la cuadrícula, y el programa indica si la palabra se encuentra o no en la sopa de letras.

## Características del Proyecto

- Generación de cuadrícula de letras
- Inclusión de palabras ocultas en diferentes direcciones
- Búsqueda de palabras por parte del usuario
- Indicación de si la palabra se encuentra o no en la sopa de letras

## Código Original

Este código implementa un juego de *sopa de letras* en la terminal con características personalizables, donde los jugadores deben encontrar palabras ocultas en una cuadrícula de letras aleatorias. 
Este código implementa un juego de *sopa de letras* en la terminal con características personalizables, donde los jugadores deben encontrar palabras ocultas en una cuadrícula de letras aleatorias. Aquí te explico cómo funciona:

### *Estructura del Código*

# 1. *Imports y Configuración Inicial*:
   - Importa bibliotecas necesarias como random, os, time, y colorama. La biblioteca colorama se utiliza para agregar colores a la salida en la terminal y destacar las palabras que el jugador encuentra o se omiten.
   - Crea un diccionario llamado palabras_colocadas que almacenará las palabras que se insertan en la sopa de letras junto con su posición inicial y dirección en la sopa.

# 2. *Listas de Palabras y Dificultades*:
   - El código contiene tres listas de palabras divididas por nivel de dificultad: dificil, medio, y facil. Cada lista incluye palabras relacionadas con la programación, y a cada palabra se le asigna un puntaje. El puntaje dependerá de la longitud y complejidad de la palabra.

# 3. *Funciones Clave*:

   - **limpiar_pantalla()**: Limpia la pantalla de la terminal (dependiendo del sistema operativo).
   - **configurar_dificultad(dificultad)**: Configura los parámetros del juego según la dificultad seleccionada por el jugador. Para cada dificultad, establece el tamaño de la sopa de letras (filas y columnas), la cantidad de palabras a insertar y las posibles direcciones de colocación.
   - **priorizar_lista_usuario()**: Permite que las palabras personalizadas del jugador se agreguen a la sopa de letras, reemplazando las predeterminadas si es necesario.
   - **generar_sopa_de_letras()**: Crea una sopa de letras vacía, inicializando todas las celdas con guiones (-).
   - **llenar_con_aleatorias()**: Rellena los espacios vacíos de la sopa de letras con letras aleatorias.
   - **colocar_en_sopa()**: Intenta colocar una palabra en la sopa de letras en una dirección válida (horizontal, vertical, diagonal), si es posible. La palabra se coloca una letra a la vez en las celdas de la sopa.
   - **validar_espacio()**: Comprueba si hay suficiente espacio en la cuadrícula para colocar una palabra en la dirección seleccionada.
   - **reemplazar_letra()**: Inserta una letra específica en la posición seleccionada de la sopa.
   - **imprimir_sopa_de_letras()**: Imprime la sopa de letras actual en la terminal de forma organizada.
   - **escoger_separar_en_lista()**: Selecciona una palabra al azar de la lista de palabras disponibles, la convierte en una lista de letras y la elimina de la lista original.
   - **penalizar_por_errores()**: Calcula la penalización que se aplicará al jugador dependiendo de cuántos intentos incorrectos ha tenido.
   - **verificar_coordenadas()**: Solicita al jugador que ingrese las coordenadas donde cree que se encuentra la palabra.
   - **calcular_bono_tamano()**: Calcula un bono adicional de puntos basado en el tamaño de la sopa y la cantidad de palabras insertadas.
   - **calcular_puntaje()**: Calcula el puntaje total según la dificultad elegida y el tiempo que tardó el jugador en completar la sopa.

# 4. *Flujo del Juego*:
   - El juego comienza preguntando al jugador si quiere una *sopa de letras predefinida* (con dificultad fácil, media o difícil) o una *personalizada*. Si elige personalizada, puede ajustar las dimensiones de la sopa, el número de palabras, y las direcciones en las que aparecerán las palabras.
     
   - Luego, el programa crea la sopa de letras, coloca las palabras seleccionadas, y rellena los espacios vacíos con letras aleatorias.
     
   - El jugador debe encontrar las palabras ocultas. Puede ingresar coordenadas manualmente o pedir que se resalten automáticamente, pero al hacerlo recibirá una penalización de puntos.
     
   - Cada vez que el jugador encuentra una palabra, la pantalla se limpia y se actualiza la sopa de letras, destacando las palabras encontradas en *verde* y las omitidas en *rojo*.
     
   - El puntaje total depende de la rapidez con la que el jugador complete la sopa, la cantidad de palabras encontradas correctamente y el tamaño de la sopa.

# 5. *Interacción con el Jugador*:
   - El código ofrece opciones de interacción, como elegir si buscar las palabras manualmente, resaltar las palabras automáticamente o salir del juego.
     
   - El programa también muestra la lista de palabras pendientes y su estado (encontrada u omitida), destacándolas con colores.
  
# 6. *Puntaje y Final del Juego*:
   - Al finalizar la sopa de letras (ya sea porque se encontró todas las palabras o porque el jugador decidió salir), el juego calcula el puntaje total en función de los errores cometidos, el tiempo transcurrido, y un bono por el tamaño de la sopa.
     
   - El jugador recibe un mensaje final dependiendo de su desempeño.

## Estructura
````mermaid
flowchart TD;
    A(Inicio) --> B[Sopa de Letras]; 
    B --> C;C{¿Desea jugar con una sopa de letras ya lista o desea crearla?}--Predefinida-->D{¿Desea un nivel facil, medio o estas preparado para el dificil?};
    C--Personalizada-->E;
    E[Digite un número de filas con las que desea jugar]
    D--Facil-->F;F[10X10
    Horientación: HV
    XXX palabras]
    D--Medioo-->G;G[15X15
    Horientación: H,V,D
    XXX palabras]
    D--Dificil-->H;H[30X30
    H,V,D
    XXX palabras]
    F-->FF;G-->FF;H-->FF
    FF[Generar sopa de letras segun nivel y modalidad]
    FF--Encontraste una palabra-->FFF;FFF[Escribe las coordenadas de la palabra encontrada junto con la palabra]
    FFF-->z;z{¿Las coordenadas son correctas para la palabra encontrada?}
    z--si-->zz;zz[El programa cambia el color de la palabra en la sopa de letras]
    z--noo-->ZZZZ;ZZZZ[Incorrecto, intentalo de nuevo]
    ZZZZ-->FFF
    zz--El usuario encuentra y digita la ultima palabra-->zzz;zzz[Tiempo de juego:
    Puntaje:
    Observación:]
    zzz-->fin;fin{¿Quiere jugar de nuevo?}
    fin-->finn;finn[Si];finn-->B;fin-->finnn;finnn[No]
    finnn-->finalizar;finalizar[Gracias por jugar]
    E-->I;I[Digite número de columnas con las que desea jugar]
    I-->J;J[Digite la cantidad de palabras con las que desea jugar]
    J-->K;K[Horientaciones posibles:
    Horizontal
    Vertical
    Diagonal]
    K-->L;L[Digite el numero de la horientación con la que desea jugar]
    L-->LL;LL{¿Desea jugar con otra horientación?}
    LL--si-->L
    LL--Noo-->M;M{¿Desea palabras aleatorias o las quiere elegir?}
    M--Aleatorioo-->FF
    M--Elegir-->O;O[Cuentas con las siguientes palabras para generar tu lista]
    O-->P;P[Escribe las palabras con las que desearia jugar según lista]
    P-->Q;Q{¿Desea proponer palabras nuevas?}
    Q--si-->R;R[¿Cuántas palabras quiere ingresar?]
    Q--Noo-->SS;SS[Establecer palabras de la lista predeterminada]
    SS-->FF
    R-->S;S[Porfavor digite las palabras]
    S-->FF

````
## Instalar Biblioteca colorama
• Instalar python

• Abrir VS code

• Abrir terminal  VS code

• Para instalar la biclioteca correctamente, debes poner el siguiente codigo en el terminal
````python
pip install colorama
````
• Verificar instalación
````python
pip show colorama
````
• Usar colorama
````python
import colorama
from colorama import Fore, back , style
````
# funciones clave  para la sopa de letras:

# 1. *Funciones de configuración y utilidades*
````python
def limpiar_pantalla():
    os.system('cls')
````
- Esta función limpia la pantalla de la terminal.
  
- En sistemas Windows, usa os.system('cls') para limpiar la terminal.


````python
def configurar_dificultad(dificultad):
    if dificultad == 'FACIL':
        return 10, 10, 5, [(0,1), (1,0)], facil
    if dificultad == 'MEDIO':
        return 15, 15, 10, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1)], medio
    if dificultad == 'DIFICIL':
        return 30, 30, 15, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], dificil
    return
````

- Configura el tamaño de la sopa de letras y sus características según la *dificultad* elegida:
  
  - FACIL: Una cuadrícula de 10x10, con 5 palabras a insertar y solo dos direcciones permitidas (horizontal y vertical).
    
  - MEDIO: Una cuadrícula de 15x15, con 10 palabras y más direcciones (horizontal, vertical y diagonal en una dirección).
    
  - DIFICIL: Una cuadrícula de 30x30, con 15 palabras y todas las direcciones posibles.
    
- Devuelve el número de filas, columnas, cantidad de palabras y rotaciones posibles, junto con la lista de palabras correspondientes a la dificultad elegida.


````python
def priorizar_lista_usuario(lista_palabras, lista_palabras_usuario):
    for palabra in lista_palabras_usuario:
        lista_palabras[palabra] = lista_palabras_usuario[palabra]
    return lista_palabras
````
- Esta función toma las palabras personalizadas del usuario (si existen) y las añade a la lista de palabras del juego (lista_palabras), priorizándolas sobre las palabras predefinidas.
  
- Básicamente, sobrescribe cualquier palabra de la lista predefinida que tenga el mismo nombre que las personalizadas.

# 2. *Funciones relacionadas con la sopa de letras*

````python
def generar_sopa_de_letras(filas, columnas):
    sopa_de_letras = {}
    for fila in range(filas):
        for columna in range(columnas):
            sopa_de_letras[(fila, columna)] = '-'  # Inicializa cada posición con un guion
    return sopa_de_letras
````
- Crea una sopa de letras vacía representada por un *diccionario* donde cada celda tiene como clave un par de coordenadas (fila, columna) y como valor un guion (-), lo que indica que está vacía.
  
- El tamaño de la sopa es determinado por el número de filas y columnas especificado.

````python
def llenar_con_aleatorias(sopa_de_letras, filas, columnas):
    letras_posibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for fila in range(filas):
        for columna in range(columnas):
            if sopa_de_letras[(fila, columna)] == '-':
                sopa_de_letras[(fila, columna)] = random.choice(letras_posibles)
````

- Rellena los espacios vacíos (indicados por guiones -) de la sopa de letras con letras aleatorias del alfabeto (A-Z).
  
- Recorre toda la sopa de letras y si encuentra una celda vacía, coloca una letra al azar en esa posición.


````python
def palabra_cabe_en_sopa(letras_palabra, filas, columnas, direccion_fila, direccion_columna):
    if direccion_fila == 0:
        return len(letras_palabra) <= columnas
    elif direccion_columna == 0:
        return len(letras_palabra) <= filas
    else:
        return len(letras_palabra) <= min(filas, columnas)
````

- Verifica si una palabra puede caber en la sopa de letras en la dirección especificada.
  
- Si la palabra se coloca horizontalmente (direccion_fila == 0), verifica que la longitud de la palabra no exceda el número de columnas.
  
- Si se coloca verticalmente (direccion_columna == 0), verifica que no exceda el número de filas.
  
- Para colocaciones diagonales, verifica que la longitud de la palabra no exceda el tamaño mínimo entre las filas y columnas.

````python
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
````

- Intenta colocar una palabra en la sopa de letras en una dirección válida. Recorre las posibles direcciones aleatoriamente hasta encontrar una que tenga suficiente espacio.
  
- Si una palabra ya ha sido colocada, la función la ignora.
  
- Coloca la palabra letra por letra en la sopa y actualiza el diccionario palabras_colocadas con su posición y dirección.

````python
def validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
    contador = 0
    for letra in letras_palabra:
        nueva_fila = inicio_fila + contador * direccion_fila
        nueva_columna = inicio_columna + contador * direccion_columna
        if nueva_fila < 0 o nueva_fila >= filas o nueva_columna < 0 o nueva_columna >= columnas:
            return False
        if sopa_de_letras[(nueva_fila, nueva_columna)] != '-' and sopa_de_letras[(nueva_fila, nueva_columna)] != letra:
            return False
        contador += 1
    return True
````

- Verifica si hay espacio suficiente para colocar una palabra en la sopa, comenzando desde una posición inicial dada y en la dirección especificada.
  
- Se asegura de que no haya letras que entren en conflicto con las letras de la palabra y que no se salga de los límites de la sopa.


````python
def reemplazar_letra(sopa_de_letras, fila, columna, nueva_letra):
    sopa_de_letras[(fila, columna)] = nueva_letra.lower()
````

- Reemplaza el contenido de una celda específica en la sopa de letras con una nueva letra.
  
- La letra se almacena en minúsculas para diferenciarla de las letras aleatorias, que están en mayúsculas.

# 3. *Funciones de interacción con el jugador*

````python
def imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)
python
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
            print(f' {

letra} |', end=' ')
        print()
        print("   +" + "----+" * columnas)
````

- Imprime la sopa de letras de forma organizada en la terminal.
  
- Muestra las filas y columnas con números para que el jugador pueda identificar fácilmente las coordenadas.

````python
def verificar_coordenadas(sopa_de_letras, palabra)
python
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
````

- Solicita al jugador las coordenadas de una palabra que intenta encontrar en la sopa de letras.
  
- Verifica que las coordenadas ingresadas estén dentro del rango válido y que sean números.

# 4. *Funciones de puntuación*

````python
def penalizar_por_errores(intentos)
python
def penalizar_por_errores(intentos):
    if intentos == 1:
        return 10
    elif intentos == 2:
        return 20
    elif intentos >= 3:
        return 50
````

- Aplica una penalización de puntos al jugador dependiendo de cuántos errores ha cometido en un intento de buscar una palabra.
  
- A mayor número de errores, mayor será la penalización.

````python
def calcular_bono_tamano(filas, columnas, cantidad_palabras)
python
def calcular_bono_tamano(filas, columnas, cantidad_palabras):
    return (filas * columnas) * (cantidad_palabras / 10)
````

- Calcula un bono de puntos adicional basado en el tamaño de la sopa de letras (número de filas por columnas) y la cantidad de palabras insertadas en la sopa.
  

````python
def calcular_puntaje(dificultad, tiempo_transcurrido)
python
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
````

- Calcula el puntaje final basado en el *tiempo* que tardó el jugador en completar la sopa de letras y la dificultad seleccionada.
  
- A menor tiempo transcurrido, mayor será el puntaje obtenido.

Estas funciones hacen que el juego sea dinámico, interactivo y mantenga un sistema de puntuación que premia la rapidez y precisión del jugador. ¡Es un juego entretenido y educativo que combina lógica y diversión!


# Afrontar retos
Interfaz: Era de nuestro agrado jugar con una interfaz gráfica, donde el usuario tuviera una mejor experiencia

[![sopa-11.png](https://i.postimg.cc/sf0WyRg7/sopa-11.png)](https://postimg.cc/3WmNCVpx)

sin embargo, nos afrontamos a diferentes problemas al usar la biblioteca tkinter como por ejemplo:

• Planteamiento de un ``nuevo´´ codigo

• Tiempo

• Falsas expectativas

• Descartar varias funciones del codigo original

[![sopa-1.png](https://i.postimg.cc/hvwQ0V5p/sopa-1.png)](https://postimg.cc/wRXBqRHm)

# Solución :)
• Jugar desde la consola lo mas realista posible

• Proponer el estilo del juego Batalla Naval 

## Conclusión

• En conclusión, la sopa de letras en Python es un juego divertido y desafiante que demuestra nuestras habilidades de programación.

• Sin duda alguna, fue un proceso retador, el cual nos tomo bastante tiempo. 

•Creemos que es importante hacer una previa planeación para así realizar un buen proyecto, el cual no llegue a tomar demasiado tiempo. 

• Pese a todo estamos orgullosos de nuestro trabajo y esperamos que disfruten jugando con nuestra sopa de letras.

