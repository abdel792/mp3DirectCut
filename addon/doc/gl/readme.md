# mp3DirectCut #

* Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Descargar  [versión estable][1]
* Descargar [versión de desenvolvemento][2]

# Presentación #

Este complemento permite mellorar a accesibilidade do programa mp3DirectCut
co NVDA.

Probouse coas versións de mp3DirectCut que van dende a 212 ata a 223.

## Atallos de teclado ##

Este complemento ofrece as seguintes ordes-:

* B

    * Utilizado para confirmar a correcta colocación do marcador de inicio
      da selección B.

* Ctrl+Shift+B

    * Utilizado para indicar a posición do marcador de inicio da selección
      B.
    * Premelo dúas veces permíteche obter a duración da selección.

* Ctrl+Shift+D

    * Proporciona a duración dende o comezo do arquivo ata a posición actual
      do cursor de reprodución.
    * Premelo dúas veces permíteche obter a duración total.

* Ctrl+R

    * confirma que a selección foi cancelada.

* Ctrl+Shift+R

    * Proporciona o tempo restante dende a posición actual do cursor de
      reprodución ata o final do arquivo.

* Ctrl+Shift+E

    * Utilizado para indicar a posición do marcador de finalización da
      selección N.
    * Premelo dúas veces permíteche obter as posicións recapitulativas B e
      N, e a duración da selección.

* Ctrl+Shift+P

    * Proporciona referencia da parte actual e o número total de partes do
      arquivo actual.

* Ctrl+Shift+Space

    * Utilizado para determinar o nivel actual do vúmetro durante a
      grabación.
    * Premelo dúas veces restabléceo.

* Frecha Abaixo

    * Permíteche ver a posición actual do punto de inserción.
    * Esta orde tamén posiciona o cursor na ubicación do marcador de
      finalización da selección N, informando da localización dese marcador
      se se fixo unha selección.
    * Na caixa de diálogo de volume, informa do seguinte valor ó que se pode
      chegar xeralmente con frechaAbaixo.
    * Por defecto ste valor non se fala.

* Fin

    * Move o cursor de reprodución ao final do arquivo actual e proporciona
      o tempo total.

* Inicio

    * Move o cursor de reprodución ao inicio do arquivo actual.

* Frecha esquerda

    * Permite realizar un rebobinado breve dun segundo durante a
      reprodución, informando da duración actual.
    * Esta duración é configurable nas opcións do mp3directcut.

* N

    * Utilizado para confirmar a correcta colocación do marcador de
      finalización da selección N.

* Avance de Páxina

    * Permite realizar un salto cara adiante de 10 segundos durante a
      reprodución, informando da duración actual.
    * Esta duración é configurable nas opcións do mp3directcut.

* Retroceso de Páxina

    * Permite realizar un rebobinado de de 10 segundos durante a
      reprodución, informando da duración actual.
    * Esta duración é configurable nas opcións do mp3directcut.

* R

    * Permite preparar unha grabación na que podes premer espazo para
      comezar.

* Frecha Dereita

    * Permite realizar un avance breve dun segundo durante a reprodución,
      informando da duración actual.
    * Esta duración é configurable nas opcións do mp3directcut.

* Ctrl+Frecha Dereita

    * Móvese ao seguinte punto de corte, informando da duración actual.

* Ctrl+Frecha Esquerda

    * Móvese ao punto de corte anterior, informando da duración actual.

* Shift+Frecha Dereita

    * Permite realizar avances breves de catro décimas de segundo durante a
      reprodución, informando da duración actual.

* Shift+Frecha Esquerda

    * Permite realizar un retroceso breve de catro décimas de segundo
      durante a reprodución, informando da duración actual.

* S

    * Utilizado para deter a lectura e obter a duración actual.

* Espazo

    * Se a grabación está lista, comezala.
    * Se hai unha grabación en progreso, parala posicionando o cursor ao
      comezo.
    * Se un arquivo está cargado, comezar a lectura.
    * Se hai unha lectura en progreso, permite facer unha pausa fornecendo a
      duración actual.
    * Se a lectura está pausada, permite reiniciala dende a ubicación
      actual.

