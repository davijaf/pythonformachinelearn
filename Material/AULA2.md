# INTRODUÇÃO

Olá! Seja bem-vindo!

Você sabia que aplicar adequadamente os conceitos de Matemática e Estatística são habilidades essenciais para o cientista de dados?

Durante a construção de uma aplicação de Machine Learning (ML), há processos como exploração de dados, limpeza de dados, modelagem, algoritmos de ML e avaliação de algoritmos que exigem noções a respeito desses conceitos.

Já dentro do campo de Estatística, existe a aleatoriedade, que faz uso do acaso. Embora a aleatoriedade pareça o oposto do raciocínio ou da inteligência, ela pode ser uma forma bastante efetiva, inclusive, para resolver determinados problemas, pois aplicações, como criptografia, simulação, pesquisas científicas, jogos e inteligência artificial, utilizam aleatoriedade para serem mais eficientes.

É por isso que, nesta aula, você vai aprender sobre ferramentas matemáticas e aleatoriedade, podendo acompanhar a resolução de problemas por meio das bibliotecas Math e Random. Vamos lá?

## Objetivos
Resolver problemas utilizando a aleatoriedade;
Escolher e combinar métodos para tratamento de dados numéricos;
Aplicar métodos matemáticos para a resolução de problemas.

# Tópico 1 – Módulo Random

## OBJETIVOS

Aprender a definição de números pseudoaleatórios;
Conhecer e aplicar os métodos do módulo Random;
Aplicar o método de Monte Carlo.
Os números aleatórios são úteis para uma variedade de propósitos, como gerar chaves de criptografia de dados, simular e modelar fenômenos naturais complexos e para selecionar amostras aleatórias de conjuntos de dados maiores. Eles também têm sido usados ​​esteticamente, por exemplo, na Literatura e na música e, claro, sempre são populares para jogos e apostas com o intuito de gerar elementos não previsíveis, criando a sensação de acaso, surpresa e incerteza.

Já em ML, a aleatoriedade é utilizada em vários momentos, como para seleção de features (características) dos dados, para validação dos modelos de ML e até em algoritmos de ML, como a Floresta Aleatória (random forest), que gera um grande número de modelos aleatórios individuais que operam como um conjunto para realizar uma determinada tarefa.

A partir disso, pode surgir a questão: como as máquinas, que foram programadas para seguirem sempre os mesmos passos, conseguem gerar números aleatórios? Neste tópico, você vai conferir uma resposta para isso a partir dos métodos do módulo Random e aprender o que são os números pseudoaleatórios. Vamos lá!

Bem, com o advento dos computadores, os programadores reconheceram a necessidade de uma forma de introduzir aleatoriedade em um programa de computador.

No entanto, por mais surpreendente que possa parecer, é difícil fazer com que um computador faça algo por acaso. Um computador segue integralmente as instruções que você deu e, portanto, é totalmente previsível. Uma máquina que não segue suas instruções dessa maneira certamente está danificada.

Na realidade, a maioria dos números aleatórios usados​​em programas de computador são pseudoaleatórios, o que significa que são gerados de uma forma previsível usando uma fórmula matemática. Mas, para a maioria dos casos, números pseudoaleatórios são o suficiente para resolver o problema. Entretanto, há outros problemas para os quais eles não são suficientes, como você pode conferir no boxe Saiba Mais, a seguir.

Ícone Saiba Mais
Ícone “Saiba Mais”.
Computadores não conseguem gerar números aleatórios, e isso pode ser problemático no mundo moderno. Assista ao vídeo Por que computadores não podem gerar números aleatórios?, que explica um pouco sobre como computadores funcionam e como podemos gerar números verdadeiramente aleatórios usando-os. Acesse o vídeo por meio deste link. Observação: o vídeo não tem o recurso de Libras, mas conta com legenda. Para acioná-la, verifique as configurações do YouTube.

Bom, números pseudoaleatórios são o suficiente para trabalhar com Ciência de Dados, certo? A seguir, verifique se é possível distinguir números aleatórios gerados por um ser humano e por um computador.

Vamos fazer um brincadeira! Existem duas sequências de números entre 1 e 5 a seguir. Analise-as e reflita se há algum padrão em uma das sequências? Confira:


Uma das sequências foi gerada por uma máquina, e a outra foi criada por uma pessoa qualquer. Qual das duas sequências aleatórias você acha que foi gerada por uma máquina?

Se você respondeu que foi a sequência “a”, você acertou. A grande questão é que nós, seres humanos, gostamos muito de padrões. É muito difícil para um ser humano criar uma sequência realmente aleatória, pois, muitas vezes, atribuímos padrões a coisas que, na verdade, não existem. Por exemplo, a sequência do item “b”, apesar de ser uma sequência aleatória, apresenta um padrão, que é o de cada número aparecer 3 vezes (o número 2 aparece 3 vezes; o número 3 aparece 3 vezes etc.) e nenhum número se repete sequencialmente.

