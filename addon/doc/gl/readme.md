# mp3DirectCut

* Autor(es): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Presentación #

Este complemento mellora a accesibilidade do programa mp3DirectCut con NVDA.

Probouse con versións de mp3DirectCut desde a 212 ata a 233.

## Atallos de teclado ##

Este complemento ofrece os seguintes comandos:

* B

    * Utilízase para confirmar a colocación correcta do marcador de inicio da selección B.

* Ctrl+Shift+B

    * Utilízase para indicar a posición do marcador de inicio da selección B.
    * Unha dobre pulsación permíteche saber a duración da selección.

* Ctrl+Shift+D

    * Dá a duración desde o principio do arquivo ata a posición actual do cursor de reprodución.
    * Unha dobre pulsación permíteche saber a duración total.

* Ctrl+R

    * Confirma que se cancelou a selección.

* Ctrl+Shift+R

    * Dá o tempo restante desde a posición actual do cursor de reprodución ata o final do arquivo.

* Ctrl+Shift+E

    * Utilízase para indicar a posición do marcador de fin da selección N.
    * Unha dobre pulsación dá un resumo das posicións B e N, e a duración da selección.

* Ctrl+Shift+P

    * Dá a referencia da parte actual e o número total de partes no arquivo actual.

* Ctrl+Shift+Space

    * Utilízase para determinar o nivel actual do indicador de volume (vúmetro) durante a gravación.
    * Unha dobre pulsación reiníciao.

* Flecha abaixo

    * Permíteche ver a posición actual do cursor de reprodución.
    * Este comando tamén sitúa o cursor na localización do marcador de fin da selección N, mentres dá a localización deste marcador se se fixo unha selección.
    * No cadro de diálogo de volume, vocaliza o seguinte valor ao que se pode chegar xeralmente coa frecha abaixo.
    * Este valor non se vocaliza por defecto.

* End

    * Move o cursor de reprodución ao final do arquivo actual e dá o tempo total.

* Home

    * Move o cursor de reprodución ao principio do arquivo actual.

* Flecha esquerda

    * Permite facer un breve regreso atrás dun segundo durante a reprodución, mentres dá a duración actual.
    * Esta duración é configurable nas opcións de mp3DirectCut.

* N

    * Utilízase para confirmar a colocación correcta do marcador de fin da selección N.

* Page Down

    * Permite facer un salto adiante de 10 segundos durante a reprodución, mentres dá a duración actual.
    * Esta duración é configurable nas opcións de mp3DirectCut.

* Page Up

    * Permite facer un regreso atrás de 10 segundos durante a reprodución, mentres dá a duración actual.
    * Esta duración é configurable nas opcións de mp3DirectCut.

* R

    * Permite preparar unha gravación e saber se podes premer a barra espazadora para comezar.

* Flecha dereita

    * Permite facer un breve avance dun segundo durante a reprodución, mentres dá a duración actual.
    * Esta duración é configurable nas opcións de mp3DirectCut.

* Ctrl+Flecha dereita

    * Móvese ao seguinte punto de división, mentres dá a duración actual.

* Ctrl+Flecha esquerda

    * Móvese ao punto de división anterior, mentres dá a duración actual.

* Shift+Flecha dereita

    * Permite facer un breve avance de catro centésimas de segundo durante a reprodución, mentres dá a duración actual.

* Shift+Flecha esquerda

    * Permite facer un breve retroceso de catro centésimas de segundo durante a reprodución, mentres dá a duración actual.

* S

    * Utilízase para deter a lectura e dar a duración actual.

* Space

    * Se a gravación está lista, inicia esta gravación.
    * Se hai unha gravación en curso, deténa posicionando o cursor ao principio.
    * Se hai un arquivo cargado, inicia a lectura.
    * Se hai unha lectura en curso, permite facer unha pausa dando a duración actual.
    * Se a lectura está en pausa, permite reiniciar a lectura desde a localización actual.

* Flecha arriba

    * Permíteche ver a posición actual do cursor de reprodución.
    * Este comando tamén sitúa o cursor na localización do marcador de inicio da selección B, mentres dá a localización deste marcador se se fixo unha selección.
    * No cadro de diálogo de volume, vocaliza o valor anterior ao que se pode chegar xeralmente coa frecha arriba.
    * Este valor non se vocaliza por defecto.

* NVDA+H

    * Permite abrir a axuda do complemento actual.

## Compatibilidade ##

* Este complemento é compatible coas versións de NVDA desde a 2019.3 en diante.

## Cambios para 20240327.0.0

* Corrixiuse un erro que causaba un erro de rexistro ao recargar os complementos, grazas a Rob, da lista de correo nvda-addons;

## Cambios para 20240326.0.0

* Actualizouse a compatibilidade para nvda-2024.1.;
* Eliminouse a ligazón de descarga do readme, a ligazón de descarga para futuras actualizacións agora só estará dispoñible desde a tenda de complementos.

## Cambios para 20231229.0.0 ##

* Engadiuse unha implementación compatible cara atrás para admitir o modo de fala baixo demanda, que pronto estará dispoñible con nvda-2024.1.

## Cambios para 20231007.0.0 ##