* Frecha Arriba

    * Permíteche ver a posición actual do punto de inserción.
    * Este comando tamén posiciona o cursor na ubicación do marcador de
      comezo da selección B, informando da localización deste marcador se se
      fixo unha selección.
    * Na caixa de diálogo de volume, reporta o valor anterior ao que se pode
      chegar xeralmente con frechaArriba.
    * Por defecto ste valor non se fala.

* NVDA+H

    * Permite abrir a axuda do complemento actual.

## compatibilidade ##

* Este complemento é compatible coas versións de NVDA que van dende a 2016.4
  ata a 2019.1.

## Cambios para a versión 19.02 ##

* Engadida a configuración do complemento ao panel de opcions dispoñible
  dende NVDA 2018.2;
* Cambiado o numerado de versións utilizando YY.MM (O ano en dous díxitos,
  seguido dun punto, seguido do mes en dous díxitos);
* Engadida compatibilidade co novo formato de versións de complementos,
  aparecido dende NVDA 2019.1.

## Cambios para a versión 4.0 ##

* Engadida a Compatibilidade do commplemento con Python 2.7 e 3;
* Arranxado un fallo coas rutas do complemento que conteñan caracteres non
  ASCII.

## Cambios para a versión 3.0 ##

* Utilízase o módulo gui.guiHelper para asegurarse da correcta aparencia do
  diálogo de configuración do complemento;
* Utilízase formato en lugar de %s para cadeas formateadas;
* Cúmprense as directrices de cumprimentación.

## Cambios para a versión 2.3 ##

* Engádese a licenza GPL ao complemento;
* Cámbiase o atallo de teclado do script que da fin á seleción de Ctrl +
  Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N non funciona coas
  últimas versións do mp3DirectCut;
* engadiuse un script para confirmar que a selección cancelouse con
  'Control+r';
* Fixéronse algunhas correcións no código do appModule 'mp3directcut.py'.

## Cambio para la versión 2.2 ##

* Correción dos scripts que dan a localización dos marcadores de seleción.

## Cambios para a versión 2.1.1 ##

* Borrado do script dando a duración total e engadida esta información para
  o script que da o tempo transcorrido;
* Engadida a posibilidade de activar ou desactivar os anuncios relacionados
  coa tecla de espazo nas opcións de configuración do complemento, por
  separado dos outros anuncios;
* Engadida a posibilidade para activar ou desactivar o anuncio para a boa
  colocación de marcas de seleción nas opcións de configuración do
  complemento;
* Engadido o anuncio da parte actual cando se move entre os pontos de corte;
* Correción dos anuncios relacionados coas teclas verticais;
* Engadido un Script para abrir a axuda do actual complemento accesible
  grazas á orde de teclado "NVDA+H";
* Desprazamento do menú de configuración do complemento do menú Ferramentas
  ao menú Preferencias do NVDA.

## Cambios para a versión 2.1 ##

* Engadido un Script para falar o seguinte ponto de corte co Control+Frecha
  Dereita;
* Engadido un Script para falar o ponto de corte anterior co Control+Frecha
  Esquerda;
* Engadido un Script para falar o desprazamento de 4 centésimas de segundo
  cara adiante co Shift+Frecha Dereita;
* Engadido un Script para falar o desprazamento de 4 centésimas de segundo
  cara atrás co Shift+Frecha Esquerda;
* Corrección do summary do complemento "para mp3DirectCut" a "mp3DirectCut".

## Cambios para a versión 2.0 ##

* Engadido un Script para saber o tempo restante co "Control+Shift+R";
* Corrección da lectura das duracións incluindo as horas;
* Engadida a posibilidade de diferenciar milésimas ou centésimas de
  segundos.

## Cambios para a versión 1.1 ##

* Engadida a posibilidade de incluír a categoría mp3DirectCut nos Xestos de
  Entrada;

    * So serán visibles durante a utilización do programa mp3DirectCut.

* Engadida a posibilidade para activar ou desactivar as mensaxes
  automáticas, no menú Ferramentas do NVDA, elemento 'configuración de
  mp3DirectCut';

## Cambios para a versión 1.0 ##

* versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