Agora outro exemplo: uma pessoa jogando dados durante algum tempo pode acabar achando que criou um tipo de padrão nos números. Esse aparente padrão significa que o nosso cérebro está criando padrões onde não há. O acaso não segue ordem ou qualquer regra. Quando você joga um dado na mesa, você não sabe qual vai ser o número que vai ficar para cima. E não importa quantas vezes você jogue, você não consegue identificar um padrão nos números. Justamente por ser aleatório.

Os números pseudoaleatórios apontados nos itens anteriores foram gerados por meio do módulo Random do Python, que é uma biblioteca que contém vários métodos e funções, o que permite operações e utiliza números aleatórios para gerar algum resultado. Aprenda como usá-lo na próxima página.

Vamos começar pela prática: abra o programa Jupyter Notebook para executar o código a seguir, que é um código de exemplo de utilização do módulo Random.

import random
print(random.random()) # 0.4288890546751146
print(random.random()) # 0.7611303723546115
Analisando o código:

Primeiramente, foi importado o módulo random (linha 1);
Em seguida, foi utilizado o método random (linhas 2 e 3), que retorna o próximo número decimal aleatório no intervalo [0.0, 1.0), ou seja, 0.0 <= x < 1.0. O método Random retorna um número aleatório diferente toda vez que é chamado.
Você deve estar se perguntando: “mas se a função Random só retorna números entre 0 e 1, como eu faço para gerar um número, por exemplo, entre 10 e 20?”.

Bom, para isso, vamos criar uma função para nos auxiliar, como mostra o código da próxima página.

A seguir, é demonstrado o código de uma função que retorna um número aleatório maior que 1. A função é criada a partir do método Random do módulo Math. Confira.

def minha_funcao_random(numero_minimo,numero_maximo):
  diferenca = numero_maximo - numero_minimo
  return diferenca * random.random() + numero_minimo

print(minha_funcao_random(10,20)) # 19.10975962449124

print(minha_funcao_random(10,20)) # 15.822275730589492
Analisando o código:

Após ser escolhido um intervalo, a função minha_função_random calculará a diferença entre dois valores indicados pelo usuário. Nesse caso, foram escolhidos os valores 10 e 20;
O valor resultante da diferença 20 – 10 será guardado na variável diferenca, ou seja, o valor 10.
Em seguida, esse número, proveniente da diferença dos dois valores, é multiplicado por um número aleatório entre 0 e 1, resultando em um número aleatório entre 0 e 10.
Por fim, para o número ficar no intervalo correto, entre 10 e 20, ele é somado ao valor 10, que é o número que inicia o intervalo até o número resultante da multiplicação, gerando um número aleatório entre 10 e 20.
A seguir, verifique como funciona a função que cria números pseudoaleatórios, que será a base de todas as funções do módulo Random.

Bem, como os números aleatórios são criados por meio de uma fórmula matemática, essa fórmula precisa de um número qualquer que vai dar início à geração dos próximos números aleatórios, chamado de semente. Para passar um número pré-definido de semente, você pode utilizar a função seed (‘semente’ em inglês), como mostra o seguinte código.

import random

random.seed(10)

print(random.random()) # 0.5714025946899135

print(random.random()) # 0.4288890546751146

random.seed(10)

print(random.random()) # 0.5714025946899135

print(random.random()) # 0.4288890546751146

random.seed(1234)

print(random.random()) # 0.9664535356921388

print(random.random()) # 0.4407325991753527
Analisando o código:

Na linha 3, note que a função seed está sendo chamada com o valor 10 como argumento, fazendo com que os próximos números aleatórios gerados sigam uma sequência pré-definida.
Na linha 9, perceba que se usarmos a mesma semente (seed), que é o valor 10, obteremos a mesma sequência de valores aleatórios.
Na linha 15, definimos outro valor como argumento, gerando outra sequência aleatória.
Mas o que você acha que acontece se você usar o módulo Random sem definir um valor para a semente? Nesse caso, é usada como padrão a hora do sistema atual ou uma fonte de aleatoriedade do seu sistema operacional, caso haja uma disponível.

Bem, agora que você sabe como funciona a geração de números pseudoaleatórios, confira, na próxima página, quais outros métodos desse módulo podem ser utilizados.

Anteriormente criamos uma função chamada ‘minha_funcao_random’ que gerou números decimais aleatórios que estavam dentro de um intervalo [x, y) específico. Ao invés de utilizar nossa função, podemos usar a função uniform(a, b) do módulo Random, que retorna um número decimal aleatório N de forma que a <= N <= b, como apresentado neste código:

import random

print(random.uniform(10,20)) # 16.014634495610515

Uma distribuição de probabilidade é um modelo matemático que relaciona um certo valor da variável com a sua probabilidade de ocorrência. Em probabilidade e estatística, a distribuição normal é uma das distribuições de probabilidade mais utilizadas para modelar fenômenos naturais. Isso se deve ao fato de que um grande número de fenômenos naturais apresenta sua distribuição de probabilidade quase normal.

