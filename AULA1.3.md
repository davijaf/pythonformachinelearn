# Introdução

Olá!
Você, certamente, utiliza datas no seu cotidiano para lembrar do aniversário de uma pessoa querida, da estreia de uma série ou de um curso, dentre outras ocasiões, não é mesmo? Existem muitas aplicações do mundo real que exigem a manipulação de datas e horas, como é o caso de situações de Machine Learning.

A exemplo disso, suponha que você queira acompanhar como o uso da rede social Instagram mudou ao longo do tempo, conferir a variação de renda da família brasileira durante a última década ou até analisar a audiência por semana de um reality show. Então, vem a questão: como trabalhar com datas em um programa Python?

Nesta aula, você vai aprender a como criar datas, comparar uma com a outra, identificar qual é mais antiga e, ainda, manipular informação de dias.

Bons estudos!

## Objetivos

Escrever datas em Python;
Manipular informações de datas;
Converter datas em strings e vice-versa.

# Tópico 1 – Conhecendo o Módulo Datetime

## OBJETIVOS

Utilizar o pacote datetime;
Definir os tipos date e datetime;
Alterar datas com timedelta.

Existem diversos módulos em Python que manipulam informações de datas, horas e calendário, cada qual com sua funcionalidade específica. Aqui você vai conhecer apenas os módulos essenciais, começando pelo datetime.

Esse módulo permite que você atribua datas a variáveis e as manipule normalmente. Assim, é possível passar datas como argumentos para funções, compará-las, adicionar ou subtrair.

Para realizar essas operações, o módulo cria dois tipos, chamados de date e datetime, que são variações de tipos de dados. Cada tipo tem o seu contexto adequado. Ao fim desta aula, você saberá quando usar cada um deles. Além disso, você aprenderá a transformar datas em strings, extraindo somente a informação que você quer. Por exemplo, poderá escolher entre mostrar 01/01/2021 ou mostrar 01 de janeiro de 2021. Com isso, você poderá criar aplicações mais personalizadas, exibindo somente as informações essenciais ao contexto. A escolha será sua.

Durante os exemplos desta aula, será levada em consideração a data referente ao dia 14/05/2021. Considere essa data como exemplo nos códigos durante o restante do conteúdo.

Vamos começar do mais básico, importando o tipo date do módulo datetime. Essa classe é útil para representar objetos que você quer trabalhar com datas. Confira o código a seguir que mostra como importar o módulo datetime e imprimir o tipo date.

from datetime import date
print(date) # class 'datetime.date'>
Quando nos referimos à data, isso envolve três informações importantes: dia, mês e ano. Por exemplo, considere que a data de hoje é 14/05/2021. Para representá-la usando a classe date, fazemos da seguinte forma:

hoje = date.today()
print(hoje) # 2021-05-14
Figura 1 – O módulo datetime fornece as classes para manipulação de datas e horas

A data aparece de uma forma diferente, não acha? Nesse formato, ela é exibida por ano-mês-dia. Você deve estar acostumado com o formato dia/mês/ano. No entanto, é fácil modificar de um formato para outro em Python. Você conhecerá como fazer isso mais adiante.

A seguir, confira como declarar uma variável do tipo date passando, como argumentos, dados fornecidos por você.

Embora seja útil saber o dia de hoje, você pode querer definir suas próprias datas. Por exemplo, confira o código a seguir que declara uma variável do dia 1º de janeiro de 2021:

dia_primeiro = date(2021, 1, 1)
print(dia_primeiro) # 2021-01-01
Ao declarar uma variável, atribuímos um objeto do tipo date passando três argumentos: ano, mês e dia. Todos os parâmetros são obrigatórios e devem ser passados obrigatoriamente nessa ordem. Esses valores podem ser acessados pelos atributos year, month e day, respectivamente, como exibido neste código: função filtrar, mas iremos refiná-la aos poucos ao longo desta aula. Tudo bem?

print(dia_primeiro.year) # 2021
print(dia_primeiro.month) # 1
print(dia_primeiro.day) # 1
Os valores para o parâmetro de ano devem ser números inteiros positivos, portanto, não dá para representar anos antes de Cristo utilizando o módulo datetime. Para os valores de meses, deve-se utilizar somente os valores de 1 a 12, devido ao número de meses. Os valores de dias só aceitam valores entre 1 e 31. Caso você passe algum valor fora deste intervalo, ou algum valor sem sentido, por exemplo, “30 de fevereiro”, o programa irá disparar uma exceção do tipo ValueError. Então, procure utilizar valores que façam sentido no contexto de datas.

Você sabe por que quando se escreve print (dia_primeiro), a data é exibida primeiro pelo ano? Descubra o porquê no boxe a seguir.

Ícone Você sabia?
Ícone “Você Sabia”.
O formato de exibição das datas estudado até agora é chamado ISO 8601 e é um padrão internacional de exibição de datas. Nesse padrão, os elementos de datas e horas são exibidos do mais significativo para o menos significativo. Por exemplo: ano-mês-dia e hora-minuto-segundo. Pode parecer curioso agora, mas é muito fácil de organizar arquivos e informações seguindo esse formato.

Por exemplo, suponha que você gosta bastante de cinema e quer organizar a lista de filmes que você já assistiu em ordem cronológica. É mais fácil organizar, primeiro, por ano, mês e, depois, por dia. Funcionaria da seguinte forma: uma pasta com filmes de 2021, e dentro as pastas: janeiro, fevereiro, março, abril e maio. Com isso, dentro de cada pasta de mês, você dividiria por dia. Assim, quando fosse procurar os filmes de uma data específica posteriormente, poderia achá-lo mais rápido.

