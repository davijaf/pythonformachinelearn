# INTRODUÇÃO

Olá! Seja bem-vindo!

Nesta aula, você vai conhecer um pouco mais sobre Ciência da Computação, mais especificamente sobre bibliotecas Python.

Esse é um assunto bem interessante e rico em detalhes. Para você ter uma noção da versatilidade que o Python oferece, é possível compará-lo a um canivete suíço, um utensílio moderno que agrupa diversos elementos e funcionalidades. Nesse objeto, há chave de fenda, abridor de latas, saca-rolhas e outras ferramentas agrupadas. Pensando assim, o Python é como um canivete desses, ao instalá-lo, várias bibliotecas padrões já estarão acessíveis para você utilizar, e cabe a você saber quais são e como usá-las.

A seguir, você vai conhecer várias bibliotecas muito utilizadas por desenvolvedores para criarem aplicações robustas e deixarem seu software mais confiável e de fácil manutenção, o que poupa seu tempo de desenvolvimento e reduz as chances de você ter que criar alguma solução do zero.

# Objetivos

Definir ferramentas rápidas e de uso eficiente da memória;
Implementar e reconhecer expressões regulares;
Desenvolver um registro flexível de eventos de sistema para aplicações.

# Tópico 1 – Itertools

## OBJETIVOS

Definir o que são funções geradoras e iteradores;
Diferenciar e aplicar funções como combinações, permutações e produtos cartesianos.
Você já percebeu que, ao longo das últimas décadas, a quantidade de dados gerados tem crescido muito? Você sabia que só em 2020, a cada minuto, foram publicadas 347 mil novos stories na rede social Instagram, 147 mil fotos no Facebook e 41 milhões de mensagens foram trocadas por WhatsApp? O surgimento da Internet aumentou de forma abrupta a quantidade de dados produzidos, deixando mais difícil o trabalho de processar esses dados em períodos curtos de tempo.

Com esse grande aumento da quantidade de dados, o processamento paralelo tornou-se uma técnica eficiente para manipulá-los. Esse processamento consiste no uso simultâneo de várias unidades de processamento (CPUs) para realizar trabalhos computacionais. Devido a isso, o itertools tornou-se o módulo ideal para processamento paralelo, pois padroniza um conjunto central de ferramentas rápidas e de uso eficiente da memória, que podem ser utilizadas sozinhas ou combinadas, tornando possível construir ferramentas sucintas e eficientes em Python puro.

# Tópico 1

O módulo itertools utiliza-se de técnicas de programação funcional, como as funções geradoras, que são funções que retornam um objeto iterável. Esse objeto iterável não possui um valor fixo, ou seja, quando invocado, um novo valor é computado, como você pode observar no exemplo a seguir:

import itertools
contador = itertools.count()

print(contador) # count(0)
print(next(contador)) # 0
next(contador)
print(next(contador)) # 2

No exemplo apresentado, você pode notar que a função count retorna um iterador. A variável chamada ‘contador’ recebe esse iterador e, à medida que é invocada, por meio da função next, é computado um novo valor a essa variável. Com isso, esse valor é computado somando mais 1 ao valor anterior e tendo um mesmo comportamento de um iterador qualquer dentro de um ForLoop.

Essa técnica é chamada de avaliação preguiçosa (em inglês, lazy evaluation), que é o processo de adiar a avaliação de uma expressão até que ela seja necessária, e muito utilizada para criar sequências grandes ou infinitas sem estourar a memória da máquina.

Note que é possível invocar infinitas vezes a variável criada por meio da função count. Se você não tomar cuidado e acabar colocando um iterador em um ForLoop, é possível que o código entre em um loop infinito, ou seja, seu programa não finalizará. Caso ocorra, será necessário fechar o programa manualmente.

Nas próximas páginas, você vai poder se aprofundar nos métodos do módulo itertools, priorizando os métodos mais importantes para um cientista de dados. Vamos lá!

Análises combinatórias são muito poderosas e podem auxiliar em diversos tipos de problemas. Essas análises são bastante utilizadas em estatística e, como você sabe, estatística é uma das competência necessárias de um cientista de dados. Observe o código a seguir para conhecer exemplos de como utilizar o método combinations para fazer combinações.

import itertools

print(itertools.combinations("ABC",2)) # <itertools.combinations at 0x1916522f130>