Na página seguinte, conheça como criar uma distribuição normal com Python.

No módulo Random existe a função normalvariate (μ, σ), que simula a distribuição normal, em que μ é a média (valor que demonstra a concentração dos dados de uma distribuição) e σ é o desvio padrão da distribuição (variação das observações em relação à média delas). O símbolo σ² representa a variância, calculada pela raiz quadrada do desvio padrão.

No gráfico a seguir, observe que o eixo X representa todos os valores existentes, e o eixo Y representa a probabilidade daquele valor existir na distribuição. Pode ser fácil perceber que os parâmetros para criação da distribuição vermelha é 0 para o valor da média, e 1 para o valor da variância, isso faz com que a probabilidade de um número 0 existir seja de 40%. Confira.

Figura 1 - Três distribuições normais com valor de média e desvio padrão diferentes.

Agora, vamos utilizar o código a seguir para gerarmos um número aleatório com a mesma probabilidade da distribuição vermelha. Em seguida, entenda como utilizar métodos que se utilizam da aleatoriedade para funcionar.

import random

print(random.normalvariate(0,1)) # 0.11772784154963907

Você pode gerar um número inteiro aleatório em Python com a função randint(a, b), que retorna um inteiro aleatório N de forma que a <= N <= b. Como exemplo, vamos usar essa função para simular a jogada de uma dado, ou seja, em um intervalo entre 1 e 6, como mostrado neste código.

import random

print(random.randint(1,6)) # 1

print(random.randint(1,6)) # 5
No código apresentado, foi demonstrado que o valor da primeira rolagem do dado foi igual a 1, e a segunda rolagem do dado foi igual a 5. Outra forma de simular a rolagem dos dados é utilizando a função choice, que tem como parâmetro uma lista e retorna um elemento aleatório dessa lista. Se a lista estiver vazia, um erro é retornado, como apresentado no código a seguir.

import random

dado = [1,2,3,4,5,6]

print(random.choice(dado)) # 5

print(random.choice([])) # IndexError: Cannot choose from an empty sequence
Analisando o código:

Note que criamos uma lista com os possíveis valores de um dado (de 1 a 6) e utilizamos a função choice para escolher um desses valores.
Na linha 5, a função retornou o valor 5 da lista.
Na linha 7, choice recebeu como parâmetro uma lista vazia, dessa forma, um erro é disparado.
Tudo bem até aqui? Para continuar ainda no assunto, mas de uma forma mais interessante, confira o boxe Saiba mais da próxima página.

A seguir, há um link que mostra a utilização da função choice em um site.

Ícone Saiba Mais
Ícone “Saiba Mais”.

A Wikipédia é um site que disponibiliza vários artigos, certo? Ao acessar o link a seguir, note que você é redirecionado para um artigo escolhido aleatoriamente pelo site. Confira: https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria_na_Categoria/Categoria:!Artigos_destacados

Percebeu para que serve a função choice? A partir desse link, você pode aprender algo novo todo o dia, de forma aleatória. Interessante, não é?

Pronto! Agora, vamos avançar os estudos a respeito de outras funções que também simulam o lançamento de dados.

Agora que já conseguimos simular o lançamento de um dado, verifique como podemos burlar a probabilidade de sair um valor qualquer no dado.

Em um dado do tipo padrão, a frequência com a qual qualquer um dos seis números se apresenta após uma jogada é a mesma: 1/6 ou 16,66%. Um dado viciado é aquele cuja probabilidade de se tirar um determinado número é maior que 1/6 e são vários os métodos disponíveis para viciá-lo, como aquecer e perfurar. Mas, em código, só precisamos utilizar a função choices, que, diferente da função choice, retorna uma lista de tamanho k, contendo elementos escolhidos aleatoriamente, onde k é 1 por padrão, como apresentado no código a seguir.

import random

dado = [1,2,3,4,5,6]

pesos = [1,1,1,1,2,4]

print(random.choices(dado, weights = pesos)) # [6]
Se uma sequência weights for especificada, as seleções serão feitas de acordo com os pesos relativos, ou seja, no exemplo mostrado nesta página, há uma probabilidade de 40% de ser gerado o número 6; 20% de ser gerado o número 5, e os demais possuem uma probabilidade de 10% de serem gerados. Caso seja passado o valor de k como argumento, a lista gerada terá k elementos aleatórios, com probabilidades diferentes de serem gerados cada número, devido ao parâmetro weights. Confira isso no código da próxima página.

import random

dado = [1,2,3,4,5,6]

pesos = [1,1,1,1,2,4]

print(random.choices(dado, weights = pesos, k = 10)) # [5, 6, 3, 2, 4, 3, 6, 5, 1, 6]
Analisando o código:

