# mp3DirectCut #

* Autores: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Baixar [versão estável][1]
* Baixar [versão de desenvolvimento][2]

# Apresentação: #

Este extra melhora a acessibilidade do software mp3DirectCut com o NVDA.

Foi testado com versões do mp3DirectCut variando da 212 até à 223.

## Teclas de atalho: ##

Este extra oferece os seguintes comandos:

* B

    * Usado para confirmar o marcador inicial da selecção b.

* Ctrl+Shift+B

    * Usado para indicar a posição do marcador do início da selecção B.
    * Se pressionar duas vezes, obterá a duração da selecção.

* Ctrl+Shift+D

    * Diz a duração desde o início do ficheiro até a posição actual do
      cursor de reprodução.
    * Pressionado duas vezes, diz a duração total

* Ctrl+R

    * Confirma que a selecção foi cancelada.

* Ctrl+Shift+R

    * Diz o tempo que falta, desde a posição do cursor de reprodução até ao
      final do ficheiro.

* Ctrl+Shift+E

    * Usado para indicar o marcador de  final da selecção n.
    * Pressionado duas vezes, volta a dizer as posições de b e de n e a
      duração da selecção.

* Ctrl+Shift+P

    * Diz a referência da parte actual e indica o total de partes no
      ficheiro

* Ctrl+Shift+Space

    * Usado para determinar o nível actual do medidor de vuo, durante a
      gravação.
    * Pressionado duas vezes, apaga.

* Seta para baixo

    * Permite ver a posição actual do indicador de reprodução.
    * Este comando também coloca o cursor na posição do marcador do final da
      selecção N, dizendo a sua posição, se tiver sido feita uma selecção.
    * Na caixa de diálogo de volume, oiça o próximo valor que pode ser
      obtido geralmente com seta para baixo.
    * Este valor não é falado, por padrão.

* fim

    * Move o cursor de reprodução para o final do ficheiro e diz o tempo
      total.

* Início

    * Move o cursor de reprodução para o início do ficheiro actual.

* Seta esquerda

    * Retrocede um segundo na reprodução e diz a duração.
    * Esta duração é configurável nas opções do programa.

* N

    * Usado para confirmar a posição correcta do marcador de fim de
      selecção, n.

* Página para baixo

    * Dá um avanço de dez segundos na reprodução, dizendo a duração. 
    * Esta duração é configurável nas opções do programa.

* Página para cima

    * Dá um retrocesso de dez segundos na reprodução, dizendo a duração.
    * Esta duração é configurável nas opções do programa.

* R

    * Permite preparar uma gravação, que deverá ser iniciada com uma barra
      de espaços.

* Seta para a direita

    * Avança um segundo na reprodução, dizendo a duração.
    * Esta duração é configurável nas opções do programa.

* Ctrl+seta para a direita

    * Move o cursor  para o próximo ponto de divisão, dizendo a duração
      actual.

* Ctrl+seta para esquerda

    * Move o cursor para o ponto de divisão anterior, dizendo a duração
      actual.

* Shift+seta para a direita

    * faz um breve avanço de quatro centésimos de segundos durante a
      reprodução, lendo a duração actual.

* shift+seta para a esquerda

    * Faz um breve retrocesso de quatro centésimos de segundo durante a
      reprodução, lendo a duração actual.

* S

    * Para a leitura e diz a duração actual.

* Espaço

    * Se a gravação estiver pronta, inicia-a.
    * Se estiver a ser feita uma gravação, para-a e coloca o cursor no
      início.
    * Se um ficheiro estiver carregado, inicia a reprodução.
    * Se uma reprodução estiver a decorrer, faz uma pausa e lê a duração.
    * Se uma reprodução estiver pausada, reinicia-a na posição actual do
      cursor.

* Seta para cima

    * Permite ver a posição actual do indicador de reprodução.
    * Este comando também posiciona o cursor na localização do marcador do
      início da selecção B, dizendo a sua localização, se tiver sido
      efectuada uma seleção.
    * Na caixa de diálogo de volume, verbalize o valor anterior que pode ser
      conseguido se pressionar seta para cima.
    * Este valor não é falado, por padrão.

