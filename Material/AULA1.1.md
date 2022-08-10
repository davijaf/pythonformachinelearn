# Python para Machine Learning

Olá!
Neste curso você irá aprofundar os seus conhecimentos na linguagem de programação Python direcionados para Machine Learning. Você conhecerá módulos muito utilizados por cientistas de dados, aprenderá a trabalhar mais com dados numéricos e, por fim, irá salvar e ler arquivos de dados. Esses conhecimentos são essenciais, pois as aplicações de Machine Learning consistem em ler dados numéricos e trabalhar com estes.

Você, provavelmente, já sabe o que são classes em Python, certo? Também deve conhecer o conceito da Programação Orientada a Objetos. Esse é um paradigma que rege muitas das linguagens de programação modernas, incluindo Python. No entanto, você sabia que existem outros tipos de paradigmas de programação? Nesta aula você conhecerá o paradigma da Programação Funcional e saberá como utilizar seus conceitos na linguagem Python.

Na Programação Funcional são usadas somente funções para realizar operações e gerar novos dados. Essas funções comportam-se mais como as funções vistas nas aulas de matemática do ensino médio. Existem algumas funções em Python que são muito utilizadas em aplicações de Machine Learning, como map, filter, any e all. Você aprenderá como utilizá-las para a manipulação de conjuntos de dados. Também conhecerá as funções anônimas lambda, que são capazes de poderosas operações em apenas uma linha de código!

Tudo isso para que ao final desta aula você consiga abordar problemas de programação de uma forma diferente. Você vai perceber que, utilizando Programação Funcional, torna-se mais intuitivo modelar o problema para resolvê-lo. Empolgado?

Então, vamos lá!

## Objetivos
Aprender o conceito de Programação Funcional;
Definir funções anônimas em Python;
Aplicar as funções map, filter, any e all.

# Tópico 1 – Programação Funcional

## OBJETIVOS
Aprender o conceito de Programação Funcional;
Aplicar estes conceitos em Python;
Comparar a Programação Funcional com outros paradigmas de programação.
Para iniciar sua jornada de aprendizagem nesta aula, você precisa entender o que é o paradigma da Programação Funcional e quais são as diferenças entre este e outros conceitos que você estudou anteriormente, como o de Programação Declarativa ou Programação Orientada a Objetos. Isso é importante pois, ao saber diferenciá-los, você aprenderá a melhor hora de aplicar um paradigma ou outro. Afinal, ao programar, é interessante saber sempre qual a melhor ferramenta para se utilizar.

Python permite que você aplique diversos conceitos da Programação Funcional desde formas simples até as mais complexas. Não é do escopo deste curso listar exaustivamente as possibilidades. Portanto, entenda os principais conceitos que podem ser utilizados na prática. Assim, os exemplos vão estar voltados para manipulação de dados, uma tarefa comum em Machine Learning.

Entenda mais sobre os paradigmas de programação a seguir!

Mas o que significa “paradigma de programação”? Bem, esse é apenas um modo de classificar as linguagens de programação. Você já deve conhecer o Paradigma Procedural – talvez sem nem saber o nome –, o de Orientação a Objetos e o de Programação Funcional. Existem diversos outros, mas normalmente eles são limitados a poucas aplicações.

Quando você escreve um código em Python, você provavelmente cria variáveis e modifica seus valores através de funções, correto? Então, quando uma linguagem pertence ao paradigma procedural, ela irá fornecer comandos explicitamente ao computador e agregá-los em blocos de códigos chamados de "funções“.

De forma similar, temos a Orientação a Objetos, mas ao invés de agrupar as instruções em funções, você deve aglutinar em classes e métodos. As chamadas a esses métodos normalmente atualizam os atributos das classes. Percebeu um ponto em comum? Utilizar funções e métodos modifica o valor de variáveis.

Por outro lado, a Programação Funcional tem uma característica principal que a distingue dos outros paradigmas: as funções utilizadas atuam somente com os valores de entrada, não modificam nenhum outro valor que não seja o retorno da saída e não produzem efeitos colaterais. Confuso? Pense da seguinte forma: para um valor de entrada, a função deve sempre produzir o mesmo resultado. Você vai descobrir que algumas propriedades derivam dessa condição, mas por enquanto isso nos basta. Uma função que segue esse conceito é chamada de função pura.

Analise, a seguir, exemplos de funções puras.

Analise o exemplo de uma função pura abaixo.

def filtrar(lista, limiar):
  nova_lista = []
  for elemento in lista:
    if elemento > limiar:
      nova_lista.append(elemento)
  return nova_lista