Note que foi gerada uma lista com 10 números aleatórios, devido ao valor passado para o parâmetro k.
É possível notar, também, que o valor 6 apareceu com mais frequência, pois há uma probabilidade de 40% desse número ser gerado.
A seguir, o assunto será jogo! Verifique como criar um sentimento de surpresa em um jogo, aplicando um método completamente aleatório, que é o embaralhamento. Confira como e por qual motivo embaralhar uma sequência qualquer e quais suas aplicações.

Agora vamos tratar de jogos! Para isso, vamos utilizar a função Shuffle, que é muito empregada em jogos virtuais, principalmente nos que utilizam cartas, e que é um método para embaralhar uma lista de elementos em uma ordem aleatória, como mostra este código.

import random

baralho = ['Ás de Copas','2 de Copas','3 de Copas','4 de Copas','5 de Copas','6 de Copas','7 de Copas',
'8 de Copas','9 de Copas','10 de Copas','Valete de Copas','Dama de Copas','Rei de Copas']

random.shuffle(baralho)

print(baralho) # ['Rei de Copas', '8 de Copas', '5 de Copas', 'Ás de Copas', '7 de Copas', 'Valete de Copas',
'3 de Copas', 'Dama de Copas', '6 de Copas', '4 de Copas', '10 de Copas', '9 de Copas',
'2 de Copas']
Observe que a lista que tínhamos antes está totalmente fora de ordem. Uma outra possibilidade para criar várias ordenações diferentes é utilizando permutações, assunto que provavelmente você já conhece. Perceba que mesmo para pequenas listas, o número total de permutações possíveis pode crescer rapidamente, aumentando o tempo para serem geradas. Isso implica que a maioria das permutações de uma longa sequência nunca poderá ser gerada em tempo hábil.

Resumindo, quando é inviável fazer permutações, é possível utilizar o método Shuffle para gerar várias combinações diferentes.

A seguir, conheça como usar o módulo Random para gerar amostras aleatórias com e sem reposição.

Ao invés de embaralhar os elementos, podemos pegar uma amostra aleatória dos dados, utilizando o método Sample (que significa amostra), que retorna uma lista de comprimento k de elementos exclusivos escolhidos a partir da sequência ou conjunto da população. O método Sample é usado para amostragem aleatória sem reposição, ou seja, ao retornar um elemento aleatório de uma lista, aquele elemento não poderá mais ser retornado novamente, isso faz com que cada elemento aleatório só seja retornado uma única vez.

Já o método Choices, explicado anteriormente, é usado para amostragem aleatória com reposição, ou seja, um único elemento escolhido aleatoriamente pode ser retornado mais de uma vez por ele, pois não há uma remoção daquele elemento da lista. Esse método retorna uma nova lista contendo elementos da população (que significa todos os valores possíveis), mantendo os valores originais inalterados. A lista resultante está na ordem de seleção, para que todas as subfatias também sejam amostras aleatórias válidas. Confira um exemplo a seguir.

Ícone Fique atento!
Ícone “Fique atento”.
Caso você tenha uma lista de nomes e queira fazer um sorteio com os nomes dessa lista, escolhendo o primeiro, o segundo e o terceiro lugar, se a lista retornada for ['Alex', 'Luana',’Daniel’], isso significa que o primeiro lugar ficaria com o Alex, o segundo ficaria com a Luana e o terceiro ficaria com o Daniel. Se a população tiver repetições, cada ocorrência é uma seleção possível na amostra.

No jogo de Poker, por exemplo, são escolhidas cinco cartas aleatórias para ficar no centro da mesa, onde, incialmente, somente as três primeiras são mostradas para os jogadores. Nesse caso, o método Choices seria ideal para implementar essa tarefa, na próxima página confira como utilizá-lo em um código.

import random

baralho = ['Ás de Copas','2 de Copas','3 de Copas','4 de Copas','5 de Copas','6 de Copas','7 de Copas',
'8 de Copas','9 de Copas','10 de Copas','Valete de Copas','Dama de Copas','Rei de Copas']

print(random.choices(baralho, k = 2)) # ['Valete de Copas', 'Valete de Copas']

print(random.sample(baralho, k = 2)) # ['10 de Copas', '3 de Copas']
Analisando o código apresentado:

Na linha 6, há uma amostragem com reposição que, coincidentemente, resultou na escolha de um elemento duas vezes.
Na linha 8, há uma amostragem sem reposição, ou seja, a maior amostra sem reposição que poderíamos fazer seria com k=13, pois não haveria mais elementos para serem retirados. Esses métodos são muito utilizados em pesquisas científicas e machine learning.
A seguir, verifique um método que é utilizado até hoje para fazer previsões, muito empregado para prever dados financeiros da bolsa de valores.

Designa-se por Método de Monte Carlo (MMC) qualquer método que se baseia em amostragens aleatórias massivas para obter resultados numéricos. São utilizados mais comumente em problemas de Física e de Matemática que são muito difíceis ou impossíveis de serem resolvidos com outros métodos.

O Método de Monte Carlo tem sido utilizado há muito tempo como forma de obter aproximações numéricas de funções complexas em que é inviável, ou mesmo impossível, obter uma solução analítica ou, pelo menos, determinística. A princípio, MMC pode ser usado para resolver quaisquer problemas com uma interpretação probabilística.