print(list(itertools.combinations("ABC",2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("AABC",2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("ABCD",3)))
# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]

Agora, vamos analisar o código linha por linha:

Na linha 1, importamos o módulo itertools, necessário para importar o método que iremos utilizar;
Na linha 3, tentamos imprimir as combinações com as letras da palavra “ABC”. Entretanto, o método combinations retorna um objeto iterável, e não uma lista;
Na linha 5, convertemos o objeto retornado em uma lista. Foi impresso como resultado uma lista com combinações 2 a 2 a partir da palavra ‘ABC’, onde não há repetições de combinações e a ordem não importa ('A', 'B') = ('B','A’);
Na linha 7, a lista impressa contém uma combinação que aparece duas vezes ('A', 'B'), isso acontece porque a palavra contém dois caracteres ‘A’ e a função considera que esses dois caracteres ‘A’ são diferentes;
Na linha 9, a lista impressa contém combinações 3 a 3 com as letras da palavra ‘ABCD’, onde não há repetições e a ordem não importa, assim como a combinação da linha 5. Perceba que esse método é utilizado quando queremos criar combinações onde a ordem não importa.
Prosseguindo, na próxima página, entenda onde isso pode ser aplicado.

Combinações são comuns no dia a dia e certamente você já as utiliza. Confira um exemplo: imagine que você foi a uma padaria, e que os lanches estavam em promoção pelo preço de R$ 1. Como você só tinha R$ 2, precisou escolher qual deles iria comprar. A seguir, está o menu da padaria, contendo os lanches disponíveis.

Menu de lanches disponíveis na padaria - Promoção R$ 1
[Coxinha, Pão de Queijo, Folheado, Pastel, Esfiha, Empada]

As combinações de itens que podem ser comprados com R$ 2 são, por exemplo, coxinha e pão de queijo, coxinha e folheado, coxinha e pastel, empada e pastel, empada e esfiha etc. Agora, seu objetivo é saber qual combinação trará a maior satisfação. Como você pode perceber, a ordem que você vai comprar os itens não importa e por isso esse é um problema que pode ser resolvido com combinações.

Outro assunto que engloba as analises combinatórias é a permutação, que você conhecerá na próxima página.

Permutação é um dos assuntos discutidos na disciplina de análise combinatória e é uma técnica de contagem utilizada para determinar quantas maneiras existem para ordenar os elementos de um conjunto finito.

O método permutations, utilizado para fazer permutações, trata todos os elementos como únicos, baseado em suas posições, e não em seus valores. O parâmetro r é o tamanho da permutação e, se não especificado, ele é definido como o comprimento da lista de entrada. O próximo código demonstra como fazer permutações utilizando o método permutations. Confira:

import itertools

print(list(itertools.permutations([1,1]))) # [(1, 1), (1, 1)]

print(list(itertools.permutations([1, 2]))) # [(1, 2), (2, 1)]

print(list(itertools.permutations([1, 2, 3])))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(itertools.permutations([1, 2, 3],r=2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

Agora, vamos analisar linha por linha, começando após a importação do módulo itertools e sabendo que estamos convertendo os objetos retornados, transformando-os em listas:

Nas linhas 3 e 5, criamos uma permutação com dois elementos, como o valor de r não foi passado explicitamente, então, por padrão, o método considera o tamanho da lista, ou seja, r = 2.
Na linha 7, ele considera o r = 3, devido à lista possuir 3 elementos.
Por fim, na linha 9, o valor de r foi como passado por parâmetro, criando permutações com dois elementos. Isso prova que esse método é bastante flexível podendo ser usado em diversos problemas que envolvem combinações ordenadas.
Sabendo disso, você consegue pensar em alguma situação do dia a dia que pode ser resolvida com permutações? Acompanhe na próxima página.

Uma situação bem comum que vale ser citada aqui é a organização de uma casa. Por exemplo, lavar louças, limpar o quarto, limpar o banheiro, lavar e estender roupas, dentre muitas outras atividades. Então, para otimizar seu tempo, você pode determinar a melhor ordem de fazer essas atividades, como apresentado no quadro a seguir, que mostra uma coluna com as atividades e uma coluna com as possíveis ordens de execução dessas tarefas.

Atividades:
Lavar louças
Limpar quarto
Limpar banheiro
Lavar roupa
Estender roupa

Possíveis ordens
Lavar louça, limpar quarto, limpar banheiro, estender roupa, lavar roupa
Lavar louça, limpar quarto, limpar banheiro, lavar roupa, estender roupa
Lavar louça, limpar quarto, estender roupa, limpar banheiro, lavar roupa
Lavar louça, limpar quarto, estender roupa, lavar roupa, limpar banheiro
Lavar louça, limpar quarto, lavar roupa, limpar banheiro, estender roupa
Lavar louça, limpar quarto, lavar roupa, estender roupa, limpar banheiro etc.

Sabendo disso, você precisa testar as possíveis combinações de atividades para saber qual a ordem que você consegue fazer no menor tempo, certo?

Agora você pôde aprender a resolver problemas relacionados à contagem por análise combinatória, na próxima página, conhecerá a teoria dos conjuntos, que é aplicada a elementos que são relevantes para a Matemática e que facilitam o seu entendimento e a sua manipulação.

O produto cartesiano é o conjunto de todos os pares ordenados (x,y), tais que x pertence ao conjunto A e y pertence ao conjunto B, onde a ordem interfere na elaboração do conjunto, como mostra a figura a seguir.

https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura1.png
Figura 2 – Conjuntos que formam um produto cartesiano

O código seguinte demonstra como utilizar o método product, responsável por fazer o produto cartesiano, do módulo itertools.

import itertools

print(list(itertools.product([1, 2], repeat=2))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product([1, 2], [1, 2]))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product(['Python'], ['Academy', 'Rocks'])))
# [('Python', 'Academy'), ('Python', 'Rocks')]

print(list(itertools.product([1, 2], [3, 4], [5, 6])))
# [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

Agora, vamos analisar linha por linha, começando da linha 3 e sabendo que os objetos retornados são transformados em listas.

Na linha 3, utilizamos o argumento opcional repeat para especificar quantas vezes vamos repetir a lista de entrada, como utilizamos repeat = 2, a chamada desse método ficou equivalente à chamada do método na linha 5.
Na linha 7, é possível observar o produto cartesiano de duas listas de tamanhos diferentes.
Na linha 10, fizemos o produto cartesiano a partir de 3 listas, perceba que o tamanho do iterável final é igual ao produto do tamanho de cada elemento: 2 x 2 x 2 = 8.
Será que dessa vez vai existir alguma situação do dia a dia que podemos resolver com o produto cartesiano? Analise na próxima página.

Você já se deu conta de quantas vezes parou em frente ao seu guarda-roupa e ficou na dúvida de qual peça deveria vestir? Enquanto algumas pessoas sentem muita dificuldade em encontrar a combinação perfeita, outras pessoas fazem isso de modo simples e prático.

Criar um algoritmo para saber qual é a combinação mais bonita é um problema bem difícil para a máquina entender, pois beleza é um conceito subjetivo. Contudo, a máquina pode lhe auxiliar a criar todos os pares possíveis de blusa e calça diferentes, onde, a partir disso, será possível você testar todos os pares de roupas imagináveis e informar de qual gostou mais.

Como exemplo, considere a situação em que você tem várias blusas e calças de cores diferentes e precisa decidir qual a melhor combinação, como apresentado no quadro a seguir, que mostra uma coluna com as cores de blusas, uma coluna com as opções de calças e uma coluna com as possíveis combinações.

Blusas	        Calças	        Possíveis combinações
Blusa verde	    Calça preta	    Blusa verde com calça branca
Blusa vermelha	Calça branca	Blusa verde com calça azul
Blusa azul	    Calça azul	    Blusa verde com calça roxa
Blusa laranja	Calça roxa	    Blusa verde com calça jeans
Blusa rosa	    Calça jeans	    Blusa vermelha com calça preta etc

Como existem dois conjuntos distintos, o de blusas e o de calças, o produto cartesiano é o método ideal para resolver esse problema, pois esse método é capaz de criar todos os pares possíveis entre dois conjuntos distintos.

Na sequência, exercite o que você pôde aprender até o momento, resolvendo algumas questões.

Agora, que tal praticar um pouco o que você pôde estudar sobre dominação do módulo itertools. Para isso, resolva as questões a seguir. Caso tenha alguma dúvida, você pode voltar ao conteúdo para relembrar algum assunto.

Imagine que você tenha uma lista de nomes e quer escolher dois deles, um para ser o primeiro nome e o outro para ser o sobrenome. Qual seria o melhor método a se utilizar para criar todos os pares de nomes?

Para entender como os métodos aprendidos são utilizados em Machine Learning (ML), primeiro, você precisa entender que um algoritmo de Machine Learning serve para ensinar uma determinada máquina a desempenhar tarefas. Ele possibilita pegar um conjunto de dados de entrada e gerar as saídas com base em determinados padrões encontrados, como mostra a figura a seguir:

Figura 3 – Fluxo padrão de algoritmos de Machine Learning
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura2.png

Para ficar mais claro, confira dois exemplos de algoritmos de ML diferentes. Para o primeiro algoritmo, temos como entrada uma frase qualquer, que pode ser extraída, por exemplo, de redes sociais, de conversas diversas e outras. Com isso, o modelo retorna qual o possível sentimento que a pessoa teve quando escreveu a frase, como raiva, tristeza ou alegria, como ilustrado a seguir:

Figura 4 – Exemplo de conjuntos de dados de entrada e saída
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura3.png

O próximo algoritmo, ilustrado em sequência, recebe como entrada as informações de uma casa, como localização e quantidade de quartos. E o modelo retorna qual será o preço de avaliação da casa.

Figura 5 – Exemplo de conjuntos de dados de entrada e saída
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura4.png

A seguir, você vai conhecer onde podem ser utilizados os métodos que você pôde aprender nesta aula.

Agora imagine que você foi contratado pela Netflix e recebeu a demanda de um algoritmo de Machine Learning que tem como entrada um usuário e um filme e tem como saída a previsão da nota que aquele usuário dará ao filme, assim como ilustrado a seguir:

Figura 6 – Exemplo de conjuntos de dados de entrada e saída
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura5.png

Sabendo disso, você precisa fazer um código que sugira filmes aos usuários. Desse modo, precisamos testar todas as combinações possíveis de usuários e filmes e ver quais combinações possuem as melhores notas, como “Usuário 3 dará a nota 5 ao filme 2”, assim como mostra a próxima imagem. Então, qual o melhor método usar para fazer essa combinações?

Figura 7 – Exemplo de sistema de recomendação que prevê a nota que o usuário dará para um filme
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura6.png

Nesse caso, fazer o produto cartesiano é o mais indicado porque ele retornará todos os pares entre usuários e filmes, podendo testar todas as combinações possíveis. Note, na imagem, que foram feitas duas combinações com notas altas, agora é só sugerir esses filmes aos usuários correspondentes. A seguir, confira como utilizar o módulo log em nossos códigos.

# Tópico 2 – Expressões regulares

## Objetivos

Compreender a interpretação de strings em Python;
Organizar os caracteres especiais para expressões regulares;
Aplicar e praticar a utilização das funções de pesquisa.

Bem-vindo ao tópico de expressões regulares, também conhecidas como Regex (regular expression), em Python. Elas são uma ferramenta de programação muito poderosa, e são usadas para uma variedade de propósitos, como extração de recursos de texto, substituição de strings e outras manipulações de strings.

Não será exagero mencionar que sem ter conhecimento de Expressões Regulares, não é possível construir um sistema baseado em Processamento de Linguagem Natural (PLN), ou Natural Language Processing (NLP), como chatbots, interface de usuário conversacional, Web Scraping entre outros.

Regex tem muitos elementos e recursos importantes que ajudam a construir um sistema útil, solução de expressões adequadas para extração ou manipulação de strings.

Uma Expressão Regular é um conjunto de caracteres, ou um padrão, que é usado para localizar correspondência em uma determinada string. Na próxima página, conheça um exemplo de Expressão Regular.

Confira o exemplo de expressão regular a seguir:

[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

Essa é uma expressão que identifica endereços de e-mail como correspondências válidas. Ao longo das aulas, você vai entender o que cada parte dessa expressão significa, certo? Em regra, se houver um padrão em qualquer string, você pode facilmente extrair, substituir e fazer várias outras operações de manipulação de string usando expressões regulares.

As expressões regulares são uma linguagem em si, pois têm seus próprios compiladores e quase todas as linguagens de programação populares suportam o trabalho com regex.

A partir desse momento, ao utilizar regex, vamos sempre usar a letra r antes da string. O r indica que a string é bruta, desse modo não serão considerados caracteres especiais. Sem o r, a barra invertida (backslash) ‘\’ faria com que o caractere que vem a seguir fosse considerado um caractere especial. Como é mostrado no código seguinte, com e sem o r como prefixo da string:

print('\tTabulação') # ‘ Tabulação’

print(r'\tTabulação') # ‘\tTabulação’

A seguir, você vai descobrir como utilizar o módulo de expressões regulares para buscar padrões em uma string.

Os métodos que vamos usar para trabalhar com expressões regulares (regex) em Python reside em um módulo denominado re. Por enquanto, vamos nos concentrar no método search(). Esse método recebe como parâmetro uma expressão regular e uma string, e seu papel é fazer a varredura na string, procurando o primeiro local onde há uma correspondência do padrão regex que foi passado. O código a seguir demostra exemplos de utilização do método search.

import re

palavra = r'otorrinolaringologista 816'

print(re.search(r'rino', palavra)) # <re.Match object; span=(4, 8), match='rino'>

print(re.search(r'ri', palavra)) # <re.Match object; span=(4, 6), match='ri'>

print(re.search(r'rino', palavra).group(0)) # rino

print(re.search(r'100', palavra)) # None

Agora, vamos analisar linha por linha:

Na linha 1, podemos notar que o módulo re foi importado, isso servirá para utilizarmos os métodos de manipulação de regex;
Na linha 3, criamos uma variável chamada ‘palavra’ e atribuímos uma string bruta a ela utilizando o prefixo r;
Nas demais linhas, usamos o método search para encontrar uma correspondência do padrão, passada como argumento, na variável ‘palavra’. Ao encontrar a correspondência, o método search retorna um objeto Match, que contém o índice onde o padrão foi encontrado;
Na linha 5, foi encontrada uma correspondência da substring ‘rino’ entre os índices 4 e 8;
Na linha 7, utilizamos outra substring como padrão. Neste exemplo, a substring ‘ri’ contém duas vezes na variável ‘palavra’, entretanto, o método search retorna somente o objeto da primeira ocorrência que, nesse caso, estava entre os índices 4 e 6;
Na linha 9, ao utilizar o método group(0) do objeto Match retornado é retornada a correspondência encontrada;
Por fim, na linha 11, o valor retornado é None pois não foi encontrada correspondência na string ‘palavra’.

Nas expressões anteriores, você pode notar que não foram usados caracteres especiais, que são símbolos que representam classes de caracteres comuns, mas eles são bem comuns na prática diária. O quadro a seguir mostra uma lista desses caracteres, na coluna da esquerda, e o que eles representam, na coluna da direita.

Símbolo	Representação
.	Qualquer caractere exceto nova linha
\d	É um dígito (0-9)
\D	Não é um dígito (0-9)
\w	Caractere de palavra (a-z, A-Z, 0-9, _)
\W	Não é um caractere verbal
\s	Espaço em branco (espaço, tabulação, nova linha)
\S	Não é espaço em branco (espaço, tabulação, nova linha)
\b	Limite de palavras
\B	Não é um limite de palavra
^	Começo de uma string
$	Fim de uma string
[]	Corresponde aos caracteres entre colchetes
[^ ]	Corresponde a caracteres, MENOS o que está entre colchetes
|	Ou
( )	Grupo

Por exemplo, ao invés de procurar um número específico em uma string, você pode utilizar o símbolo \d, que representa um número entre 0 e 9, deixando a pesquisa mais flexível. Na próxima página, confera onde utilizar regex no dia a dia.

Há alguns mecanismos de localização, como o do editor de texto do Visual Studio Code (vscode), que permitem a utilização de expressões regulares para encontrar correspondências no documento, basta ativá-lo. A imagem seguinte mostra um pequeno exemplo no vscode de uma pesquisa usando o caractere especial \d. Com isso, é possível notar que a pesquisa buscou todos os dígitos do documento (caracteres marcados de laranja à direita).

Figura 8 – Exemplo no vscode de pesquisa que usa o caractere especial \d
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura7.jpg

Você pode utilizar essa função de pesquisa no seu dia a dia, quando, por exemplo, precisar encontrar quais e-mails estão contidos dentro de um grande texto. Isso parece simples de fazer, mas considere que existem e-mails dos mais diferentes domínios além de caracteres ‘@’ que não representam um e-mail. Essas possibilidades deixam todo o problema mais complexo.

Nas próximas páginas, você pode conferir, a partir de exemplos, como utilizar os caracteres especiais e como utilizar regex para resolver problemas complexos.

amos analisar um caso. Para isso, considere a lista de dados pessoais a seguir:

Laura Maria da Silva
(46) 93201-6392
(89) 42010-7411
(61) 47405-4895
Rua José Geraldo
lauramaria@hotmail.com
Le@d Dell Technologies

Como você faria para extrair os números de telefone com os seus respectivos DDDs, a partir da string apresentada? Bom, primeiro você deve tentar buscar somente o DDD de cada número. Confira isso no seguinte código:

import re
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61)
        47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
        Technologies"

print(re.search(r'[0-9][0-9]', palavra)) # <re.Match object; span=(23, 25), match='46'>

print(re.findall(r'[0-9][0-9]', palavra))
# ['46', '93', '20', '63', '92', '89', '42', '01', '74', '11', '61', '47', '40', '48', '95']

print(re.findall(r'\W[0-9][0-9]\W', palavra)) # ['(46)', '(89)', '(61)']

Agora, analise linha por linha, começando após a importação do módulo. Nos exemplos, vamos utilizar o símbolo [0-9], que é equivalente ao símbolo \d, ou seja, que significa um número qualquer de 0 a 9. Ao unirmos dois símbolos lado a lado significa que queremos duas vezes aquele símbolo. No caso de [0-9][0-9], significa que queremos um número de dois dígitos:

Na linha 2, criamos uma variável chamada ‘palavra’ e atribuímos uma string bruta a ela utilizando o prefixo r;
Na linha 6, é possível notar que o método retorna um objeto Match, que contém a correspondência ‘46’, e essa substring está entre os índices 23 e 25, ou seja, o primeiro DDD;
Na linha 8, optamos por utilizar o método findall, que, ao invés de retornar um objeto da primeira correspondência encontrada, retornará uma lista de todas as correspondências. É possível notar, na linha 8, que o método retornou vários pares de números, dentre eles estão os DDDs de cada número de telefone;
Na linha 11, utilizamos o ‘\W’, que é um símbolo que significa um caractere não verbal, que corresponderá aos parênteses que ficam em volta do DDD. Dessa forma, conseguimos buscar todos os DDDs da personagem do exemplo.

A seguir conheça como deixar a expressão ainda mais simples utilizando quantificadores.

Quanto mais padrões você coloca nas expressões regulares, maiores elas ficam. Para facilitar a criação das expressões, são utilizados quantificadores de repetição. Esses quantificadores possuem o papel de fazer com que os mecanismos das **expressões regulares correspondam a uma determinada quantidade de ocorrências**. A tabela a seguir associa um símbolo à quantidade de ocorrências que aquele símbolo representa. Confira:

Quantificadores

*	0 ou mais
+	1 ou mais
?	0 ou um
{3}	Número exato
{3,4}	Faixa de números (mínimo, máximo)

Quais mudanças você faria na expressão anterior, de identificar os DDDs, para deixar a expressão mais simples, utilizando os quantificadores? No decorrer deste curso, você vai aprender a como utilizar esses quantificadores para deixar as expressões mais simples, a partir de exemplos. Vamos nessa!

Para você entender melhor como utilizar os quantificadores, observe três exemplos de correspondência de DDD apresentados no seguinte código:

import re
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61)
        47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
        Technologies"

print(re.findall(r'\W[0-9][0-9]\W', dados)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\W[0-9]{2}\W', dados)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\W\d{2}\W', dados)) # ['(46)', '(89)', '(61)']

Nas linhas 6, 8 e 10 dos exemplos apresentados, é mostrado o mesmo padrão utilizando símbolos diferentes:

Na linha 6, criamos uma expressão regular sem utilizar quantificadores, repetindo o símbolo duas vezes para achar a ocorrência duas vezes;
Na linha 8, utilizamos o quantificador {2} para explicitar que queremos somente duas correspondências dessa expressão, ou seja, dois dígitos. Não havendo a necessidade de repetir símbolos;
Na linha 10, foi demonstrado que o caractere especial \d é equivalente ao caractere especial [0-9], como o quantificador {2}.
Para exercitar seu conhecimento sobre o assunto em questão, responda ao que se pede na página a seguir.

De acordo com o que você pôde aprender sobre identificação do DDD de um número usando ER, responda a questão a seguir:

Agora vamos trabalhar com um número telefônico completo. Como já temos a expressão que busca somente o DDD, vamos fazer agora a expressão que busca somente o número telefônico. O código a seguir demonstra qual expressão regular foi utilizada para reconhecer esse número. Observe:

import re
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61)
        47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
        Technologies"