A função filtrar, na primeira linha de código, possui dois valores de entrada: lista e limiar. Ela produz um valor de saída: nova_lista. Além disso, ela não gera nenhum efeito colateral. Isso mesmo, nenhuma variável externa é modificada ou acessada, não há chamadas à função print, nenhuma variável é descartada. Todo o escopo da função envolve ler parâmetros e retornar um valor. Essa é, por definição, uma função pura. Alguns defensores ortodoxos da Programação Funcional podem criticar alguns aspectos da nossa função filtrar, mas iremos refiná-la aos poucos ao longo desta aula. Tudo bem?

Abaixo, confira uma curiosidade sobre linguagens de programação que possuem características de mais de um paradigma de programação.

Ícone Saiba Mais
Ícone “Saiba Mais”.
As principais linguagens de programação modernas fornecem recursos de diferentes paradigmas de programação, ou seja, são multiparadigmas. É possível escrever um código em Python sem usar classes ou fazer um programa totalmente orientado a objetos, assim como aplicar somente funções da Programação Funcional. É até comum que códigos eficientes misturem esses conceitos e utilize cada um da melhor forma.

A seguir, analise exemplos de funções impuras.

Agora, confira exemplos de funções impuras e as razões pelas quais elas não se adequam à Programação Funcional. Analise o código a seguir:


a = 2
def soma(b):
  b = b + a
  return b
print(soma(1))

Essa função é considerada impura, porque ela não depende somente dos valores de entrada. A variável a, na primeira linha de código, está fora do escopo da função. Essa é uma violação de pureza da função. Além disso, o valor de a pode mudar durante a execução do programa, então se chamarmos soma(1) em outro momento, pode ser que ela retorne um valor diferente. Confira o outro código abaixo:

class A:
  atributo = 0

  def mudar_valor(self, x):
    self.atributo = x
objeto = A()
objeto.mudar_valor(5)
print(objeto.atributo)

O método mudar_valor, na quarta linha do código, é impuro porque modifica uma variável que não pertence ao escopo da função. A execução dessa função com o mesmo parâmetro irá sempre repetir o mesmo comportamento, mas ainda assim não é uma função pura.

Na próxima página, entenda como transformar uma função impura em uma função pura.

Para tornar a função soma definida anteriormente em uma função pura, você precisa fazer um simples ajuste. Basta adicionar a variável a como argumento da função. Conforme o código abaixo:

def soma(a, b):
  b = b + a
  return b
print(soma(2, 1))

No entanto, nem toda função é facilmente convertida. Não há como modificar o método mudar_valor de forma simples. Modificá-lo tornaria o código bem mais complexo do que precisa. Logo, códigos orientados a objetos dificilmente são códigos funcionais. Mas isso não é um problema. Cada paradigma tem suas devidas aplicações. A Programação Funcional é muito útil para trabalhar com grandes conjuntos de dados, pois faz um gerenciamento de memória inteligente. Essa é uma tarefa rotineira no contexto de Machine Learning. Logo, é comum usar técnicas da Programação Funcional.

A pureza de uma função garante que o sistema irá ter um comportamento consistente ao longo da aplicação. Isto é especialmente importante na Programação Funcional, pois nesse paradigma você deve modelar um problema através do uso de funções. Garantir que um problema será resolvido de forma consistente é exigir que as funções se comportem de maneira consistente. Ficou mais clara a necessidade de funções puras? Já os outros paradigmas, normalmente, são utilizados para controlar o estado das variáveis que o programa manipula. Na Programação Funcional será modelado um problema em si.

Além do conceito de função pura, você vai aprofundar seus conhecimentos em mais alguns conceitos utilizados na Programação Funcional que estão disponíveis em Python. Se deseja modelar um problema através de funções, precisa expandir as possibilidades de como trabalhamos com elas. Confira a seguir como funções são representadas como objetos em Python.

Você deve ter aprendido que uma variável, na linguagem Python, pode ter diferentes tipos: inteiro, ponto flutuante, booleano, lista, entre outros. Mas você sabia que uma variável também pode receber uma função? Exatamente! Uma função em Python pode ser tratada como qualquer outro objeto. Portanto, dizemos que ela é um objeto de primeira classe.

Confira o exemplo a seguir:

def soma(a, b):
  return a + b
f = soma
print(f(1, 2)) # Resultado é 3

