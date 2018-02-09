# mp3DirectCut #

*	 Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descargar  [versión estable][1]
*	 Descargar [versión de desenvolvemento][2]

# Presentación #

Este complemento permite mellorar a accesibilidade do programa mp3DirectCut
co NVDA.

Probouse coas versións de mp3DirectCut que van dende a 212 ata a 223.

## Atallos de teclado ##

Este complemento ofrece as seguintes ordes-:

*	B
	*	Usado para confirmar a colocación correcta da marca de comezo da selección B.
*	Control+Shift+B
	*	Usado para indicar a ubicación da marca de comezo da selección B.
	*	Premendo dos dúas veces da a duración da selección.
*	Control+Shift+D
	*	Da a duración transcorrida dende o comezo do arquivo ata a ubicación actual do cursor de reproducción.
	*	Premendo dúas veces da o tempo total.
*	Control+R
	*	Confirma que a seleción se cancelou.
*	Control+Shift+R
	*	Da o tempo restante dende a posición actual do cursor de reproducción ata o remate do arquivo.
*	Control+Shift+E
	*	Usado para indicar a ubicación da marca de remate da selección N.
	*	Premendo dúas veces da un recapitulativo da ubicación dass marcas B e N, así como a duración da selección.
*	Control+Shift+P
	*	Da a referencia da parte actual, así como o número total de partes.
*	Control+Shift+Espazo
	*	Usado para indicar o valor actual do nível do vúmetro.
	*	Premendo dúas veces permite reiniciar este nível.
*	Frecha Abaixo
	*	Permite dar a duración actual.
	*	Se se fixo unha selección, coloca o cursor na ubicación da marca de remate da selección N dando a ubicación desta marca.
	*	Nas opcións do control do volume do mp3directcut, da o valor seguinte que xeralmente se accede coa frecha abaixo.
	*	E que non se fala por defecto.
*	Fin
	*	Permite mover o cursor de reproducción ao final do arquivo actual e da o tempo total.
*	Inicio
	*	Permite mover o cursor de reproducción ao comezo do arquivo actual.
*	Frecha Esquerda
	*	Permite facer un retroceso dun segundo durante unha reproducción, dando a duración actual.
	*	A duración deste retroceso é configurable nas opcións de mp3directcut.
*	N
	*	Permite confirmar a colocación correcta da marca do remate da selección N.
*	Avance de páxina
	*	Permite facer un salto cara adiante de 10 segundos durante unha reprodución, dando a duración actual.
	*	A duración deste salto cara adiante é configurable nas opcións do mp3directcut.
*	Retroceso de páxina
	*	Permite facer un salto cara atrás de 10 segundos durante unha reproducción, dando a duración actual.
	*	A duración deste salto cara atrás é configurable nas opcións do mp3directcut.
*	R
	*	Permite preparar unha grabación e indica se podes premer sobre a barra espaciadora para comezar.
*	Frecha Dereita
	*	Permite facer un avance dun segundo durante unha reprodución, dando a duración actual.
	*	A duración deste avance é configurable nas opcións do mp3directcut.
*	Control+Frecha Dereita
	*	Despraza ao seguinte punto de corte, dando a duración actual.
*	Control+Frecha Esquerda
	*	Despraza ao punto de corte anterior, dando a duración actual.
*	Shift+Frecha Dereita
	*	Permite facer un avance de catro centésimas de segundo durante unha reproducción, dando a duración actual.
*	Shift+Frecha Esquerda
	*	Permite facer un retroceso de catro centésimas de segundo durante unha reproducción, dando a duración actual.
*	S
	*	Usado para deter a lectura, dando a duración actual.
*	Espazo
	*	Se a gravación está lista, inicie esta gravación.
	*	Se está a realizar unha gravación, deténche colocando o cursor ao principio.
	*	Se se carga un ficheiro, inicie a lectura.
	*	Se unha lectura está en progreso, permite facer unha pausa, dando a duración actual.
	*	Se a lectura está en pausa, permite reiniciar a lectura desde a localización actual.
*	Frecha Alta
	*	Permite dar a duración actual.
	*	Se se fixo unha selección, coloca o cursor na ubicación da marca de inicio da selección B dando a ubicación desta marca.
	*	Nas opcións do control do volume do mp3directcut, da o valor anterior que xeralmente se accede coa frecha alta.
	*	E que non se fala por defecto.
*	NVDA+H
	*	Permite abrir a axuda do complemento actual.

## Change for version 4.0 ##

*	 Added the Compatibility of the add-on with both Python 2.7 and 3;
*	 Fixed a bug with add-on paths that contain non-ASCII characters.

## Cambios para a versión 3.0 ##

*	 Utilízase o módulo gui.guiHelper para asegurarse da correcta aparencia do
   diálogo de configuración do complemento;
*	 Utilízase formato en lugar de %s para cadeas formateadas;
*	 Cúmprense as directrices de cumprimentación.

## Cambios para a versión 2.3 ##

*	 Engádese a licenza GPL ao complemento;
*	 Cámbiase o atallo de teclado do script que da fin á seleción de Ctrl +
   Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N non funciona coas
   últimas versións do mp3DirectCut;
*	 engadiuse un script para confirmar que a selección cancelouse con
   'Control+r';
*	 Made some corrections in the code of the appModule 'mp3directcut.py'.

## Cambio para la versión 2.2 ##

*	 Correción dos scripts que dan a localización dos marcadores de seleción.

## Cambios para a versión 2.1.1 ##

*	 Borrado do script dando a duración total e engadida esta información para
   o script que da o tempo transcorrido;
*	 Engadida a posibilidade de activar ou desactivar os anuncios relacionados
   coa tecla de espazo nas opcións de configuración do complemento, por
   separado dos outros anuncios;
*	 Engadida a posibilidade para activar ou desactivar o anuncio para a boa
   colocación de marcas de seleción nas opcións de configuración do
   complemento;
*	 Engadido o anuncio da parte actual cando se move entre os pontos de
   corte;
*	 Correción dos anuncios relacionados coas teclas verticais;
*	 Engadido un Script para abrir a axuda do actual complemento accesible
   grazas á orde de teclado "NVDA+H";
*	 Desprazamento do menú de configuración do complemento do menú Ferramentas
   ao menú Preferencias do NVDA.

## Cambios para a versión 2.1 ##

*	 Engadido un Script para falar o seguinte ponto de corte co Control+Frecha
   Dereita;
*	 Engadido un Script para falar o ponto de corte anterior co Control+Frecha
   Esquerda;
*	 Engadido un Script para falar o desprazamento de 4 centésimas de segundo
   cara adiante co Shift+Frecha Dereita;
*	 Engadido un Script para falar o desprazamento de 4 centésimas de segundo
   cara atrás co Shift+Frecha Esquerda;
*	 Corrección do summary do complemento "para mp3DirectCut" a
   "mp3DirectCut".

## Cambios para a versión 2.0 ##

*	 Engadido un Script para saber o tempo restante co "Control+Shift+R";
*	 Corrección da lectura das duracións incluindo as horas;
*	 Engadida a posibilidade de diferenciar milésimas ou centésimas de
   segundos.

## Cambios para a versión 1.1 ##

*	 Engadida a posibilidade para incluir as ordes do complemento entre os xestos de entrada, na categoría "mp3DirectCut";
*	 Serán visibles só durante unha utilización do programa mp3DirectCut.
*	 Engadiuse a posibilidade de activar ou desactivar as mensaxes automáticas, no menú Ferramentas NVDA, elemento de menú "Configuración do complemento mp3DirectCut";

## Cambios para a versión 1.0 ##

*	 versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
