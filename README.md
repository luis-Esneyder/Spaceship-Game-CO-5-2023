## Spaceship-Game

Spaceship es un juego creado con ayuda de la libreria pygame, utilizamos porgramación orientada a objetos, utilizando clases en python. Acontinuación mostramos la estructura del proyecto.


## Estructura Del Proyecto
La Estructura del proyecto es la seguida por pygame, manejo de ebentos, actualizaciones de los componentes y por ultimo el pintado de estos, siguiendo esa logica el proyecto se divide en:
- asses, donde se guardam recursos publicos como las imagenes, musica, etc
- components, es donde esta la base del proyecto, aquí se crean las clases que nos permiten el funcionamiento y el manejo del juego.
- utils, en esta parte vamos a ver que se utiliza de forma que ayuda a mantener buenas practicas de programación a la hora de normbar constantes que se manejan de forma global en la app







## Game
La idea del juego es eliminar las naves enemigas que van a pareciendo, esquivar las balas y los enemigos para ir ganando puntuación, al transcurrir el tiempo, la velocidad del juego va aumentando en una unidad.

Al eliminar algunos (solo el Malevolo Cucarachon) enemigos estos pueden arrojar corazones y aumentar la vida del jugador, también al aumentar el puntaje en 10 aprece un escudo que al obtenerlo el jugador se vuelve inmune a daños, tanto del enemigo como de las balas de los enemigos, esto por 3 segundos.
## Naves Enemigas

vamos a ver el comportamiento de las naves

Naves Básicas
-
las naves básicas son 3 y van aparecer en el transcurso del juego bajo dos condiciones. Maximo en pantalla pueden haber 4 y aparecen de forma aleatoria cada segundo, al morir estas naves no arrojan habilidades ni vida extra al jugador.
- Red Ship, es la nave más básica con un rango de movimiento de 50 en el x, con una la posición en este eje aumentando en 5 unidades, en el eje y se mueve hacia bajo aumentando en 1 unidad, esta nave dispara cada 1.5 segundos, tiene una vida de 1 y por ultimo al morir da un punto al jugador  
- Gray Ship, esta nave tiene un rango de movimiento de 150 en el x, con una la posición en este eje aumentando en 7 unidades, en el eje y se mueve hacia bajo aumentando en 3 unidad, esta nave dispara cada 1 segundo, tiene una vida de 4 y por ultimo al morir da 2 punto al jugador  
- Black Ship, esta nave tiene un rango de movimiento de la mitad de la pantalla en el x, con una la posición en este eje aumentando en 10 unidades, en el eje y se mueve hacia bajo aumentando en 1 unidad, esta nave dispara cada 1 segundo, tiene una vida de 4 y por ultimo al morir da 3 punto al jugador

Malevolo Cucarachon
-
Esta nave enemiga en màs fuerte que las naves básica, apareciendo si el puntaje del jugador en mayor que 10, al aprecer el primero este ira apareciendo cada 4 segundos 
- El Malevolo Cucarachon tiene un rango de movimiento en el eje x de toda la pantalla con un incremento en este 15 unidades, en el eje y el incremento es de 1.5 unidades, el Malevolo Cucarachon tiene una vida de 8 y al morir le da al jugador 5 puntos además de arrojar un coranzon que incrementa la vida del jugador.
