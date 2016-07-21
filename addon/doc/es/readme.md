# mp3DirectCut-2.2

*	 Autor(es): Abdel, Rémy, Abdellah ZINEDDINE, Jean-François COLAS
*	 Descargar [versión estable][1]
*	 Descargar [versión de desarrollo][2]

# Presentación #

Este complemento permite de mejorar la accesibilidad del software mp3DirectCut con NVDA.

Ha sido probado con las versiones de mp3DirectCut que van desde la 212 hasta la 222.

## Órdenes de teclado ##

Este complemento ofrece las órdenes siguientes, que se puede modificar llendo al menú "Preferencias/Gestos de entrada", en la categoría "mp3DirectCut" :

*	B
	*	Permite de confirmar la colocación correcta del Tag de inicio de selección B.
*	Control+Shift+B
	*	Permite de indicar la ubicación del Tag de inicio de selección B.
	*	Pulsando dos veces da la duración de la selección.
*	Control+Shift+D
	*	Da la duración recorrida desde el inicio del archivo hasta la ubicación actual del cursor de reproducción.
	*	Pulsando dos veces da el tiempo total.
*	Control+Shift+R
	*	Da el tiempo restante desde la posición actual del cursor de reproducción hasta el final del archivo.
*	Control+Shift+N
	*	Permite de indicar la ubicación del Tag de final de selección N.
	*	Pulsando dos veces da un recapitulativo de la ubicación de los Tags B y N, así como la duración de la selección.
*	Control+Shift+P
	*	Dara la referencia del sector actual, así como el número total de sectores.
*	Control+Shift+Espacio
	*	Permite de indicar el valor actual del nivel del vúmetro.
	*	Pulsando dos veces permite de reiniciar este nivel.
*	Flecha Abajo
	*	Permite de dar la duración actual.
	*	Si se ha hecho una selección, coloca el cursor en la ubicación del Tag de final de selección N dando la ubicación de este Tag.
	*	En las opciones del control del volumen de mp3directcut, da el valor siguiente que generalmente se accede con la flecha abajo y que no es verbalizado por defecto.
*	Fin
	*	Permite de mover el cursor de reproducción al final del archivo actual y da el tiempo total.
*	Inicio
	*	Permite de mover el cursor de reproducción al inicio del archivo actual.
*	Flecha Izquierda
	*	Permite de hacer un retroceso hacia atrás de un segundo durante una reproducción, dando la duración actual. La duración de este retroceso es configurable en las opciones de mp3directcut.
*	N
	*	Permite de confirmar la colocación correcta del Tag de final de selección N.
*	Avance de página
	*	Permite de hacer un salto hacia adelante de 10 segundos durante una reproducción, dando la duración actual. La duración de este salto hacia adelante es configurable en las opciones de mp3directcut.
*	Retroceso de página
	*	Permite de hacer un salto hacia atrás de 10 segundos durante una reproducción, dando la duración actual. La duración de este salto hacia atrás es configurable en las opciones de mp3directcut.
*	R
	*	Permite de preparar una grabación y indica si puedes pulsar sobre la barra espaciadora para iniciar.
*	Flecha Derecha
	*	Permite de hacer un avanzado hacia adelante de un segundo durante una reproducción, dando la duración actual. La duración de este avanzado es configurable en las opciones de mp3directcut.
*	Control+Flecha Derecha
	*	Desplaza al siguiente punto de corte, dando la duración actual.
*	Control+Flecha Izquierda
	*	Desplaza al punto de corte anterior, dando la duración actual.
*	Shift+Flecha Derecha
	*	Permite de hacer un avanzado hacia adelante de cuatro centésimas de segundo durante una reproducción, dando la duración actual.
*	Shift+Flecha Izquierda
	*	Permite de hacer un retroceso hacia atrás de cuatro centésimas de segundo durante una reproducción, dando la duración actual.
*	S
	*	Permite de detener la reproducción en curso, dando la duración actual.
*	Espacio
	*	Si la grabación está lista, permite de iniciar ésta.
	*	Si una grabación está en curso, permite de detenerla, colocando el cursor al inicio del archivo.
	*	Si un archivo está abierto, permite de  iniciar la reproducción.
	*	Si una reproducción  está en curso, permite de efectuar una pausa, dando la duración actual.
	*	Si una reproducción  está en pausa, permite de reiniciar la reproducción desde la ubicación actual.
*	Flecha Arriba
	*	Permite de dar la duración actual.
	*	Si se ha hecho una selección, coloca el cursor en la ubicación del Tag de inicio de selección B, dando la ubicación de este Tag.
	*	En las opciones del control del volumen de mp3directcut, da el valor anterior que generalmente se accede con la flecha arriba y que no es verbalizado por defecto.
*	NVDA+H
	*	Permite de abrir la ayuda del actual complemento.

## Cambios para la versión 2.1.1 ##

*	 La corrección de scripts que dan la selección marcadores ubicaciones.

## Cambios para la versión 2.1.1 ##

*	 Supresión del script dando la duración total y añadida esta información para el script que da el tiempo transcurrido;
*	 Añadida la posibilidad de activar o desactivar los anuncios relacionados con la tecla de espacio en las opciones de configuración del complemento, por separado de los otros anuncios;;
*	 Añadida la posibilidad para activar o desactivar el anuncio para la buena colocación de Tags de selección en las opciones de configuración del complemento;
*	 Añadido el anuncio del sector actual cuando se mueve entre los puntos de corte ;;
*	 Corrección de los anuncios relacionados con las teclas verticales;
*	 Añadido un Script para abrir la ayuda del actual complemento accesible gracias a la orden de teclado "NVDA+H";
*	 Desplazamiento del menú de configuración del complemento del menú Herramientas al menú Preferencias de NVDA.

## Cambios para la versión 2.1 ##

*	 Añadido un Script para vocalizar el siguiente punto de corte con Control+Flecha Derecha;
*	 Añadido un Script para vocalizar el punto de corte anterior con Control+Flecha Izquierda;
*	 Añadido un Script para vocalizar el desplazamiento de 4 centésimas de segundo hacia adelante con Shift+Flecha Derecha;
*	 Añadido un Script para vocalizar el desplazamiento de 4 centésimas de segundo hacia atrás con Shift+Flecha Izquierda;
*	 Corrección del summary del complemento de "para mp3DirectCut" a "mp3DirectCut".

## Cambios para la versión 2.0 ##

*	 Añadido un Script para saber el tiempo restante con Control Shift R;
*	 Corrección de la lectura de las duraciones incluyendo las horas;
*	 Añadida la posibilidad de diferenciar milésimas o centésimas de segundos.

## Cambios para la versión 1.1 ##

*	 Añadida la posibilidad para incluir las órdenes del complemento entre los Gestos de entrada, en la categoría "mp3DirectCut";
	*	 Ellas serán visibles sólo durante una utilización del software mp3DirectCut.
*	 Añadido el idioma español entre los idiomas de traducción;
*	 Se ha añadido la posibilidad de activar o desactivar los mensajes automáticos, en el menú Herramientas NVDA, elemento de menú "Configuración del complemento mp3DirectCut".

## Cambios para la versión 1.0 ##

*	 Primera  versión

[1]: http://cyber25.free.fr/nvda-addons/mp3DirectCut-2.2.nvda-addon

[2]: http://cyber25.free.fr/nvda-addons/mp3DirectCut-2.2-dev.nvda-addon