Ícone Saiba Mais
Ícone “Saiba Mais”.
O nome Monte Carlo surgiu durante o projeto Manhattan, na Segunda Guerra Mundial. Por ser secreto, o trabalho exigia um codinome e sugeriram usar o nome Monte Carlo. Referindo-se ao Cassino Monte Carlo, em Mônaco.

Agora, pensando no MMC e no seu conceito, reflita sobre a seguinte pergunta: qual a probabilidade de jogar dois dados ao mesmo tempo e eles caírem com o mesmo lado para cima? Pense um pouco e avance para a próxima página.

Bom, você tem duas soluções para resolver esse problema, uma é calcular quantas possibilidades há de dois dados caírem com o mesmo lado para cima, {1,1} , {2,2} , {3,3} , {4,4} , {5,5} , {6,6}, ou seja, 6 possibilidades, e quantas combinações diferentes podem surgir dos lançamentos dos dados, que seriam 36 combinações. Agora, basta dividir 6 por 36 e você terá que a probabilidade de jogar dois dados ao mesmo tempo e eles caírem com o mesmo lado para cima é de 16,66%.

Outra solução mais divertida para esse problema seria lançar esses dados inúmeras vezes e contar quantas vezes os dados caíram com o mesmo lado para cima, após ter esse número, basta dividir pela quantidade de lançamentos que foram feitos. Certamente, esse método daria muito mais trabalho, mas é por isso que temos as máquinas para fazerem o trabalho árduo para nós.

Você consegue fazer esse código? Caso consiga, compare a sua resposta com o código da próxima página e confira a explicação.

Resumindo o Método de Monte Carlo, explicado na página anterior, ele tem como premissa que é possível chegar à probabilidade de certo evento ocorrer a partir de várias tentativas aleatórias. A seguir, confira o código criado para fazer vários lançamentos de dois dados, em que foi feita uma tentativa de calcular a probabilidade de dois dados lançados ao mesmo tempo caírem com o mesmo lado para cima.

import random

numero_de_tentativas = 2000000
quantidade_de_acertos = 0

for _ in range(numero_de_tentativas):
  dado_1 = random.randint(1,6)
  dado_2 = random.randint(1,6)

  if (dado_1 == dado_2):
    quantidade_de_acertos += 1

print(quantidade_de_acertos/numero_de_tentativas) # 0.166654
Analisando os principais pontos do código:

Na linha 3, é possível perceber pela variável numero_de_tentativas, que serão feitos 2 milhões de lançamentos dos dois dados.
Nas linhas 7 e 8, você pode notar os lançamentos de cada um dos dados.
Nas linhas 10 e 11, é feita a contagem de quantas vezes os dados caíram com a mesma face para cima.
Por fim, é feita a divisão no número de acertos pela quantidade de lançamentos totais. Note que o MMC acaba sendo bem preciso. O valor resultante combinou com o valor que calculamos anteriormente.
Bom, com esse assunto, concluímos o primeiro tópico. Podemos dizer que você pôde aprender bastante até aqui, certo? Mas não é só isso! A seguir, verifique como utilizar o módulo Math do Python.

# Tópico 2 – Módulo Math

## OBJETIVOS

Conhecer as etapas de um projeto de ML;
Diferenciar quais são as constantes do módulo Math;
Definir como fazer tratamento em dados numéricos;
Praticar a utilização dos métodos disponíveis no módulo Math.
Cálculos matemáticos são uma parte essencial da maioria do desenvolvimento Python. Se você está trabalhando em um projeto científico, uma aplicação financeira ou qualquer outro tipo de esforço de programação, você simplesmente não pode escapar da necessidade de matemática.

Em ML, a Estatística forma uma parte vital para organizar e assimilar os dados. A Matemática atua como um pré-requisito para ter uma sólida compreensão dos conceitos estatísticos. Saiba que notações, métodos e operações em Matemática ajudarão na assimilação de tópicos avançados em Estatística, como análise multivariada.

Com base nisso, você vai conhecer como tratar valores numéricos e onde usar funções que são utilizadas em algoritmos de ML dentre outras particularidades sobre esse tema.

Como apresentado anteriormente, esses conceitos a respeito de cálculos matemáticos estão presentes em quase todas as etapas de projetos de ML, assim, antes de partir para as funções, confira as etapas que fazem parte de um projeto de ML e a descrição de cada uma delas.

A seguir, você encontra as principais etapas de um projeto de ML e a descrição do que é feito em cada etapa, desde o entendimento do problema até a utilização efetiva do sistema. Confira.