Quando se faz análises de dados ao longo do tempo, também chamadas de análises temporais, é importante definir intervalos de tempo. Dessa forma, você define uma data inicial e uma data final e trabalha com as informações nesse intervalo. Um exemplo de aplicação seria verificar o estado de seca no Brasil em 2021.

Suponha que você tem a informação de dias que choveram em 2021 e quer calcular tendências de seca ou cheia. Nesse caso, é interessante trabalhar com pequenos intervalos de tempo, de semanas ou até de um mês. Para trabalhar com intervalos de datas, é importante saber como comparar uma data com outra e dizer qual é a maior ou a menor.

Para aprender sobre operações de comparação com datas, você precisa definir uma data inicial e uma data final de um período de tempo. Com esse intuito, vamos trabalhar outro exemplo, com as datas de início e fim do BBB 21. O programa começou em 25 de janeiro de 2021 e terminou em 04 de maio de 2021. Confira o código a seguir, que cria os objetos date com as respectivas datas citadas:

data_inicio = date(2021, 1, 25)
data_fim = date(2021, 5, 4)
print(f"O BBB 21 iniciou em {data_inicio} e terminou em {data_fim}") # O BBB 21 iniciou em 2021-01-25 e terminou em 2021-05-04
Você pode comparar as duas datas utilizando os operadores ==, !=, < e >. Você sabe o que os dois primeiros operadores fazem? O primeiro operador irá retornar verdadeiro se as datas forem iguais, ou seja, quando os anos, os meses e os dias forem exatamente iguais. Enquanto o segundo operador retornará verdadeiro se as datas forem diferentes. Agora o que fazem os operadores ‘<‘ e ‘>’, ou melhor, o que seria uma data menor ou maior que outra? A ordem de precedência é a regra que define como as datas são ordenadas, ou seja, a regra que diz quando uma data é menor ou maior do que outra.

Um objeto A do tipo date é considerado menor que outro objeto B do tipo date quando A precede B. Mas, afinal, o que isso significa? Lembrando o nosso exemplo, data_inicio e data_fim.,a data_inicio acontecem antes de data_fim? Se sim, então dizemos que data_inicio precede data_fim. Sendo assim, seguindo essa definição, data_inicio é menor que data_fim, correto? Vamos testar na próxima página.

Confira estas linhas:

print(data_inicio < data_fim) # True
print(data_inicio > data_fim) # False
Por meio desse exemplo, você pode notar que o nosso raciocínio se provou correto. Então, agora, você sabe comparar datas e informar qual é a menor. Assim, ao se trabalhar em um intervalo de tempo, é possível saber se uma data pertence a esse intervalo ou não.

Além de realizar comparações, você sabia que pode subtrair uma data da outra? Por exemplo, você quer saber qual foi a duração do BBB 21 a partir da data de início e da data final. Para isso, basta subtrair as duas datas, correto? Podemos fazer isso em Python da seguinte forma:

diferenca_dias = data_fim - data_inicio
print(diferenca_dias) # 99 days, 0:00:00
Vamos refletir um pouco sobre o que ocorreu nesse exemplo. Por que o print da variável diferenca_dias escreveu “99 days, 0:00:00”? Como você imaginou que deveria ser o tipo da variável? Pode-se deduzir que o resultado é um objeto que armazena a informação de 99 dias e informações zeradas de hora, aparentemente. A variável diferenca_dias é do tipo timedelta. Este é um tipo auxiliar, do módulo datetime, que permite armazenar informação de diferença entre datas e horas. Confirme isso com o código a seguir, que imprime o tipo da variável diferenca_dias:

print(type(diferenca_dias)) # <class 'datetime.timedelta'>
Perceba que, realmente, estamos lidando com um objeto do tipo timedelta, e não mais date. Isso significa que sempre que uma data for subtraída de outra, o resultado será um objeto do tipo timedelta, e não mais do tipo date. Entendido? Na próxima página, confira como os dias podem ser negativos em um timedelta.

Perceba que, se você fizer data_inicio - data_fim, o resultado será um timedelta com o atributo days = -99. Ou seja, um valor de dias negativos. Parece não fazer sentido, não é? Pense como se fossem números inteiros. Em outras palavras, se você subtrair um valor menor por um valor maior, o resultado será negativo. Portanto, para objetos do tipo timedelta, onde o atributo days tem valor negativo, é indicado a subtração de uma data mais antiga por uma data mais nova.

O objeto timedelta não tem muitos métodos, então, iremos usá-lo mais como um auxílio para as nossas operações. No entanto, ele possui um atributo chamado “days”, que é a quantidade de dias de diferença entre duas datas, que é do tipo inteiro. Agora podemos corrigir nosso print da diferença dos dias, para mostrar somente essa informação.

Além disso, tem um erro no nosso cálculo. A duração de dias entre uma data d1 e uma data d2 é: (d2 - d1) + 1. Lembre-se de somar sempre 1 para calcular a duração de um intervalo de tempo, ok? O código corrigido fica da seguinte forma:

diferenca_dias = data_fim - data_inicio
duracao = diferenca_dias.days + 1
print(f"A duração do BBB 21 foi de {duracao} dias") # A duração do BBB 21 foi de 100 dias
Pratique mais com timedelta na página seguinte.

Perceba que não é uma coisa de outro mundo pensar em diminuir uma data de outra, pois com esse cálculo se obtém o intervalo de dias entre as duas. Contudo, o que não faz sentido é somar duas datas.

