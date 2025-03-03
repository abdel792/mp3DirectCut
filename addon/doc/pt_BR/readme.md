# mp3DirectCut #

* Autor(es): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Apresentação #

Esse complemento melhora a acessibilidade do software mp3DirectCut com o
NVDA.

Foi testado com versões do mp3DirectCut variando da 212 até à 223.

## Atalhos do teclado ##

Este complemento oferece os seguintes comandos:

* B

    * Usado para confirmar o posicionamento correto do marcador do início da
      seleção B.

* Ctrl+Shift+B

    * Usado para indicar a posição do marcador do início da seleção B.
    * Pressionado duas vezes diz a duração da seleção.

* Ctrl+Shift+D

    * Diz a duração desde o início do arquivo até a posição atual do cursor
      de reprodução.
    * Pressionado duas vezes diz a duração total.

* Ctrl+R

    * Confirma que a seleção foi cancelada.

* Ctrl+Shift+R

    * Diz o tempo restante da posição atual do cursor de reprodução até o
      final do arquivo.

* Ctrl+Shift+E

    * Usado para indicar a posição do marcador no final da seleção N.
    * Pressionado duas vezes recapitula dizendo posições B e N, e a duração
      da seleção.

* Ctrl+Shift+P

    * Diz a referência da parte atual e o número total de partes no arquivo
      presente.

* Ctrl+Shift+Espaço

    * Usado para determinar o nível atual do medidor de volume, durante a
      gravação.
    * Pressionado duas vezes redefine-o.

* Seta para Baixo

    * Permite ver a posição atual da cabeça (indicador) de reprodução.
    * Este comando também coloca o cursor na posição do marcador do final da
      seleção N, enquanto dizendo o local desse marcador se uma seleção foi
      feita.
    * Na caixa de diálogo de volume, vocaliza o próximo valor que pode ser
      alcançado geralmente com a seta para baixo.
    * Este valor não é vocalizado por padrão.

* End

    * Move o cursor de reprodução ao final do arquivo atual e diz o tempo
      total.

* Home

    * Move o cursor de reprodução ao início do arquivo atual.

* Seta para Esquerda

    * Retrocede brevemente um segundo durante a reprodução, dizendo a
      duração atual.
    * Esta duração é configurável nas opções do mp3directcut.

* N

    * Usado para confirmar a posição correta do marcador de fim de seleção
      N.

* Page Down

    * Avança 10 segundos durante a reprodução, dizendo a duração atual.
    * Esta duração é configurável nas opções do mp3directcut.

* Page Up

    * Retorna 10 segundos durante a reprodução, dizendo a duração atual.
    * Esta duração é configurável nas opções do mp3directcut.

* R

    * Permite preparar uma gravação e que você pode pressionar a barra de
      espaço para iniciar.

* Seta para Direita

    * Avança brevemente um segundo durante a reprodução, dizendo a duração
      atual.
    * Esta duração é configurável nas opções do mp3directcut.

* Ctrl+Seta para Direita

    * Move para o próximo ponto de divisão, dizendo a duração atual.

* Ctrl+Seta para Esquerda

    * Move para o ponto de divisão anterior, dizendo a duração atual.

* Shift+Seta para Direita

    * Faz um breve avanço de quatro centésimos de segundos durante a
      reprodução, dizendo a duração atual.

* Shift+Seta para Esquerda

    * Faz um breve retrocesso de quatro centésimos de segundos durante a
      reprodução, dizendo a duração atual.

* S

    * Usado para interromper a leitura e dizer a duração atual.

* Espaço

    * Se a gravação estiver pronta, inicia esta gravação.
    * Se uma gravação estiver em andamento, para-a posicionando o cursor no
      início.
    * Se um arquivo estiver carregado, inicia a leitura.
    * Se uma leitura estiver em andamento, permite fazer uma pausa dizendo a
      duração atual.
    * Se a leitura estiver em pausa, permite reiniciar a leitura a partir do
      local atual.

* Seta para Cima

    * Permite ver a posição atual da cabeça (indicador) de reprodução.
    * Este comando também posiciona o cursor na localização do marcador do
      início da seleção B, dizendo o local desse marcador se uma seleção foi
      feita.
    * Na caixa de diálogo de volume, vocalize o valor anterior que pode ser
      alcançado geralmente com seta para cima.
    * Este valor não é vocalizado por padrão.

* NVDA+H

    * Permite abrir a ajuda do complemento atual.

## Compatibilidade ##

* Esse complemento é compatível com as versões do NVDA a partir da versão
  2019.3.

## Alterações para a versão 20240327.0.0

* Corrigido um bug que causava um erro de registro ao recarregar plug-ins,
  graças a Rob, da lista de discussão nvda-addons;

## Alterações para 20240326.0.0

* Compatibilidade atualizada para nvda-2024.1;
* Excluído o link de download do readme, o link de download para futuras
  atualizações agora só estará disponível na loja de complementos.

## Alterações para 20231229.0.0 ##