Ao executar o código acima, você percebe que o resultado seria o mesmo de chamar a função soma(1, 2)? Ou seja, podemos nos referir à função soma por f no restante do código, sem nenhuma perda de informação. Ao inspecionar o tipo da variável f, você verá que o retorno é objeto da classe “function”, conforme o trecho abaixo:

print(type(f)) # <class ‘function’>

A seguir, entenda como passar uma função como argumento para outras funções.

Agora, você deve estar se perguntando, “Então, se uma função se comporta como uma variável em Python, quer dizer que posso criar funções que recebem outras funções como argumento?” E a resposta é sim! Com isso, é possível começar a criar aplicações mais complexas.

Por exemplo, você tem o seguinte problema: todo ano acontece a vacinação da gripe H1N1 e, por isso, todas as pessoas deveriam se vacinar. Contudo, há uma ordem de prioridade para tomar as vacinas: primeiro, os idosos acima de 75 anos; depois, idosos entre 60 e 74 anos; e, por último, as pessoas abaixo de 60 anos. Então, como criar uma função que receba como argumento uma lista de idades e retorne uma lista filtrada de acordo com a fase? Bem, já foi definida a função filtrar anteriormente, relembre-a abaixo.

def filtrar(lista, limiar):
  nova_lista = []
  for elemento in lista:
    if elemento > limiar:
      nova_lista.append(elemento)
  return nova_lista

Ela ainda não está pronta para resolver o problema proposto. Portanto, você poderia adicionar alguns if’s e else’s no código e outro limiar como argumento, não é mesmo? Mas isso vai tornar o código um pouco confuso e de difícil manutenção. Tente fazer esse exercício e você perceberá.

Adicionar comandos que resolvam o problema não parece ser a melhor abordagem inicialmente. O que você acha de tentar outra técnica?

Na próxima página, você entenderá como modelar esse problema utilizando funções.

Ao invés de começar a modificar a função filtrar, o primeiro passo é modelar o problema. As fases de vacinação atendem a certos critérios. Então, o ideal é criar uma função para cada fase que avalie se uma idade atende ao critério definido anteriormente.

Comece a construir a solução criando três funções: primeira_fase, segunda_fase e terceira_fase. Cada função recebe como argumento uma idade e retorna verdadeiro ou falso se aquela idade pertence àquela fase. Conforme os códigos a seguir:

def primeira_fase(idade):
  return idade >= 75
def segunda_fase(idade):
  return 60 <= idade <= 74
def terceira_fase(idade):
  return idade <= 59

O código é bem direto com relação aos critérios estabelecidos. Além disso, todas as funções são puras. Este é um requisito importante para o restante da solução. Agora, você pode perceber como utilizar essas funções em conjunto com a filtrar.

A seguir, você modificará a função filtrar para utilizar as funções definidas aqui.

Agora você pode modificar a função filtrar para, ao invés de receber um limiar, receber um argumento chamado critério, que avalia se a idade atual atende ou não ao requisito. E quais serão os valores passados para esse argumento? As funções que acabaram de ser definidas primeira_fase, segunda_fase e terceira_fase. Segue o código modificado.

def filtrar(lista, criterio):
  nova_lista = []
  for elemento in lista:
    if criterio(elemento):
      nova_lista.append(elemento)
  return nova_lista

Perceba que o argumento criterio é declarado normalmente como outro parâmetro. No entanto, na linha 4 ele é chamado como uma função e se comportará de acordo com a função passada como argumento. Você consegue perceber a versatilidade e poder desse código? Dessa forma, a função filtrar se tornou bem genérica. Agora é só criar o código que chamará essas funções para ver como tudo se comporta.

Abaixo, entenda um pouco sobre o uso do laço for em funções puras e uma alternativa a esse recurso de linguagem.

Normalmente, os códigos que seguem a Programação Funcional evitam o uso de laços de repetição, como utilizado na função filtrar. Ao invés disso, é utilizada a recursão para percorrer um conjunto de dados. Recursão é o ato de uma função retornar a si mesma. Ou seja, ao invés de uma função retornar um valor de saída, ela chamará a si novamente. Como a recursão é um conceito bem complexo e que causa confusão a muitos programadores, ela não será abordada neste curso. Mas vale a pena você pesquisar sobre o assunto, pois a recursão é uma ótima forma de modelar problemas do mundo real, especialmente matemáticos. Caso se interesse pelo assunto, pode acessar ao site Algoritmos em Python, neste link você poderá conferir mais sobre a recursão.
https://algoritmosempython.com.br/cursos/algoritmos-python/introducao/tipos-algoritmos/