Por outro lado, é normal somar uma data e uma quantidade de dias. Um exemplo de aplicação da vida real é o esquema de vacinação da Covid-19. As vacinas adotadas no Brasil necessitam de uma segunda dose para que o processo de imunização esteja completo. A vacina Coronavac, desenvolvida pelo Instituto Butantã, define um intervalo de 28 dias entre a primeira e a segunda dose. Considerando que você tomou a primeira dose no dia 14/05/2021, que data será daqui a 28 dias para o reforço da segunda dose? Para descobrir, basta usar date e timedelta. Para esse caso, também é preciso importar o módulo timedelta, conforme o código mostrado a seguir:

from datetime import date, timedelta
hoje = date(2021, 5, 14)
intervalo_dias = timedelta(days=28)
dia_futuro = hoje + intervalo_dias
print(f"Daqui a 28 dias será {dia_futuro}") # Daqui a 28 dias será 2021-06-11
Analisando o código na linha 4, é declarado um objeto do tipo timedelta, passando como argumento o valor 28, que é o número de dias do intervalo. Agora, você sabe que daqui a 28 dias será 06 de junho de 2021. No caso da vacina Astrazeneca, o intervalo é de 12 semanas entre as duas doses. Você pode calcular o dia da segunda dose trocando o argumento days por weeks e passando como argumento o valor 12. Ao testar, você terá como resultado o dia 06 de agosto de 2021.

Vamos criar outras aplicações agora. Suponha que você tenha uma lista de datas de eventos e quer ordená-las cronologicamente a partir da primeira que ocorreu. Você pode usar simplesmente o método sorted, correto? Confira o seguinte código:

atas = [date(2016, 7, 6), date(2012, 10, 24), date(2020, 3, 19), date(2021, 8, 24), date(2021, 8, 12), date(2013, 5, 29), date(2018, 9, 2), date(2019, 1, 19), date(2012, 7, 2), date(2018, 9, 5)]
print(sorted(datas)) # [datetime.date(2012, 7, 2), datetime.date(2012, 10, 24), datetime.date(2013, 5, 29), datetime.date(2016, 7, 6), datetime.date(2018, 9, 2), datetime.date(2018, 9, 5), datetime.date(2019, 1, 19), datetime.date(2020, 3, 19), datetime.date(2021, 8, 12), datetime.date(2021, 8, 24)]
Perceba que o resultado é uma lista de datas ordenadas de forma crescente pelo ano, depois pelo mês e, por fim, pelo dia. Bem padrão, certo? Só que você decidiu que quer ordenar de acordo com o mês. Primeiro, todas as datas de janeiro, depois fevereiro e assim por diante. Como você faria? Lembre-se de que, na aula de Programação Funcional, você aprendeu que o método sorted pode receber o argumento key. Então, você pode utilizar uma função lambda que retorna somente o atributo month das datas para o argumento key. Nesse caso, o método sorted irá ordenar levando em consideração somente os meses das datas. Confira o código a seguir, que ordena as datas passando o atributo month para o argumento key da função sorted:

print(sorted(datas, key=lambda d: d.month)) # [datetime.date(2019, 1, 19), datetime.date(2020, 3, 19), datetime.date(2013, 5, 29), datetime.date(2016, 7, 6), datetime.date(2012, 7, 2), datetime.date(2021, 8, 24), datetime.date(2021, 8, 12), datetime.date(2018, 9, 2), datetime.date(2018, 9, 5), datetime.date(2012, 10, 24)]
Você consegue perceber que as datas estão ordenadas pelo mês? Tente ordená-las pelo dia agora. Basta trocar o atributo month pelo day na função lambda.

É recomendável exercitar também a passagem da informação de ‘dia’ junto à informação de ‘mês’ para a função lambda e ordenar os objetos date por dois atributos ao mesmo tempo. Confira como fazer isso na próxima página.

Você percebeu que nos exemplos da ordenação por meses a ordem dos dias e a dos anos estão meio embaralhadas? Isso acontece porque a função sorted é considerada estável. Você sabe o que isso significa?

Bom, um método de ordenação estável preserva a ordem dos elementos de acordo com a lista original caso eles empatem no critério de ordenação. Na lista original, date(2016, 7, 6) veio antes de date(2012, 7, 2). Como o critério de ordenação é o mês, eles estão empatados. Então, a ordem na lista final se mantém a mesma.

Agora, como você acha que podemos fazer para ordenar por dia e por mês ao mesmo tempo? É simples: basta modificar a função lambda de forma a considerar os dois atributos ao invés de só um. Observe isso no código a seguir:

print(sorted(datas, key=lambda d: (d.month, d.day))) # [datetime.date(2019, 1, 19), datetime.date(2020, 3, 19), datetime.date(2013, 5, 29), datetime.date(2012, 7, 2), datetime.date(2016, 7, 6), datetime.date(2021, 8, 12), datetime.date(2021, 8, 24), datetime.date(2018, 9, 2), datetime.date(2018, 9, 5), datetime.date(2012, 10, 24)]
Nos casos em que há empate nos meses, o dia também é levado em consideração e vice-versa. Contudo, ainda é possível ordenar passando o ano, o mês e o dia para a função lambda, mas isso é o mesmo que ordenar da forma padrão. Ou seja, fazer esse cálculo seria mais complexo para produzir o mesmo resultado.

A seguir, conheça como trabalhar com informações de data e hora usando o tipo datetime.

Apenas a informação de data é insuficiente para os problemas do dia a dia, como um alarme personalizado por dia, em que a hora de despertar muda dos dias da semana para o fim de semana. Uma aplicação de calendário que salva eventos por dia e hora também precisa de informações extras.

No contexto de Machine Learning, podemos citar o problema para calcular o horário que os stories do Instagram são mais populares, de modo a direcionar seu algoritmo de divulgação. Ter somente os dias da semana e do mês em um objeto date não permite extrair essa informação mais detalhada. Em todos esses casos, você também deve salvar eventos por ‘hora’.