print(re.findall(r'\W\d{2}\W', dados)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\d{5}\W\d{4}', dados)) # ['93201-6392', '42010-7411', '47405-4895']

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', dados))
# ['(46) 93201-6392', '(89) 42010-7411', '(61) 47405-4895']


Sobre esse código, cabe fazer algumas observações:

Na linha 8, é possível utilizar a expressão ‘\d{5}’, que significa que queremos um número qualquer de 5 dígitos;
Para corresponder ao traço ‘-’, utilizamos o símbolo ‘\W’;
Por fim, para o número restante de 4 dígitos, utilizamos a expressão ‘\d{4}’;
Após definidas as duas expressões, basta uni-las em uma só. Para isso, utilizamos o símbolo ‘\s’, que representa um espaço.
Com isso, você consegue buscar os números telefônicos de qualquer texto. Mas como você já deve saber, nem tudo é perfeito, e haverá números sem o DDD em alguma parte do texto. Exercite seus conhecimentos sobre esse assunto visto neste tópico na próxima página.

Continuando o que foi mostrado, o que você faria se fossem retirados o DDD de um número telefônico da sting como mostrado a seguir? Analise-a e pense em uma solução que você utilizaria para buscar todos os números telefônicos, novamente, com e sem DDD. Vamos lá!

palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61)
        47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
        Technologies"