Na próxima página, você aprenderá a aplicar a função, filtrar uma lista e conferir o resultado.


Inicialmente é preciso criar uma lista de idades e então dividir essas idades em primeiro, segundo e terceiro grupos. Cada grupo é criado a partir da chamada da função filtrar e de acordo com a respectiva fase. Note como ficou o código abaixo.

idades = [30, 45, 60, 72, 75, 99]
primeiro_grupo = filtrar(idades, primeira_fase)
segundo_grupo = filtrar(idades, segunda_fase)
terceiro_grupo = filtrar(idades, terceira_fase)
print(primeiro_grupo) # [75, 99]
print(segundo_grupo) # [60, 72]
print(terceiro_grupo) # [30, 45]

O código é bastante intuitivo, de fácil legibilidade e facilmente escalável. Ele é escalável, porque, caso surjam novas fases, por exemplo, quarta_fase, será necessário criar somente uma nova função e passar para filtrar como argumento. Sendo assim, não é mais preciso modificar internamente essa função.

Por último, mas não menos importante, filtrar continua sendo uma função pura. Ela não depende de nada além dos seus parâmetros e não produz nenhum resultado ao não ser a saída. Ah, também não produz efeitos colaterais.

Você percebe que modelar o problema através de funções e repassá-las como argumentos para outras transforma a leitura, deixando-a mais fácil? Esse mesmo problema poderia ser resolvido de formas mais procedurais, mas os códigos seriam mais confusos. Por isso, há problemas que se encaixam melhor no paradigma da Programação Funcional. Espero que ao final desta aula você aprenda melhor como identificar esses problemas.

A seguir, conheça uma curiosidade sobre funções puras disponíveis em Python.

Existem diversas funções no Python que recebem outras funções como argumentos. A função sorted, utilizada para ordenar um conjunto de dados, é um exemplo. É possível passar uma função que especifica como vai ser a ordenação dos elementos.

Em Python, é muito comum o uso de decoradores para passar uma função como argumento. No entanto, é um tópico extenso e que não é muito utilizado nas aplicações de Machine Learning. Apesar de não ser utilizado em Machine Learning, é importante que você entenda, pois é um recurso muito utilizado em códigos Python. Você pode encontrar códigos na internet que utilizam um decorador.

Caso queira aprofundar seus conhecimentos sobre esse assunto, você pode conferir o site Python Academy. Neste link, será possível conferir mais sobre decorador.

https://pythonacademy.com.br/blog/domine-decorators-em-python

Até aqui, você pôde compreender a importância da Programação Funcional, mas talvez ache trabalhoso o processo de criação de funções puras. Então, é preciso tomar cuidados extras e garantir a consistência de execução. Para a nossa sorte, em Python, já existem recursos funcionais para criarmos códigos mais legíveis, eficientes e escaláveis. A seguir, no próximo tópico, aprenda a como criar funções anônimas em Python que consigam expressar funções rápidas em apenas uma linha de código!

# Tópico 2 – Funções Anônimas

## OBJETIVOS
Conhecer funções anônimas em Python;
Aplicar as funções lambda;
Analisar casos de uso.

Bom, até agora você aprendeu conceitualmente como aplicar a Programação Funcional em um problema, certo? Para isso, primeiro, você teve de modelar a solução através de funções e passar estas como argumento para construir uma solução de mais alto nível. No entanto, como você pôde perceber, muitas vezes temos que definir funções muito curtas. Por exemplo, as funções primeira_fase, segunda_fase e terceira_fase. Não seria mais prático poder defini-las em uma linha somente quando necessário?

A partir dessa necessidade, você vai aprender a como utilizar funções anônimas em Python. Elas também podem ser chamadas de funções lambda ou expressões lambda. Estas funções são definidas sem nome e só utilizam uma linha de código. Elas são versáteis e práticas para utilizar quando precisar de uma única função simples e curta.

Ainda nesse tópico, conheça alguns casos de uso para que você consiga perceber melhor como pode aplicá-las usando todo o seu potencial.

Vamos lá?

As funções anônimas são aquelas que podem ser definidas em Python sem a necessidade de um nome. Isso mesmo, ao invés de você declarar def funcao(x), você pode utilizar a palavra-chave lambda. Por esta razão, elas também são denominadas funções lambda. Analise o exemplo abaixo. Perceba que primeiro foi declarado uma função que retorna o quadrado de um número.

def quadratica(x):
  return x*x