Vamos estudar agora o tipo datetime que, além de armazenar datas, como a classe date, armazena a hora. Vamos começar com a importação dele no código:

from datetime import datetime
Os nomes são iguais, mas o primeiro datetime refere-se ao módulo e o segundo à classe.

Vamos trabalhar com este exemplo: que horas são na sua cidade? Você pode utilizar o método now para descobrir:

hora_atual = datetime.now()
print(hora_atual) # 2021-05-14 21:07:34.264714
Confira a explicação desse código na página seguinte.

Vamos analisar esta primeira linha: hora_atual = datetime.now(). Ela retorna a data e a hora atual do computador, sendo a hora armazenada na variável hora_atual.

Já nesta segunda linha: print(hora_atual) # 2021-05-14 21:07:34.264714, há o print com o resultado dessa variável. Essa data e hora podem parecer menos usuais pelo fato de que, normalmente, estamos acostumados a ler dia/mês/ano e hora:minuto. Mas agora vamos destrinchar esse formato incomum.

A data vem no formato ano-mês-dia, ou seja, hoje, por exemplo, é dia 14 de maio de 2021. Em seguida, temos as informações das horas: são 21 horas, 7 minutos, 34 segundos e 264714 microsegundos. Como você pode notar, são informações bem específicas, não é mesmo? Talvez você não precise de tantos detalhes nesse momento, mas há aplicações em que um milésimo de segundo faz a diferença.

O objeto datetime se comporta de forma muito similar ao objeto date. Para declarar uma variável desse tipo, precisamos, primeiro, passar os argumentos obrigatórios, como ano, mês e dia, depois podemos passar os opcionais, como hora, minuto, segundo e microssegundo. Confira os seguintes exemplos que mostram objetos datetime sendo criados com diferentes atributos como parâmetros.

d1 = datetime(2021, 5, 15, 18, 1, 59, 123456)
d2 = datetime(2021, 5, 15, 18, 1, 59)
d3 = datetime(2021, 5, 15, 18, 1)
d4 = datetime(2021, 5, 15, 18)
d5 = datetime(2021, 5, 15)
print(d1, d2, d3, d4, d5) # 2021-05-15 18:01:59.123456 2021-05-15 18:01:59 2021-05-15 18:01:00 2021-05-15 18:00:00 2021-05-15 00:00:00
Perceba que a cada variável de tempo que não é preenchida, a informação correspondente recebe o valor de zero. Se não passarmos qualquer informação de hora, a variável representa o início do dia à meia-noite. Pratique a criação de um objeto datetime na próxima página.

Além das informações de ano, mês e dia, um objeto datetime possui os atributos de hora, minuto, segundo e microssegundo, como exibido neste código:

print(d1.hour, d1.minute, d1.second, d1.microsecond) # 18 1 59 123456
Além disso, você pode querer saber qual é o dia da semana de uma data, como em um alarme. Nos aplicativos de alarme encontrados nos smartphones hoje em dia, é possível configurar em quais dias um alarme vai tocar. Nesse contexto, é importante que a aplicação verifique sempre se o dia atual coincide com o dia definido no alarme. Para isso, você pode utilizar duas funções: weekday e isoweekday. A diferença é que os valores da primeira função vão de 0 a 6, e os da segunda função variam entre 1 e 7.

Comentamos, anteriormente, sobre o padrão ISO 8601. Nesse padrão, e em muitos países da Europa, a semana começa na segunda-feira e termina no domingo. As duas funções seguem essa norma para a contagem dos dias da semana. Confira o código a seguir, que mostra um exemplo de aplicação das funções weekday e isoweekday:

dia_primeiro = datetime(2021, 1, 1)
print(dia_primeiro.weekday(), dia_primeiro.isoweekday()) # 4 5
print(f"01 de Janeiro de 2021 é o dia {dia_primeiro.weekday()}, logo uma sexta-feira") # 01 de Janeiro de 2021 é o dia 4, logo uma sexta-feira
Note a diferença de valores entre as funções e no nosso exemplo, weekday retorna 4, ou seja, considerando segunda-feira como dia 0, sexta-feira possui valor 4. Os métodos weekday e isoweekday também estão presentes na classe date. Na página seguinte, inicie o desenvolvimento de uma aplicação que utiliza esses métodos. Vamos lá!

Aprenda ainda mais sobre como aplicar o datetime com a seguinte aplicação: suponha que você gosta muito de estudar Python e decidiu colocar seus conhecimentos de datas e horas em prática. Então, você vai criar um programa que toca um alarme às 20:30h e um depois de 30 segundos. Só que você lembrou que tem um compromisso às terças e quintas. Portanto, você deve mudar a hora do alarme para às 21:30h. Como criar esse programa?

Vamos começar de forma simples! Primeiro, você deve criar a data inicial da segunda-feira. Neste exemplo, usaremos o dia 24/05/2021 como início da semana. Confira:

inicio = datetime(2021, 5, 24, 20, 30)
Perceba que o datetime já foi inicializado com a hora certa do alarme. Agora, vamos criar uma lista de datas da semana, calculando os próximos dias. Podemos utilizar um timedelta para isso. Para não escrever manualmente, tente colocar dentro de um “for”, o que acha? O código a seguir cria os dias da semana a partir da data de início utilizando um laço for, observe:

semana = [inicio]
for i in range(1, 7):
  dia_seguinte = inicio + timedelta(days=i)
  semana.append(dia_seguinte)