1. Coleta de dados: etapa em que o cientista de dados usa a linguagem SQL para coletar dados de um ou vários bancos de dados para construir sua tabela inicial de análise. Em muitos casos, o Python é usado para coletar dados via Application Programming Interface (API).
2. Limpeza dos dados: após a coleta, o cientista de dados avalia o conjunto de dados, procurando, principalmente, por outliers através de métodos matemáticos, devido a erros no sistema e inconsistência nos dados, por exemplo, a idade de um ser humano acima de 200 anos.
3. Exploração de dados: momento de analisar os dados em busca de respostas para as hipóteses levantadas pelo time de negócio, utilizando estatística para encontrar insights. A maioria dos projetos de Ciência de Dados acaba nessa fase, pois um modelo de ML nem sempre é a solução necessária para o negócio.
4. Modelagem de dados: preparação dos dados para "ensinar" os algoritmos de ML. As principais atividades nessa fase são transformações de variáveis categóricas e seleção de features.
5. Algoritmos de ML: fase da aplicação dos algoritmos de ML para criar um modelo do fenômeno observado. Seja um fenômeno de venda, churn entre outros. Lembrando que algoritmos de ML são, em sua essência, funções matemáticas, certo?
6. Avaliação dos algoritmos de ML: etapa para avaliar a performance dos algoritmos de ML em termos de suas principais métricas. As métricas, puramente estatísticas, variam de acordo com o problema e com o que o time de negócio espera do modelo de ML.
7. Publicação do modelo em produção: última etapa do processo, em que o cientista de dados torna seu modelo público e com acesso aos seus resultados. Geralmente, feito por meio de um banco de dados ou de um API.
Pronto! Conhecendo essas etapas, você pode entender como usar as funções matemáticas.

Para cálculos matemáticos simples em Python, você pode usar os operadores matemáticos incorporados, como adição, subtração, divisão e multiplicação. Mas operações mais avançadas, como exponenciais, logarítmicas, trigonométricas ou funções de potência, não são incorporadas. Mas será que isso significa que é preciso implementar todas essas funções do zero? O que você acha?

Felizmente, não. O Python fornece um módulo especificamente projetado para operações matemáticas de alto nível: o módulo.math. Esse módulo é um recurso importante projetado para lidar com operações matemáticas. Ele oferece a você a capacidade de realizar cálculos matemáticos comuns e úteis dentro de sua aplicação, podendo ser utilizado para efetuar, por exemplo, combinações e permutações usando fatoriais: a altura de um poste usando funções trigonométricas, a decadência radioativa usando a função exponencial, a curva de uma ponte de suspensão usando funções hiperbólicas, equações quadráticas etc.

Uma vez que o módulo vem embalado com a versão Python, você não precisa instalá-lo separadamente. Usá-lo é apenas uma questão de importar o módulo Math. Ao longo desta aula, você deverá conferir os métodos mais importantes desse módulo.

A seguir serão apresentadas algumas constantes e métodos básicos do módulo Math. Vamos lá!

O código a seguir demonstra como utilizar algumas constantes disponibilizadas no módulo Math e métodos que identificam as respectivas constantes. Após conferir o código, avance para a sua análise.

import math

print(math.pi) # 3.141592653589793

print(math.inf) # inf

print(-math.inf) # -inf

print(math.inf > 100000000000) # True

print(math.isinf(100000000000)) # False

print(math.isinf(math.inf)) # True

print(math.nan) # nan

print(math.isnan(10)) # False

print(math.isnan('Texto')) # TypeError

print(math.isnan(math.nan)) # True

Analisando o código:

Na linha 1, foi importado o módulo Math.
Na linha 3, foi chamada a constante Pi (π), que é a razão da circunferência de um círculo ao seu diâmetro. Perceba que o valor Pi é dado a quinze casas decimais em Python.
Nas linhas 5 e 7, há uma chamada constante ‘infinito’, com valor positivo e negativo, respectivamente, que não pode ser definido por um número, é um conceito matemático representando algo que é interminável ou ilimitado.
Na linha 9, há uma comparação do infinito com o valor cem bilhões, provando que infinito é maior que esse valor.
Nas linhas 11 e 13, é utilizado o método isinf para saber se o elemento é infinito.
Na linha 15, é chamada a constante NaN ou ‘Não é um número’ (Not a Number), que pode indicar que uma variável que deveria ser numérica foi corrompida. Geralmente, valores NaN aparecem quando você coleta dados de uma base de dados.
Nas linhas 17, 19 e 21, foi utilizado o método isnan para saber se o elemento é um NaN. Note que o valor 10 retorna falso e, caso o valor seja um texto, é disparado um erro, só retornando verdadeiro se o valor for a constante NaN.
Agora confira uma curiosidade a respeito da constante citada anteriormente: a constante Pi. Depois conheça mais constantes do módulo Math.

Ícone Saiba Mais
Ícone “Saiba Mais”.
Um fato interessante é que Pi é a constante matemática mais reconhecida e conhecida do mundo. Tem data de celebração própria, chamada Dia do Pi, que cai em 14 de março (14/03).

Nas próximas páginas, entenda como utilizar métodos do módulo Math para fazer tratamento em dados numéricos.

