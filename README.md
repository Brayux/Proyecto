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

 ## Proyecto Programacion de computadores:
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

Nuestro código en Python utiliza las siguientes características:

- Uso de listas y matrices para generar la cuadrícula de letras
- Funciones para generar palabras al azar y ocultarlas en la cuadrícula
- Bucles para buscar la palabra ingresada por el usuario

## Diagrama Juego
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

## Instalar pip tkinter




## Conclusión

En conclusión, el equipo ProGreening ha desarrollado un proyecto final de programación de computadores que cumple con los objetivos planteados. La sopa de letras en Python es un juego divertido y desafiante que demuestra nuestras habilidades de programación. Estamos orgullosos de nuestro trabajo y esperamos que disfruten jugando con nuestra sopa de letras.