E aí, o que você achou? Chegou a uma conclusão? Compare o que você concluiu com o que será mostrado e explicado na próxima página.

Vamos utilizar a nova string que foi apresentada na tela anterior. Agora que não temos mais o DDD de um dos números telefônicos, se usássemos a expressão regular '\W\d{2}\W\s\d{5}\W\d{4}‘, apresentada no código anterior, só seriam retornados 2 dos 3 números contidos na nova string. Sabendo disso, vamos criar uma nova expressão que busca números telefônicos sem o DDD. O código a seguir mostra o retorno esperado de cada expressão regular:

import re
palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61)
        47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d Dell
        Technologies"

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', dados)) # ['(46) 93201-6392', '(61) 47405-4895']

print(re.findall(r'\d{5}\W\d{4}', dados)) # ['93201-6392', '42010-7411', '47405-4895']

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}', dados))
# ['(46) 93201-6392', '42010-7411', '(61) 47405-4895']
Analisando o código, na linha 8, é possível notar a expressão regular para encontrar os números telefônicos sem o DDD, entretanto, queremos os números telefônicos que contenham ou não os DDDs. Para isso, é necessário combinar as duas expressões para buscar os dois formatos de números telefônicos. Assim, basta unir as duas expressões utilizando o operador ou ‘|’, como demonstrado na linha 10.