Existem alguns métodos no módulo Math que fazem um tratamento nos dados passados como argumento, esses métodos são muito utilizados em ML para fazer a limpeza nos dados, ou seja, o processo de identificação de partes incompletas, incorretas, imprecisas ou irrelevantes dos dados e, em seguida, substituindo, modificando, ou excluindo os dados sujos ou grosseiros. O código a seguir demonstra como fazer alguns desses tratamentos. Observe-o com atenção.

import math

print(math.ceil(9.24)) # 10

print(math.ceil(-9.24)) # -9

print(math.floor(9.89)) # 9

print(math.floor(-9.89)) # -10

print(math.trunc(9.80)) # 9

print(math.trunc(-9.80)) # -9

print(math.fabs(2.3)) # 2.3

print(math.fabs(-2.3)) # 2.3
Após conferir o código, verifique sua análise na próxima página.

Analisando o código:

A partir das linhas 3 e 5, você pode notar a utilização do método ceil (teto), esse método retorna o menor valor inteiro maior ou igual ao determinado número passado como argumento, ou seja, um arredondamento para cima.
Nas linhas 7 e 9, é usado o método floor (piso), que retorna o valor inteiro mais próximo que seja menor ou igual ao determinado número passado como argumento, ou seja, um arredondamento para baixo.
Nas linhas 11 e 13, note que foi utilizado o método trunc, que significa truncamento, esse método é usado para manter apenas a parte inteira e eliminar a parte decimal de um determinado número passado como argumento.
Nas linhas 15 e 17, foi usado o método fabs, que é responsável por retornar o valor absoluto de um determinado número passado como argumento, ou seja, usado para definir que tanto desvios positivos quanto negativos possuam o mesmo peso.
Você sempre deve passar um número como argumento para esses métodos. Se você tentar inserir qualquer outro valor, então você disparará um erro do tipo TypeError.

Na próxima página, confira alguns exercícios e aproveite para testar os conhecimentos aprendidos até aqui.

Além dos métodos que fazem um tratamento nos dados, há os que fazem cálculos mais complexos a partir dos valores passados como argumento. O seguinte código demonstra como usar esses métodos, do módulo Math, que envolvem cálculos mais avançados.

import math

print(math.pow(10, 2)) # 100.0

print(math.sqrt(100)) # 10.0

print(math.log(100, 10)) # 2.0

print(math.factorial(6)) # 720
Agora vamos analisar algumas linhas do código:

Na linha 3, utilizamos o método pow, que, ao receber como entrada dois parâmetros, x e y, retornará x elevado à potência y, ou seja, 102 = 100.
Na linha 5, foi usado o método sqrt, que tem o propósito de calcular a raiz quadrada de qualquer número real positivo. Para calcularmos o logaritmo (método que não possui aleatoriedade) de um número, utilizamos o método puramente matemático, chamado log, que, ao receber dois números, x e y, retornará o valor da potência que y deve ter para chegar ao resultado x, ou seja, para o resultado ser igual a 100, o valor 2 tem que ser a potência de 10.
Na linha 9, foi utilizado o método factorial, que é utilizado para calcular o fatorial de um número, que é o produto de todos os inteiros positivos menores ou iguais a esse número, ou seja, fatorial de 6 é igual a 6! = 6x5x4x3x2x1 = 720.
Na próxima página, há a continuação do código. A partir disso, continue a estudar os métodos do módulo Math.

A seguir, é apresentada a continuação do código da página anterior, que demonstra como utilizar mais alguns métodos disponibilizadas no módulo Math.


print(math.isclose(10, 8, rel_tol=0.2)) # True

print(math.isclose(10, 5, abs_tol=5)) # True

print(math.gcd(10, 15)) # 5
Analisando essas linhas:

Nas linhas 11 e 13, foi usado o método isclose (está perto), que determina se dois números estão próximos um do outro, felizmente, é possível definir a tolerância de proximidade.
Na linha 11, foi empregado o parâmetro rel_tol para a tolerância, que é um valor em porcentagem. Nesse caso, é 20%, e para saber se o número está próximo usamos essa fórmula: x-(x*0.2) <= y <= x+(x*0.2), em que x é o maior valor e y é o menor valor passado como argumento.
Na linha 13, foi usado o parâmetro abs_tol para a tolerância, que é um valor absoluto. Nesse caso, é 5, ou seja, para saber se o número está próximo, é usada a fórmula: |x-y| <= 5, onde x e y são os valores passados como argumento. Por fim, na linha 15, foi usado o método gcd (MDC, Maior Divisor Comum), que calcula o maior número inteiro que divide os dois números.
Mas onde você acha que pode utilizar esses métodos no dia a dia? Confira um exemplo na próxima página.

Imagine que você decidiu comprar pizza para a família toda. Uma pizzaria oferece pizzas médias com raio de 30cm e grandes com raio de 45cm, ao preço de R$ 40,00 e R$ 50,00 cada uma, respectivamente. Você compraria duas pizzas médias ou uma grande?