print(semana) # [datetime.datetime(2021, 5, 24, 20, 30), datetime.datetime(2021, 5, 25, 20, 30), datetime.datetime(2021, 5, 26, 20, 30), datetime.datetime(2021, 5, 27, 20, 30), datetime.datetime(2021, 5, 28, 20, 30), datetime.datetime(2021, 5, 29, 20, 30), datetime.datetime(2021, 5, 30, 20, 30)]
print(len(semana)) # 7
Pronto, a lista de dias da semana foi criada. O primeiro dia é referente à segunda-feira, dia 24, e o último dia é o domingo, dia 30 de maio. Além disso, observe que a lista possui 7 dias. Depois, é preciso modificar as horas dos dias 25 e 28, pois eles correspondem à terça-feira e à quinta-feira, respectivamente. Daria para fazer isso manualmente, mas, para evitar cometer algum deslize, como errar o número do índice, vamos tentar de outra forma. Que tal modelar esse problema com funções? Observe a seguir.

Vamos utilizar a abordagem da Programação Funcional para este caso. Você criará uma função que recebe um datetime como argumento e verifica qual o dia da semana. Caso seja um dia de terça-feira ou quinta-feira, retornamos um novo objeto datetime como o valor de hora igual a 21. Caso contrário, retornamos o mesmo argumento de entrada. Confira como fica o código desta função chamada de muda_horário:

def muda_horario(dia):
  if dia.weekday() == 1 or dia.weekday() == 3:
    return dia.replace(hour=21)
  else:
    return dia
No exemplo, foi utilizado um método da classe datetime, chamado replace. Este método retorna um novo objeto, mudando os valores dos argumentos que passamos. Nesse caso, precisamos mudar o valor da hora para 21. Então, um novo objeto é criado, possuindo todos os atributos iguais aos da variável dia, exceto o atributo de hora.

Agora é preciso aplicar a função muda_horario para a lista de dias da semana. Lembra como aplicamos uma função a todos os elementos de lista de uma vez só? Utilizando a função map, como no código seguinte:

semana_atualizada = list(map(muda_horario, semana))
print(semana_atualizada) # [datetime.datetime(2021, 5, 24, 20, 30), datetime.datetime(2021, 5, 25, 21, 30), datetime.datetime(2021, 5, 26, 20, 30), datetime.datetime(2021, 5, 27, 21, 30), datetime.datetime(2021, 5, 28, 20, 30), datetime.datetime(2021, 5, 29, 20, 30), datetime.datetime(2021, 5, 30, 20, 30)]
Com a execução desse código, você tem agora a lista de horários atualizada de acordo com seus compromissos. Caso você queira mudar os dias ou a hora do alarme, é só atualizar a função muda_horário.

Suponha que você tem um amigo que mora nos Estados Unidos e que quer estudar Python com você. O problema é que quando for 20:30h na sua cidade, será outro horário para ele, devido ao fuso horário. Conheça, na próxima página, as opções que o módulo datetime fornece para trabalhar com fuso horário.

O módulo datetime fornece duas classes para lidar com os fusos horários. A primeira é a classe base abstrata tzinfo para armazenamento e configuração de detalhes de fuso horário. Por ser uma classe abstrata, não é possível criar objetos diretamente dela. É preciso criar subclasses, certo?

Você pode criar a sua própria subclasse ou utilizar a timezone também fornecida no módulo datetime. Esta timezone utiliza os padrões de fusos horários que conhecemos a partir de uma diferença fixa para o Tempo Universal Coordenado ou UTC. O objeto datetime possui um atributo tzinfo para atribuições de fuso horário das subclasses da tzinfo. Uma definição curiosa: objetos que utilizam informação de fusos horários são chamados de conscientes e os que não utilizam são chamados de ingênuos.

Além dessa, há uma classe no módulo datetime chamada time. Essa classe armazena somente as informações de tempo, como horas, minutos, segundos e microssegundos. Além desses, também possui um atributo tzinfo, que funciona de forma similar ao atributo tzinfo do tipo datetime. Você deve ter percebido que a classe time contém atributos similares ao datetime. É porque a classe datetime é uma combinação da classe date e da classe time em uma só.

Nessa aula procuramos dar um enfoque mais prático para os tipos de cenários mais encontrados em aplicações de Machine Learning. Por isso, foram apresentadas mais aplicações com as classes date, datetime e timedelta. No entanto, sinta-se à vontade para ler a documentação oficial do módulo datetime e estudar mais sobre os outros tipos de classes e métodos existentes nesse tão importante módulo da linguagem Python. Confira a documentação oficial no link a seguir, da página datetime - Tipos básicos de data e hora.

Durante os estudos em Programação, é normal encontrarmos problemas ou termos dúvidas sobre o funcionamento das bibliotecas. Por exemplo, você aprendeu que o objeto timedelta aceita os argumentos days e weeks, então você pode pensar em tentar o argumento months. É um pensamento coerente, mas, infelizmente, você irá se deparar com um erro do tipo TypeError. Quando você tiver dúvidas sobre o funcionamento de um objeto ou de uma biblioteca em Python, você tem alguns recursos: pesquisar o seu problema em um mecanismo de busca na internet, como o Google, ler a documentação oficial ou procurar no site Stack Overflow. Confira mais sobre este último, um importante recurso para programadores, na próxima página.

O Stack Overflow é o principal site de perguntas e respostas de programação atualmente. Ele tem uma comunidade bem ativa na língua inglesa, mas também presente na língua portuguesa. Muitos usuários recorrem ao site para tirar dúvidas sobre bugs (problemas de código), comportamento de bibliotecas ou para achar uma resolução de um problema.

