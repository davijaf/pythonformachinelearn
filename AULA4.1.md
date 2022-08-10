# Introdução

Olá, seja bem-vindo!

Você sabia que um computador pode estar conectado a uma série de dispositivos, como teclados, mouses, microfones, alto-falantes, telas, telas sensíveis ao toque, partes de aeronaves ou carros e até braços mecânicos? Bom, alguns desses dispositivos fornecem dados de entrada para programas, enquanto outros recebem a resposta do processamento, o que muitas vezes é um processo com começo, meio e fim. No entanto, existe um canal de comunicação que pode ser usado tanto para ler como para escrever dados. Esse canal tem como principal característica a permanência dos dados, mesmo quando o sistema é desligado.

Sabe que canal é esse? Se você pensou em arquivos, então acertou em cheio! Arquivos são como documentos de papel, pois permitem guardar configurações e resultados de processamento, funcionando como uma memória de longo prazo e possibilitando que informações sejam usadas várias vezes ou apagadas caso se tornem desnecessárias.

Nesta aula, você conhecerá as ferramentas mais importantes para ler e escrever informações em arquivos. Isso significa também ter contato com a notação hexadecimal de bytes, com noções do processo de codificação de números e caracteres em sequências de bytes e, além disso, de decodificação ou interpretação. Vamos lá?

## Objetivo

Usar arquivos de texto para armazenar e recuperar informação textual;
Conhecer as notações hexadecimais em Python para representação de bytes;
Entender os conceitos de codificação e decodificação de dados e seu funcionamento básico;
Entender como arquivos binários podem ser usados para representar informação.

## Tópico 1: Lendo arquivos de texto

## OBJETIVOS

Entender o conceito de arquivo de texto;
Usar operações de abertura e leitura em arquivos de texto;
Entender a representação de quebras de linha e tradução automática.
Como você deve saber, o alfabeto básico da computação é o binário, ou seja, a unidade mínima de informação é um único dígito binário, ou bit, que pode assumir os valores 0 e 1. Mas, assim como as letras de A a Z ou como os dígitos decimais não são muito úteis sozinhos, bits precisam ser agrupados em unidades maiores para formar unidades de informação comparáveis a sílabas ou palavras. Você certamente já leu ou ouviu falar neste agrupamento: o byte.

Um byte corresponde a 8 dígitos binários consecutivos e, na Computação, geralmente é usado como unidade de medida de informação ao invés dos próprios bits. Afinal, com 8 dígitos binários, um byte consegue representar até 256 valores distintos, o que é suficiente para representar as 26 letras do alfabeto latino, os 10 dígitos da base decimal e os sinais matemáticos e de pontuação mais usados. Caso você tenha ficado curioso sobre o valor 256, relembre um pouco de análise combinatória. Um bit representa 2 valores distintos; uma cadeia de 8 bits pode representar 28 = 256 valores; logo, um byte pode representar até 256 valores.

Neste tópico, você aprenderá a ler o conteúdo de arquivos de texto.

Arquivos de texto são considerados um dos arquivos mais simples que existem, pois utilizam bytes consecutivos para representar caracteres. Assim, ao ler um arquivo de texto, você estará essencialmente lendo strings.

Assumindo a existência de um arquivo chamado poesia1.txt, como mostra o trecho abaixo, contendo a primeira estrofe do famoso poema Canção do Exílio, do poeta Gonçalves Dias, este arquivo contém apenas o conteúdo textual mostrado, sem qualquer formatação adicional.

Minha terra tem palmeiras
Onde canta o Sabiá
As aves, que aqui gorjeiam,
Não gorjeiam como lá.

Para realizar a leitura do arquivo indicado anteriormente, deve-se digitar o código a seguir, lembrando que o arquivo Python deve estar na mesma pasta que o arquivo poesia1.txt para funcionar. Curioso para entender como ler o arquivo usando Python?

Bom, comece escrevendo ‘arq = open('poesia1.txt')’. Esta função, open, recebe o caminho de um arquivo como argumento (do tipo string) e retorna um objeto que nos permite realizar manipulações no arquivo, dentre elas, a leitura.

Para ler o conteúdo do arquivo como uma string, use o método read do objeto arq: texto = arq.read(). Pronto, isso é tudo! O conteúdo da variável texto será exibido, como mostrado a seguir. Repare nas sequências '\n’, que aparecem três vezes no texto: esta notação indica o caractere de quebra de linha no Python.

"Minha terra tem palmeiras\nOnde canta o Sabiá\nAs aves, que aqui gorjeiam,\nNão gorjeiam como lá."

A última coisa que você deve fazer antes de terminar é lembrar de usar o método close para fechar o arquivo: arq.close(). Fechar arquivos é fundamental, pois arquivos abertos, que não serão mais usados, podem causar erros de lógica no programa e esgotamento de recursos, já que a quantidade total de arquivos abertos é limitada pelo sistema operacional. Assim, o programa total deve estar da seguinte forma:

arq = open('poesia1.txt’)
texto = arq.read()
print(texto)
arq.close()

A seguir, conheça alguns detalhes sobre o uso da função open.

O primeiro parâmetro da função open corresponde ao caminho do arquivo e poderia ser algo como 'C:/Usuários/Fulano/intro-python-14/poesia1.txt', por exemplo. Mas assumindo que ambos os arquivos, texto e Python estejam no mesmo diretório ('C:/Usuários/Fulano/intro-python-14'), basta escrever open('poesia1.txt'). Caso você passe um caminho de um arquivo que não existe, esta função gera um erro do tipo FileNotFound, seguido do nome do arquivo.

Da mesma forma que fechar um arquivo que não será mais utilizado é uma prática importante, lembre-se de que também é um erro tentar ler um arquivo que já foi fechado. Assim, o código abaixo resulta em “ValueError: I/O operation on closed file”.

arq = open('poesia1.txt’)
texto = arq.read()
arq.close()
arq.read()
Entenda um pouco mais sobre o uso de barras no box de informação a seguir!

Ícone Fique atento!
Ícone “Fique atento”.
Embora os caminhos no Windows sejam tipicamente escritos com uma contrabarra ‘\’ separando os diretórios, você pode separá-los com uma barra ao especificá-los na função open, pois o Python sabe como interpretar isso. Esta forma é mais conveniente, já que a contrabarra é usada dentro de strings para representar caracteres especiais, como o '\n', e tem que ser duplicada para dar o efeito de uma única contrabarra. Em outras palavras, com contrabarras, o caminho do exemplo teria que ser escrito como 'C:\\Usuários\\Fulano\\intro-python-14’. Então, fique bem atento ao uso de barras nesse caso.

Na próxima página, confira uma alternativa para ler o arquivo progressivamente.

Você acabou de aprender a ler um arquivo de texto inteiro com o método read, mas isso nem sempre é prático ou prudente, já que o arquivo pode ser muito grande. Uma forma comum de ler um arquivo de texto é através da leitura linha a linha, o que pode ser feito com o método readline, aplicado nas linhas 2 e 3 do programa abaixo.

arq = open('poesia1.txt')
linha1 = arq.readline()
linha2 = arq.readline()
print('Linha 1:', linha1) # Linha 1: Minha terra tem palmeiras
print('Linha 2:', linha2) # Linha 2: Onde canta o Sabiá
Você conseguiu notar algo estranho ou interessante na saída deste programa? Por um lado, cada vez que o método readline é chamado, o objeto arq lê uma linha diferente, o que indica que este objeto tem um tipo de memória. Por outro lado, os comandos print produzem linhas vazias extras após cada impressão na tela. Este é um detalhe sutil: o resultado do método readline inclui o caractere de quebra de linha, como você pode verificar pelo conteúdo das variáveis linha1 e linha2, localizado nas linhas 2 e 3, que têm valores 'Minha terra tem palmeiras\n' e 'Onde canta o Sabiá\n', respectivamente. Como o comando print já insere uma quebra de linha ao fim de uma linha impressa, o resultado mostra linhas em branco adicionais.

Voltando à questão da memória, o que acontece se você usar o método read, apresentado na tela anterior, agora considerando que duas linhas já foram lidas? O resultado corresponderia a uma string com as duas linhas restantes, ou seja, "As aves, que aqui gorjeiam,\nNão gorjeiam como lá.".

Neste ponto, se você tentasse ler novamente do arquivo, usando read ou readline, o que aconteceria? Você receberia uma string vazia, indicando que o final do arquivo foi atingido. Não importa quantas vezes você repetisse isso, o resultado continuaria a ser a string vazia! Por isso, uma forma comum de ler um arquivo de texto é usar um laço while, que só termina quando uma linha vazia é lida.

Na sequência, você aprenderá a ler arquivos de texto de caractere em caractere.

O exemplo anterior mostrou que o objeto arquivo permite realizar leitura linha a linha de um arquivo, pois mantém uma espécie de “marca-páginas” interno. Na verdade, esta leitura pode ser refinada ao nível de um caractere individual, através de um parâmetro opcional, passado ao método read. Esse parâmetro indica o número de caracteres a ser lido, e seu uso é exemplificado pelo código abaixo.

arq = open('poesia1.txt')
texto1 = arq.read(5)
arq.read(1)
texto2 = arq.read
print(texto1) # Minha
print(texto2) # terra

No primeiro uso, na linha 2, o método read lê os 5 primeiros caracteres, correspondentes à palavra “Minha”. Na linha 3, o caractere seguinte, um espaço em branco, é lido e descartado de forma que os 5 caracteres seguintes, lidos na linha 3, correspondem à palavra “terra”.

Esse comportamento é possível graças ao ponteiro de arquivo. O ponteiro de arquivo é um número inteiro, não negativo, análogo ao índice em uma lista ou string, que corresponde à próxima posição do arquivo que será lido, em relação ao início do arquivo. O valor do ponteiro de arquivo pode ser recuperado usando o método tell, sem parâmetros. Após as operações de leitura no programa acima, 11 caracteres foram lidos, então arq.tell() retornaria 11.

Mais adiante, você aprenderá que este ponteiro pode ser reposicionado dentro do arquivo, como se você passasse as páginas de um livro. A seguir, pratique sobre os métodos read e tell.


O ponteiro de arquivo pode apresentar algumas surpresas. Embora a primeira linha do texto, “Minha terra tem palmeiras”, tenha 25 caracteres, se você usar readline para ler esta linha, o ponteiro indicará 27. A razão disso é que o Windows utiliza '\r\n' para indicar a quebra de linha, ao invés de apenas '\n'. O objeto arquivo do Python realiza uma conversão automática durante a leitura de '\r\n' para o formato '\n’.

Mais uma informação para você não se esquecer quando realizar a leitura de um arquivo.

Note que o método read pode ser desobediente. Se o ponteiro de arquivo estiver posicionado no fim do arquivo, qualquer tentativa de leitura retornará uma string vazia, independentemente do parâmetro passado a read.

Bom, isso conclui a parte de leitura de arquivos. No próximo tópico, você aprenderá a escrever em arquivos de texto. Empolgado? Então, vamos lá!

# Tópico 2: Escrevendo arquivos de texto

## OBJETIVOS

Entender o conceito de codificação de caracteres;
Usar a abertura de arquivo em modo de escrita e a operação de escrita para gravar texto;
Entender o funcionamento do ponteiro de arquivo;
Conhecer os diferentes modos de abertura de arquivo.

Até aqui, você pôde aprender a abrir e a ler o conteúdo de arquivos de texto. A operação oposta, ou seja, a de escrever em arquivos de texto, é o tema desta seção. Devido à sua simplicidade, arquivos de texto são comumente utilizados para armazenamento de informações. Todas as noções adquiridas até o momento, de abertura e fechamento de arquivo, ponteiro de arquivo e codificação de caracteres, serão fundamentais para entender como funciona a escrita de arquivos.

Algo que fica bastante transparente ao trabalhar com arquivos de texto, da maneira como você aprendeu até o momento, é a questão da codificação. Em termos simples, uma codificação é a convenção que diz como caracteres são mapeados em números binários e vice-versa. A codificação inglesa American Standard Code for Information Interchange (ASCII) com a qual você teve contato anteriormente, utiliza um byte por caractere. A tabela abaixo ilustra os valores decimais de alguns caracteres na codificação ASCII.

Caractere	+	,	-	.	0	1	2	A	B	C	a	b	c	{
ASCII	43	44	45	46	48	49	50	65	66	67	97	98	99	123
Esta codificação, uma das mais antigas ainda em uso. Ela aproveita apenas 7 dos 8 bits em um byte, de forma que é capaz de armazenar 128 (27) valores distintos, o que é bem pouco. Em particular, caracteres acentuados e “ç” (bastante usados em línguas latinas) bem como os caracteres cirílicos usados na Rússia e os ideogramas do leste asiático ficam todos de fora.

Por isso, o mais comum em versões ocidentais do Windows é usar a codificação CP-1252, que utiliza todos os 8 bits de um byte e, portanto, consegue representar um total de 256 (28) valores, ou seja, o dobro da ASCII. Para valores de 0 a 127, CP-1252 é idêntica à ASCII mas a partir de 128 estão localizados os caracteres acentuados, como os que usamos em português, além de outros. Outro padrão de codificação muito adotado atualmente é o UTF-8. Este padrão é capaz de representar todos os caracteres existentes nos diversos idiomas, podendo usar até 4 bytes para isso.

Talvez você se pergunte por que é relevante saber sobre codificação de caracteres. Confira esta resposta na próxima página.

Ocorre que é impossível adivinhar com 100% de certeza a codificação usada em um arquivo de texto, por isso a função open tem um parâmetro, chamado encoding, que permite especificar manualmente a codificação usada no arquivo lido. Para especificar manualmente a codificação do arquivo poesia1.txt como CP-1252, você deve escrever a seguinte linha de código:

arq = open('poesia1.txt', encoding='cp1252’)
Se você estiver no Windows, não há diferença entre isso e arq = open('poesial.txt'), uma vez que esta já é a codificação padrão do sistema. Porém, em macOS e Linux, ou mesmo em uma versão grega do Windows, a situação já seria diferente, uma vez que a codificação padrão desses sistemas seria outra.

Mais adiante, você aprenderá a abrir arquivos de texto com finalidade de escrita.

Você se lembra de que, para ler um arquivo de texto, a primeira coisa a fazer é abri-lo com a função open, passando o nome do arquivo? De forma parecida, para escrever um arquivo de texto, você poderia começar com a seguinte linha:

arq_escrita = open('escrita.txt', 'w', encoding='cp1252’)
O segundo parâmetro, que aparece entre o nome do arquivo e a codificação, chama-se mode, que é o modo de abertura do arquivo. O valor ‘w’ (do inglês "write", ou "escrever“) indica que o arquivo escrita.txt deve ser criado com finalidade de escrita. Assim como na leitura, assume-se que o arquivo escrita.txt esteja na mesma pasta que o código Python que executa esse comando. Caso o arquivo não exista, ele é criado, mas, se existir, ele é completamente apagado antes de ser retornado como objeto para a variável arq_escrita. O modo padrão de abertura é 'r' (do inglês "read", ou “ler"), de forma que open('poesia1.txt') é sinônimo de open('poesia1.txt', 'r’).

Bom, uma vez aberto o arquivo para escrita, o novo método que será utilizado é o write, que recebe como parâmetro uma string. Esta string será escrita no arquivo, traduzindo-a para a codificação de caracteres, informada à função open. Por exemplo, o código abaixo é uma continuação do anterior. Ele escreve as duas primeiras linhas da Canção do Exílio e, então, fecha o arquivo.

arq_escrita.write('Minha terra tem palmeiras\n')
arq_escrita.write('Onde canta o sabiá')
arq_escrita.close()
Repare que foi adicionada uma quebra de linha ao fim da string do primeiro verso, na linha 2, pois o método write escreve exatamente o que é passado. Na verdade, há uma pequena exceção à essa regra: ao escrever um arquivo no Windows, cujas quebras de linhas são representadas por '\r\n', o método realizará a conversão automática de '\n' para '\r\n', de maneira inversa ao que é feito pelo método read.

A seguir, você irá compreender como se comporta o ponteiro de arquivo com relação à operação de escrita.

Você se lembra do ponteiro de arquivo? Para um arquivo aberto em modo de leitura, ele indica a posição do próximo caractere a ser lido. Já no modo de escrita, ele indica a próxima posição a ser escrita. Este ponteiro pode ser reposicionado, utilizando o método seek (do inglês, “buscar”), que recebe como parâmetro a posição de destino do ponteiro.

O ponto crítico é que, ao mover esse ponteiro para o meio do arquivo, novas chamadas ao método write escrevem os caracteres passados por cima dos que já existem. Somente quando o ponteiro atingir novamente o fim do arquivo é que os novos caracteres inseridos vão causar um aumento no tamanho desse arquivo. O programa abaixo ilustra essa dinâmica.

arquivo = open('restos.txt', 'w')
arquivo.write('0123456789')
arquivo.seek(0)
arquivo.write('abcd')
arquivo.close()
O conteúdo final do arquivo restos.txt é “abcd456789”. Afinal, após a primeira operação de escrita, na linha 2, o ponteiro é reposicionado no início do arquivo, de forma que a segunda operação de escrita, na linha 4, sobrescreve os 4 primeiros caracteres, “0123” com “abcd”.

É possível descartar o restante do arquivo, a partir da 5ª posição, usando o método truncate (do inglês, “truncar”). Ele recebe, como parâmetro opcional, o novo comprimento do arquivo. Se este tamanho não for informado, o arquivo será apagado após a posição atual do ponteiro de arquivo. Assim, bastaria adicionar arquivo.truncate() entre as linhas 4 e 5 para ficar com resultado final “abcd”. Em qualquer situação, arquivo.truncate(0) apaga completamente o arquivo, o que por sinal é feito toda vez que o arquivo é aberto com modo 'w’, e nem sempre é uma situação desejada. Então, fique atento!

Ícone Saiba Mais
Ícone “Saiba Mais”.
O método seek tem um segundo parâmetro numérico, que altera o significado do primeiro. Por padrão, o ponteiro é deslocado para uma posição em relação ao começo do arquivo, mas também é possível fazer isso a partir do fim do arquivo ou da posição atual. Para mais informações, consulte a documentação por meio deste link.

A seguir, você aprenderá sobre outros modos de abertura de arquivo.

Os modos de leitura e de escrita são mutuamente excludentes. Em outras palavras, quando o segundo parâmetro de open é 'r', usar o método write gera um erro do tipo UnsupportedOperation. Abrir com modo 'w' só permite escrever, assim como modo 'r' só permite ler. Em ambos os casos, tentar realizar a outra operação gera um erro do tipo indicado. Isso previne erros de lógica porque o mais comum é abrir um arquivo só para ler ou só para escrever. Ou seja, para fazer os dois, é preciso deixar isso explícito.

Porém, caso você queira realmente fazer isso, pode usar os modos de abertura 'r+' ou 'w+'. A diferença entre eles é que 'r+' irá falhar caso o arquivo indicado não exista, enquanto 'w+' irá apagá-lo caso ele exista. Em outras palavras, estes novos modos de abertura se comportam de forma similar aos já conhecidos 'r' e 'w', mas tornam possível leitura e escrita alternadas.

Há ainda dois modos de abertura adicionais: 'a' e 'a+', onde a letra “a” vem do verbo inglês append, que significa acrescentar. Estes modos são similares a 'w' e 'w+', pois permitem escrever e criá-los no arquivo caso não existam. A diferença é que nesse modo os dados não são apagados do arquivo após a sua abertura e o ponteiro de arquivo é posicionado ao fim desse arquivo automaticamente. Estes modos são particularmente úteis para arquivos que crescem durante longos períodos de tempo antes de serem apagados, como registros de login ou históricos de atividades. Você se recorda do módulo logging já estudado neste curso? O parâmetro filemode funciona da mesma forma que o parâmetro mode em um arquivo. No caso de escrita de logs, é muito comum utilizar o modo ‘a’.

O quadro a seguir resume os modos de abertura de arquivo, apresentando duas colunas relacionadas, uma com o modo e a outra com a descrição.

Modo	Descrição
'r'	Abre para leitura, falhando se o caminho não existir.
'w'	Abre para escrita, apagando se o caminho existir e criando se não existir.
'a'	Abre para escrita, começando do final se existir, criando se não existir.
'r+'	Abre para leitura/escrita, falhando se o caminho não existir.
'w+'	Abre para leitura/escrita, apagando se o caminho existir e criando se não existir.
'a+'	Abre para leitura/escrita, começando do final se existir, criando se não existir.
Pratique sobre modos de abertura de arquivo por meio da atividade a seguir.

# Tópico 3: Notação hexadecimal e codificação de dados

## OBJETIVOS

Conhecer a notação hexadecimal e a representação de bytes em Python;
Entender o processo de codificação de caracteres;
Entender os principais esquemas de codificação de números inteiros.
Todos os dados de um computador são armazenados, em última instância, em bits. No entanto, um único bit, por só ter dois estados, 0 ou 1, representa pouca informação, de maneira que a unidade mínima de informação, normalmente utilizada em computação, é o byte, composto de 8 bits.

Assim como caracteres podem ser codificados de várias maneiras usando sequências de bytes, como as codificações CP-1252 e UTF-8 mencionadas anteriormente, os números também podem ser codificados de diversas formas. Na maior parte do tempo, não é preciso se preocupar com qual representação é usada internamente pelo Python. Porém, quando você importa dados vindos de arquivos com formatos exóticos ou programas externos, produzir dados que sigam essas convenções torna essa questão primordial. Outra situação em que você deve pensar na representação de números seria na criação de um formato próprio, para ter maior controle sobre a eficiência de armazenamento. Neste tópico, você aprenderá um pouco a respeito das notações usadas para representar padrões de bytes arbitrários em Python.

Você se lembra da notação binária? Ela utiliza exclusivamente os algarismos 0 e 1, diferentemente da decimal, que dispõe dos algarismos 0 a 9. Por isso, em geral, é necessário usar muito mais dígitos em binário para expressar uma determinada grandeza do que em decimal. Contudo, ela foi adotada como notação básica da computação porque é conveniente para a criação de computadores usando circuitos eletrônicos, já que o 1 pode ser representado pela passagem de corrente elétrica e o 0, por sua ausência.

Entretanto, a base mais usada para representar dados brutos em computação é uma terceira, a chamada base hexadecimal. Ela é caracterizada por 16 algarismos, que incluem os mesmos que a decimal, de 0 a 9, seguidos das letras “A” a “F” para representar os algarismos restantes, cujos valores vão de 10 a 15. Assim, o número “10” não representa dez, em hexadecimal, mas sim dezesseis.

Parece estranho? A lógica é a mesma que você usaria para contar em decimal: você usa os algarismos de “0” a “F” para contar de zero a quinze. Depois disso, o próximo valor é representado voltando ao algarismo “0” e adicionando um dígito com o algarismo “1” à sua esquerda. O próximo número, “11”, representa o número dezessete em decimal e o “1F” representa o número trinta e um em decimal. Se adicionarmos 1 ao número “1F”, o dígito da direita volta a ser “0” novamente e o da esquerda passa a ser “2”, obtendo o número “20”, que representa o número trinta e dois em decimal.

A tabela abaixo ilustra a interpretação dos dígitos “111” em três bases diferentes, onde cada linha representa uma: binária, decimal e hexadecimal.

Representação	Dígitos	Valor em decimal
Decimal	        111	    111
Binário	        111     7
Binário	        111     273

A seguir, aprenda mais sobre converter números hexadecimais para decimais.

Agora considere a situação em que você se depara com o número for 2B3F. Como calcular qual é esse valor na base decimal? Há um algoritmo simples para transformar todo número de qualquer base para a base decimal. Ao estudar introdução a Python, você deve ter aprendido que o número 10 em binário é o valor 2 na base decimal. E, nesta aula, o valor 10 em hexadecimal é o valor 16 na base decimal. Tem uma lógica para isso, e você irá aprender o procedimento de conversão agora.

Analise o seguinte número hexadecimal com os algarismos separados por casa. Saiba que o valor de casa começa em 0 a partir do dígito menos representativo. Por exemplo, o número 3EF possui o dígito F na casa 0; o dígito E na casa 1; e o dígito 3 na casa 2. Ele está dividido na tabela a seguir.

Exemplo 1
Algarismo	3	E	F
Casa	    2	1	0

Exemplo 2
Algarismo	                    3	E	F
Valor do símbolo (em decimal)	3	14	15

Para converter esse número da base hexadecimal (base 16) para a base decimal (base 10), você deve pegar o valor da base e elevar ao número da casa em que aquele símbolo está. Após isso, você o multiplica pelo valor em decimal do símbolo, repetindo esse processo para cada símbolo do algarismo. Confira o exemplo da conversão para o número 3EF:

16^2 * 3 + 16^1 * 14 + 16^0 * 15
= 256 * 3 + 16 * 14 + 1 * 15
= 1007.

Agora para o valor 10 na base hexadecimal, o dígito 1 está na casa 1, e o dígito 0 está na casa 0, logo o valor convertido é:

16^1 * 1 + 16^0 * 0 = 16.

Para a base binária, você pode utilizar a mesma fórmula, somente trocando 16 por 2, pois é a base do sistema, certo? E como ficaria para o valor de exemplo citado acima 2B3F? Simples, o dígito 2 está na casa 3; o dígito B na casa 2; o dígito 3 na casa 1; e o dígito F na casa 0. Logo, o valor em decimal é:

16^3 * 2 + 16^2 * 11 + 16^1 * 3 + 16^0 * 15
= 4096 * 2 + 256 * 11 + 16 * 3 + 1 * 15
= 11.071.

Resultou em um número grande para uma representação aparentemente pequena, não acha? Pratique um pouco mais com valores hexadecimais na atividade da próxima página.

Em Python, é possível escrever números inteiros diretamente nas bases binária e hexadecimal. Para isso, basta prefixá-los com “0b” ou "0x", respectivamente. No caso hexadecimal, os algarismos de "A" a "F" podem ser tanto maiúsculos como minúsculos. Exemplos de números expressos desta forma são: 0x2A e 0b101010 (ambos quarenta e dois) ou 0x21 e 0b100001 (ambos trinta e três). Entretanto, o comando print(0x2A, 0b101010) produz a saída “42 42”, já que ele sempre formata números em base decimal.

No sentido contrário, as funções bin e hex convertem números inteiros em strings binárias ou hexadecimais. Por exemplo, hex(42) produz '0x2A’ e bin(42), que produz '0b101010'.

Embora ler e escrever em hexadecimal requeira uma certa prática, é mais importante entender o que esta notação significa do que ser capaz de fazer contas e conversões rapidamente. Alguns dos valores mais importantes que você deve reconhecer com facilidade são 0x00 (zero), 0x0A (dez), 0x10 (dezesseis) e 0xFF (duzentos e cinquenta e cinco).

Mas você faz ideia de por que a base hexadecimal é utilizada? Isso tem tudo a ver com bytes serem usados como unidade de informação. Afinal, um dígito hexadecimal pode representar 16 valores distintos, que é o mesmo número de possibilidades dadas por 4 dígitos binários. Assim, um dígito hexadecimal é uma notação compacta para 4 dígitos binários. Portanto, um byte, que pode assumir 256 valores distintos (como os números de 0 a 255), pode ser representado compactamente por dois dígitos hexadecimais. Além de economizar um dígito em relação à base decimal, não há espaço para enganos, uma vez que dois dígitos hexadecimais só produzem 16 x 16 = 256 valores. Diferentemente de três dígitos decimais, que podem representar 1000 valores distintos.

Assim como caracteres podem ser codificados de várias maneiras usando sequências de bytes, como as codificações CP-1252 e UTF-8 mencionadas anteriormente, números também podem ser codificados de diversas formas. Quando você lê ou escreve um arquivo de texto, os métodos read e write fazem, automaticamente, a conversão dos bytes gravados no arquivo para caracteres de strings e vice-versa, com base na codificação informada pelo parâmetro encoding à função open. Porém, é possível ler arquivos a nível de bytes individuais, decidindo como esses bytes devem ser interpretados como números ou caracteres em Python.

Descubra, adiante, como codificar e decodificar strings manualmente.

Quando você utiliza strings em Python, a menor unidade de informação que você pode extrair é a de um caractere individual, pois o papel de uma variável do tipo str é representar uma sequência de caracteres, independentemente de como eles se traduzem em sequências de bytes. Porém, existe um outro tipo de dado cuja função é representar arranjos de bytes de maneira precisa, chamado bytes.

Assim como strings, os objetos do tipo bytes, chamados strings de bytes, são sequências imutáveis, podem ser indexados, fatiados além de somados e multiplicados através dos operadores + e *. O método encode (em português, codificar) permite converter strings em strings de bytes, como exemplificado abaixo:

verso = 'Minha terra tem palmeiras'
verso_bytes = verso.encode('ascii')
print(verso_bytes)     # b'Minha terra tem palmeiras’

O resultado parece uma string, mas repare no prefixo “b”, que antecede o resultado. Este prefixo indica que o resultado é uma string de bytes (tipo bytes), e não de caracteres (tipo str). Tanto que, se você indexar a variável verso_bytes, como em verso_bytes[0] ou verso_bytes[1], terá como resposta os números 77 e 105, respectivamente, que correspondem aos códigos ASCII das letras “M” e “i”. Portanto, strings de bytes são sequências de números, não de caracteres.

Compreenda um pouco mais sobre isso na próxima página.

Acompanhe este outro exemplo, que introduz algumas novidades:

verso = 'Onde canta o sabiá'
print(verso.encode('cp1252')) # b'Onde canta o sabi\xe1'
print(verso.encode('utf8')) # b'Onde canta o sabi\xc3\xa1'
As codificações CP-1252 e UTF-8, usadas nas linhas 2 e 3, são idênticas em quase tudo, exceto na codificação do “á” em “sabiá”: a primeira usa o byte 0xE1, igual a 225; a segunda usa os bytes 0xC3 e 0xA1, iguais a 195 e 161. Mas repare que, dentro de uma string de bytes, o prefixo dos números hexadecimais é “\x”, e não “0x”.

Mas, se strings de bytes são sequências de números, por que são impressas de forma parecida com strings de caracteres? É apenas por conveniência. Ler dados binários não é fácil, principalmente quando há números misturados com texto. Como quase todas as codificações de caracteres permitem a utilização das letras A a Z maiúsculas e minúsculas, dos algarismos de 0 a 9, dos sinais matemáticos e das pontuações mais comuns, é mais fácil e abreviado imprimir estes bytes usando caracteres do que os seus códigos hexadecimais.

Esta abreviação é feita para todos os bytes com valores entre 30 e 126. Todos os demais são representados pela notação hexadecimal.

Aprenda, a seguir, algumas noções de como números inteiros são codificados.

Apesar de existirem muitas codificações de caracteres, com números inteiros, existem apenas duas codificações fundamentalmente diferentes: a “com sinal” e a “sem sinal”. A codificação sem sinal usa todos os bits disponíveis para representar a magnitude do número, mas só admite números maiores ou iguais a zero. Por outro lado, a representação com sinal reserva um bit para o sinal do número e os restantes para a magnitude, dividindo a amplitude igualmente entre números negativos e não negativos.

A seguinte tabela apresenta três colunas relacionando a codificação nos esquemas mais comuns, de 1, 2, 4 ou 8 bytes, com e sem sinal, com os valores mínimo e máximo representáveis para cada um desses esquemas.

Codificação	        Valor mínimo                Valor máximo
1 byte sem sinal	0	                        255
1 byte com sinal	-128	                    127
2 bytes sem sinal	0	                        65,536
2 bytes com sinal	-32,768	                    32,767
4 bytes sem sinal	0	                        4,294,967,295
4 bytes com sinal	-2,147,483,648	            2,147,483,647
8 bytes sem sinal	0	                        18,446,744,073,709,551,615
8 bytes com sinal	-9,223,372,036,854,775,808	9,223,372,036,854,775,807

Acompanhe mais explicações sobre algumas representações a seguir.

A representação usando um byte sem sinal admite 28 = 256 números, que vão de 0 a 28 – 1 = 255. Quando um bit é tomado para o sinal, o valor mínimo passa a ser -27 = -128 e o máximo 27 - 1 = 127. As outras representações seguem a mesma lógica: quando d bits sem sinal são usados, a faixa de valores vai de 0 a 2d – 1. Quando um bit é tomado para o sinal, a faixa de valores passa a variar de -2d-1 a 2d-1 - 1.

A representação sem sinal é muito simples: basta escrever o número em base binária, como você aprendeu a fazer! Portanto, a codificação de 252 em um byte com sinal é "1111 1100", em binário, ou "FC", em hexadecimal.

Agora, a representação com sinal é mais detalhada. Se o bit de sinal (correspondente ao dígito de maior valor) for 0, o número é interpretado como se não tivesse sinal. Portanto, "0111 1100" binário (ou "7C" hexadecimal) designa o número 124 na representação com sinal. Porém, se o bit de sinal fosse um, ou seja, o número fosse "1111 1100" binário (ou "FC" hexadecimal), o valor aí codificado seria -4, e não -124!

Esta sutileza é melhor detalhada na próxima página.

A representação com sinal é contraintuitiva porque o bit de sinal tem que ser interpretado de forma especial. Normalmente, ao converter um número de binário para decimal, cada dígito multiplica uma potência de 2. Por exemplo, o número “1101" em binário pode ser convertido para decimal calculando (1x23 + 1x22 +0x21 + 1x20) = 13. No entanto, enquanto que, na codificação sem sinal, o bit mais à esquerda valeria 27 = 128, na codificação com sinal, ele vale –128. Portanto, para converter “1111 1100" binário para decimal, você pode realizar o cálculo abaixo:

-27 + 26 + 25 + 24 + 23 + 22 =
-128 + 64 + 32 + 16 + 8 + 4 =
-4

A última linha mostra o resultado esperado, -4. Agora é mais fácil entender por que o valor mínimo é -128? Basta que o bit de sinal valha 1, e os demais valham 0 para obter este valor. Por outro lado, quando o primeiro bit é zero e todos os outros são 1, o valor é (26+25 +24+ 23+22+21+20) = 127, que corresponde ao máximo valor positivo. A tabela abaixo ilustra a representação de alguns números inteiros usando um byte. A primeira coluna corresponde ao número; a segunda coluna informa se a representação é com ou sem sinal; e as duas seguintes colunas mostram a representação correspondente nas notações hexadecimal e binária. Repare que números positivos menores ou iguais a 127 têm a mesma representação com ou sem sinal.

Número	Sinal?	Hex.	Bin.	    String
0	    Sim/Não	00	    0000 0000	'\x00'
255	    Não	    FF  	1111 1111   '\xFF'
252	    Não	    FC	    1111 1100   '\xFC'
-4	    Sim	    FC	    1111 1100   '\xFC'
124	    Sim/Não	7C	    0111 1100 	'\x7C'
129	    Não	    81  	1000 0001   '\x81'
-127	Sim	    81  	1000 0001   '\x81'
1	    Sim/Não	01	    0000 0001 	'\x01'

A seguir, pratique seus conhecimentos na atividade da próxima página.

Trabalhar com codificações binárias de dados é um assunto que requer bastante familiaridade com as notações binária e hexadecimal, além dos esquemas de codificação de dados. A boa notícia é que, na maior parte do tempo, não é necessário mexer com informação em um nível tão detalhado, como o dos bytes. Mesmo quando é preciso, existem módulos no Python que contêm funções para converter para as codificações mais comuns. Portanto, o que realmente importa é ter uma noção de como esse processo funciona.

Antes de finalizar esse assunto, acompanhe a seguir algumas informações importantes sobre o tema.

Ícone Saiba Mais
Ícone “Saiba Mais”.
O módulo da struct da biblioteca padrão contém funções que transformam números inteiros ou pontos flutuantes em strings de bytes e vice-versa, de acordo com a representação desejada. Com isso, você fornece números e obtém as strings de bytes desejadas ou fornece as strings de bytes e obtém os números correspondentes. Explorar este módulo é a melhor forma de entender como as codificações numéricas funcionam. Para mais informações, acesse a documentação oficial de Python através dos links:

Interpretar bytes como dados binários compactados: https://docs.python.org/pt-br/3.7/library/struct.html.

Ferramentas principais para trabalhar com fluxos: https://docs.python.org/pt-br/3.7/library/io.html.

Outra informação importante é sobre a representação de número ponto flutuante. Esse assunto não será abordado aqui, pois é bem mais sofisticado que a de números inteiros. Mas é importante que você saiba que ele existe e que a principal codificação de número de ponto flutuante em uso é o padrão IEEE 754, que prevê números de 2, 4 ou 8 bytes. Para aprofundar seus conhecimentos, pesquise sobre esse padrão e aumente seu repertório sobre o tema!

No próximo tópico, você conhecerá uma maneira muito mais simples de guardar e recuperar informações em Python.

# Tópico 4: Arquivos Binários

## OBJETIVOS
Entender a diferença entre arquivos de texto e arquivos binários;
Entender os modos de abertura binários.

Quando você lê ou escreve arquivos de texto, basta informar a codificação usada à função open uma vez para que o Python realize as conversões necessárias entre sequências de bytes e caracteres (leitura), ou vice-versa (escrita). Dessa forma, você pode, confortavelmente, trabalhar com o conceito de strings (ou seja, sequências de caracteres) de maneira abstrata, sem se preocupar com qual padrão de bytes é usado pelo Python ou pelos arquivos para representar os caracteres em si.

Porém, arquivos também podem ser abertos em modo binário, o que significa que as operações de leitura e escrita passam a trabalhar com strings de bytes ao invés de caracteres. Consequentemente, codificação e decodificação passam a ser responsabilidade sua, mas você ganha controle preciso sobre a representação da informação, o que é útil para importar/exportar dados de/para algum formato de arquivo ou programa externo que não seja suportado pela biblioteca padrão.

Nesta última seção, você compreenderá como os arquivos podem ser abertos em modo binário. Vamos lá?

Para abrir um arquivo para leitura ou escrita em modo binário, basta usar os mesmos códigos de abertura aprendidos anteriormente, acrescidos de uma letra b. Assim, open('dados.dat', 'rb') abre o arquivo dados.dat para leitura em modo binário, assim como open('dados.dat', 'wb') o abre para escrita em modo binário. De maneira simples, isso quer dizer que as chamadas ao método read retornam strings de bytes, ao invés de strings de caracteres, e que, analogamente, as chamadas ao método write devem receber strings de bytes como parâmetro. O quadro abaixo lista os modos de abertura binários na primeira coluna, detalhando-os na segunda.

Modo	Descrição
'rb'	Abre para leitura binária, falhando se o caminho não existir.
'wb'	Abre para escrita binária, apagando se o caminho existir e criando se não existir.
'ab'	Abre para escrita binária, começando do final se o caminho existir e criando se não existir.
'rb+'	Abre para leitura/escrita binária, falhando se o caminho não existir.
'wb+'	Abre para leitura/escrita binária, apagando se o caminho existir e criando se não existir.
'ab+'	Abre para leitura/escrita binária, começando do final se o caminho existir e criando se não existir.
Entenda isso melhor acompanhando o programa a seguir.

O programa abaixo, com o qual você já deve estar familiarizado, abre o arquivo poesia.txt em modo de leitura, com codificação CP-1252, e realiza a leitura do conteúdo com o método read.

arq = open('poesia1.txt', 'r',
            encoding='cp1252')
texto = arq.read()
arq.close()
Se este arquivo fosse aberto em modo binário, seria necessário decodificar os bytes lidos explicitamente. As linhas 1 e 2, neste caso, passariam a ser “arq = open('poesia1.txt', 'rb’)”, e a linha 3 passaria a ser “texto = arq.read().decode('cp1252’)”. De forma semelhante, para escrever texto em um arquivo aberto em modo binário, seria necessário, primeiro, convertê-lo para uma string de bytes em uma codificação escolhida, mudando de algo, como “arq.write('Uma mensagem’)”, para “arq.write('Uma mensagem'.encode('cp1252'))”.

Na próxima aula, você conhecerá outra maneira de guardar dados em arquivos binários e poderá decidir qual é a mais simples para você usar.

Ícone Saiba Mais
Ícone “Saiba Mais”.
Existem diversos outros módulos dedicados à leitura e à escrita de arquivos. Conheça alguns listados a seguir:

csv - Lê e escreve arquivos com extensão .csv, um formato texto usado para trocar dados entre diferentes editores de planilhas, como o Excel;
json - Lê e escreve arquivos com extensão .json, um formato texto extensivamente usado na Internet e para trocar dados entre diferentes linguagens de programação modernas;
struct - Permite controle fino sobre a codificação e a decodificação de números e strings ao nível dos bytes individuais;
pillow - Serve para ler/escrever arquivos de imagens.
Na próxima aula, você conhecerá mais sobre o assunto.

Nesta aula, você pôde aprender a trabalhar com arquivos em Python. Arquivos são uma maneira de armazenar informações a longo prazo, de maneira que possam ser usadas múltiplas vezes pelo mesmo programa ou por programas diferentes. Você compreendeu que esses arquivos guardam, fundamentalmente, sequências de bytes com um significado especial.

Além disso, você pôde entender que bytes são, em geral, representados na exótica base hexadecimal, que é bem mais compacta e legível do que a base binária. Para poder construir sequências de bytes a partir de números ou caracteres, ou interpretar estas sequências no sentido contrário, você aprendeu os princípios da codificação e decodificação binária.

Também teve a oportunidade de perceber que, ao lidar com arquivos cujo conteúdo é exclusivamente textual, é possível abri-los como arquivos de texto, especificando uma codificação de caracteres e deixando que o Python realize as transformações entre bytes e caracteres de maneira totalmente transparente. Já os arquivos binários servem para quando você necessita de maior controle sobre os processos de codificação e decodificação. Nesses casos, é possível utilizar módulos da biblioteca padrão que realizam importação e exportação de formatos usados por diversos programas.

Agora que você aprendeu tudo isso, pode resolver os exercícios propostos e colocar em prática seus conhecimentos nos programas que desenvolver. Faça isso para consolidar sua aprendizagem e melhorar ainda mais a sua experiência com programação em Python!

Bons estudos!

## Referências
PYTHON. Funções embutidas – open. Disponível em: https://docs.python.org/pt-br/3.7/library/functions.html#open. Acesso em: 02 jul. 2020.
PYTHON. Leitura e escrita de arquivos. Disponível em: https://docs.python.org/pt-br/3.7/tutorial/inputoutput.html#reading-and-writing-files. Acesso em: 02 jul. 2020.
WIKIPÉDIA. Representação de números com sinal. Disponível em: https://pt.wikipedia.org/wiki/Representa%C3%A7%C3%A3o_de_n%C3%BAmeros_com_sinal. Acesso em: 02 jul. 2020.
WIKIPÉDIA. Unicode. Disponível em: https://pt.wikipedia.org/wiki/Unicode. Acesso em: 02 jul. 2020.


## Glossário
Para conhecer o significado dos termos técnicos estudados nesta aula, selecione a palavra desejada.

Arquivo Binário https://leadfortaleza.com.br/ead/glossary/Arquivo%20Bin%C3%A1rio
Arquivo Texto https://leadfortaleza.com.br/ead/glossary/Arquivo%20Texto
Base Hexadecimal https://leadfortaleza.com.br/ead/glossary/Base%20Hexadecimal
Codificação de Caracteres https://leadfortaleza.com.br/ead/glossary/Codifica%C3%A7%C3%A3o%20de%20Caracteres
Codificação https://leadfortaleza.com.br/ead/glossary/Codifica%C3%A7%C3%A3o
Decodificação https://leadfortaleza.com.br/ead/glossary/Decodifica%C3%A7%C3%A3o
Formato de Arquivo https://leadfortaleza.com.br/ead/glossary/Formato%20de%20Arquivo
Objeto Arquivo https://leadfortaleza.com.br/ead/glossary/Objeto%20Arquivo
Ponteiro de Arquivo https://leadfortaleza.com.br/ead/glossary/Ponteiro%20de%20Arquivo