Provavelmente, você já sabe como usar a biblioteca Math. Então, use os métodos contidos nesse módulo para saber qual das opções tem o melhor custo benefício. O seguinte código ilustra como pode ser feito para comparar as duas opções.

import math

area_pizza_media = math.pi * math.pow(30, 2)

print(area_pizza_media * 2) # 5654.8667764616275

area_pizza_grande = math.pi * math.pow(45, 2)

print(area_pizza_grande) # 6361.725123519331
Para saber qual a melhor opção, compare a área das duas pizzas. Para calcular a área delas use a fórmula da área de uma circunferência, que é igual a Pi vezes o raio ao quadrado. Esse cálculo foi utilizado nas linhas 3 e 7, modificando apenas o raio (30 e 45) para considerar os dois tamanhos de pizza. Por fim, é preciso multiplicar a área da pizza média por 2, pois você deve considerar que são duas pizzas médias, e imprimir os dois resultados na tela. Com isso, é possível concluir que a área da pizza grande é bem maior. Agora ficou fácil decidir qual escolher.

A seguir, confira como utilizar funções trigonométricas, ou seja, funções angulares importantes no estudo dos triângulos e na modelação de fenômenos periódicos.

Vários algoritmos de ML utilizam distância para prever ou classificar algo, por exemplo, k-means, KNN etc. em que o objetivo é determinar a qual grupo uma determinada amostra vai pertencer com base nas amostras vizinhas. Ao contrário dos outros algoritmos, ele não constrói um modelo, ele faz somente o cálculo de distância.

A seguir, há duas imagens, uma de um triângulo retângulo com dois de seus lados medindo 3 e 4 centímetros cada, e a outra imagem contém um plano cartesiano com dois pontos, posicionados nas coordenadas (1,3) e (3,2).

https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104630456230965/aula/img/figura3.png
Figura 3 – Triângulo pitagórico

https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104630456230965/aula/img/figura4.png
Figura 4 – Plano cartesiano com dois pontos especificados

Conferiu direitinho as imagens e os seus dados? Na próxima página, verifique os códigos referentes a elas e, em seguida, acompanhe uma explicação.

Código do triângulo pitagórico:

import math

math.hypot(3, 4) # 5.0
Código do plano cartesiano com dois pontos especificados:

import math

print(math.dist((1,3),(3,2))) # 2.23606797749979
Na imagem do triângulo retângulo, é possível utilizar o método hypot. Para calcular a hipotenusa deste triângulo, é possível notar que o resultado é igual a 5. Na imagem do plano cartesiano, dá para utilizar o método dist para calcular a distância entre dois pontos. Interessante, não é mesmo?

Bom, foi bastante conteúdo até aqui. Caso você tenha qualquer dúvida, revise o conteúdo ou pesquise o quanto achar necessário.

Aqui você pôde aprender sobre a importância da aleatoriedade e como usá-la a seu favor em Python. Isso vai lhe permitir criar soluções incríveis, que envolvem simulações, para problemas do dia a dia. Além disso, você aprendeu sobre o módulo Math, que fornece funções úteis para a realização de cálculos matemáticos que possuem muitas aplicações práticas.

Agora é hora de aplicar o que você aprendeu em situações reais. Caso tenha dúvidas, pesquise. Lembre-se que a prática e a pesquisa são formas importantíssimas de avançar nos estudos.

Até mais!

## Referências

DOCS PYTHON. math – Funções matemáticas. Disponível em: https://docs.python.org/pt-br/3.10/library/math.html. Acesso em: 25 maio 2021.
RANDOM.ORG. What's this fuss about true randomness? Disponível em: https://www.random.org/. Acesso em: 25 maio 2021.
REAL PYTHON. Generating Random Data in Python (Guide). Disponível em: https://realpython.com/python-random/. Acesso em: 25 maio 2021.
REAL PYTHON. The Python math Module: Everything You Need to Know. Disponível em: https://realpython.com/python-math-module/. Acesso em: 25 maio 2021.
TABLEAU. Dez habilidades que todo cientista de dados deve ter. Disponível em: https://www.tableau.com/pt-br/learn/articles/data-science-skills. Acesso em: 25 maio 2021.
WIKIPÉDIA. John von Neumann. Disponível em: https://pt.wikipedia.org/wiki/John_von_Neumann. Acesso em: 25 maio 2021.
WIKIPÉDIA. Método de Monte Carlo. Disponível em: https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Monte_Carlo. Acesso em: 25 maio 2021.
WIKIPÉDIA. Pseudoaleatoriedade. Disponível em: https://pt.wikipedia.org/wiki/Pseudoaleatoriedade. Acesso em: 25 maio 2021.


# Glossário
Para conhecer o significado dos termos técnicos estudados nesta aula, selecione a palavra desejada.

Estatística
https://leadfortaleza.com.br/ead/glossary/Estatistica

MMC – Método de Monte Carlo
https://leadfortaleza.com.br/ead/glossary/MMC_Metodo_de_Monte_Carlo