Agora, retomando o exemplo de vacinas citado anteriormente, suponha que você queira calcular quantos meses e dias vão se passar entre a primeira e a segunda dose da vacina Astrazeneca. Como você faria? Para ajudá-lo na resolução deste problema, um usuário já se deparou com uma situação parecida e recorreu ao Stack Overflow. Caso você queira conferir a pergunta e resposta, confira o link a seguir sobre Saber quantos anos, meses, dias, horas etc se passaram desde uma determinada data.

No site está descrito um código que é útil para o seu problema. O código trabalha com duas datas d1 e d2 e calcula a diferença de anos, meses, dias, horas, minutos e segundos do intervalo. Parece um problema maior do que o seu. Especialmente porque a informação de ano, horas, minutos e segundos não importam muito ao seu caso. Confira o código completo a seguir, que realiza esses cálculos:

import datetime
d1 = datetime.datetime(2014,7,16,23)
d2 = datetime.datetime.now()
diff = d1 – d2
days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30
seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60
print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))
Tem muita linha de código que não parece ser interessante ao seu problema. Que tal adaptar para o seu contexto? Siga para a próxima página para conferir a adaptação.

Para tornar o código útil ao seu exemplo, é preciso, primeiro, trocar as datas d1 e d2 pelas que você utilizou anteriormente para o cálculo de dias das doses, que são as variáveis hoje e dia_futuro. Em seguida, é possível eliminar todas as linhas que não são referentes às informações de meses e dias, pois essas são as únicas informações desejadas. Por último, é só adaptar o print para exibir somente essa informação. Confira o código completo a seguir com todas essas modificações:

from datetime import datetime, timedelta
hoje = datetime(2021, 5, 14, 9, 30)
intervalo_dias = timedelta(weeks=12)
dia_futuro = hoje + intervalo_dias
diff = dia_futuro – hoje
days = diff.days
months, days = days // 30, days % 30
print("Desde {} passaram {} meses e {} dias".format(dia_futuro, months, days))
Com a ajuda do Stack Overflow, foi mais fácil achar a solução para o problema. No entanto, foi preciso adaptar o código encontrado com as suas variáveis, e somente para a informação que necessita. Esse passo de saber reutilizar trechos de código de outras pessoas é essencial na Programação, pois, muitas vezes, somente copiar e tentar rodar o programa, não vai gerar o resultado que você deseja.

Você aprendeu sobre diferentes objetos presentes no módulo datetime que representam datas e horas. Mas o que você acha da forma que as datas e as horas são exibidas pelo print? É bem diferente do que estamos acostumados. Que tal você gerar strings personalizadas com as informações de data que você quiser? Você aprenderá como transformar objetos date e datetime em strings e vice-versa no próximo tópico.

# Tópico 2 – Convertendo Datas e Strings

## OBJETIVOS

Converter datas em strings;
Criar datas a partir de strings;
Listar os diferentes códigos de formato de strings.

Quando damos um print em um objeto do tipo date ou datetime em Python, a saída está no padrão ISO 8601. No entanto, normalmente, nós queremos mostrá-la de uma maneira mais amigável, como em aplicações de tempo em smartphones ou de calendário, a exemplo do Google Agenda. Logo mais, confira como disponibilizar as datas em diferentes formatos, mostrando somente as informações que você quiser para criar aplicações mais legíveis e com melhor usabilidade.

Além disso, lembre-se de que, até agora, só criamos datas manualmente ou pegando a informação do dia. Mas e se você criar um programa que peça ao usuário que digite uma data, como em um formulário de inscrição em que se digita a data de nascimento? Essa informação seria obtida como uma string. Então, como você faria pra converter isso para um objeto de data?

Neste tópico, aprenda sobre os métodos strftime e strptime para converter de datas em strings e vice e versa. Estes métodos estão presentes tanto na classe date quanto na datetime.

O método strftime converte uma data em uma string. Ela possui um único parâmetro chamado format. Este parâmetro é uma string composta por um conjunto de códigos, tais como “%d %m”, entre diversos outros. Estes códigos representam determinados atributos de uma data, por exemplo, %d representa o atributo de dia e %m o de mês. Além disso, o código de formato representa a forma como se quer apresentar o valor, por exemplo, %Y representa o atributo de ano com 4 dígitos (2021), e %y também representa o atributo de ano, mas somente os dois últimos dígitos (21).

Para entender melhor, analise um exemplo. Vamos relembrar a variável data_inicio que criamos no começo da aula. Vamos imprimi-la utilizando o strftime e no formato dia/mês/ano, como no seguinte código:

data_inicio = date(2021, 1, 25)
print(data_inicio.strftime("%d/%m/%Y")) # 25/01/2021

Compare a saída do print com o parâmetro format. O argumento é composto pela string “%d/%m/%Y”. Mas, o que você acha que isso significa? Primeiro, vamos traduzir os códigos: %d corresponde ao valor de dia da data; %m ao valor de mês; %Y ao valor de ano. Isso significa que, quando utilizamos essa função, queremos que a data seja mostrada começando pelo dia, seguida pelo mês e, por último, pelo ano. Além disso, inserimos a barra (/) entre cada uma dessas informações.

Vamos praticar um pouco mais para consolidar. Agora você só quer a informação de mês e ano separadas apenas por um espaço. Então, o format deve ser da forma “%m %Y”, correto? Confira.

print(data_inicio.strftime("%m %Y")) # 01 2021

Assim, funcionou como deveria. Agora precisamos da informação de data no padrão americano mês - dia - ano. Note como construir o format: “%m - %d - %Y”.

print(data_inicio.strftime("%m - %d - %Y")) # 01 - 25 - 2021