Na próxima página, leia uma curiosidade sobre o módulo de expressões regulares do Python, em seguida, resolva um exercício para consolidar seus conhecimentos.

O módulo de expressões regulares do Python possui uma série de funções úteis para resolver qualquer problema, como uma função de substituição ou agrupamento. Para mais detalhes, procure a documentação do Python neste link Operações com expressões regulares.

Suponha que você possui uma empresa, mas por ser uma empresa recente, não há muitos clientes. Então, você decide enviar alguns e-mails para as pessoas, explicando quais serviços a sua empresa oferece. Infelizmente, você percebe que não possui lista de e-mails para que possa enviar um material de divulgação. De repente, você resolve procurar listas de e-mails na internet e encontra um texto contendo vários dados, inclusive e-mails de pessoas. Agora sua missão é extrair somente os e-mails que estão contidos nesse texto. Você consegue pensar em uma expressão regular que busca os e-mails válidos em uma string?

palavra = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu,
        francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'
O código apresentado contém uma string, que é apenas um trecho do texto encontrado na internet. Sua missão é criar uma expressão regular para reconhecer os e-mails contidos nessa string, tendo em vista que o último elemento dessa lista não é um e-mail.

Na próxima página, você vai conhecer como criar uma expressão regular que reconheça somente os e-mails em uma string.

Para resolver o problema da página anterior, vamos dividi-lo em partes menores. Assim, conseguiremos resolvê-lo por inteiro. Primeiro, vamos fazer uma expressão que busque a primeira parte do e-mail, ou seja, até o ‘@’. Depois, vamos fazer uma expressão que busque a segunda parte do e-mail, iniciando do ‘@’ até o ‘.’. Como é descrito neste código:

import re
palavra = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu,
        francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'

print(re.findall(r'[a-zA-Z0-9_.-]+@', dados))
# ['contato@', 'franciscojose@', 'ana.julia@', 'francisca-321-aline@', 'Le@']

print(re.findall(r'@[a-zA-Z0-9-]+\.', dados))
# ['@dellead.', '@yahoo.', '@universidade.', '@meu-trabalho.']

