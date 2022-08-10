# INTRODUÇÃO

Você está preparado para aprender sobre a mais importante estrutura de dados para operações científicas em Python, conhecer o módulo que contém as principais ferramentas numéricas da atualidade, estudar o módulo que é base para as maiores bibliotecas de Machine Learning e programar utilizando funções que são rápidas e fáceis de usar? Então, seja bem-vindo à aula sobre o módulo Numpy!

Nesta aula, você irá conhecer o módulo NumPy, que é o principal módulo para operações numéricas, tanto que virou padrão na comunidade, principalmente pela sua representação de matrizes, chamadas de NumPy arrays. Aqui, você também aprenderá que pode mascarar uma matriz caso ela tenha valores inválidos. Você não vai mais querer saber de listas!

Além disso, irá conhecer as principais funções disponíveis neste módulo. Por meio de uma série de aplicações, você deverá consolidar bem os conceitos desta aula. Ah, caso você queira acompanhar a aula de forma mais prática e já ir aplicando o que for aprendendo, use o programa Jupyter notebook!

Vamos começar?

## Objetivos
Conhecer a estrutura de dados NumPy Array;
Aplicar máscaras em matrizes;
Praticar com as diferentes funções do módulo NumPy.

# Tópico 1 – Conhecendo o Array

## OBJETIVOS

Construir um NumPy Array;
Listar os atributos de um array;
Aplicar as principais operações de um array.

Olá!
Depois da introdução da aula, você deve estar com vontade de conhecer mais sobre o tão falado módulo NumPy. Você iniciará os estudos a partir da estrutura de dados própria para guardar informações em formato de matriz. Esta estrutura é o NumPy Array. É um tipo específico criado para realizar rapidamente diversas operações matemáticas. No entanto, possui algumas limitações. Você perceberá as diferenças quando compararmos com as estruturas que você certamente já conhece, como, mais notadamente, a lista do Python.

Por ser uma classe, o NumPy Array possui atributos e métodos próprios. Você irá estudar os seus atributos, entender o que eles significam e sua importância. Além disso, você irá praticar a utilização de vários métodos e entender seus propósitos, para assim ser capaz de saber quando aplicar o método certo.

Sem mais delongas, a seguir, entenda a necessidade do tipo NumPy Array.

## Tópico 1

O módulo numpy possui diversas funções e submódulos, mas o objeto base de tudo é o NumPy Array. Ele é do tipo numpy.array e, de agora em diante, o chamaremos somente de array. Mas por que esse tipo é tão importante? Pense no seguinte problema: você tem uma lista de notas que recebeu de algumas disciplinas de determinado curso, então descobre que, se terminar este curso de Python para Machine Learning, irá dobrar cada uma das suas notas. Como você faz isso com Python usando listas? O código a seguir mostra que não é tão simples tentar abordagens diretas. Confira:

print([1, 2, 3] * 2)     # [1, 2, 3, 1, 2, 3]
print([1, 2, 3] + [1, 2, 3])     # [1, 2, 3, 1, 2, 3]

Você pode pensar em usar o map em conjunto com uma estrutura de repetição, como for ou while. É verdade, mas não é tão prático. Se além das suas notas, você tiver uma lista onde cada elemento é uma outra lista, contendo todas as notas dos seus amigos, começa a ficar mais trabalhoso manipular somente as listas. Além disso, esse tipo de dado não é capaz de passar o real número de informações armazenadas, como no código a seguir, onde uma lista com 9 números só demonstra ter tamanho 3:

notas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(notas)) # 3

Perceba o seguinte comportamento estranho: há nove elementos na sua lista, mas a função len afirma que a lista é de tamanho três. Isso acontece porque há três listas, e cada uma delas contém três elementos. Só que as funções padrão de lista não nos permitem ter noção dessa informação mais detalhada.

A verdade é que não há um tipo padrão no Python para trabalhar com o conceito de matrizes que, certamente, você estudou em Matemática. Elas são amplamente utilizadas em Machine Learning. Por exemplo, as Redes Neurais são uma técnica conhecida da área e são basicamente compostas de blocos de matrizes. Aprenda, a seguir, como declarar uma variável do tipo array.

Para utilizar o módulo NumPy, você deve instalá-lo primeiro. No seu Jupyter Notebook, digite o seguinte comando e espere sua conclusão. Após instalado, pode utilizar o módulo normalmente.

conda install numpy
Para declarar um array, é preciso importar o módulo numpy, saiba que é comum na comunidade importar na forma abreviada: np. Em seguida, você deve declarar arrays simples.

import numpy as np
matriz1d = np.array([1, 2, 3])
matriz2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

Perceba que a criação de uma matriz é bem direta e até utilizamos das mesmas listas que utilizamos anteriormente. É importante notar que, ao declararmos um array, é preciso passar somente um argumento, que deve ser uma sequência de elementos.

Agora você conhecerá a vantagem de realizar operações matemáticas com o array. Confira o código abaixo que realiza as mesmas operações matemáticas descritas na página anterior, mas agora utilizando uma matriz.

print(matriz1d * 2)    # [2, 4, 6]
print(matriz1d + matriz1d)    # [2, 4, 6]

Note que operações matemáticas funcionam como esperaríamos com matrizes matemáticas. Você lembra o que é uma matriz? É simplesmente uma tabela. Comumente, matrizes possuem o tamanho de m x n, onde m é o número de linhas e n o número de colunas. Para obter o tamanho de um array no python, utilizamos o atributo shape, que é uma tupla que contém as informações de quantos elementos são armazenados em cada dimensão de um array. Note isso no código abaixo, onde se verifica o tamanho da matriz declarada anteriormente.

print(matriz2d.shape)    # (3, 3)

Compare este valor (3, 3) com o resultado da função len da página anterior. Agora é possível ter melhor noção do número total de elementos na matriz. Na página a seguir, há uma explicação mais detalhada sobre a diferença de comportamento nas operações entre listas e matrizes.

Em Python, o operador ‘+’ tem um significado diferente para cada tipo de objeto. Em números, ele funciona como a soma da Matemática. Para strings, ele concatena as duas cadeias de caracteres. Este é o mesmo comportamento para as listas. Ao somar duas listas, os elementos da segunda lista são inseridos no final da primeira. Por outro lado, para o tipo array do NumPy, o operador ‘+’ realiza uma soma elemento a elemento. Compare os diferentes comportamentos entre listas e arrays no código a seguir:

print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
print(np.array([1, 2, 3]) + np.array([4, 5, 6]))  # [5 7 9]
Note como no caso das listas, o resultado final possui tamanho maior do que as originais. Ao contrário da soma dos arrays, que o resultado possui o mesmo tamanho.