* Despois de colocar os puntos de corte e despois de abrir a xanela de propiedades de corte con "Ctrl+N", engadiuse accesibilidade ao título desta xanela indicando o índice da parte.
* No modo de lectura, despois de mover os marcadores de inicio ou fin das seleccións coas teclas 1 a 6 do teclado alfanumérico, engadiuse o inicio automático da lectura desde a nova posición;
* Corrixiuse un erro que ocorría ao consultar o tempo restante con "control+shift+r" desde o principio da pista.

## Cambios para 20230728.0.0 ##

* Aplicáronse as regras de flake8 e mypy ao código;
* Cambiouse a versión mínima admitida de NVDA á 2019.3 para admitir as anotacións introducidas en Python 3.

## Cambios para 20230607.0.0 ##

* Engadíronse os seguintes fluxos de traballo:
 * auto-update-translations - para actualizar automaticamente as traducións desde o sistema de tradución de NVDA.
 * release-on-tag..yaml: para construír e publicar o complemento axiña que se envíe unha nova etiqueta (tag);
 * manual-release.yaml: para construír e lanzar novas versións del complemento manualmente.
* Traducións actualizadas.

## Cambios para a versión 20230508.0.0 e posteriores ##

* Cambiouse o número de versión, a versión mínima de NVDA e a ligazón de descarga segundo as convencións/requisitos da tenda.

## Cambio para a versión 20.12 ##

* Detense a voz durante a gravación e a lectura para as últimas versións de mp3DirectCut;
* Corrixiuse a lectura do tempo restante para novas versións de NVDA que usan Python 3.

## Cambio para a versión 19.02 ##

* Engadiuse a configuración do complemento no panel de axustes dispoñible desde nvda 2018.2;
* Cambiouse a numeración das versións usando AA.MM (o ano en 2 díxitos, seguido dun punto, seguido do mes en 2 díxitos);
* Engadiuse compatibilidade co novo formato de versións de complementos, aparecido desde nvda 2019.1.

## Cambio para a versión 4.0 ##

* Engadiuse a compatibilidade do complemento tanto con Python 2.7 como con 3;
* Corrixiuse un erro cos camiños do complemento que conteñen caracteres non ASCII.

## Cambio para a versión 3.0 ##

* Utilizouse o módulo gui.guiHelper para garantir a aparencia correcta do diálogo de configuración do complemento;
* Utilizouse format en lugar de %s para as cadeas con formato;
* Utilizouse o cumprimento das pautas para a implementación.

## Cambio para a versión 2.3 ##

* Engadiuse a licenza GPL ao complemento;
* Cambiouse o atallo do script que dá o final da selección de Ctrl + Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N no funciona coas últimas versións de mp3DirectCut;
* Engadiuse un script para confirmar que a selección se cancelou con 'Ctrl+r';
* Fixéronse algunhas correccións no código do appModule 'mp3directcut.py'.

## Cambio para a versión 2.2 ##

* Corrección dos scripts que dan as localizacións dos marcadores de selección.

## Cambio para a versión 2.1.1 ##

* Eliminouse o script que dá o tempo total e engadiuse esta información ao script que dá o tempo transcorrido;
* Engadiuse a posibilidade de activar ou desactivar os anuncios relacionados coa tecla espazo nas opcións de configuración do módulo, por separado doutros anuncios;
* Engadiuse a posibilidade de activar ou desactivar o anuncio de colocación dos marcadores de selección nas opcións de configuración do módulo;
* Engadiuse o anuncio da parte actual ao moverse polos puntos de corte;
* Corrección dos anuncios relacionados coas teclas verticais;
* Engadiuse un script para abrir a axuda do complemento actual con 'NVDA+H';
* Desprazamento do menú de configuración do complemento desde o menú Ferramentas ao menú Preferencias de NVDA.

## Cambio para a versión 2.1 ##

* Engadiuse un script para vocalizar o movemento ao seguinte punto de división con Control+Flecha dereita;
* Engadiuse un script para vocalizar o movemento ao punto de división anterior con Control+Flecha esquerda;
* Engadiuse un script para vocalizar o desprazamento de 4 centésimas de segundo cara adiante, con Shift+Flecha dereita;
* Engadiuse un script para vocalizar o desprazamento de 4 centésimas de segundo cara atrás, con Shift+Flecha esquerda;
* Corrección do resumo do complemento de 'for mp3DirectCut' a 'mp3DirectCut'.

## Cambio para a versión 2.0 ##

* Engadiuse un script para saber o tempo restante con 'Control Shift R';
* Corrixiuse a lectura de duracións que inclúen horas;
* Engadiuse a capacidade de diferenciar milésimas ou centésimas de segundo.

## Cambio para a versión 1.1 ##

* Engadiuse a posibilidade de incluír a categoría mp3DirectCut nos Xestos de Entrada;

    * Serán visibles só durante o uso do programa mp3DirectCut.

* Engadiuse a posibilidade de activar ou desactivar as mensaxes automáticas, no menú de ferramentas de NVDA, elemento 'configuración de mp3DirectCut';

## Cambio para a versión 1.0 ##

* Versión inicial.