print(re.findall(r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', dados))
# ['@dellead.com', '@yahoo.com.br', '@universidade.edu', '@meu-trabalho.net']

print(re.findall(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', dados)) # ['contato@dellead.com', 'franciscojose@yahoo.com.br', 'ana.julia@universidade.edu', 'francisca-321-aline@meu-trabalho.net']
Agora, vamos detalhar o código:

Na linha 5, a expressão regular ‘[a-zA-Z0-9_.-]’ significa a busca de um caractere entre ‘a’ e ‘z’, ou um dígito entre 0 e 9, ou um símbolo entre ‘_’, ‘.’ e ‘-’. Com o símbolo ‘+’ após essa expressão ([a-zA-Z0-9_.-]+), isso significa a busca por uma cadeia de caracteres (ou uma palavra) com tamanho igual ou maior que 1, que poderá conter todos os caracteres anteriormente citados e que termine com o símbolo ‘@’;
Na linha 9, buscamos uma cadeia de caracteres que começam com ‘@’ e terminam com ‘.’ e que podem conter letras, números e traços;
Na linha 10, incrementamos a expressão da linha 9, que significa a busca de qualquer cadeia de caracteres após o ‘.’;
Na linha 15, juntamos todas as expressões regulares e conseguimos distinguir todos os e-mails válidos.
Regex é muito útil quando é necessário automatizar tarefas de encontro de padrões específicos em texto. Agora que dominamos Regex, vamos conhecer a próxima biblioteca padrão.

# Tópico 3 – Logging

## OBJETIVOS

Definir configurações básicas da ferramenta logging;
Avaliar e formatar a saída de mensagens;
Classificar a gravidade das mensagens.
Neste tópico, trataremos sobre Logging, uma ferramenta que pode ajudar você a desenvolver uma melhor compreensão do fluxo de um programa e a descobrir cenários que você pode nem ter pensado durante o desenvolvimento. Por exemplo, lhe alertar caso uma expressão regular não esteja com um padrão de correspondência aceitável. Portanto, um arquivo de log pode ser utilizado para auditoria e diagnóstico de problemas em softwares, informando qual era o estado do programa antes de chegar à linha de código onde ocorreu o erro.

Ao registrar dados úteis nos lugares certos, você pode tanto depurar erros facilmente quanto usar os dados para analisar o desempenho do aplicativo para planejar o dimensionamento ou observar os padrões de uso. Desse modo, o logging torna-se uma ferramenta essencial para o cientista de dados, podendo ser útil para saber se seu modelo de Machine Learning ainda possui uma boa performance, podendo até dar respostas caso não esteja prevendo os dados tão bem.

Certamente, você já deve ter lido ou ouvido falar em caixa-preta (mostrada na imagem a seguir), nome popular dado ao sistema de registro de dados existentes em aviões. Esse sistema é usado, por exemplo, em casos de acidentes ou demais problemas que ocorrem durante o voo, sendo a coisa mais importante a se achar após os sobreviventes. Mas, afinal, o que essa caixa tem de mais, como a apresentada a seguir?

Figura 9 – Caixa preta

A caixa-preta possui mensagens enviadas e recebidas à torre de comandos/operações bem como condições do voo, conversas que ocorrem dentro da cabine e variações técnicas de aceleração, altitude e potência da aeronave. A incorporação desses sistemas nos aviões permitiu a melhoria da segurança nas viagens aéreas, já que foi possível detectar falhas que anteriormente davam origem a acidentes graves cuja causa não era possível ou muito difícil de determinar.

Agora imagine que a caixa-preta seja um arquivo de log, o avião seja o software e as pessoas sejam os usuários do sistema. Caso o software apresente algum problema ou pare de funcionar corretamente, você deve buscar o registro de log que contém os possíveis erros ou falhas do sistema.

Na próxima página, conheça como é formada a estrutura do log.

A imagem a seguir demonstra o exemplo de um arquivo de log, aberto no programa Bloco de Notas, nomeado de ‘logs’. Que tal conhecer detalhes sobre esse arquivo? Vamos lá?!

Figura 10 – Exemplo de um arquivo de log
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura9.png

Esse log foi criado a partir de um programa, que não nos é relevante neste momento. Primeiro, começamos com a extensão do arquivo. Todo arquivo possui uma extensão, que seria a palavra que aparece logo após o último ponto, em um nome de arquivo. Por exemplo, pode possuir a extensão png, jpeg ou jpg; e um documento pode possuir a extensão doc, txt ou pdf, assim como os arquivos de log possuem a extensão log.

Na próxima página, confira como é formatado o arquivo de log e o que é necessário que ele contenha.

Observe um trecho do arquivo de log que foi transcrito. Nesse caso, focamos somente nos três primeiros registros do arquivo ‘logs’, em que cada uma das linhas segue um padrão bem definido.

Figura 11 – Exemplo de um arquivo de log
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura10.png

Como você pôde notar, na primeira parte de um log, há os dados de data e hora. Isso é muito útil para saber que horas ocorreu o problema ou para encontrar um problema ocorrido anteriormente. Na segunda parte, há um dado de nível de gravidade que nos diz o quão crítica é aquela mensagem. Nesse exemplo, é possível perceber que todas as mensagem são para fins de informação (INFO). Por fim, na terceira parte, consta a mensagem em si.

A partir desse log, podemos tirar uma conclusão: o fluxo do programa que o gerou seguia mais ou menos estes passos:

1. Tenta se conectar ao banco de dados (MongoDB);
2. Faz leituras dos dados de um dia especifico na tabela 1;
3. Faz leituras dos dados de um dia especifico na tabela 2.
Repetindo esse fluxo constantemente.
Assim, você pode entender como um log é importante, pois ele possui o papel de gravar as mensagens de como anda o processo de um determinado programa, facilitando o trabalho de manutenção do programador. Na próxima página, você vai aprofundar mais seus conhecimentos em como criar um arquivo log e nos níveis de gravidade que um log pode ter.

Antes de construir nosso primeiro programa que utiliza log, temos que entender como funcionam as mensagens de log, certo? Essas mensagens possuem uma categorização. Por padrão, existem cinco níveis que indicam a gravidade dos eventos. Cada um possui um método correspondente que pode ser usado para registrar eventos nesse nível de gravidade.

O quadro a seguir contém uma coluna com o nome do nível do log, outra com o valor de gravidade do nível do log e outra com a explicação de quando uma mensagem deve conter esse nível de log, em ordem decrescente de gravidade.

Nível	    Valor gravidade	Quando deve ser utilizado em uma mensagem
CRITICAL	50	            Quando há uma interferência que o programa não consegue continuar a funcionar corretamente.
ERROR	    40	            Quando ocorre uma interferência momentânea de alguma funcionalidade.
WARNING	    30	            Quando ocorre um erro mas não interfere na execução do programa.
INFO	    20	            Para obter informações do programa, como ele está funcionando e como está sendo utilizado, para fins de conhecimento.
DEBUG	    10	            Quando se quer saber se todas as instruções estão funcionando corretamente.

Na próxima página, é apresentado como escrever um código que cria logs, utilizando esses níveis de gravidade.

O módulo de registro (logging) fornece um registrador padrão, que permite que você comece a criar mensagens de log sem precisar fazer muitas configurações. A seguir, há um código simples que cria cinco mensagens de log. Em seguida, é mostrado o arquivo de log gerado pelo código.

import logging

#Criação e configuração do objeto logger
logging.basicConfig(filename = 'logs.log')
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

Figura 12 – Arquivo de log gerado pelo código
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura11.png

Entenda o que acontece em cada linha:

Na linha 1, foi feita a importação do módulo de registro;
Na linha 4, foi criado o arquivo de log chamado ‘logs.log’;
Na linha 5, foi atribuída a variável ‘logger’ ao arquivo criado na linha 4;
Da linha 8 à 12, foram criadas várias mensagens de log, cada uma com um nível de gravidade diferente.
A saída mostra o nível de gravidade e a palavra ‘root’ antes de cada mensagem. ‘root’ é o nome que o módulo de registro dá ao seu criador de logs padrão. Essa formatação, que mostra o nível, o nome e a mensagem, separados por dois pontos ( :), é o formato de saída padrão. Entretanto, a saída pode ser configurada para incluir itens, como dados de data, hora, número de linha e outros detalhes.

Observe que as mensagens ‘debug’ e ‘info’ não foram registradas. Isso ocorre porque, por padrão, o módulo de registro salva as mensagens com um nível de gravidade igual à ‘warning’ ou superior. Você pode mudar isso configurando o módulo de registro para registrar eventos de todos os níveis, se desejar.

Entenda mais sobre prioridades na próxima página.

Agora, você tem o código que foi utilizado na página anterior. Contudo, foi feita uma pequena alteração nele para que também sejam persistidas mensagens com um menor nível de gravidade. Após o código, é mostrada a imagem de como ficará o arquivo de saída do log depois da alteração do código:

import logging

#Criação e configuração do objeto logger
logging.basicConfig(filename = 'logs.log',
level = logging.DEBUG
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

Figura 13 – Arquivo de log gerado pelo código
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104617971174153/aula/img/figura12.png

Usando o parâmetro level no basicConfig(), você pode definir o nível de mensagens de log que deseja registrar. Isso pode ser feito passando como argumento uma das constantes disponíveis na classe, permitindo que todas as mensagens de valor, igual ou acima, do valor da constante definida sejam registradas.

Na linha 5, definimos agora o nível mais baixo de log. Isso significa que todas as mensagens com gravidade igual ou maior que Debug serão apresentadas. Isso permite que, quando necessário, você possa mudar o nível de gravidade para fazer manutenções no código. Entretanto, a formatação da mensagem de log não está tão clara e legível. Na página seguinte, você confere como torná-la mais amigável.

Embora você possa passar qualquer variável, que venha representar uma string de seu programa, como uma mensagem para seus logs, existem alguns elementos básicos que podem ser facilmente adicionados ao formato de saída.

O quadro a seguir mostra a lista de atributos disponíveis para formatar a saída do log. Na coluna da esquerda, está o nome do atributo; na coluna do meio, a formatação; na coluna da direita, a descrição. Para facilitar, vamos utilizar os atributos mais importantes, que são: asctime, nome do nível e mensagem.

O atributo “asctime” retorna a hora que a mensagem foi gravada. O atributo “nome do nível” retorna qual o nível de gravidade da mensagem. Por fim, o atributo “mensagem” retorna a mensagem gravada.

Nome do atributo	Formatação	Descrição
asctime	            %(asctime)s	Hora legível por humanos quando o registro é criado. Por padrão, ele está no formato '2003-07-08 16: 49: 45.896' (os números após a vírgula correspondem à parte em milissegundos do tempo).
Nome do nível	    %(levelname)s	Nível de registo de texto para a mensagem (‘DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
mensagem	        %(message)s	A mensagem registrada quando o log é criado.

Você pode encontrar as informações contidas na imagem no site do Python, no link que traz informações sobre Recurso de utilização do Logging para Python.

Na próxima página, você vai conhecer como formatar a saída do log para conter os atributos descritos anteriormente.

O seguinte código exemplifica como configurar o log para deixar a formatação das mensagens como queremos. Após o código, é apresentado o texto que é o exemplo de como ficará a saída no arquivo de log.

import logging

#Criação e configuração do objeto logger
FORMATACAO_MSG = "%(asctime)s | %(levelname)s -> %(message)s"

logging.basicConfig(filename = 'logs.log',
level = logging.DEBUG,
format = FORMATACAO_MSG)
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')

Agora confira o texto de como ficará a saída no arquivo de log:

2021-05-10 20:36:38,996 | DEBUG -> depuração
2021-05-10 20:36:38,997 INFO -> informação
2021-05-10 20:36:38,997 | WARNING -> aviso
2021-05-10 20:36:38,997 ERROR -> erro
2021-05-10 20:36:38,997 CRITICAL -> critico
Como você pode notar, a formatação do log foi definida na linha 4, o %(asctime)s adiciona o hora e a data da mensagem, %(levelname)s adiciona a gravidade da mensagem e %(message)s adiciona a mensagem em si.

Na linha 8, utilizamos a variável ‘FORMATACAO_MSG’, que contém a formatação do log, como argumento para o parâmetro format no basicConfig(). Assim, você pode definir o formato da mensagem de registro, facilitando a leitura do arquivo e a identificação de algum erro ocorrido.

Na próxima página, você conhecerá outras configurações que pode fazer no arquivo de log.

Ao utilizar o módulo de log, você vai se deparar com o seguinte problema, os novos logs de utilização do sistema se juntarão com os antigos, mesmo que o programa seja reiniciado. O texto a seguir é um exemplo das mensagens registradas em um arquivo de log.

2021-05-10 20:36:38,996 | DEBUG -> debug
2021-05-10 20:36:38,997 | INFO -> info
2021-05-10 20:36:38,997 | WARNING -> warning
2021-05-10 20:36:38,997 | ERROR -> error
2021-05-10 20:36:38,997 | CRITICAL -> critical
2021-05-10 20:39:52,303 | DEBUG -> debug
2021-05-10 20:39:52,304 | INFO -> info
2021-05-10 20:39:52,384 | WARNING -> warning
2021-05-10 20:39:52,384 | ERROR -> error
2021-05-10 20:39:52,304 | CRITICAL -> critical
Neste log apresentado, o programa foi executado duas vezes, uma execução às 20:36:38 e outra às 20:39:52. Entretanto, ao invés de haver somente os dados do novo log, houve um acréscimo de mensagens novas ao log.

Quem define esse comportamento é o atributo filemode. O padrão do filemode na configuração do log é a letra “a”, que significa anexar.

Prosseguindo nesta aula, saiba como apagar os dados antigos de log a cada nova execução do programa.

Para apagar os dados antigos de log, temos que mudar o valor atribuído ao parâmetro filemode. Para isso vamos defini-lo como “w”, essa letra significa que queremos sobrescrever os dados do log a cada nova execução do programa. Em seguida, confira o código alterado e um exemplo do novo log gerado.

import logging

#Criação e configuração do objeto logger
FORMATACAO_MSG = "%(asctime)s | %(levelname)s -> %(message)s"

logging.basicConfig(filename = 'logs.log',
level = logging.DEBUG,
format = FORMATACAO_MSG
filemode = 'w')
logger = logging.getLogger()

#Testando o logger
logger.debug('depuração')
logger.info('informação')
logger.warning('aviso')
logger.error('erro')
logger.critical('critico')
Confira agora o código alterado e um exemplo do novo log gerado.

2021-05-10 20:43:30,103 | DEBUG -> depuração
2021-05-10 20:43:30,104 | INFO -> informação
2021-05-10 20:43:30,184 | WARNING -> aviso
2021-05-10 20:43:30,184 | ERROR -> erro
2021-05-10 20:43:30,104 | CRITICAL -> critico
Na linha 9 desse código apresentado, está a alteração feita no parâmetro filemode. Desse modo, perceba que o novo arquivo de log gerado não contém as mensagens antigas de log.

Na próxima página, usaremos exceções para implementar logs em um programa, os conceitos sobre exceções foram apresentados na aula sobre POO do curso de Introdução a Python. Por exemplo, uma exceção que utilizaremos é chamada de ZeroDivisionError, que é disparada quando você tenta dividir um número por zero.

A seguir, há o código de um programa que calcula a divisão entre dois números, repetindo esse processo três vezes até sua finalização. Além disso, você encontra a saída do código e os dados que foram inseridos manualmente, em tempo de execução.

for _ in range(3):
  try:
    print('Vamos dividir dois números!')

    num_1 = int(input('Digite o primeiro número:'))
    num_2 = int(input('Digite o segundo número:'))

    print('O resultado é',num_1/num_2)

  except ZeroDivisionError:
    print('Essa operação é impossível')

  except Exception as erro:
    print(erro)
    print('Tente novamente')

  finally:
    print('----------------------')

Vamos dividir dois números!
Digite o primeiro número: 1
Digite o segundo número: 2
O resultado é 0.5
Vamos dividir dois números!
Digite o primeiro número: 2
Digite o segundo número: 0
Essa operação é impossível
Vamos dividir dois números!
Digite o primeiro número: 7
Digite o segundo número: a
invalid literal for int() with base 10: 'a‘
Tente novamente
Uma das coisas que mais chama a atenção nos dados de saída, é a linha que contém invalid literal for int() with base 10: 'a‘. Como não há um registro de logs, é necessário apresentar o erro na tela, porque, caso escondêssemos o erro, não saberíamos que erro correu para conseguirmos corrigi-lo.

Esse código foi feito para termos uma base de como um programa fica sem utilizar técnicas de log. A seguir, você terá o mesmo código com a adição das mensagens de log para fins de comparação. Tente fazê-lo antes de comparar com a implementação a seguir.

O código anterior foi alterado para adicionarmos as mensagens de log. A seguir, observe o código modificado e, em seguida, a saída dos dados na tela.

logger.info('O programa foi iniciado')
for i in range(3):
  try:
    logger.debug('Iteração número {0}'.format(i))
    print('Vamos dividir dois números!')

    num_1 = int(input('Digite o primeiro número:'))
    logger.debug('O usuário digitou o primeiro número: {0}'.format(num_1))

    num_2 = int(input('Digite o segundo número:'))
    logger.debug('O usuário digitou o segundo número: {0}'.format(num_2))

    resultado = num_1/num_2
    print('O resultado é',resultado)
    logger.debug('O resultado da operação: {0}'.format(resultado))

  ZeroDivisionError:
    print('Essa operação é impossível')
    logger.warning('O usuário tentou fazer uma divisão por 0')

  Exception as erro:
    print('Erro, tente novamente!')
    logger.error('Erro não esperado ->'+str(erro))

  finally:
    print('----------------------')

logger.info('O programa foi finalizado')

Vamos dividir dois números!
Digite o primeiro número: 1
Digite o segundo número: 2
O resultado é 0.5
Vamos dividir dois números!
Digite o primeiro número: 2
Digite o segundo número: 0
Essa operação é impossível
Vamos dividir dois números!
Digite o primeiro número: 7
Digite o segundo número: a
Erro, tente novamente!

Nessa versão, não é preciso mais mostrar o erro na tela, agora os erros estão registrados no log. Foram deixadas implícitas a importação e a configuração do módulo logging. Por fim, confira na próxima página como ficou o arquivo de log.

Como podemos observar, o texto a seguir exemplifica quais as mensagens que foram armazenadas no log após a alteração do programa. O nosso programa agora nos dá todas as informações sobre sua execução, desde inicialização à finalização do programa. Observe.

2021-05-10 20:46:30,280 | INFO -> O programa foi iniciado
2021-05-10 20:46:30,280 | DEBUG -> Iteração número 0
2021-05-10 20:46:34,700 | DEBUG -> O usuário digitou o primeiro número: 1
2021-05-10 20:46:35,271 | DEBUG -> O usuário digitou o segundo número: 2
2021-05-10 20:46:35,271 | DEBUG -> O resultado da operação: 0.5
2021-05-10 20:46:35,281 | DEBUG -> Iteração número 1
2021-05-10 20:47:02,141 | DEBUG -> O usuário digitou o primeiro número: 2
2021-05-10 20:47:03,901 | DEBUG -> O usuário digitou o segundo número: 0
2021-05-10 20:47:03,901 | WARNING -> O usuário tentou fazer uma divisão por 0
2021-05-10 20:47:03,901 | DEBUG -> Iteração número 2
2021-65-10 20:47:07,237 | DEBUG -> O usuário digitou o primeiro número: 7
2021-05-10 20:47:08,485 | ERROR -> Erro não esperado -> invalid literal for int() with base 10: 'a‘
2021-05-10 20:47:08,486 | INFO -> O programa foi finalizado

As informações de debug fornecem o passo a passo de como o programa é executado para facilitar a manutenção de erros futuros. Na mensagem de nível ‘erro’ do log, foi impressa a exceção disparada naquele momento, ou seja, não esperávamos que o usuário digitasse uma letra. Caso queira diminuir o número de mensagens de logs, basta alterar o valor do atributo level nas configurações do log.

Você pode utilizar os logs para acompanhar a performance do seu algoritmo de Machine Learning para saber se ele ainda está fornecendo previsões boas e para quando for preciso dar a próxima manutenção.

Chegamos ao fim dessa aula. Espero que você tenha gostado dessa jornada. Ao longo dos estudos, você pôde aprender três novas ferramentas essenciais para ter em seu kit de ferramentas. Com o itertools, você pode escrever um código mais rápido e com maior eficiência de memória, que geralmente é mais simples e fácil de ler.

Além disso, você conheceu como criar padrões complexos com expressões regulares e executar correspondência de regex em Python, muito utilizado em chatbots, para facilitar o trabalho com strings. Por fim, aprendeu a utilizar o módulo de registro, cujo design é muito prático e deve se adequar ao seu caso de uso em qualquer projeto. Você pode adicionar um log básico a um projeto pequeno ou pode ir tão longe quanto quiser caso esteja trabalhando em um grande projeto.

Essas três ferramentas removerão muitos atritos do seu processo de desenvolvimento e lhe ajudará a encontrar oportunidades para levar seu aplicativo para o próximo nível. Embora você tenha estudado muitas técnicas, essa aula apenas contempla a superfície do assunto. Isso significa que sua jornada está apenas começando.

Bons estudos!

## Referências
DOCS PYTHON. A Biblioteca Padrão do Python. Disponível em: https://docs.python.org/pt-br/3/library/ - Acesso em: 25 maio 2021
DOCS PYTHON. itertools - Funções que criam iteradores para laços eficientes. Disponível em: https://docs.python.org/pt-br/3/library/itertools.html - Acesso em: 25 maio 2021.
DOCS PYTHON. logging- Recurso de utilização do Logging para Python. Disponível em: https://docs.python.org/pt-br/3/library/logging.html - Acesso em: 25 maio 2021.
DOCS PYTHON. re - Operações com expressões regulares. Disponível em: https://docs.python.org/pt-br/3/library/re.html - Acesso em: 25 maio 2021.
GITHUB. CoreyMSchafer/code_snippets. Disponível em: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions - Acesso em: 25 maio 2021.
PYTHON ACADEMY. A biblioteca itertools do Python. Disponível em: https://pythonacademy.com.br/blog/a-biblioteca-itertools-do-python - Acesso em: 25 maio 2021.
REAL PYTHON.Itertools in Python 3, By Example. Disponível em: https://realpython.com/python-itertools/ - Acesso em: 25 maio 2021.
REAL PYTHON. Logging in Python. Disponível em: https://realpython.com/python-logging/ - Acesso em: 25 maio 2021.
REAL PYTHON. Regular Expressions: Regexes in Python (Part 1). Disponível em: https://realpython.com/regex-python/ - Acesso em: 25 maio 2021.
WIKIPÉDIA. Expressão regular. Disponível em: https://pt.wikipedia.org/wiki/Express%C3%A3o_regular - Acesso em: 25 maio 2021.

Para conhecer o significado dos termos técnicos estudados em nossa aula, selecione a palavra desejada.

## Glossário

Objeto iterável
https://leadfortaleza.com.br/ead/glossary/Objeto_iteravel
Avaliação preguiçosa
https://leadfortaleza.com.br/ead/glossary/Avaliacao_preguicosa
Expressão regular
https://leadfortaleza.com.br/ead/glossary/Expressao_regular
Regex
https://leadfortaleza.com.br/ead/glossary/Regex
PLN
https://leadfortaleza.com.br/ead/glossary/PLN
ML
https://leadfortaleza.com.br/ead/glossary/ML

Um baralho é um conjunto de cartas que compõem um jogo. Geralmente, os baralhos possuem 52 cartas, sendo 13 cartas de cada uma das quatro categorias ou naipes (paus, ouros, copas e espadas). Sendo assim, cada naipe possui cartas com valores de 1 a 13. Então, imagine que você possui os dois conjuntos, naipes = [paus, ouros, copas, espadas] e valores = [1,2,3,4,5,6,7,8,9,10,11,12,13]. A partir dessas duas listas, qual método é o mais indicado para se obter todos os pares de um baralho? Do 1 de paus ao 13 de espadas.