É uma função tão pequena, basicamente uma expressão, que seria mais cômodo usar somente a linha de retorno, não é mesmo? Por isso, podemos transformá-la em uma função lambda. Entenda como ficaria no trecho de código abaixo:

lambda x: x*x

Compreenda cada elemento, na linha de código acima.

A palavra "lambda” é a palavra chave que indica a criação de uma função de uma linha só;
Já o “x” é o argumento da função lambda;
O ":” indica o início do cálculo da função; e
Por fim, "x*x” é o cálculo da função lambda.
Você pode estar se perguntando, se lambda é uma função, cadê o seu retorno? Nas expressões lambda, o retorno ocorre de maneira implícita. Ou seja, o que você escrever do lado direito como cálculo da função sempre vai ser retornado.

Na próxima página, você terá outros exemplos de aplicação da função lambda.

Agora, será criado uma função lambda que retorna a soma de dois números:

lambda a,b: a+b

Perceba que você pode passar mais argumentos para a expressão, basta separar por vírgulas. Além disso, você pode passar argumentos de outros tipos para a função. Por exemplo, criar uma função que transforma somente o primeiro caractere de uma palavra em maiúsculo. Conforme o trecho abaixo:

lambda x: x[0].upper() + x[1:]

Agora você possivelmente deve estar se perguntando, “se uma função é anônima, como a chamamos?” Lembre-se de que funções comportam-se como qualquer outro tipo em Python, ou seja, você pode atribuí-las a variáveis. Confira o código a seguir:

f1 = lambda a,b: a+b
print(f1(1, 2))
f2 = lambda x: x[0].upper() + x[1:]
print(f2('olá mundo')) # 'Olá mundo’

Como pode ser percebido, é possível aplicar f1 e f2 em todo o código como funções normalmente. É uma vantagem poder declarar funções em somente uma linha, caso sejam curtas o suficiente. Só que a maior versatilidade das funções lambda é poder passá-las como argumentos para outras funções. Assim, os códigos tornam-se mais compactos e legíveis.

Na próxima página, continue aplicando a função lambda. Nesse caso, como argumento para a função filtrar previamente definida.

Relembre, agora, a solução que foi dada ao problema de separar uma lista de idades em diferentes grupos para vacinação. Podemos adaptar o código final para ter menos funções, utilizando a expressão lambda. Conforme o seguinte trecho:

idades = [30, 45, 60, 72, 75, 99]
primeiro_grupo = filtrar(idades, lambda x: x >= 75)
segundo_grupo = filtrar(idades, lambda x: 60 <= x <= 74)
terceiro_grupo = filtrar(idades, lambda x: x <= 59)
print(primeiro_grupo) # [75, 99]
print(segundo_grupo) # [60, 72]
print(terceiro_grupo) # [30, 45]

Percebe como o código se tornou menor? Além disso, é igualmente legível e completamente funcional.

A grande vantagem de utilizar expressões lambda é a facilidade em criar funções rapidamente sem a necessidade de quebra de fluxo. Ou seja, uma pessoa que estiver lendo o código vai entender tudo sem precisar ficar indo e voltando, procurando as definições das funções auxiliares. Interessante, não acha?

A seguir, analise como utilizar a expressão lambda com a função sorted do Python.

A função sorted já foi mencionada anteriormente nesta aula. Ela é uma função que ordena um grupo de elementos. Se eles forem números, serão ordenados do menor para o maior. Se forem palavras, serão ordenadas alfabeticamente. Confira as duas linhas abaixo:

print(sorted([20, 1, 5, 19, 6])) # [1, 5, 6, 19, 20]
print(sorted(['programacao', 'funcional', 'e', 'legal'])) # ['e', 'funcional', 'legal', 'programacao']

Suponha que você queira ordenar a lista de palavras pelo tamanho delas, ao invés de ser pela ordem alfabética. Como você faria isso? A função sorted tem um argumento chamado key. O argumento key recebe uma função que indica o critério pelo qual devemos ordenar. Se dissermos que o critério é o tamanho da palavra, então ele ordenará do menor tamanho ao maior tamanho. A expressão lambda é extremamente conveniente para isso. Analise o código a seguir:

print(sorted(['programacao', 'funcional', 'e', 'legal'], key=lambda x: len(x))) # ['e', 'legal', 'funcional', 'programacao']

Nestas situações em que uma função recebe uma outra função como argumento, a expressão lambda mostra o seu verdadeiro potencial. No entanto, elas possuem algumas limitações. A seguir, entenda sobre a restrição de estruturas complexas nas funções lambda.