A operação de multiplicação (*) de um array por um número consiste na multiplicação de cada um dos elementos do array por este número. Enquanto na lista, esta operação simplesmente repete todos os elementos no final da lista. Esta repetição é feita pelo número de vezes do fator da multiplicação. Ou seja, se o fator é 2, a lista será duplicada. Se o fator for 3, será triplicada, e assim por diante. O código abaixo ilustra as diferenças citadas:

print([1, 2, 3]*3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(np.array([1, 2, 3])*3)  # [3 6 9]
Perceba como, no caso da lista, ela triplicou de tamanho, pois o fator de multiplicação era 3. Ao passo que no caso do array, a multiplicação triplicou o valor de cada elemento.

Os operadores + e * funcionam da forma como esperávamos ao lidar com matrizes. Este comportamento permite realizar operações geométricas, como soma de vetores ou pontos, e estatísticas, como cálculo da média.

A seguir, saiba mais sobre dimensão em matrizes.

Um conceito importante de matrizes é o seu número de dimensões. Por exemplo, uma matriz m x n tem dimensão 2, porque tem m linhas e n colunas. Uma matriz tridimensional possui também profundidade, ou seja, tem dimensão 3 e tamanho m x n x c, onde c é número de canais de profundidade. E é possível seguir adiante trabalhando com mais dimensões. Na prática, é pouco comum lidar com matrizes acima de três dimensões. Confira o código abaixo:

import numpy as np
matriz1d = np.array([1, 2, 3])
matriz2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
[[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(matriz1d.ndim)  # 1
print(matriz2d.ndim)  # 2
print(matriz3d.ndim)  # 3
Você pode pensar: mas a matriz1d tem uma linha e 3 colunas, não teria dimensão 2? Da maneira que foi declarada, não! Da forma que foi declarada, é uma matriz unidimensional ou vetor. Um vetor é um caso especial de matriz cuja dimensão é 1. Por isso, se você der um print no shape da variável matriz1d, vai notar que só aparece um número, como no código abaixo:

print(matriz1d.shape)  # (3,)
Em termos práticos, não há diferença, você pode trabalhar com uma matriz unidimensional de n colunas como se fosse uma matriz bidimensional 1 x n. Na próxima página, você entenderá mais sobre tensores.

Abaixo, confira um box Saiba Mais que explica um pouco sobre o que é um tensor.

Ícone Saiba Mais+
Ícone “Saiba Mais+”.
Formalmente, uma matriz é estritamente bidimensional. Na matemática, o termo correto para uma matriz de com dimensões acima de 2 é um tensor. Sendo assim, uma matriz é um tensor de ordem 2, ou de 2 dimensões. Um vetor é um tensor de ordem 1 e um número é um tensor de ordem zero. No entanto, no mundo da programação, é comum nos referirmos a matrizes multidimensionais. Esta nomenclatura será utilizada neste conteúdo, certo?

A seguir, confira como realizar operações matemáticas básicas com matriz.

Como em Matemática, as matrizes em NumPy realizam operações matemáticas básicas, como soma, subtração, multiplicação e multiplicação por número. Confira abaixo alguns exemplos das operações descritas anteriormente:

matriz2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2d2 = np.array([[20, 12, 10], [16, 55, 45], [33, 27, 18]])
print(matriz2d + matriz2d2)
print(matriz2d2 - matriz2d)
print(matriz2d*2)

Para ajudar a verificar os resultados, confira as tabelas abaixo. Confira se o seu programa obteve valores iguais.

A seguir, conheça mais sobre multiplicação de matrizes.

Você se lembra como funciona a multiplicação de matrizes? Seja A uma matriz m x n e B uma matriz n x p, a multiplicação de A e B é uma matriz C de dimensões m x p. Isso quer dizer que as dimensões devem ser compatíveis. Além disso, a ordem da multiplicação importa, geralmente, A*B ≠ B*A. A multiplicação de matrizes em NumPy é utilizando o método dot. Confira a seguir alguns exemplos:

1.print(np.dot(matriz2d, matriz2d2)) # [[151 203 154] [358 485 373] [565 767 592]]
2.print(np.dot(matriz2d2, matriz2d)) # [[138 180 222] [551 667 783] [267 345 423]]
3.matriz23 = np.array([[1, 2, 3], [4, 5, 6]])
4.print(matriz23.shape) # (2, 3)
5.print(np.dot(matriz23, matriz2d)) # [[30 36 42] [66 81 96]]
6.print(np.dot(matriz2d, matriz23)) # ValueError: shapes (3,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

Nas linhas 1 e 2 do código acima, é possível perceber que o resultado da multiplicação dos mesmos elementos, mas com a ordem diferente, produziu valores diferentes. Na linha 4, a variável matriz23 é declarada e possui tamanho 2x3. Como a matriz2d possui tamanho 3x3, é possível realizar a multiplicação matriz23*matriz2d, porém a operação matriz2d*matriz23 não é possível devido à incompatibilidade de tamanhos. Ao tentar realizá-la, uma exceção ValueError é lançada, causando interrupção do programa.

Na próxima página, confira mais sobre o operador * em matrizes.

O operador * também funciona para matrizes multidimensionais em python. No entanto, ele não estará realizando a multiplicação de matrizes. Este operador realiza uma operação própria do NumPy chamada broadcasting. Esta operação é realizada quando se deseja trabalhar com arrays de diferentes tamanhos. Nesse caso, o array menor é “propagado” pelo array maior, realizando as operações. Para mais informações, confira: broadcasting.

Bem prática a biblioteca NumPy para operações de matrizes, não é? Mas talvez você ache chato somente aprender as operações matemáticas sem uma aplicação do mundo real. Na página seguinte, há uma aplicação bem interessante envolvendo operações matriciais.

Para dar um gostinho de que matrizes podem fazer aplicações interessantes, confira o código abaixo:

ponto_original= np.array([3, 4])
rotacao = np.array([[-1.0, 0.0], [0.0, -1.0]])
ponto_rotacionado = np.dot(rotacao, ponto_original)
print(ponto_rotacionado) # [-3. -4.]
translacao = np.array([5.0, 0.0])
ponto_transladado = ponto_original + translacao
print(ponto_transladado) # [8. 4.]
escala = 2
ponto_escalonado = ponto_original * escala
print(ponto_escalonado) # [6 8]

No código, você pode verificar diferentes operação matemáticas envolvendo matrizes. Na linha 1, é declarado um vetor chamado ponto_original. Ele representa o ponto (3, 4) em um plano cartesiano. Em seguida, uma matriz 2x2, chamada rotação, é declarada e ao multiplicar as duas variáveis, é obtido um vetor (-3, -4). Perceba que este vetor é como se fosse o espelho do original. Isso acontece porque a matriz rotação é uma matriz específica para rotacionar pontos pelo espaço 2D. Não será discutido como calcular os valores dessa matriz de rotação, pois é um assunto complexo. Após a rotação, é adicionado o vetor de translação ao ponto original e produzido o vetor (8, 4), pois este vetor representa uma operação de deslocamento no eixo X no mundo 2D. E, por último, multiplicar o ponto original por um número 2 produz um ponto (6, 8), que significa duplicar os atributos de um ponto no espaço.

Na próxima página, confira uma imagem que ilustra todas as operações descritas.

https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104746263793450/aula/img/Imagem1.png
Figura 1 – Gráfico de pontos com os resultados das operações matriciais descritas no código.

Matrizes são muito aplicadas para realizar operações, como as descritas anteriormente, em jogos, animações e na área da Computação Gráfica. No entanto, essas mesmas operações são também aplicadas em Machine Learning. Todo o processo de aprendizado que um algoritmo de Machine Learning faz envolve um número grande de operações matriciais que não cabe neste conteúdo, mas matrizes realizam o que é chamado de transformação linear e são a base de uma área da Matemática chamada Álgebra Linear.

A seguir, aprenda sobre outras formas de se criar um array com NumPy.

Confira um código com diversos exemplos para inicialização de matrizes utilizando métodos próprios da biblioteca. Cada um tem uma aplicação específica, que você perceberá a necessidade com o tempo.

print(np.zeros((1, 3))) # [[0. 0. 0.]]
print(np.ones((2, 2))) # [[1. 1.] [1. 1.]]
print(np.full((1, 2), 3)) # [[3 3]]
print(np.full((2, 1), np.nan)) # [[nan] [nan]]
A função zeros recebe como argumento um shape específico e inicializa uma matriz contendo somente valores zeros. Nesse caso, o argumento foi (1, 3). De forma similar, a função ones retorna uma matriz com valores 1.0. Na linha 3, é utilizada a função full. Esta função recebe dois argumentos: um shape e um valor. Então, a função full retorna uma matriz de tamanho igual ao do shape passado como argumento e preenchida com valores iguais ao valor que também é passado como argumento. No primeiro exemplo (linha 3), foi passado o valor 3 e shape (1, 2), então é criado um vetor preenchido somente com valores iguais a três. No segundo exemplo acima, é utilizado um shape (2, 1) e o valor np.nan. Este é um Not a Number, como você já deve ter estudado em conteúdos de bibliotecas matemáticas.

Note que as funções zeros e ones são especiais da função full, onde o valor de preenchimento é 0.0 e 1.0, respectivamente. Essas três funções são muito utilizadas quando você já tem em mente um tamanho e um valor específico para inicialização da matriz.

Na próxima página, há uma explicação sobre os tipos de dados na criação de um NumPy Array.

Em todos os exemplos até então foi omitido o tipo de dado a ser armazenado nas matrizes. Nas funções array, zeros, ones e full, tem um parâmetro opcional chamado dtype. É possível especificar se os valores vão ser inteiros, floats, complexos, entre outros. Além disso, é possível criar tipos próprios contendo mais de um tipo básico, por exemplo, um campo inteiro e outro float. Para saber mais, confira o link sobre Arrays Estruturados.

Conheça mais funções de inicialização de arrays na próxima página.

Continuando os exemplos de inicialização de matrizes utilizando métodos próprios da biblioteca, serão exibidos agora os métodos arange e linspace. Confira o código abaixo.

print(np.arange(5)) # [0 1 2 3 4]
print(np.arange(0, 2, 0.4)) # [0. 0.4 0.8 1.2 1.6]
print(np.linspace(0, 2, 5)) # [0. 0.5 1. 1.5 2. ]

Na linha 1, é utilizada a função arange, que se comporta da mesma forma que a função range da biblioteca padrão de Python. Se passado somente um valor como argumento, este funciona como valor limitante e é produzida uma sequência de elementos iniciando em 0 até o último número antes desse valor limite. O exemplo arange(5) produz o vetor resultante [0, 1, 2, 3, 4]. No entanto, é possível dizer como se quer gerar essa sequência de números, passando como argumento o valor inicial, o valor limite e o passo a ser dado na sequência. Na linha 2, esses argumentos são 0, 2 e 0.4, respectivamente. Assim, a ideia é produzir uma sequência que inicialize em 0 e dê passos de 0.4 de tamanho até chegar a 2. Isto produz o vetor [0. 0.4 0.8 1.2 1.6].

Devido a aspectos de imprecisão numérica ao utilizar o float, a função arange nem sempre produz um número consistente de elementos. Nesse caso, é preferível utilizar a função linspace. Ela recebe três argumentos, o primeiro é o valor inicial, o segundo é o valor final e o terceiro é o número de elementos da sequência. No exemplo, o valor inicial é 0 e o final é 2, que no caso vai ser incluído na sequência, e o número de passos é 5. Então, é produzida a sequência [0. 0.5 1. 1.5 2. ].

As funções arange e linspace são bem parecidas, e você pode obter o mesmo resultado com as duas se desejar. Mas como escolher qual usar? De forma geral, pode-se usar arange com valores inteiros ou quando tiver um valor de passo específico. Já a linspace deve ser utilizada quando quiser incluir o valor final na sequência ou tiver um número fixo de elementos para produzir. Tudo bem até aqui?

Continuando o estudo das matrizes em NumPy, acompanhe a seguir como realizar indexação e operações de fatiamento.

A indexação nos Arrays do Numpy funciona de forma similar à indexação das listas. Na indexação de um array, é possível passar um índice específico, um intervalo sem passo ou um intervalo com passo. Configura alguns exemplos a seguir:

vetor = np.arange(10)
print(vetor[5]) # 5
print(vetor[5:]) # [5 6 7 8 9]
print(vetor[:5]) # [0 1 2 3 4]
print(vetor[2:8]) # [2 3 4 5 6 7]
print(vetor[0:10:2]) # [0 2 4 6 8]

Esses resultados devem ser intuitivos para você, não é? Pois, no caso, os vetores funcionam de forma bem similar a listas. Agora podemos utilizar esses mesmos conceitos em matrizes multidimensionais. A ideia é que iremos operar em cada dimensão de forma independente. Assim, você pode utilizar um mecanismo de indexação (índice ou intervalo) específico para cada dimensão. Na primeira, você pode passar um índice, e na segunda um intervalo, ou vice-versa. Depende do seu intuito. Confira o código abaixo que ilustra diferentes cenários de indexação em matrizes multidimensionais.

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz) # [[1 2 3] [4 5 6] [7 8 9]]
print(matriz[1, 1]) # 5
print(matriz[:, 1]) # [2, 5, 8]
print(matriz[0, :]) # [1, 2, 3]
print(matriz[:2, 1:]) # [[2, 3], [5, 6]

Agora confira, na próxima página, a explicação para cada um dos resultados dos prints acima.

No primeiro print do segundo trecho do código da página anterior, todo o conteúdo da variável matriz é impresso na tela. No segundo, somente o elemento que está na segunda linha e na segunda coluna é exibido, que é o elemento 5. No terceiro, são exibidas todas as linhas, mas somente da segunda coluna, resultando no vetor [2, 5, 8]. Na linha 5, é exibida somente a primeira linha, contendo todas as colunas, produzindo o vetor [1, 2, 3]. Por último, são selecionadas as duas primeiras linhas e as duas últimas colunas, resultando na matriz de tamanho 2x2 e valores [[2, 3], [5, 6]]. As tabelas abaixo representam os resultados obtidos e ilustram melhor as operações realizadas.

Pode parecer um pouco diferente, a princípio, trabalhar com várias dimensões, mas simplesmente pense nas operações de indexação agindo de forma independente em cada eixo. A seguir, aprenda como manipular o shape de uma matriz.

A partir de um Array, é possível obter muitos outros arrays de diferentes shapes. Há duas funções principais para isso: ravel e reshape. A primeira retorna um vetor unidimensional com todos os valores, como se as dimensões tivessem sido “achatadas”. O método reshape recebe como argumento o novo shape, transforma a matriz original e cria uma nova com o tamanho especificado. É importante observar que o novo shape deve ser compatível com o shape original. Pois as matrizes devem possuir o mesmo número de elementos. Confira o código a seguir que ilustra casos de uso.

matriz_coluna = np.array([[1, 2], [3, 4], [5, 6]])
print(matriz_coluna.shape) # (3, 2)
vetor = matriz.ravel()
print(vetor) # [1 2 3 4 5 6]
matriz_linha = matriz_coluna.reshape((2, 3))
print(matriz_linha) # [[1 2 3] [4 5 6]]
matriz_invalida = matriz_coluna.reshape((2, 4)) # ValueError: cannot reshape array of size 6 into shape (2,4)

Pronto. Agora é preciso compreender um pouco dessas linhas de código, certo? Vamos para a próxima página.

O código começa inicializando uma matriz_coluna que possui 3 linhas e 2 colunas, contendo 6 elementos. É possível verificar o shape da matriz na linha 2, cujo resultado é (3, 2). Na linha 3, atribuímos a variável vetor à matriz “achatada” através da utilização do método ravel, cujo o resultado é impresso como [1 2 3 4 5 6]. Em seguida, a variável matriz_linha é obtida a partir do método reshape, que retorna uma matriz com 2 linhas e 3 colunas. Na linha 6, é possível perceber que os elementos foram redistribuídos para se adequar ao novo shape.

Qual a ordem para essa redistribuição? Inicialmente, todos os valores da primeira linha são alocados. Em seguida, os da segunda; e assim por diante, até o fim. Caso uma linha não possa ser totalmente movida para a nova linha, somente a quantidade de valores é movida e o restante segue para uma nova linha da nova matriz. Por exemplo, a linha original [3, 4] foi separada, onde o valor 3 foi para a primeira linha da nova matriz e o valor 4 foi para a segunda linha.

Confuso? Treine um pouco mais com alguns exemplos até se sentir confiante. Mas a ordem sempre é da primeira linha até o final, certo?

Na linha 7 do código, é feita uma tentativa de reshape com um tamanho incompatível e uma exceção ValueError é disparada, pois 6 elementos não podem ser redistribuídos em um shape (2, 4). Para isso, seria preciso ter 2x4 = 8 elementos.

Ufa! Já deu para perceber que você aprendeu muita coisa sobre NumPy e seus Arrays até aqui.

O tipo Array é a base de dezenas de bibliotecas que você encontrará na sua trilha de aprendizagem de Machine Learning, entre elas podemos destacar: Pandas, Matplotlib e Scikit-Learn. Essa adoção universal da biblioteca se deu pela sua facilidade de uso, eficiência das operações e um número grande de funções numéricas importantes para cálculos matemáticos.

Agora, caso você queira, pode relaxar um pouco e praticar o que aprendeu até agora utilizando as funções prontas do NumPy. Assim, você poderá aprender melhor quando utilizar as funções adequadas, concorda?

Caso queira aprender mais, avance para o próximo tópico e conheça as funções universais do NumPy.

# Tópico 2 – Funções do NumPy

## OBJETIVOS

Conhecer funções universais do NumPy;
Aplicar funções aritméticas em arrays;
Obter informações de índice em arrays.

Até então você aprendeu muito sobre a criação de arrays e operações matemáticas com arrays e seus atributos. Agora está na hora de conhecer mais sobre as funções universais do NumPy. Essas funções operam nos elementos individualmente e nos permitem realizar aplicações interessantes, como realizar uma análise de dados das vendas anuais da Dell. Calculando a média e os valores máximos e mínimos, é possível extrair informações sobre quais meses venderam mais e menos computadores, respectivamente. Você também pode utilizar as funções do NumPy para analisar as chuvas no Brasil e descobrir por que um mês é considerado seco ao comparar com a média histórica. Ou até mesmo se pode utilizar o módulo NumPy para calcular a média móvel de casos da Covid-19 do seu estado ou cidade.

Neste tópico, você irá aplicar funções que extraem informações dos arrays e aprenderá como realizar essas operações em diferentes dimensões das matrizes. Para melhor consolidar o grande conjunto de informações que você acompanhará durante esse tópico, você irá trabalhar com uma aplicação até o final. Caso você já queira praticar, você pode usar o Jupyter notebook, certo?

A seguir, comece inicializando a sua matriz a ser utilizada na aplicação.

Existem diversas funções no módulo NumPy e listá-las aqui pode ser exaustivo. Para melhor entender o uso, você irá trabalhar com um exemplo de aplicação agora. Assim, aos poucos irá saber a melhor hora de usar cada função. Então, suponha que, após a conclusão do curso Python para Machine Learning, você conseguiu um emprego como cientista de dados em uma empresa que vende computadores. O seu novo chefe lhe pediu para analisar as vendas dos últimos 10 anos por mês. O resultado é a seguinte matriz.

vendas_anos = np.array([[149, 499, 112, 430, 115, 390, 187, 316, 361, 483, 353, 400],
[258, 222, 461, 263, 384, 210, 452, 372, 417, 364, 468, 397],
[259, 329, 417, 132, 318, 256, 362, 496, 232, 132, 306, 174],
[117, 148, 480, 201, 160, 292, 146, 209, 298, 215, 358, 234],
[169, 229, 381, 119, 225, 270, 379, 272, 167, 332, 144, 359],
[358, 434, 228, 300, 122, 247, 142, 127, 191, 356, 450, 308],
[105, 251, 317, 147, 214, 280, 289, 338, 498, 133, 304, 225],
[156, 165, 299, 461, 290, 123, 451, 450, 353, 191, 167, 451],
[149, 377, 389, 176, 103, 439, 269, 132, 200, 391, 426, 175],
[137, 107, 229, 227, 198, 206, 432, 169, 323, 141, 155, 233]])
print(vendas_anos.shape)
Note que o shape da nossa variável vendas_anos é 10x12. Cada linha da matriz representa um ano e cada coluna representa um mês. Então é possível interpretar a matriz da seguinte maneira: o número de vendas do mês de janeiro do primeiro ano é vendas_anos[0, 0], que é igual a 149.

Agora, digamos que o seu chefe pediu para você dizer duas informações pra ele: a média de vendas de cada ano e a média de vendas por mês. Como você faria? É possível fazer manualmente utilizando algum laço de repetição e utilizando listas auxiliares para o cálculo. No entanto, as funções disponíveis no NumPy são eficientes, ou seja, são mais rápidas do que se você tentar fazer manualmente. Então, aprenda mais sobre a função mean na próxima página.

A função mean do NumPy calcula a média de uma matriz. Para utilizá-la, você pode utilizar a função mean diretamente do pacote numpy ou como método de um objeto array. Confira o código a seguir.

print(np.mean(vendas_anos))
print(vendas_anos.mean())
O resultado de ambos os prints é o valor 275,7. Ou seja, a venda mensal de todos os anos e todos os meses é de 275,7 computadores. No entanto, não foi isso que o seu chefe pediu, certo? Você deve responder a média de todos os anos e de todos os meses separadamente. Vamos fazer agora somente para o primeiro ano, passando o índice 0 como linha para a variável vendas_anos, depois você aprenderá como calcular para todos de uma vez só. O código abaixo ilustra como fazer.

primeiro_ano = vendas_anos[0, :]
print(primeiro_ano.mean())
O valor deu 316,25, correto? Caso contrário, confira o seu código e tente novamente. Lembre-se de que, para retornar à primeira linha, utilizamos a indexação de matrizes de forma independente. O índice 0 representa a primeira linha, e ‘:’ representa todas as colunas. Dê um print no shape da variável primeiro_ano e notará que ela possui shape (12,). Aliás, como dica para todo este tópico, sempre faça o print do shape das suas variáveis para garantir que está obtendo as matrizes no tamanho correto. Você pode realizar as operações que parecem certas, mas trabalhar na dimensão errada.

Você já conhece a função mean, agora como fazer para obter a média de todos os anos de uma vez só? As funções que você acompanhará neste tópico possuem um parâmetro opcional chamado axis. Confira mais sobre isso na página a seguir.

O parâmetro axis representa o eixo no qual você quer fazer a operação. Como assim? Um eixo da matriz é o mesmo que a dimensão. Ah! Lembre-se que a matriz vendas_anos é uma matriz de tamanho 10x12, contendo 10 linhas e 12 colunas. Por ter linhas e colunas, tem dimensão 2, ou seja, tem 2 eixos. O primeiro eixo, ou eixo 0, é o das linhas. O segundo eixo é o das colunas.

Cada linha é um vetor de dimensão 12, como ilustrado na variável primeiro_ano do exemplo da página anterior. E cada coluna é um vetor de dimensão 10. Basta pensar que cada vetor de um eixo possui o tamanho do outro eixo.

Como a variável primeiro_ano é um vetor unidimensional, somente possui um eixo, correto? Então podemos utilizar a função mean com o parâmetro axis=0.

print(primeiro_ano.mean(axis=0))

O resultado continua sendo 316,25. Agora aprenda como utilizar o parâmetro axis para uma matriz de duas dimensões de uma só vez. Vamos lá!

Antes de você aprender como utilizar o parâmetro axis na função mean, é melhor aprender como aplicar numa matriz menor. Depois, vamos para a matriz vendas_anos. Suponha que você tem a tabela 3x2 a seguir:

Quando o parâmetro axis é especificado com o valor 0, a função mean vai calcular a média dos elementos de todo aquele eixo. Ou seja, quando axis=0, a média é calculada ao longo de todas as linhas, gerando um resultado para cada linha. Neste caso, o resultado é [2.0, 5.0], pois a média de [1, 2, 3] é o 2.0, e a média de [4, 5, 6] é 5.0.

Agora, calcule para o eixo igual a 1. A função mean vai calcular a média ao longo de todas as colunas. Ou seja, a média de [1, 4], a média de [2, 5] e a média de [3, 6]. Isto resulta no vetor [2.5, 3.5, 4.5]

De forma geral, lembre-se de que, quando o eixo é especificado, a função vai ser aplicada em todo aquele eixo. Além disso, o resultado terá o tamanho da outra dimensão. Se uma matriz tem tamanho m x n, quando axis=0, o resultado terá tamanho (n, ) e quando axis=1, o tamanho será (m, ).

Agora que você entendeu melhor como aplicar o argumento axis, aprenda como responder às perguntas do seu chefe.

O seu chefe pediu para você dizer a média de vendas de cada ano. Ou seja, você deve calcular a média de todas as colunas por ano, certo? Então, se a média é no eixo das colunas, o parâmetro axis deve ser igual a 1. Confira o código abaixo para realizar isso.

media_ano = vendas_anos.mean(axis=1)
print(media_ano) # [316.25 355.66666667 284.41666667 238.16666667 253.83333333 271.91666667 258.41666667 296.41666667 268.83333333 213.08333333]
print(media_ano.shape) # (10, )

Observe como o primeiro valor do nosso vetor media_ano é igual ao valor que você obteve ao calcular manualmente a média para o primeiro ano. Isso é um indicativo de que você fez corretamente. Além disso, ao dar um print no shape da variável media_ano, você pode observar que o seu tamanho é 10. Ou seja, a média de vendas dos últimos 10 anos. Muito bem!

Agora faça o mesmo com os meses. Acompanhe.

Se você quer saber a média de todos os meses ao longo de todos os anos, você deve fazer a média no eixo dos anos. Para fazer isso, o valor de axis deve ser 0. Verifique o código a seguir.

media_meses = vendas_anos.mean(axis=0)
print(media_meses) [185.7 276.1 331.3 245.6 212.9 271.3 310.9 288.1 304. 273.8 313.1 295.6]
print(media_meses.shape) # (12, )

Dessa vez, você não calculou anteriormente a média de todos os meses de janeiro ao longo dos anos em uma variável isolada para comparar com o resultado utilizando o parâmetro axis e verificar se os valores estão certos. No entanto, o shape da variável media_meses é igual a 12, que é o número de meses no ano. Isso é outro indicativo de que você fez a operação no eixo correto.

Parabéns! Você já sabe responder às perguntas que seu chefe fez. E então, foi fácil obter esses dados com NumPy? Por você ter feito de forma tão eficiente, o seu chefe já pensou em novos dados para você obter para ele. Ele quer que você calcule o maior número de vendas anuais. Como calcular isso? Verifique na próxima página.

Para calcular o maior número de vendas nos anos, você deve fazer duas coisas distintas: calcular a soma de vendas de todos os anos, ou seja, de todas as colunas, e encontrar o valor máximo da lista resultante. Para realizar esses dois passos distintos, você vai precisar utilizar a função sum e a função max. Confira o código abaixo, que realiza esses dois passos para você.

soma_ano = vendas_anos.sum(axis=1)
print(soma_ano.shape) # (10, )
print(soma_ano) # [3795 4268 3413 2858 3046 3263 3101 3557 3226 2557]
maximo_vendas_anuais = soma_ano.max()
print(maximo_vendas_anuais) # 4268

Na linha número um, é calculado o total de vendas em cada ano. De forma parecida com a função mean, é passado o parâmetro axis com o valor 1, ou seja, é realizada a soma de todas as colunas. Para verificar se você obteve o tamanho correto do vetor, é realizado o print do shape do vetor resultante, que é igual a 10, correspondente aos 10 anos. Em seguida, é impresso o vetor de vendas. Para obter o maior valor dessa lista, é utilizado o método max, assim, você obtém o valor de 4268. Este foi o maior valor de vendas anuais nos últimos 10 anos.

Para matrizes unidimensionais, o método max de um array funciona que nem a função max da biblioteca padrão do Python. Porém, para matrizes de dimensões maiores que 1, é possível passar o parâmetro axis também. Quando o eixo é passado como argumento, é selecionado o maior valor daquele eixo e o resultado é um vetor unidimensional. Confira os exemplos a seguir:

print(vendas_anos.max()) # 499
print(vendas_anos.max(axis=0)) # [358 499 480 461 384 439 452 496 498 483 468 451]
print(vendas_anos.max(axis=1)) # [499 468 496 480 381 450 498 461 439 432]

Perceba que o método sem argumentos calculou o maior valor de toda a matriz vendas_anos. Com o parâmetro axis=0, é obtido o maior valor de vendas para cada mês em todos os anos, por isso o vetor tem 12 elementos. E para o valor de axis igual a 1, é calculado o máximo de vendas de cada ano, tendo assim um vetor com 10 valores.

Agora, qual foi o ano que obteve a maior venda? É fácil inspecionar o vetor de 10 elementos e dizer que foi a primeira posição, mas e se o vetor tivesse 100 elementos? 1.000? Ou até mesmo 10.000? Aprenda como encontrar a posição do maior valor de um array a seguir.

Caso você tenha um array e queira encontrar a posição que contém o maior valor, você utilizará a função argmax. Esta função retorna um índice e pode ser usado para acessar o array original. Confira o exemplo a seguir.

indice_max = soma_ano.argmax()
print(indice_max) # 1
print(soma_ano[indice_max]) # 4268

Como é possível conferir com o exemplo acima, o índice do maior valor no array soma_ano é 1. Salvando este valor na variável indice_max, é possível então obter o valor correspondente no vetor original. Felizmente, esse valor é igual ao valor obtido anteriormente.

Agora, faça um exercício supondo que os 10 últimos anos sejam o intervalo de 2011 a 2020, calcule o mês de maior venda em cada ano e imprima essas informações. O código da próxima página realiza isso.

import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'pt_BR')
anos = np.arange(2011, 2021)
meses = list(map(lambda x: datetime.strptime(str(x), "%m"), np.arange(1, 13)))
meses = list(map(lambda x: x.strftime("%B").title(), meses))
print(anos)
print(meses)
for i in range(len(anos)):
indice_max_ano = vendas_anos[i, :].argmax()
maior_venda_ano = vendas_anos[i, indice_max_ano]
print(f"A maior venda de {anos[i]} ocorreu no mês de {meses[indice_max_ano]} e foi de {maior_venda_ano} computadores")

O código inicia importando as bibliotecas da aula ‘Trabalhando com datas’, pois você quer imprimir as informações detalhadas e em português, como configurado na linha 4. Nas linhas 6 a 8 é criado um vetor de anos através da função arange e uma lista de meses utilizando as funções strptime e strftime para transformar os números 1 a 12 nos meses escritos por extenso. As linhas 9 e 10 dão um print nessas variáveis para você verificar se as variáveis foram criadas corretamente.

Então, o código entra num laço for, iterando sobre o número de anos. Para cada ano, é selecionada a linha correspondente da matriz vendas_anos. Então, é calculada o índice de maior venda e o respectivo valor. Em seguida, na linha 15 é feito um print das informações que foram pedidas.

Perceba que você utilizou conceitos desde a primeira aula deste curso até aqui para construir um exemplo completo em 15 linhas. Parabéns! Você fez um ótimo trabalho até então. Não se preocupe se alguns detalhes do último exemplo foram confusos, o código foi condensado para conter mais operações por linha. E acredite, ele poderia ser ainda menor! Releia o código e rode em sua máquina também. Coloque prints, cheque o tamanho dos arrays. É sempre importante verificar cada passo do seu programa.

A seguir, aprenda mais sobre funções similares do NumPy às que foram estudadas até aqui.

Na página seguinte, você deverá acompanhar a explicação do código acima.

Abaixo, confira um box Saiba Mais a respeito das funções matemáticas do módulo Numpy.

Assim como existe a função max e argmax, existem os métodos min e argmin no módulo NumPy. Eles funcionam de forma similar, só que retornam o menor valor e índice do menor valor, respectivamente. Além disso, existem outras dezenas de funções matemáticas além da mean e sum. Para referência completa de todas as funções disponíveis, somente conferindo a documentação oficial. Infelizmente, essa documentação só se encontra disponível em inglês.

Você aprendeu mais sobre algumas funções existentes no NumPy e como utilizar o eixo para calcular as informações por linha ou por coluna, de acordo com a necessidade. Seria exaustivo listar aqui todas as funções disponíveis e fica ao seu critério procurar mais. No entanto, caso você tenha alguma necessidade específica ao lidar com arrays, procure na internet, provavelmente já tem uma função para o que você precisa!

Caso queira dar uma pausa para revisar o que estudou até aqui, fique à vontade! Caso queira continuar, avance para o próximo tópico e aprenda a utilizar máscaras para lidar com dados inválidos em um array.

# Tópico 3 – O Array Mascarado

## OBJETIVOS

Conhecer o módulo numpy.ma;
Mascarar um array;
Aplicar funções em um array mascarado.

Imagine que no exemplo do tópico anterior, você tivesse que lidar com as vendas dos últimos 30 anos. Só que, ao receber a matriz de dados, você percebeu que alguns valores são inválidos, por exemplo, são NaN. Isso ocorreu porque no início o sistema era antigo e dava muitos erros. Isso gerou um erro no banco de dados. E agora? Como trabalhar com uma matriz que contém dados inválidos? É para isso que utilizamos o módulo numpy.ma.

Este módulo permite que você utilize máscaras nos arrays. As máscaras servem para ocultar os dados inválidos. Assim, eles não são exibidos e nem participam nas operações. Dessa forma, é possível trabalhar com matrizes sem se preocupar com dados faltantes. Esse é um problema bem comum em Machine Learning.

Está na hora de aprender a utilizar o módulo numpy.ma. Vamos lá!

Lidar com dados inválidos ou faltantes é um problema comum de um cientista de dados. A biblioteca NumPy oferece uma solução para lidar com este problema através do módulo numpy.ma. Este módulo permite criar arrays mascarados, onde, além de possuir valores e um shape, estes possuem uma máscara informando quais valores devem ser considerados inválidos. Confira o código abaixo com um exemplo:

import numpy.ma as ma
dados_invalidos = np.array([1, 2, 3, np.nan, 5])

Na primeira linha é importado o módulo numpy.ma simplesmente como ma para facilidade de escrita de código mais adiante. Na segunda, um array é declarado com 5 elementos, onde o quarto é um valor NaN. No entanto, você não quer trabalhar com um valor NaN no seu array. Pois, você terá valores indesejados ao tentar operar com um array assim. Para mascarar somente esse valor no array, utilizamos a classe masked_array, como no código abaixo:

dados_mascarados = ma.masked_array(dados_invalidos, mask=[False, False, False, True, False])
print(dados_mascarados) # [1.0 2.0 3.0 -- 5.0]

Perceba como foi fácil criar um array mascarado. Você precisou criar um masked_array passando o array com dados inválidos como argumento de entrada e um outro argumento chamado máscara. Este argumento é uma lista que diz se cada elemento deve ser mascarado ou não. No seu caso, você só quis mascarar o quarto elemento, portanto somente o elemento 4 da máscara possui valor verdadeiro. Ao dar um print na variável dados_mascarados, você pode perceber que o elemento np.nan não aparece. No seu lugar, é possível perceber dois hífens ‘--’.

Compare, a seguir, como as operações funcionam em um array com dados inválidos e outro mascarado.

Você vai sentir a maior utilidade de um array mascarado agora, ao aplicar as funções do NumPy. Por que? Porque um dado inválido no meio da sua matriz pode causar resultados indesejados. Relembre a função mean. Qual o resultado da média de um array em que um dos valores é np.nan? Difícil responder. Suponha que você tem um array que deveria ter somente valores positivos, como o array de vendas. Caso o array possua algum valor negativo, este pode ser considerado inválido. Assim, se você deseja saber o menor valor de vendas em um período, o resultado seria um número negativo, o que não faz sentido. Para saber mais como as operações se comportam em um array mascarado, compare abaixo os resultados das operações de algumas funções mais comuns.

print(dados_invalidos.mean()) # nan
print(dados_mascarados.mean()) # 2.75
print(np.median(dados_invalidos)) # nan
print(np.ma.median(dados_mascarados)) # 2.5
print(dados_invalidos.min()) # nan
print(dados_mascarados.min()) # 1.0
print(dados_invalidos.argmin()) # 3
print(dados_mascarados.argmin()) # 0

Há alguns pontos para analisar nestes exemplos. Vamos lá!

Primeiro, perceba como o elemento np.nan invalida as operações de média e mediana, que são as funções mean e median, respectivamente. Pois o resultado da soma de um número com um valor NaN é um NaN (Not a Number). Além disso, mesmo o elemento não sendo um número válido, o método min retorna o np.nan como resultado. Ele também influencia o resultado do método argmin.

Agora compare com os resultados obtidos utilizando o array mascarado. Todos os valores são coerentes e estão corretos! Você pode verificar a conta manualmente. Além disso, perceba que a função median está presente no módulo numpy.ma. Caso você usasse a função np.median, o resultado também seria NaN.

Aprenda, a seguir, como criar arrays mascarados sem saber a posição, somente o valor indesejado.

No exemplo anterior, foi fácil de localizar a posição do elemento np.nan. O array só tinha 5 elementos, assim, fica fácil identificar qual a posição que se quer mascarar. Mas e se o array tiver 100 elementos e você não souber o índice do elemento, ou dos elementos, inválidos? Torna-se mais complicado passar a máscara manualmente para o construtor de masked_array. Você pode criar um array passando uma condição como máscara, ao invés de uma lista explícita de valores. O módulo numpy.ma internamente verifica a condição e cria a lista de valores de máscara automaticamente. Para criar um array mascarado passando uma condição de máscara, você utilizará a função masked_where. A função masked_where recebe como primeiro argumento a condição e como segundo argumento o array com dados inválidos. Confira abaixo a criação de um array com números inválidos que será tratado de duas formas diferentes com o masked_where.

from random import sample
array_invalido = np.arange(20)
indices = sample(array_invalido.data, k=5)
array_invalido[indices] = -999
print(array_invalido) # [ 0 1 -999 3 -999 5 -999 7 8 9 10 11 12 -999 14 -999 16 17 18 19]
Este exemplo começa importando o método sample da biblioteca random, que você estudou na aula anterior. Este método será utilizado para selecionar elementos sem reposição de um array. Na linha 3 nós criamos um array_invalido com elementos de 0 a 19. Em seguida, nós utilizamos a função sample para selecionar 5 índices aleatórios. Por esse motivo, se você rodar este código, o seu resultado deve ser diferente do descrito neste conteúdo.

Após selecionados os índices, os 5 valores do vetor foram substituídos por -999. Este é o valor inválido do exemplo. Perceba que nós passamos uma lista com 5 índices de uma só vez ao array_invalido e alteramos todos de uma vez. O tipo Array do NumPy nos dá essa facilidade: permitir indexação utilizando uma lista de dados. O mesmo não é possível com uma lista tradicional do Python. Note no print do array que há 5 elementos aleatoriamente escolhidos como -999. Avance para a próxima página para aprender como mascarar este array.

Perceba que devido à aleatoriedade da função sample, você não consegue sempre saber qual será a posição dos valores inválidos. Por isso, é mais fácil criar um vetor especificando, para a função mascarar, quais valores são iguais a -999, correto? Você também pode pensar que quer mascarar todos os valores menores do que zero. As duas formas de raciocínio estão corretas e são feitas no código abaixo.

array_mascarado = np.ma.masked_where(array_invalido == -999, array_invalido)
print(array_mascarado) # [0 1 -- 3 -- 5 -- 7 8 9 10 11 12 -- 14 -- 16 17 18 19]
array_mascarado2 = np.ma.masked_where(array_invalido < 0, array_invalido)
print(array_mascarado2) # [0 1 -- 3 -- 5 -- 7 8 9 10 11 12 -- 14 -- 16 17 18 19]
Na primeira linha do código a função masked_where é chamada recebendo dois argumentos, o segundo argumento é o array_invalido que você quer mascarar. A primeiro argumento é a condição de máscara. Que condição é essa? Nesse exemplo, é onde o valor de array_invalido for igual a -999. Logo o argumento torna-se array_invalido == -999. Na linha 2, é impressa a variável e é possível notar que todos os valores -999 foram mascarados.

Para realizar a segunda condição, é preciso checar os valores abaixo de zero do array. Para fazer isso, basta passar como argumento a condição array_invalido < 0. Novamente, ao imprimir o array é possível ver que os valores negativos foram mascarados e o resultado é igual ao da primeira condição.

Você pode estar achando estranho comparar todo um vetor a um número. A verdade é que o tipo Array do NumPy realiza a comparação elemento a elemento e retorna um array de booleanos como resultado. Confira a seguir.

print(array_invalido < 0) # [False False True False True False True False False False False False False True False True False False False False]
Como é possível observar, o resultado é um array onde cada elemento de array_invalido foi comparado a zero. Caso o valor seja menor, retorna True e caso contrário, retorna False. Note que este array se parece com o array de máscara que você passou no começo do estudo do módulo numpy.ma. É desta forma que o módulo atua internamente. Ele gera o vetor de booleanos e utiliza para mascarar os elementos do array. Confira na próxima página mais sobre indexação com valores booleanos em NumPy.

Você aprendeu que um NumPy Array suporta indexação através de lista de inteiros. Ele também suporta indexação através de lista de booleanos. Nessa operação, o resultado é um array, onde os elementos são os valores, e os índices possuem valor True. No exemplo anterior, caso você utilizasse o vetor de booleanos do resultado da condição como índice de array_invalido, o resultado seria um array somente contendo valores -999. Este tipo de indexação através de listas no NumPy é um tópico chamado de indexação avançada.

Para finalizar nosso assunto sobre arrays mascarados, que tal aprender sobre como preencher os valores inválidos? Suponha que você queira preencher os valores com a média dos valores válidos, como utilizar esta média para substituir os outros? Há algumas formas de fazer isto, mas você utilizará a função filled para esta tarefa. Verifique.

media = array_mascarado.mean()
print(media) # 10
array_preenchido = array_mascarado.filled(media)
print(array_preenchido) # [ 0 1 10 3 10 5 10 7 8 9 10 11 12 10 14 10 16 17 18 19]
Você iniciou calculando a média através do método mean, cujo valor é 10. Para gerar um novo array preenchido, você usa o método filled da variável array_mascarado. O argumento deste método é o valor com o qual se deseja preencher. Neste caso, você utilizou a média para preenchimento, gerando um novo valor onde todos os valores inválidos foram substituídos por 10.

É isso! Parabéns por ter chegado até aqui!

Parabéns! Você terminou a aula do módulo NumPy. Nesta aula, você aprendeu muito sobre o tipo de dados NumPy Array e como utilizá-lo para realizar várias operações matemáticas. Você também praticou bastante com essas operações, calculando médias e somatórios. Por fim, conheceu mais sobre como mascarar dados inválidos para que esses valores não influenciem suas análises.

O módulo NumPy possui muitos recursos e somente arranhamos a superfície nesta aula. Durante a sua trajetória na área de Machine Learning, você aprofundará muito o seu conhecimento neste módulo. Nas referências da aula há muitos materiais em português para você continuar estudando. No entanto, é sempre bom deixar o link para o site oficial da ferramenta com um manual de uso e referência, não é mesmo? Infelizmente, esses dois links só estão disponíveis em inglês.

Com a conclusão desta aula, você terminou o estudo das principais bibliotecas matemáticas e numéricas em Python. Lembre-se de praticar e revisitar o conteúdo para aprofundar seus conhecimentos.

Bons estudos e até mais!

## Referências

PYTHON. Como criar um array no Python com NumPy. Disponível em: http://www.bosontreinamentos.com.br/programacao-em-python/como-criar-um-array-no-python-com-numpy/. Acesso em 21 jun. 2021.
PYTHON. Arrays mais elaborados. Disponível em: http://www.estruturas.ufpr.br/disciplinas/pos-graduacao/introducao-a-computacao-cientifica-com-python/introducao-python/2-3-arrays-mais-elaborados/. Acesso em 21 jun. 2021.
PYTHON. Entendendo a biblioteca NumPy. Disponível em: https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355. Acesso em 21 jun. 2021.
(Em inglês)
PYTHON. NumPy user guide. Disponível em: https://numpy.org/doc/stable/user/. Acesso em 21 jun. 2021.
PYTHON. NumPy Reference. Disponível em: https://numpy.org/doc/stable/reference/. Acesso em 21 jun. 2021.

## Glossário
Para conhecer o significado dos termos técnicos estudados em nossa aula, selecione a palavra desejada.

Array
https://leadfortaleza.com.br/ead/glossary/Array
Shape
https://leadfortaleza.com.br/ead/glossary/Shape
Tensor
https://leadfortaleza.com.br/ead/glossary/Tensor