Ah! Fique atento a uma informação: não existem só esses três códigos %d, %m e %Y, certo? Na verdade, existe uma tabela de códigos com diferentes formatos. Podemos escrever o mês por extenso, escrever somente os últimos dois dígitos do ano, entre outras opções. Na próxima página, conheça a tabela com diferentes códigos de formato.

A tabela a seguir mostra os principais códigos úteis do strftime. Estes códigos serão utilizados no decorrer desta aula para você consolidá-los bem. Você pode sempre consultar esta tabela caso não se lembre de uma informação exata. A primeira coluna (da esquerda) contém os códigos; a segunda coluna (do meio) apresenta uma descrição simples da informação que ele representa; e a terceira coluna (da direita) mostra exemplos de uso:

Código	Descrição	                    Exemplo
%A	    Nome do dia da semana completo	Monday, Tuesday, …, Sunday
%d	    Número do dia da semana	        01, 02, …, 31
%b	    Nome do mês de forma abreviada	Jan, Feb, Mar, ... , Dec
%B	    Nome do mês completo	        January, February, …, December
%m	    Número do mês	                01, 02, …, 12
%y	    Dois últimos dígitos do ano	    01, 02, …, 99
%Y	    Número do ano completo	        0001, 0002, …, 2021, ...,
%H	    Número da hora	                01, 02, …, 24
%M	    Número do minuto	            01, 02, …, 59
%S	    Número do segundo	            01, 02, …, 59
%j	    Número do dia do ano	        001, 002, …, 365, 366
%W	    Número da semana do ano	        00, 01, …, 53

Você deve ter notado que os nomes retornados pela função estão escritos em inglês. Infelizmente, as funções não possuem, por padrão, suporte para outros idiomas. Portanto, começaremos trabalhando com as informações em inglês e depois você aprenderá como transformar manualmente para português.

Agora que você conheceu outros códigos, vamos retomar o exemplo das datas do BBB 21. A seguir, conheça como escrever a data de início do programa da seguinte forma: 25 of January of 2021 is a Monday, onde January (janeiro em inglês) é o mês por extenso e Monday (segunda-feira em inglês) é o dia da semana. Para isso, utilize a função strftime. A solução é a seguinte:

print(data_inicio.strftime("%d of %B of %Y is a %A")) # 25 of January of 2021 is a Monday
Com a mesma variável, você pode gerar strings com valores totalmente diferentes utilizando diferentes informações. No código a seguir, é gerada uma string informando o dia e a semana do ano da variável data_inicio. O dia do ano é a posição do dia em questão dentre todos os 365 dias do ano. A semana do ano é o número da semana dentre todas as 53 semanas presentes em um ano.

print(data_inicio.strftime("É o dia %j da semana %W do ano")) # É o dia 025 da semana 04
Muito bem! Existem muitas formas de praticar os diferentes códigos do strftime! Sinta-se à vontade para continuar testando. Caso você se depare com erros, procure no Stack Overflow, como mostrado anteriormente.

Você já deve ter notado que a string passada como argumento para a função strftime pode conter palavras, certo? Ela não precisa conter somente os códigos de formato diretamente. Nos exemplos que você acabou de analisar, foi possível escrever frases completas utilizando informações do tipo date em conjunto.

O problema é que os títulos continuam em inglês, então aprenda, a seguir, como modificá-los para português.

Para gerar as datas em português, é preciso fazer uma configuração simples. Mas, para fazer essa configuração, é preciso entender que as funções strftime e strptime utilizam a região do código como parâmetro para definir qual idioma deve ser usado para fornecer as informações textuais. Se você não informar nada, elas vão assumir que você está nos Estados Unidos. Então, é preciso informar ao código Python que você mora no Brasil. Para isso, utilize o módulo locale. Confira o trecho a seguir:

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
Pronto! Basta adicionar essas duas linhas, e o código está pronto para exibir informações de data em Português. Observe, a seguir, o mesmo exemplo mostrado anteriormente:

print(data_inicio.strftime("%d de %B de %Y é uma %A")) # 25 de janeiro de 2021 é uma segunda-feira
Bem simples, não foi? Você aprendeu como utilizar os atributos de um objeto date para gerar strings. Prosseguindo nesta aula, conheça como fazer o mesmo para os objetos do tipo datetime.

Lembra que um objeto datetime consiste de uma informação de data e uma informação de hora? Bem, você já aprendeu a utilizar as informações de data com a função strftime. Agora você irá focar nos argumentos de tempo, como horas, minutos e segundos. Caso não tenha notado, eles estão listados na tabela de códigos apresentada anteriormente. Analise o exemplo seguinte, que ilustra o uso do método strftime com códigos de hora, minuto e segundo:

inicio = datetime(2021, 5, 24, 20, 30, 5)
print(inicio.strftime("A hora de inicio do estudo é às %H:%M:%S"))
Perceba que não há muita variação de possibilidades com as informações de tempo, mas teste com outros exemplos e analise os resultados que obtiver. Para conhecer outros códigos de formatação referentes às informações de tempo, além dos apresentados na tabela, consulte a documentação oficial presente no texto a seguir:

Ícone Saiba Mais
Ícone “Saiba Mais”.
Não existem muitos códigos diferentes para as informações de hora, minuto e segundo, como existem para as informações de data. No entanto, você pode consultar a documentação oficial e exercitar com os códigos que não foram apresentados neste material. Acesse a documentação oficial neste link da página datetime - Tipos básicos de data e hora.

Não há necessidade de decorar todos os códigos e as suas funcionalidades. Portanto, a documentação deve sempre ser usada como referência ao construir seus códigos que envolvem datetime.

Até aqui, você aprendeu a converter datas e horas em strings! Na sequência, aprenda o inverso: como extrair informações de datas e horas de dentro de strings. Vamos lá!

