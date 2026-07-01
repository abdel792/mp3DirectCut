# mp3DirectCut

* Autor(es): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Apresentação #

Este suplemento melhora a acessibilidade do programa mp3DirectCut com o NVDA.

Foi testado com versões do mp3DirectCut que vão desde a 212 até à 233.

## Atalhos de teclado ##

Este suplemento oferece os seguintes comandos:

* B

    * Utilizado para confirmar o posicionamento correto do marcador de início da seleção B.

* Ctrl+Shift+B

    * Utilizado para indicar a posição do marcador de início da seleção B.
    * Uma dupla pressão permite obter a duração da seleção.

* Ctrl+Shift+D

    * Dá a duração desde o início do arquivo até à posição atual do cursor de reprodução.
    * Uma dupla pressão permite obter a duração total.

* Ctrl+R

    * Confirma que a seleção foi cancelada.

* Ctrl+Shift+R

    * Dá o tempo restante desde a posição atual do cursor de reprodução até ao fim do arquivo.

* Ctrl+Shift+E

    * Utilizado para indicar a posição do marcador de fim da seleção N.
    * Uma dupla pressão dá um resumo das posições B e N, e a duração da seleção.

* Ctrl+Shift+P

    * Dá a referência da parte atual e o número total de partes no arquivo atual.

* Ctrl+Shift+Space

    * Utilizado para determinar o nível atual do indicador de volume (vu-meter) durante a gravação.
    * Uma dupla pressão reinicia-o.

* Seta para Baixo

    * Permite ver a posição atual do cursor de reprodução.
    * Este comando também posiciona o cursor na localização do marcador de fim da seleção N, enquanto dá a localização deste marcador se tiver sido feita uma seleção.
    * Na caixa de diálogo do volume, vocaliza o valor seguinte que pode ser alcançado geralmente com a seta para baixo.
    * Este valor não é vocalizado por predefinição.

* End

    * Move o cursor de reprodução para o fim do arquivo atual e dá o tempo total.

* Home

    * Move o cursor de reprodução para o início do arquivo atual.

* Seta para a Esquerda

    * Permite fazer um breve regresso atrás de um segundo durante a reprodução, enquanto dá a duração atual.
    * Esta duração é configurável nas opções do mp3DirectCut.

* N

    * Utilizado para confirmar o posicionamento correto do marcador de fim da seleção N.

* Page Down

    * Permite fazer um salto em frente de 10 segundos durante a reprodução, enquanto dá a duração atual.
    * Esta duração é configurável nas opções do mp3DirectCut.

* Page Up

    * Permite fazer um regresso atrás de 10 segundos durante a reprodução, enquanto dá a duração atual.
    * Esta duração é configurável nas opções do mp3DirectCut.

* R

    * Permite preparar uma gravação e saber se pode premir a barra de espaço para iniciar.

* Seta para a Direita

    * Permite fazer um breve avanço de um segundo durante a reprodução, enquanto dá a duração atual.
    * Esta duração é configurável nas opções do mp3DirectCut.

* Ctrl+Seta para a Direita

    * Move para o ponto de divisão seguinte, enquanto dá a duração atual.

* Ctrl+Seta para a Esquerda

    * Move para o ponto de divisão anterior, enquanto dá a duração atual.

* Shift+Seta para a Direita

    * Permite fazer um breve avanço de quatro centésimos de segundo durante a reprodução, enquanto dá a duração atual.

* Shift+Seta para a Esquerda

    * Permite fazer um breve retrocesso de quatro centésimos de segundo durante a reprodução, enquanto dá a duração atual.

* S

    * Utilizado para parar a leitura e dar a duração atual.

* Space

    * Se a gravação estiver pronta, inicia esta gravação.
    * Se uma gravação estiver em curso, para-a posicionando o cursor no início.
    * Se um arquivo estiver carregado, inicia a leitura.
    * Se uma leitura estiver em curso, permite fazer uma pausa dando a duração atual.
    * Se a leitura estiver em pausa, permite reiniciar a leitura a partir da localização atual.

* Seta para Cima

    * Permite ver a posição atual do cursor de reprodução.
    * Este comando também posiciona o cursor na localização do marcador de início da seleção B, enquanto dá a localização deste marcador se tiver sido feita uma seleção.
    * Na caixa de diálogo do volume, vocaliza o valor anterior que pode ser alcançado geralmente com a seta para cima.
    * Este valor não é vocalizado por predefinição.

* NVDA+H

    * Permite abrir a ajuda do suplemento atual.

## Compatibilidade ##

* Este suplemento é compatível com as versões do NVDA desde a 2019.3 em diante.

## Alterações para 20240327.0.0

* Corrigido um erro que causava um erro de registo ao recarregar os suplementos, graças a Rob, da lista de correio nvda-addons;

## Alterações para 20240326.0.0

* Atualizada a compatibilidade para o nvda-2024.1.;
* Eliminada a ligação de transferência do readme, a ligação de transferência para futuras atualizações estará agora apenas disponível a partir da loja de suplementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação compatível com versões anteriores para suportar o modo de fala sob pedido, que estará brevemente disponível com o nvda-2024.1.

## Alterações para 20231007.0.0 ##

