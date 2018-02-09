# mp3DirectCut #

*	 Autores: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Baixar [versão estável][1]
*	 Baixar [versão de desenvolvimento][2]

# Apresentação: #

Este extra melhora a acessibilidade do software mp3DirectCut com o NVDA.

Foi testado com versões do mp3DirectCut variando da 212 até à 223.

## Teclas de atalho: ##

Este extra oferece os seguintes comandos:

* B
* Usado para confirmar a colocação correcta do marcador do início da selecção B.
* Ctrl+Shift+B
* Usado para indicar a posição do marcador do início da selecção B.
* Pressionado duas vezes dá-lhe a duração da selecção.
* Ctrl+Shift+D
* Dá a duração desde o início do ficheiro até a posição actual do cursor de reprodução.
* Pressionado duas vezes dá-lhe a duração total.
* Ctrl+R
* Confirma que a selecção foi cancelada.
* Ctrl+Shift+R
* Dá o tempo restante da posição actual do cursor de reprodução até ao final do ficheiro.
* Ctrl+Shift+E
* Usado para indicar a posição do marcador do final da selecção N.
* pressionado duas vezes dá posições recapitulativas B e N e a duração da seleção.
* Ctrl+Shift+P
* Dá a referência da parte real e do número total de peças no ficheiro actual.
* Ctrl+Shift+Espaço
* Usado para determinar o nível actual do vu-meter, durante a gravação.
* Pressionado duas vezes repõe.
*	Seta para baixo
* Permite ver a posição actual do cabeçalho de reprodução.
* Este comando também posiciona o cursor na posição do marcador do final da selecção N, enquanto dá a localização deste marcador se uma selecção foi feita.
* Na caixa de diálogo de volume, vocalise o próximo valor que pode ser alcançado geralmente com seta para baixo.
* Esse valor não é vocalizado por padrão.
*	End
* Move o cursor de reprodução para o final do ficheiro actual e dá o tempo total.
*	home
* Move o cursor de reprodução para o início do ficheiro actual.
*	Seta esquerda
* Vamos fazer um breve retorno de um segundo durante a reprodução, enquanto damos a duração actual.
* Esta duração é configurável nas opções do mp3directcut.
* N
* Usado para confirmar a colocação correcta do marcador no final da selecção N.
* Página para baixo
* Dá um salto em frente de 10 segundos durante a reprodução, enquanto dá a duração actual.
* Esta duração é configurável nas opções do mp3directcut.
*	Página para cima
* Vamos fazer um retorno de volta de 10 segundos durante a reprodução, enquanto damos a duração actual.
* Esta duração é configurável nas opções do mp3directcut.
* R
* Permite preparar uma gravação e pode pressionar a barra de espaço para começá-la.
*	Seta direita
* Permite fazer um breve recuo de um segundo durante a reprodução, enquanto dá a duração actual.
* Esta duração é configurável nas opções do mp3directcut.
* Ctrl + Seta direita
* Move para o próximo ponto de divisão, enquanto dá a duração actual.
* Ctrl + Seta para a esquerda
* Move para o ponto de divisão anterior, enquanto dá a duração actual.
* Shift + Seta direita
* Permite fazer um breve avanço de quatro centésimos de segundos durante a reprodução, enquanto dá a duração actual.
* Shift + Seta para a esquerda
* Permite fazer um breve atraso de quatro centésimos de segundos durante a reprodução, enquanto dá a duração actual.
* S
* Usado para parar a leitura e dar a duração actual.
* Espaço
* Se a gravação estiver preparada, começa a gravação.
* Se uma gravação estiver em andamento, para-a posicionando o cursor no início.
* Se um ficheiro estiver carregado, começa a leitura.
* Se uma leitura estiver em andamento, permite fazer uma pausa dando a duração actual.
* Se a leitura estiver pausada, permite reiniciar a leitura a partir da localização actual.
* Seta para cima
* Permite ver a posição atual do cabeçalho de reprodução.
* Este comando também posiciona o cursor na localização do marcador do início da selecção B, enquanto dá a localização desse marcador se uma selecção foi feita.
* Na caixa de diálogo de volume, vocaliza o valor anterior que pode ser alcançado geralmente com a seta para cima.
* Esse valor não é vocalizado por padrão.
* NVDA + H
* Permite abrir a ajuda deste extra.

## Alterações para a versão 4.0 ##

*	 Adicionada a compatibilidade do extra com o Python 2.7 e 3;
*	 Corrigido um bug com caminhos de localização do extra que contenham
   caracteres não-ASCII.

## Alterações para a versão 3.0 ##

*	 Utilizou-se o módulo gui.guiHelper para garantir a aparência correcta do
   diálogo de configuração do extra;
*	 Passou a usar-se o comando format em vez de %s para seqüências de
   caracteres formatadas;
*	 Foram usadas as necessárias directrizes para implementação.

## Alterações para a versão 2.3 ##

*	 Adicionada a licença GPL ao addon;
*	 Alterado o atalho do script que fornece o fim da selecção de Ctrl + Shift
   + N para Ctrl + Shift + E porque Ctrl + Shift + N não funciona com as
   versões mais recentes do mp3DirectCut;
*	 Adicionado um script para confirmar que a selecção foi cancelada com
   'Ctrl+r';
*	 Foram feitas algumas correcções no código do appModule 'mp3directcut.py'.

## Alterações para a versão 2.2 ##

*	 Correcção dos scripts que dão os locais dos marcadores de selecção.

## Alterações para a versão 2.1.1 ##

*	 Foi removido o script que dava o tempo total e adicionada esta informação
   ao script que fornece o tempo decorrido;
*	 Adicionada a capacidade de activar ou desactivar os anúncios relacionados
   à tecla de espaço nas opções de configuração do módulo, separadamente de
   outros anúncios;
*	 Adicionada a capacidade de activar ou desactivar o anúncio da colocação
   das marcas de selecção nas opções de configuração do módulo;
*	 Adicionado o anúncio da parte actual ao passar pelos pontos de corte;
*	 Correcção de anúncios relacionados a teclas verticais;
*	 Adicionado um script para abrir a ajuda do extra actual com 'NVDA + H';
*	 Deslocamento do menu de configuração do extra do menu Ferramentas para o
   menu Preferências do NVDA.

## Alterações para a versão 2.1 ##

*	 Adicionado um script para vocalizar mover-se para o próximo ponto de
   divisão com control+seta para a direita;
*	 Adicionando um script para vocalizar mover-se para o ponto de divisão
   anterior com Control+Seta para a esquerda;
*	 Adicionado um script para vocalizar o avanço de 4 centésimas de segundo,
   com Shift+Seta para a direita;
*	 Adicionado um script para vocalizar o retrocesso de 4 centésimas de
   segundo, com Shift+Seta para a esquerda;
*	 Correção do resumo do addon de 'para mp3DirectCut' para 'mp3DirectCut'.

## Alterações para a versão 2.0: ##

*	 Adicionado um script para saber o tempo restante com 'Control+Shift+R';
*	 Fixada a uração da leitura, incluindo horas;
*	 Adicionada a Habilidade para diferenciar milésimos ou centésimos de
   segundo.

## Alterações para a versão 1.1: ##

*	* Adicionada a capacidade de incluir a categoria mp3DirectCut nomenu definir comandos;
* 	Eles serão visíveis somente durante o uso do software mp3DirectCut.
* 	Adicionada a habilidade para activar ou desactivar mensagens automáticas, no menu de ferramentas do NVDA, item 'configuração do mp3DirectCut';

## Alterações para a versão 1.0 ##

*	 Versão inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