* Adicionada uma implementação compatível com versões anteriores para
  oferecer suporte ao modo falar sob demanda, que em breve estará disponível
  com o nvda-2024.1.

## Alterações para 20231007.0.0 ##

* Após colocar os pontos de corte e abrir a janela de propriedades de corte,
  com “Ctrl+N”, adicione acessibilidade ao título dessa janela indicando o
  índice da peça.
* No modo de leitura, depois de mover os marcadores de início ou de fim das
  seleções com as teclas 1 a 6 do teclado alfanumérico, a adição do início
  automático da leitura a partir da nova posição;
* Foi corrigido um erro que ocorria ao consultar o tempo restante com
  “control+shift+r” desde o início da faixa.

## Alterações para 20230728.0.0 ##

* Aplicou as regras flake8 e mypy ao código;
* Alterada a versão mínima suportada do NVDA para 2019.3 para suportar
  anotações introduzidas no Python 3.

## Alterações para 20230508.0.0 e posteriores ##

* O número da versão, a versão mínima do NVDA e o link de download foram
  alterados de acordo com as convenções/requisitos da loja.

## Alterações para a versão 20.12 ##

* Pare a fala durante a gravação e leitura das versões mais recentes do
  mp3directcut;
* Corrigido o tempo restante de leitura para novas versões do NVDA usando
  Python 3.

## Alterações para a versão 19.02 ##

* Adicionado a configuração do complemento no menu de configurações
  disponível desde o nvda 2018.2;
* Alterada a Numeração de versão, usando AA.MM (O ano em 2 dígitos, seguido
  por um ponto, seguido pelo mês em 2 dígitos);
* Adicionado a compatibilidade com o novo formato de versão do complemento,
  surgido desde o nvda 2019.1.

## Alterações para a versão 4.0 ##

* Adicionada a compatibilidade do complemento com o Python 2.7 e 3;
* Corrigida uma falha com caminhos de localização do complemento que
  contenham caracteres não-ASCII.

## Alterações para a versão 3.0 ##

* Utilizado o módulo gui.guiHelper para garantir a aparência correta do
  diálogo de configuração do complemento;
* Usando format em vez de %s para sequências de caracteres formatadas;
* Usado a conformidade com as diretrizes para implementação.

## Alterações para a versão 2.3 ##

* Adicionada a licença GPL ao complemento;
* Alterado o atalho do script que fornece o fim da seleção de Ctrl + Shift +
  N para Ctrl + Shift + E porque Ctrl + Shift + N não funciona com as
  versões mais recentes do mp3DirectCut;
* Adicionado um script para confirmar que a seleção foi cancelada com
  'Ctrl+r';
* Foram feitas algumas correções no código do appModule (módulo de
  aplicativo) 'mp3directcut.py'.

## Alterações para a versão 2.2 ##

* Correção dos scripts que dão os locais dos marcadores de seleção.

## Alterações para a versão 2.1.1 ##

* Foi removido o script que dava o tempo total e adicionada esta informação
  ao script que fornece o tempo decorrido;
* Adicionada a capacidade de habilitar ou desabilitar os anúncios
  relacionados à tecla de espaço nas opções de configuração do módulo,
  separadamente de outros anúncios;
* Adicionada a capacidade de habilitar ou desabilitar o anúncio de
  posicionamento das marcas de seleção nas opções de configuração do módulo;
* Adicionado o anúncio da parte atual ao passar pelos pontos de corte;
* Correção de anúncios relacionados a teclas verticais;
* Adicionado um script para abrir a ajuda do complemento atual com 'NVDA+H';
* Deslocamento do menu de configuração do complemento do menu Ferramentas
  para o menu Preferências do NVDA.

## Alterações para a versão 2.1 ##

* Adicionado um script para vocalizar mover-se para o próximo ponto de
  divisão com Control+Seta para Direita;
* Adicionado um script para vocalizar mover-se para o ponto de divisão
  anterior com Control+Seta para Esquerda;
* Adicionado um script para vocalizar o deslocamento de avanço de 4
  centésimos de segundo, com Shift+Seta para Direita;
* Adicionado um script para vocalizar o deslocamento de retrocesso de 4
  centésimos de segundo, com Shift+Seta para Esquerda;
* Correção do resumo do complemento de 'para mp3DirectCut' para
  'mp3DirectCut'.

## Alterações para a versão 2.0 ##

* Adicionado um script para saber o tempo restante com 'Control Shift R';
* Corrigida a duração da leitura incluindo horas;
* Adicionada a habilidade para diferenciar milésimos ou centésimos de
  segundos.

## Alterações para a versão 1.1 ##

* Acrescentada a capacidade de incluir a categoria mp3DirectCut nos gestos
  de entrada (definir comandos);

    * Eles serão visíveis apenas durante o uso do software mp3DirectCut.

* Adicionada a capacidade de habilitar ou desabilitar o anúncio de mensagens
  automáticas, no menu de ferramentas do NVDA, item 'Configurações do
  mp3DirectCut';

## Alterações para a versão 1.0 ##

* Versão inicial.

[[!tag dev stable]]