* Após colocar os pontos de corte e após abrir a janela de propriedades de corte com "Ctrl+N", foi adicionada acessibilidade ao título desta janela indicando o índice da parte.
* No modo de leitura, após mover os marcadores de início ou fim de seleção com as teclas 1 a 6 do teclado alfanumérico, foi adicionado o início automático da leitura a partir da nova posição;
* Corrigido um erro que ocorria ao consultar o tempo restante com "control+shift+r" a partir do início da faixa.

## Alterações para 20230728.0.0 ##

* Aplicadas as regras flake8 e mypy ao código;
* Alterada a versão mínima suportada do NVDA para 2019.3 para suportar as anotações introduzidas no Python 3.

## Alterações para 20230607.0.0 ##

* Adicionados os seguintes fluxos de trabalho (workflows):
 * auto-update-translations - para atualizar automaticamente as traduções a partir do sistema de tradução do NVDA.
 * release-on-tag..yaml: para construir e publicar o suplemento assim que uma nova etiqueta (tag) for enviada;
 * manual-release.yaml: para construir e lançar novas versões do suplemento manualmente.
* Traduções atualizadas.

## Alterações para a versão 20230508.0.0 e posteriores ##

* Alterado o número de versão, a versão mínima do NVDA e a ligação de transferência de acordo com as convenções/requisitos da loja.

## Alteração para a versão 20.12 ##

* Interrupção da voz durante a gravação e a leitura para as últimas versões do mp3DirectCut;
* Corrigida a leitura do tempo restante para novas versões do NVDA que utilizam o Python 3.

## Alteração para a versão 19.02 ##

* Adicionada a configuração do suplemento no painel de definições disponível desde o nvda 2018.2;
* Alterada a numeração das versões utilizando AA.MM (o ano em 2 dígitos, seguido de um ponto, seguido do mês em 2 dígitos);
* Adicionada compatibilidade com o novo formato de numeração de versões de suplementos, surgido desde o nvda 2019.1.

## Alteração para a versão 4.0 ##

* Adicionada a compatibilidade do suplemento tanto com o Python 2.7 como com o 3;
* Corrigido um erro com os caminhos do suplemento que contêm carateres não ASCII.

## Alteração para a versão 3.0 ##

* Utilizado o módulo gui.guiHelper para garantir a aparência correta da caixa de diálogo de configuração do suplemento;
* Utilizado format em vez de %s para as cadeias de carateres formatadas;
* Utilizada a conformidade com as diretrizes de implementação.

## Alteração para a versão 2.3 ##

* Adicionada a licença GPL ao suplemento;
* Alterado o atalho do script que dá o fim da seleção de Ctrl + Shift + N para Ctrl + Shift + E porque Ctrl + Shift + N não funciona com as últimas versões do mp3DirectCut;
* Adicionado um script para confirmar que a seleção foi cancelada com 'Ctrl+r';
* Efetuadas algumas correções no código do appModule 'mp3directcut.py'.

## Alteração para a versão 2.2 ##

* Correção dos scripts que dão as localizações dos marcadores de seleção.

## Alteração para a versão 2.1.1 ##

* Remoção do script que dá o tempo total e adição desta informação ao script que dá o tempo decorrido;
* Adicionada a possibilidade de ativar ou desativar os anúncios relacionados com a barra de espaço nas opções de configuração do módulo, separadamente de outros anúncios;
* Adicionada a possibilidade de ativar ou desativar o anúncio de posicionamento dos marcadores de seleção nas opções de configuração do módulo;
* Adição do anúncio da parte atual ao mover-se através do pontos de corte;
* Correção dos anúncios relacionados com as teclas verticais;
* Adição de um script para abrir a ajuda do suplemento atual com 'NVDA+H';
* Deslocação do menu de configuração do suplemento do menu Ferramentas para o menu Preferências do NVDA.

## Alteração para a versão 2.1 ##

* Adição de um script para vocalizar a deslocação para o ponto de divisão seguinte com Control+Seta para a Direita;
* Adição de um script para vocalizar a deslocação para o ponto de divisão anterior com Control+Seta para a Esquerda;
* Adição de um script para vocalizar a deslocação de 4 centésimos de segundo para a frente, com Shift+Seta para a Direita;
* Adição de um script para vocalizar a deslocação de 4 centésimos de segundo para trás, com Shift+Seta para a Esquerda;
* Correção do resumo do suplemento de 'for mp3DirectCut' para 'mp3DirectCut'.

## Alteração para a versão 2.0 ##

* Adição de um script para saber o tempo restante com 'Control Shift R';
* Corrigida a leitura de durações incluindo horas;
* Adicionada a capacidade de diferenciar milésimos ou centésimos de segundo.

## Alteração para a versão 1.1 ##

* Adicionada a possibilidade de incluir a categoria mp3DirectCut nos Gestos de Entrada;

    * Serão visíveis apenas durante a utilização do programa mp3DirectCut.

* Adicionada a possibilidade de ativar ou desativar as mensagens automáticas, no menu de ferramentas do NVDA, item 'Configuração do mp3DirectCut';

## Alteração para a versão 1.0 ##

* Versão inicial.