Imagine a seguinte situação: um usuário digitou sua data de nascimento. Então, o código utilizou a função input para coletar os dados, como mostrado neste exemplo:

print("Digite a sua data de nascimento")
data_nascimento = input()
O usuário, provavelmente, digitará a data no formato dia/mês/ano. Como você construiria um objeto date ou datetime a partir dessa string? Você pode até pensar, “eu sei usar o método split da string”. Porém, daria para utilizá-la para extrair cada informação em uma string, como mostra o exemplo a seguir:

data_split = data_nascimento.split('/')
dia = int(data_split[0])
mes = int(data_split[1])
ano = int(data_split[2])
data = date(ano, mes, dia)
Essa estratégia funciona para os casos simples. Agora, suponha que o usuário digite no formato “01 de janeiro de 1900”. Para transformar o mês por extenso para um inteiro, utilizamos a função strptime. Este método está presente somente na classe datetime. Entenda como ela funciona na próxima página.

A função strptime recebe dois argumentos: uma string na qual há uma informação de data e uma outra string contendo os códigos de formato. Este segundo argumento funciona da mesma forma que acontece na função strftime. As duas strings são comparadas, e os caracteres, que correspondem aos códigos, são extraídos com seu respectivo valor.

Por exemplo, suponha que a string é “01/02/1900”, e a segunda string é “%d/%m/%Y”. Perceba que os dois primeiros caracteres casam com %d, os dois seguintes após a barra casam com %m e os quatro últimos combinam com %Y. Logo, o resultado seria um objeto datetime com o valor de ‘dia’ igual a 01, valor de ‘mês’ igual a 02, e o valor de ano igual a 1900. Caso algum caractere exista em alguma das strings, que não está representada igualmente na outra, uma exceção do tipo ValueError é levantada, com uma mensagem de que as strings não correspondem.

Suponha que o valor da variável data_nascimento é “01/02/1990”. Compare como fica o código mostrado anteriormente utilizando a função strptime:

data = datetime.strptime(data_nascimento, "%d/%m/%Y")
print(data) # 1990-02-01 00:00:00
Por meio do resultado do print, é possível perceber que a variável data já é um objeto do tipo datetime, porque foram exibidas as informações de data e tempo. Conseguiu perceber como o strptime funciona? Confira, na página a seguir, mais exemplos de utilização da função para consolidar os seus conhecimentos.

Estude os exemplos a seguir com strings contendo informações de datas e horas e utilizando a função strptime para criar objetos datetime:

data_string1 = "02 de Abril de 1900"
data1 = datetime.strptime(data_string1, "%d de %B de %Y")
print(data1) # 1900-04-02 00:00:00
data_string2 = "O alarme toca segunda-feira às 20:30:05"
data2 = datetime.strptime(data_string2, "O alarme toca %A às %H:%M:%S")
print(data2) # 1900-01-01 20:30:05
Perceba que, por meio de strings com formatos bem diversos, é possível extrair as informações e criar um objeto datetime personalizado. Nos dois exemplos, as informações de data e tempo correspondem aos códigos nas duas strings.

A função strftime permite a escrita de strings a partir de objetos datetime, e a função strptime funciona da forma inversa: realiza a criação de objetos datetimes a partir de strings. Essas duas funções requerem prática para consolidar o seu uso, portanto, pratique além dos exemplos apresentados nesta aula.

Agora deu para entender como utilizar strptime para extrair um objeto datetime de uma string?

Chegamos ao fim desta aula do curso de Python para Machine Learning. Aqui você concluiu toda a parte de aprofundamento em Python. Com isso, você passa a conhecer mais os principais módulos da linguagem.

Nesta aula, você estudou o módulo datetime e suas diferentes classes para a representação de datas e horas. Assim, é possível criar aplicações que lidam com eventos de tempo. Você conheceu como converter datas em strings e vice e versa. Dessa forma, já é possível gerar frases com diferentes informações de data, tornando a leitura mais casual.

Datas são muito importantes na área de Machine Learning. Elas podem, por exemplo, ser usadas na criação de imagens ou consultar como uma informação mudou ao longo do tempo. Outra aplicação que utiliza bastante informação de tempo é a análise de séries temporais. Neste tipo de problema, um cientista de dados procura identificar padrões que variam em uma linha de tempo.

Agora você pode iniciar os seus estudos em bibliotecas numéricas. Nas próximas aulas, mude o foco para resolver problemas matemáticos e trabalhar com tipos de dados específicos para operações matemáticas.

Ah! Resolva as atividades propostas e revisite os conteúdos desta aula sempre que necessário para aprofundar seus conhecimentos.

Bons estudos!

## Referências

FREEPIK. Banco de imagens. Imagem sobre tecnologia. Disponível em: https://br.freepik.com/fotos-gratis/trabalhando-no-codigo_5766879.htm. Acesso em: 25 jun. 2021.
FREEPIK. Banco de imagens. Imagem sobre tecnologia. Disponível em: https://br.freepik.com/fotos-gratis/garota-na-midia-social_4191300.htm?query=using%20instagram. Acesso em: 25 jun. 2021.
PYTHON. Datetime – Como trabalhar com Data e Hora em Python usando Datetime. Disponível em: https://vaiprogramar.com/como-trabalhar-com-data-hora-python-datetime/. Acesso em 17 jun. 2021.
PYTHON. Datetime – Lidando com datas e horários. Disponível em: https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python. Acesso em: 17 jun. 2021.
PYTHON. Datetime – Tipos básicos de data e hora. Disponível em: https://docs.python.org/pt-br/3/library/datetime.html. Acesso em: 9 jun. 2021.