As expressões lambda são práticas, entretanto só permitem uma única expressão no seu corpo. Isto quer dizer que não é possível usar estruturas como while, for, if ou else dentro delas. Essas restrições diminuem o campo de aplicações. Por isso, as funções lambda são usadas em caso de funções curtas e simples.

Existem diversas funções em Python já disponíveis em que podemos utilizar a função lambda da melhor maneira. Você poderá explorá-las no próximo tópico.

# Tópico 3 – Funções Puras em Python

## OBJETIVOS
Aplicar funções a estruturas de dados com map;
Aprender a filtrar elementos;
Analisar condições de pertencimento em conjuntos de dados.

Ao longo desta aula, você aprendeu que a Programação Funcional é especialmente aplicada para manipular e tratar os dados de maneira eficiente. Chegou o momento de você estudar funções disponíveis em Python que permitem fazer essas ações, utilizando os conceitos que aprendeu até aqui, incluindo as expressões lambda.

Você aprenderá a transformar dados rapidamente através da função map, conhecer a função filter do Python e descobrir mais duas funções, all e any, que analisam determinadas condições em um conjunto de elementos. Todas essas são funções puras e permitem modelar mais facilmente os problemas.

Curioso? Então continue aprendendo sobre esse assunto nas páginas seguintes.

Uma tarefa clássica na área de Machine Learning é o tratamento de dados. Isso significa limpar dados inválidos, arredondar valores numéricos ou aplicar alguma função matemática aos valores iniciais.

Vamos supor que você tem uma lista de números de ponto flutuante que representam anos. O número de anos deveria ser um número inteiro, então não faz sentido trabalhar com um número como 2.5 anos. Para converter um número x de ponto flutuante em inteiro, é só utilizar a função int(x). E para aplicar essa função em toda uma lista de uma vez, basta utilizar a função map.

A função map recebe dois argumentos: uma função e um conjunto de dados. Em seguida, ela aplica a função a cada elemento do conjunto de dados individualmente. Analise o seguinte, código:

anos = [1.5, 2.3, 5.0, 19.4]
anos_inteiros = map(int, anos)
for ano in anos_inteiros:
  print(ano)

Na linha 2, a função map recebe como argumentos a função int e a função anos. Então, ela converte individualmente cada valor de anos para inteiro.

Na próxima página, pratique o exercício proposto e perceba o poder da função map.

Sabendo que map aplica uma função a uma lista, um elemento por vez, pratique com os pares de parâmetros da tabela a seguir. Na tabela, há três colunas: a primeira é a função a ser aplicada, a segunda é a lista com os elementos a serem modificados e a terceira é a coluna de resultado que você deve preencher. Por exemplo, função = float, lista = [4, 5, 6], a resposta correta é [4.0, 5.0, 6.0]. Agora, é a sua vez! Preencha os outros valores da tabela.

Função	Lista	Resposta
int	[1.5, 2.0, 3.6]	[1, 2, 3] Resposta: [1, 2, 3]
float	[1, 2, 3]	[1.0, 2.0, 3.0] Resposta: [1.0, 2.0, 3.0]
str.upper	['amor', 'bola', 'casa']	['Amor', 'Bola', 'Casa'] Resposta: ['AMOR', 'BOLA', 'CASA']
str.lower	[‘Amor', ‘Bola’, ‘Casa']	['amor', 'bola', 'casa'] Resposta: ['amor', 'bola', 'casa']
len	[‘amor’, ‘baixinho’, ‘coração’]	[4, 8, 7] Resposta: [4, 8, 7]
lambda x: x * 2	[1, 2, 3]	[2, 4, 6] Resposta: [2, 4, 6]
lambda x: x+5	[1, 2, 3]	[6, 7, 8] Resposta: [6, 7, 8]
lambda x: x == 2	[1, 2, 3]	[False, True, False] Resposta: [False, True, False]

Agora que você praticou a função map com diversos exemplo, saiba mais sobre o retorno dessa função a seguir.

A função map retorna um iterador, ou seja, um elemento que representa uma sequência de elementos. Para converter o resultado automaticamente para uma lista, podemos usar o método list() no retorno da função.

Analise as aplicações de map com um seguinte exemplo. Você trabalha para a Netflix e quer analisar quantos filmes ruins, médios e bons há no catálogo. Porém, o seu chefe te deu somente uma média da avaliação dos usuários. Você pode começar a modelar o seu problema. Para isso, é importante definir a função que classifica um filme. Conforme o exemplo abaixo:

def categoria(nota):
  if nota < 5.0:
    return 'ruim'
  elif 5.0 <= nota <= 7.0:
    return 'médio'
  else:
    return 'bom’

É possível classificar filmes da seguinte maneira: filmes com nota menor que 5 são classificados como ruim; entre 5 e 7 são classificados como médio; e filmes com nota acima de 7 são classificados como bons.

Tendo isso em mente, confira na próxima página como resolver o problema proposto!

Bom, agora é necessário aplicar a função que foi criada à lista de dados chamada notas que o seu chefe lhe deu. Lembre-se de que, para aplicar a função categoria, definida anteriormente, a toda lista de uma vez, é preciso usar a função map. Além disso, para ter o resultado como lista, deve ser chamado o método list. Conforme o representado no código abaixo:

notas = [9.87, 3.15, 7.53, 6.17, 0.53, 9.55, 7.7, 1.88, 7.9, 6.01]
classificacao = list(map(categoria, notas))
print(classificacao) # ['bom', 'ruim', 'bom', 'médio', 'ruim', 'bom', 'bom', 'ruim', 'bom', 'médio']

Muito bem! Você já tem a classificação dos filmes de acordo com as notas. Agora, que tal dividir esse resultado em grupos? Nesse caso, é necessário criar três grupos. Desse modo, você conseguirá contar o tamanho de cada grupo. O que acha?

Para isso, você poderia utilizar a função filtrar, lembra-se dela? Só que já existe uma função para isso no Python: função filter. Ela se comporta exatamente como essa função apresentada anteriormente, e ela só não foi apresentada antes porque era mais interessante aprender como ela funciona do que somente aplicá-la. Mas, a partir de agora, você pode começar a trabalhar com a função filter. Certo?!

A seguir, você entenderá como aplicar a função filter a esse exemplo.

A função filter recebe dois argumentos, o primeiro é a função que você quer utilizar como critério de filtragem e a segunda é o conjunto de dados. Ela também retorna um iterador, portanto precisamos utilizar o método list para obter uma lista como retorno. Abaixo, confira um exemplo básico da função filter antes de aplicá-la ao problema. Serão filtrados somente valores maiores que 5, de uma lista utilizando a expressão lambda:

filter(lambda x: x > 5, [2, 4, 6, 8, 10]) # [6, 8, 10]

Percebe como ela funciona que nem a outra função filtrar? Então, agora é só aplicá-la ao problema de avaliação das notas da Netflix. Queremos criar três grupos de filmes, um cuja nota é igual a ruim; um cujo a nota é igual a médio; e um cujo a nota igual a bom. Para isso, pode ser chamada a função filter três vezes e utilizar funções lambda para cada caso. Analise o código abaixo:

filmes_ruins = list(filter(lambda x: x == 'ruim', classificacao))
filmes_medios = list(filter(lambda x: x == 'médio', classificacao))
filmes_bons = list(filter(lambda x: x == 'bom', classificacao))

Consegue perceber como foi fácil? Se contar todas as linhas de código escritas até aqui, em treze linhas, você conseguiu classificar os filmes em três categorias e dividir em três grupos. Agora, para saber o tamanho de cada grupo, é só chamar a função len, conforme a linha abaixo:

print(len(filmes_ruins), len(filmes_medios), len(filmes_bons)) # 3 2 5

A lista de filmes passadas pelo seu chefe tem 3 filmes ruins, 2 filmes médios e 5 filmes bons! Você pode dar a boa notícia de que há mais filmes bons no seu catálogo do que ruins! Agora, e se ele lhe passar uma nova lista de filmes e perguntar a você: “existe algum filme ruim no meio? Todas as notas são boas?”

Saiba o que fazer para resolver esse novo problema na próxima página!

Você poderia repetir os mesmos passos de antes e obter as respostas. Mas existem duas funções auxiliares para isso em Python que podem reduzir o seu trabalho. São as funções any e all. Conheça melhor cada uma delas agora.

A função all recebe uma estrutura de dados como argumento e retorna verdadeiro se todos os valores são verdadeiros. Acompanhe os exemplos abaixo:

valores_verdadeiros = [True, True, True]
valores_mistos = [True, False, True]
print(all(valores_verdadeiros)) # True
print(all(valores_mistos)) # False

No primeiro caso, todos os elementos da lista são True; e no segundo caso, existe um elemento False no meio. Portanto, a função all só retorna True para a primeira lista.

De maneira similar, a função any recebe uma estrutura de dados como argumento e retorna verdadeiro se, pelo menos, um elemento da lista for verdadeiro. E retorna falso se todos são falsos, conforme o representado no código a seguir:

valores_mistos = [False, False, True]
valores_falsos = [False, False, False]
print(any(valores_mistos)) # True
print(any(valores_falsos)) # False

No primeiro caso, existe um elemento True na lista, no segundo caso, todos são falsos. Portanto, a função any só retorna True para a primeira lista.

Na próxima página, você entenderá como utilizar as funções any e all no exemplo.

Agora, entenda como utilizar as funções any e all para as perguntas do seu chefe. Primeiro, relembre todos os pedidos dele. Dada uma lista de filmes, ele deseja saber se existe algum filme ruim no meio e saber se todas as notas são boas, não é isso? Então, você irá trabalhar com a nova lista de filmes já classificados abaixo:

novas_categorias = ['bom', 'bom', 'bom', 'ruim', 'bom']

cê pode estar se perguntando: mas as funções any e all não aceitam somente valores True ou False como entrada? Exatamente, mas você estudou há pouco uma função que mapeia um conjunto de valores em outro. A map! Pode utilizá-la novamente neste problema. Primeiro, utilize-a para comparar a nota de cada filme com a avaliação ‘ruim’. Para fazer essa comparação, basta usar uma expressão lambda. Conforme o trecho a seguir:

filmes_ruins_booleano = list(map(lambda x: x == 'ruim', novas_categorias))
print(filmes_ruins_booleano) # [False, False, False, True, False]

Nesse ponto, você terá uma lista de valores booleanos. Seu interesse é saber se existe pelo menos um valor True nessa lista. Portanto, utilize a função any conforme a linha a seguir:

print(any(filmes_ruins_booleano)) # True

Para a tristeza do seu chefe, existe sim filmes ruins nas novas notas. Mas para a sua alegria, o código é bastante legível! Você conseguiu resolver o problema utilizando map e any com poucas linhas, além de ser fácil de explicar para outra pessoa o que cada trecho de código está fazendo.

Na próxima página, você entenderá como responder a outra pergunta do seu chefe.

De maneira parecida, você deve utilizar a função map para comparar se as classificações são iguais a ‘bom’. De acordo com o trecho abaixo:

filmes_bons_booleano = list(map(lambda x: x == 'bom', novas_categorias))
print(filmes_bons_booleano) # [True, True, True, False, True]

Agora, utilize a função all para saber se todos os valores de filmes_bons_booleano são verdadeiros.

print(all(filmes_bons_booleano)) # False

Como você pode notar, novamente seu chefe não ficará feliz com a resposta. No entanto, você conseguiu responder de maneira rápida e com um código que até ele poderá entender! Esse é o poder de alguém que trabalha com análise de dados. É saber pegar um conjunto de valores e, rapidamente, extrair informações. Através das funções auxiliares em Python você consegue manipular rapidamente as informações, transformando um conjunto de valores em outros mais sintéticos, agrupando de acordo com algum critério claro.

Conseguiu compreender todos os passos até aqui? Refaça os passos desse tópico, se possível. A partir de agora, você será capaz de unir todos os conceitos de Programação Funcional, Expressões lambda e funções disponíveis em Python para criar uma aplicação útil em Python que simula um cenário da vida real.

Nessa aula você aprendeu sobre Programação Funcional e entendeu como usá-la em Python! Além disso, foi ensinado como criar funções puras e percebeu como modelar problemas através de funções pode tornar a solução muito mais fácil. Depois, você conheceu funções disponíveis que permitem manipular facilmente os conjuntos de dados para fazer análises rápidas.

Existem pessoas que trabalham todos os dias analisando notas de filmes, músicas e vídeos e gerando análises parecidas com as que você aprendeu nesta aula. Você está no caminho que todo cientista de dados percorre ao aprender Machine Learning!

Nas próximas aulas, você conhecerá mais recursos da linguagem Python. Diversas funções já disponíveis que permitem tratar datas, operações matemáticas e outras estruturas de dados. Além de poder abrir e salvar arquivos na memória do seu computador.

Não se esqueça de resolver as atividades propostas, revisitar os conteúdos desta aula e aprofundar seus conhecimentos.

Bons estudos e até mais!



# Glossário
Para conhecer o significado dos termos técnicos estudados em nossa aula, selecione a palavra desejada.

Expressão lambda
Conceito:
Sinônimo de função anônima.

Função anônima
Conceito:
Uma função sem nome que permite uma única expressão em Python.

Função pura
Conceito:
Função que respeita os paradigmas da Programação Funcional.