* NVDA+H

    * Permite abrir a ajuda do extra actual.

## Compativilidade. ##

* Este extra é compatível com as versões do NVDA desde a 2016.4 até a
  2019.1.

## Alterações para a versão 19.0.2 ##

* Acrescentada a configuração do extra no menu de configurações disponível
  desde o nvda 2018.2;
* Alterada a Numeração de versão, usando AA.MM (O ano em 2 dígitos, seguido
  por um ponto, seguido pelo mês em 2 dígitos);
* Acrescentada a compatibilidade com o novo formato de versão do extra,
  surgido desde o nvda 2019.1.

## Alterações para a versão 4.0 ##

* Adicionada a compatibilidade do extra com o Python 2.7 e 3;
* Corrigido um bug com caminhos de localização do extra que contenham
  caracteres não-ASCII.

## Alterações para a versão 3.0 ##

* Utilizou-se o módulo gui.guiHelper para garantir a aparência correcta do
  diálogo de configuração do extra;
* Passou a usar-se o comando format em vez de %s para seqüências de
  caracteres formatadas;
* Foram usadas as necessárias directrizes para implementação.

## Alterações para a versão 2.3 ##

* Adicionada a licença GPL ao addon;
* Alterado o atalho do script que fornece o fim da selecção de Ctrl + Shift
  + N para Ctrl + Shift + E porque Ctrl + Shift + N não funciona com as
  versões mais recentes do mp3DirectCut;
* Adicionado um script para confirmar que a selecção foi cancelada com
  'Ctrl+r';
* Foram feitas algumas correcções no código do appModule 'mp3directcut.py'.

## Alterações para a versão 2.2 ##

* Correcção dos scripts que dão os locais dos marcadores de selecção.

## Alterações para a versão 2.1.1 ##

* Foi removido o script que dava o tempo total e adicionada esta informação
  ao script que fornece o tempo decorrido;
* Adicionada a capacidade de activar ou desactivar os anúncios relacionados
  à tecla de espaço nas opções de configuração do módulo, separadamente de
  outros anúncios;
* Adicionada a capacidade de activar ou desactivar o anúncio da colocação
  das marcas de selecção nas opções de configuração do módulo;
* Adicionado o anúncio da parte actual ao passar pelos pontos de corte;
* Correcção de anúncios relacionados a teclas verticais;
* Adicionado um script para abrir a ajuda do extra actual com 'NVDA + H';
* Deslocamento do menu de configuração do extra do menu Ferramentas para o
  menu Preferências do NVDA.

## Alterações para a versão 2.1 ##

* Adicionado um script para vocalizar mover-se para o próximo ponto de
  divisão com control+seta para a direita;
* Adicionando um script para vocalizar mover-se para o ponto de divisão
  anterior com Control+Seta para a esquerda;
* Adicionado um script para vocalizar o avanço de 4 centésimas de segundo,
  com Shift+Seta para a direita;
* Adicionado um script para vocalizar o retrocesso de 4 centésimas de
  segundo, com Shift+Seta para a esquerda;
* Correção do resumo do addon de 'para mp3DirectCut' para 'mp3DirectCut'.

## Alterações para a versão 2.0: ##

* Adicionado um script para saber o tempo restante com 'Control+Shift+R';
* Fixada a uração da leitura, incluindo horas;
* Adicionada a Habilidade para diferenciar milésimos ou centésimos de
  segundo.

## Alterações para a versão 1.1: ##

* Acrescentada a capacidade de incluir a categoria mp3DirectCut na entrada
  de comandos;

    * Esses comandos serão visíveis somente durante o uso do mp3DirectCut.

* Adicionada a capacidade de activar ou desactivar o anúncio de mensagens
  automáticas, no menu de ferramentas do NVDA, no item 'Configurações do
  mp3DirectCut';

## Alterações para a versão 1.0 ##

* Versão inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
