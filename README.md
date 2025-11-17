# Pylatro

![Pylatro](/media/img/Pylatro.jpg)

Pylatro es una adaptación de [Balatro](https://store.steampowered.com/app/2379780/Balatro/), un popular juego de cartas roguelike creado por un solo desarrollador.

Ganó el premio de Juego del Año y Juego Más Rejugable en la primera edición de los Premios DIGY en 2025.

## Cómo que roguelike?

Es una de las principales mecánicas del juego, que sea estilo roguelike significa que cada partida que jugás es única, siendo prácticamente imposible replicarla.

> El juego original tiene un sistema de RNG (Generador de Números Aleatorios) que no vamos a incluir. Sabiendo la seed (semilla o numero identificador) de la partida sí puede replicarse.

## Bueno, pero cómo se juega?

Para jugar a Pylatro, necesitás conocer primero ciertos conceptos del poker:

- Jugás con una baraja de cartas inglesas, que tiene cartas del 1 al 10, así como:
  - J (11)
  - Q (12)
  - K (13)
- Cada una de estas cartas pertenece a un palo:
  - Picas
  - Treboles
  - Diamantes
  - Corazones

Ahora sí, la escencia de Pylatro:

- En tu mano vas a tener siempre **7 cartas**
- Podés jugar hasta **5 cartas** por mano
- Podés descartar las cartas que no te gustan

> [!Note]
> Tené en cuenta que tenés una cantidad limitada de manos y de descartes por ronda

*Che pero, por que querría descartar cartas? De qué me sirve?*

> [!TIP]
> Descartar cartas es clave para encontrar una mejor mano para jugar y tener más chances de ganar.

### Manos de Poker

Las manos de poker son conjuntos de entre una y cinco cartas que se pueden jugar para ganar fichas y multiplicadores para la puntuación.

> [!Note]
> Para sumar puntos con tu jugada, tenés distintas combinaciones de cartas

| Puntos Base         | Mano de Poker     | Como Jugar la Mano                                                                                                      |
|---------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------|
| 5 Fichas x 1 Mult   | Carta alta        | Cuando no sea posible ninguna otra mano, la carta más alta que tengas. Los ases cuentan como cartas altas en esta mano. |
| 10 Fichas x 2 Mult  | Par               | Dos cartas del mismo valor. Los palos pueden ser diferentes.                                                            |
| 20 Fichas x 2 Mult  | Doble par         | Dos cartas del mismo valor y dos cartas de otro valor. Los palos pueden ser diferentes.                                 |
| 30 Fichas x 3 Mult  | Tercio            | Tres cartas del mismo valor. Los palos pueden ser diferentes.                                                           |
| 30 Fichas x 4 Mult  | Escalera          | Cinco cartas consecutivas de palos distintos. Los ases pueden contar como cartas altas o bajas, pero no ambas a la vez. |
| 35 Fichas x 4 Mult  | Color             | Cinco cartas de cualquier valor, todas del mismo palo.                                                                  |
| 40 Fichas x 4 Mult  | Full              | Tres cartas del mismo valor y dos cartas de cualquier otro valor, de dos o más palos.                                   |
| 60 Fichas x 7 Mult  | Poker             | Cuatro cartas del mismo valor. Los palos pueden ser diferentes.                                                         |
| 100 Fichas x 8 Mult | Escalera de color | Cinco cartas consecutivas, todas del mismo palo.                                                                        |
| 100 Fichas x 8 Mult | Escalera real     | Una escalera de color con as como carta más alta, formada por A K Q J 10 del mismo palo.                                |

> Queda sumar imágenes a cada mano

#### Aclaraciones

Las manos de mayor valor tienen prioridad sobre las de menor valor, no importa su nivel o puntuación. Por ejemplo, si tu mano es K K K K 2, y todas las cartas son de diamantes, la mano siempre será un poker y nunca un color.

Generalmente, solo suman puntos las cartas relevantes para la mano. Las demás, no. Por ejemplo, si se juega un as como carta alta con otras cuatro cartas, solo se cuenta el valor base de la carta alta y el valor del as para la puntuación de la mano. Las otras cartas (hasta cuatro) se descartan sin efecto alguno.

### Fichas

Las fichas son el puntaje que se multiplica por el multiplicador para obtener la puntuación final.

La cantidad de fichas depende principalmente del valor de las cartas obtenidas y de la mano de poker jugada. Las manos más fáciles valen menos fichas base, y las más difíciles, más.

Los ases valen 11 fichas, las figuras (J, Q, K) valen 10 fichas y las cartas numeradas valen fichas igual a su valor.

### Multiplicadores

Los multiplicadores en Pylatro multiplican la cantidad total de fichas en la mano que jugaste, dandote más puntos.

Las distintas manos de poker te dan distintas cantidades de multiplicador. Las combinaciones más fáciles te dan una cantidad menor de multiplicador, y las más difíciles te dan una mayor cantidad de multiplicador.

### Jokers

Los *Jokers* son cartas comodín, que van a ayudarte a sumar puntos en tus jugadas.

Los podés encontrar en la tienda después de cada ronda.

## Objetivo

El objetivo del juego es ganarle a la máquina, que pide una cantidad determinada de fichas para poder pasar al siguiente nivel.

> [!CAUTION]
> Si no te queda ninguna mano y no superaste la cantidad de fichas, gg
