# Introdução

Olá! Seja bem-vindo!

Nesta aula, você vai estudar a respeito de serialização e desserialização de objetos em Python, que é um aspecto importante de qualquer programa não comum. Isso geralmente acontece quando se salva algo em um arquivo em Python, quando a máquina lê um arquivo de configuração ou mesmo quando se responde a uma requisição HTTP.

As tarefas de serialização e desserialização acabam sendo comuns no dia a dia de programadores ou de cientistas de dados. O esquema, o formato ou o protocolo de serialização que você escolher determinará a rapidez que os programas executarão, quanto seguros serão, quanta liberdade terá para manter seu estado e quão bem operará com outros sistemas.

Em Python, a serialização permite que você pegue uma estrutura de objeto complexa e transforme-a em um fluxo de bytes que podem ser salvos em um disco ou enviados por uma rede. A serialização pode ser usada em muitas situações diferentes. Um dos usos mais comuns é salvar o estado de um algoritmo de Machine Learning após a fase de treinamento para que você possa usá-lo mais tarde sem ter que refazer o treinamento.

## Objetivos
Definir como serializar e desserializar um objeto;
Organizar os módulos utilizados para serializar objetos em Python;
Comparar e avaliar diferentes métodos de serialização.

# Tópico 1

## OBJETIVOS

Definir o que é um arquivo CSV;
Definir a estrutura de um arquivo CSV;
Comparar diferentes métodos de leitura e escrita;
Identificar em qual momento usar arquivo CSV.
Considere a seguinte situação: você precisa obter informações dentro e fora de seus programas através de outros meios possíveis, além do teclado e do console. Trocar informações por arquivos de texto é uma maneira comum de compartilhar informações entre programas. Um dos formatos mais populares para a troca de dados é o formato Comma Separated Values (CSV), podendo ser traduzido para “valores separados por vírgula”. Saiba que a grande vantagem de um arquivo CSV é o fato de ele possibilitar a importação e a exportação de arquivos com grandes quantidades de dados de uma linguagem que vários aplicativos podem ler.

Para isso, você pode contar com várias bibliotecas perfeitamente aceitáveis que você pode usar para manipulação de arquivos desse tipo. A biblioteca Python CSV, por exemplo, funcionará para a maioria dos casos. Ela fornece funcionalidade para ler e escrever nesse formato.

Nesta aula, você aprenderá a ler, a processar e a analisar estruturas CSV a partir de arquivos de texto usando Python. Você perceberá como esses arquivos funcionam e aprenderá a utilizar a biblioteca Python CSV. Vamos lá!

Um arquivo CSV é um tipo de arquivo de texto simples que usa estruturação específica para organizar dados tabulares. Por ser um arquivo de texto simples, ele pode conter apenas dados de texto reais — em outras palavras, caracteres ASCII ou Unicode imprimíveis, certo? Normalmente, os arquivos CSV usam uma vírgula para separar cada valor específico de dados, sem espaço entre eles. Confira como essa estrutura se parece:

nome da coluna 1,nome da coluna 2,nome da coluna 3

dado 1 da primeira linha,dado 2 da primeira linha,dado 3 da primeira linha

dado 1 da segunda linha,dado 2 da segunda linha,dado 3 da segunda linha

Observe como cada pedaço de dado é separado por uma vírgula. Normalmente, a primeira linha identifica o nome de uma coluna de dados e cada linha seguinte informa dados reais. Em geral, o caráter separador é chamado de delimitador e a vírgula não é a única usada. Outros delimitadores populares incluem os caracteres tab (\t), cólon (:) e semi-cólon (;). Analisar corretamente um arquivo CSV exige que saibamos qual delimitador está sendo usado. Se abrirmos o arquivo (que se utiliza da estrutura mostrada) em uma planilha, ela iria se parecer mais ou menos como consta no quadro a seguir:

nome da coluna 1	        nome da coluna 2	        nome da coluna 3
dado 1 da primeira linha	dado 2 da primeira linha	dado 3 da primeira linha
dado 1 da segunda linha	    dado 2 da segunda linha	    dado 3 da segunda linha

Os arquivos CSV são muito fáceis de se trabalhar. Qualquer linguagem que suporte a entrada de arquivos de texto e a manipulação de string (como Python) pode funcionar diretamente com esses arquivos. Na próxima página, você confere como ler um arquivo utilizando o módulo CSV.

Agora observe a leitura de um arquivo no qual utilizamos o método reader do módulo CSV. Esse método retorna um objeto reader que irá iterar sobre as linhas do arquivo fornecido. O arquivo de exemplo a seguir está no formato de texto (.txt), mas os arquivos que geralmente são utilizados possuem o formato Comma Separated Values (.csv).

Para exemplificar esse assunto, imagine que você trabalha em uma empresa e precisa analisar as informações dos seus colaboradores, como nome, departamento e mês de aniversário. Para fazer essas análises, você terá acesso ao arquivo aniversarios_funcionarios.txt. Confira um exemplo dos dados contido nesse arquivo:

nome,departamento,mês de aniversário

Pedro Lima,RH,Novembro

Gabriela Silva,TI,Março

Aqui está o código:

 import csv

 with open('aniversarios_funcionarios.txt',encoding='utf8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    print(leitor_csv)
    for linha in leitor_csv:
      print(linha)
Isso resulta na seguinte saída:

<_csv.reader object at 0x000002106A82BC10>

['nome', 'departamento', 'mês de aniversário']

['Pedro Lima', 'RH', 'Novembro']

['Gabriela Silva', 'TI', 'Março']

Cada linha devolvida pelo objeto é uma lista de elementos contendo os dados encontrados, removendo os delimitadores.

Após a importação do módulo csv (linha 1), na linha 3, foi aberto o arquivo utilizando o encoding ‘utf8’ para serem consideradas as letras brasileiras (ç,ê,á).
Na linha 4, o objeto arquivo (arquivo_csv) e o delimitador foram passados como argumento do método reader. O parâmetro delimitador define qual o caractere que separa os dados em cada linha. Dessa forma, facilita muito a leitura e a manipulação dos dados contidos em um arquivo.
Mas será que há um jeito melhor de manipular os dados desse arquivo? Confira na próxima página.

Imagine, agora, que trabalhar com lista foi um pouco desafiador para você, devido à necessidade de decorar a ordem do significado dos elementos no arquivo. Então, em vez de lidar com uma lista de elementos individuais, você pode ler dados do arquivo diretamente em um dicionário (dict) também. Para exemplificar isso, será usado o mesmo arquivo definido anteriormente ('aniversarios_funcionarios.txt). No código a seguir, observe como utilizar o método DictReader.

 import csv

 with open('aniversarios_funcionarios.txt',encoding='utf8') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv, delimiter=',')
    print(type(leitor_csv))
    for linha in leitor_csv:
      print(linha)
Isso resulta na seguinte saída:


{'nome': 'Pedro Lima', 'departamento': 'RH', 'mês de aniversário': 'Novembro'}

{'nome': 'Gabriela Silva', 'departamento': 'TI', 'mês de aniversário': 'Março'}

Cada linha devolvida pelo objeto é um dicionário em Python contendo os dados encontrados, removendo os delimitadores. De onde vieram as chaves do dicionário? Presume-se que a primeira linha do arquivo CSV contenha as chaves a serem usadas para construir o dicionário. Se você não tiver isso no arquivo CSV, você deve especificar suas próprias chaves definindo o parâmetro opcional fieldnames com uma lista de chaves. Caso o arquivo tenha muitas colunas, esse método acaba facilitando a manipulação dos dados, assim, não é necessário mais se lembrar dos dados pelo índice da coluna.

Ícone Fique Atento
Ícone “Saiba Mais+”.
Lembre-se de que, ao longo da sua jornada de aprendizado, irão ocorrer alguns erros ao utilizar os módulos apresentados. Caso precise encontrar a solução de um determinado problema você pode pesquisar na documentação do módulo em que esteja trabalhando ou nos fóruns da internet. O mais conhecido é o stackoverflow, que você pode acessar por este link.

Na próxima página, acompanhe como criar um arquivo CSV do zero utilizando o módulo CSV. Vamos lá!

Você também pode escrever para um arquivo CSV usando o método writer e writerow. O método writer retorna um objeto de escrita responsável por converter os dados de usuário em strings. Já o método writerow escreve os dados passados como argumento no objeto writer. No código apresentado a seguir, note um exemplo da utilização desses métodos.

 import csv

 with open('aniversarios_funcionarios_novo.csv',encoding='utf8',mode='w',newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')

    escritor_csv.writerow(['nome', 'departamento', 'mês de aniversário'])
    escritor_csv.writerow(['Pedro Lima', 'RH', 'Novembro'])
    escritor_csv.writerow(['Gabriela Silva', 'TI', 'Março'])
Esse código gera o seguinte arquivo de saída:

nome;departamento;mês de aniversário

Pedro Lima;RH;Novembro

Gabriela Silva;TI;Março

Vamos analisá-lo:

Na linha 3, foram passados mais dois argumentos para as funções open, mode e newline. O parâmetro mode recebe uma string opcional que especifica o modo no qual o arquivo é aberto, o valor padrão é ‘r’, que significa que se quer abrir um arquivo para leitura, entretanto foi utilizada a string 'w’, que permite a escrita no arquivo. O parâmetro newline controla como o modo de novas linhas funciona, que pode ser None, '', '\n', '\r' e '\r\n’. Vamos utilizar como argumento uma string vazia para não ser adicionada uma nova linha, pois o método writerow já insere uma nova linha por padrão. Além disso, criamos um novo arquivo, chamado aniversarios_funcionarios_novo, que possui o formato csv.
Na linha 4, além de ser utilizado o método writer, foi implantado ‘;’ como delimitador dos dados, que é um formato muito comum no Brasil, pois a ‘,’ é utilizada para definir valores decimais.
Nas linhas 6, 7 e 8, por fim, note que consta o método writerow para adicionar novos dados ao arquivo, passando como argumento a lista de dados a serem adicionados.
A seguir, confira como adicionar novos dados utilizando um dicionário como argumento.

Uma vez que é possível ler dados de um arquivo a partir de um dicionário, é justo que você deve ser capaz de escrevê-lo a partir de um dicionário também. O método DictWriter cria um objeto que funciona como um objeto de escrita comum, mas mapeia dicionários nas linhas de saída. No seguinte código, confira um exemplo da utilização desse método.

 import csv

 with open('aniversarios_funcionarios_novo_dict.csv',encoding='utf8',mode='w',newline='') as arquivo_csv:
    fieldnames = ['nome', 'departamento', 'mês de aniversário']
    escritor_csv = csv.DictWriter(arquivo_csv, delimiter=';',fieldnames=fieldnames)

    escritor_csv.writeheader()
    escritor_csv.writerow({'nome': 'Pedro Lima', 'departamento': 'RH', 'mês de aniversário': 'Novembro'})
    escritor_csv.writerow({'nome': 'Gabriela Silva', 'departamento': 'TI', 'mês de aniversário': 'Março'})
    escritor_csv.writerow({'mês de aniversário': 'Agosto', 'nome': 'Marcelo Oliveira'})


O código descrito gera o seguinte arquivo de saída:

nome;departamento;mês de aniversário

Pedro Lima;RH;Novembro

Gabriela Silva;TI;Março

Marcelo Oliveira;;Agosto

Vamos fazer uma análise:

Na linha 5, ao chamar o método DictWriter, foi utilizado o parâmetro fieldnames para definir quais são os nomes das colunas contidas no arquivo. Isso faz sentido quando você pensa sobre isto: sem uma lista de fieldnames, não é possível saber quais chaves usar para recuperar valores de dicionários.
Na linha 7, foi utilizado um método chamado writeheader, que tem o papel de pular a primeira linha do arquivo. Isso é necessário, pois, na primeira linha do arquivo, há o nome das colunas que foram definidas na linha 5.
Nas linhas 8, 9 e 10, por fim, foi usado o método writerow para inserir novos dados ao arquivo. Perceba que, na linha 10, mudamos a ordem de inserção dos dados e removemos um dado; mesmo assim, o método se comportou da maneira correta, e isso foi possível porque foi utilizada uma estrutura de chave e valor para inserirmos dados no arquivo.
Na próxima página, você pode exercitar seus conhecimentos nesse assunto.

# Tópico 2 – JSON

## OBJETIVOS

Definir o que é um JSON;
Descrever a estrutura de um JSON;
Relacionar elementos Python com elementos JSON;
Definir os métodos do módulo JSON.
Desde a sua criação, JavaScript Object Notation (JSON) tornou-se rapidamente o padrão de fato para a troca de informações, por exemplo, para coletar informações através da internet ou armazenar seus dados em um banco de dados de documentos. De um jeito ou de outro, você está em constante contato com aplicações que usam JSON. Felizmente, essa é uma tarefa bastante comum e, como acontece com as tarefas mais comuns, o Python a torna quase supérflua. Neste tópico, você vai conhecer como dominar esse assunto.

Então, usamos JSON para armazenar e trocar dados. Não é nada mais do que um formato padronizado que a comunidade usa para passar dados por aí. Tenha em mente que JSON não é o único formato disponível para este tipo de trabalho, mas, provavelmente, é o mais utilizado no mundo.

Não tão surpreendentemente, JSON foi inspirado por um subconjunto da linguagem de programação JavaScript. A simplicidade com que os dados são estruturados no formato JSON permite que ele seja utilizado em qualquer tipo de linguagem de programação. Em última análise, a comunidade, em geral, adotou o JSON porque é fácil para humanos e máquinas criá-lo e entendê-lo.

Os dados contidos em um arquivo no formato JSON devem ser estruturados por meio de uma coleção de pares com nome e valor ou ser uma lista ordenada de valores. A seguir, você confere um arquivo chamado exemplo_json. Seus elementos devem conter:

Chave: Corresponde ao identificador do conteúdo. Por isso, deve ser uma string delimitada por aspas;
Valor: Representa o conteúdo correspondente e pode conter os seguintes tipos de dados: string, array, object, number, boolean ou null.
 {
 "primeiro_nome": "João",
 "sobrenome": "Silva",
 "passatempos": ["correr", "nadar", "jogar"],
 "idade": 35,
  "fumante": false,
 "possui_filhos": true,
 "possui_carro": null,
 "filhos": [
   {
     primeiro_nome": "Aline",
     "idade": 6
   },
   {
     primeiro_nome": "Enzo",
     "idade": 8
   }
 ]
 }

 Como você pode notar, json suporta tipos primitivos, como strings e números, bem como listas aninhadas e objetos. Isso se assemelha a um dicionário Python.

Perceba que ainda há algumas diferenças em relação ao dicionário do Python. Os valores booleanos (true e false) não possuem a primeira letra maiúscula como no python. Também possuem o elemento null, que é um valor especial que não se refere a um objeto; em Python, utiliza-se None. No quadro a seguir, você encontra as diferenças de tipo entre Python (na coluna da esquerda) e JSON (na coluna da esquerda).

Python	            JSON
list,tuple	        array
str	                string
int, long, float	number
True	            true
False	            false
None	            null
Na próxima página, você vai conhecer como usar um JSON com a biblioteca json do Python.

Agora confira como utilizar o Python para abrir o arquivo de texto, chamado exemplo_json, que contém a estrutura dos elementos em JSON. O conteúdo desse arquivo foi mostrado na página anterior. O código seguinte demonstra como abrir esse arquivo usando o módulo json.

 import json

 arquivo_json = open('exemplo_json.txt',encoding='utf8')

 pessoa = json.load(arquivo_json)

 arquivo_json.close()

 print(type(pessoa)) # <class 'dict'>

 print(pessoa) # {'primeiro_nome': 'João', 'sobrenome': 'Silva', 'passatempos': ['correr', 'nadar','jogar'],'idade':35,'fumante': False, 'possui_filhos': True, 'possui_carro': None, 'filhos': [{'primeiro_nome': 'Aline',
'idade':6},{'primeiro_nome': 'Enzo', 'idade': 8}]}
Vamos analisar esse código:

Na linha 3, após a importação do módulo JSON, observe que o arquivo está em formato de texto (.txt). Geralmente, os arquivos contendo estrutura JSON possuem a extensão .json;
Na linha 5, foi utilizado o método load, que desserializa um arquivo, ou seja, converte um arquivo de texto estruturado em formato JSON para um dicionário em Python, facilitando a manipulação de objetos mais complexos;
Na linha 7, foi usado o método close, que é responsável por fechar o arquivo que foi aberto na linha 3;
Na linha 9, é possível confirmar que o objeto retornado é um dicionário;
Na linha 10, você confere como ficou o dicionário após a extração do arquivo JSON.
Como você pôde acompanhar, existe uma lista de objetos JSON contidos na chave ‘filhos’, isso demonstra que podemos criar estruturas hierárquicas dentro de um JSON.

Na próxima página, você vai conhecer como converter esse dicionário em um objeto JSON.

Continuando com o código da página anterior, você pode usar o dicionário Python, já utilizado para desserializar o arquivo, para serializá-lo novamente em um objeto JSON. Confira o código que possui um exemplo de como é feito para serializar novamente.

 json.dumps(pessoa) # '{"primeiro_nome": "Jo\\u00e3o", "sobrenome": "Silva", "passatempos": ["correr", "nadar","jogar"],
"idade": 35, "fumante": false, "possui_filhos": true, "possui_carro": null, "filhos":
[{"primeiro_nome":"Aline", "idade": 6}, {"primeiro_nome": "Enzo", "idade": 8}]}'

 json.dumps(pessoa,ensure_ascii=False) # '{"primeiro_nome": "João", "sobrenome": "Silva", "passatempos": ["correr",
"nadar","jogar"], "idade": 35, "fumante": false, "possui_filhos": true,
"possui_carro": null,"filhos": [{"primeiro_nome": "Aline", "idade": 6},
{"primeiro_nome": "Enzo", "idade": 8}]}'
No código apresentado, note que foi usado o método dumps passando como argumento o dicionário pessoa. Saiba que isso significa que estamos tentando converter o dicionário em um objeto JSON.

Na linha 12, é possível notar que o resultado contém caracteres que não existiam no dicionário pessoa, como Jo\\u00e3o, isso ocorre porque, por padrão, é garantido que a saída não contenha os caracteres ASCII (como abordado em outro momento deste curso, no assunto “Guardando na Memória”).
Para resolver esse problema, atribuímos o valor False ao parâmetro ensure_acii, na linha 14, fazendo que seja considerado o padrão utf-8 para gerar o JSON.
O arquivo JSON utiliza-se de inúmeros caracteres para definir toda sua estrutura, bem diferente de um arquivo CSV, que só utiliza um caractere delimitador para definir os dados. Isso torna o arquivo CSV mais leve que um arquivo JSON.

Confira, na próxima página, como serializar um objeto JSON em um arquivo de extensão .json.

Imagine que você precisa fazer um algoritmo de Machine Learning que recomende filmes. Para isso, você primeiro precisa dos dados do filme e serializá-lo em alguma estrutura de dados. Aqui, será usado o filme Toy Story como exemplo. O código a seguir ilustra um exemplo de serialização de um JSON contendo os dados do filme Toy Story, sendo criado do zero a partir de um dicionário.

 import json

 filme = {}
 filme['Nome'] = 'Toy Story'
 filme['Direção'] = 'John Lasseter'
 filme['Produção executiva'] = ['Edwin Catmull','Steve Jobs']
 filme['Gênero'] = ['animação','aventura','comédia']
 filme['Produtora'] = ['Walt Disney Pictures','Pixar Animation Studios']
 filme['Lançamento'] = [{'País': 'Estados Unidos',
                      'Data': '22/11/1995'},
                      {'País': 'Brasil',
                      'Data': '22/12/1995'},
                      {'País': 'Portugal',
                      'Data': '29/03/1996'}]
 filme['Orçamento (US$)'] = 30000000
 filme['Receita (US$)'] = 406594102

 arquivo_json = open('exemplo_2_json.txt',mode='w',encoding='utf8')

 json.dump(filme, arquivo_json, ensure_ascii=False)

 arquivo_json.close()
Figura 1 – Pôster de divulgação do filme Toy Story

O código apresentado gera um arquivo JSON, ou seja, arquivo que segue a estrutura apresentada nas telas anteriores. O arquivo de saída é: {"Nome": "Toy Story", "Direção": "John Lasseter", "Produção executiva": ["Edwin Catmull", "Steve Jobs"], "Gênero": ["animação", "aventura", "comédia"], "Produtora": ["Walt Disney Pictures", "Pixar Animation Studios"], "Lançamento": [{"País": "Estados Unidos", "Data": "22/11/1995"}, {"País": "Brasil", "Data": "22/12/1995"}, {"País": "Portugal", "Data": "29/03/1996"}], "Orçamento (US$)": 30000000, "Receita (US$)": 406594102}

Na próxima página, você pode analisar melhor o código.

Continuando o assunto, vamos focar no trecho do código da tela anterior a partir da linha 18.

 arquivo_json = open('exemplo_2_json.json',mode='w',encoding='utf8')

 json.dump(filme, arquivo_json, ensure_ascii=False)

 arquivo_json.close()
Vamos analisar o código:

Na linha 18, foi utilizada a função open para criar o arquivo em formato JSON. Definimos o parâmetro mode como escrita e utilizamos o parâmetro encoding para passar o padrão do teclado brasileiro (utf-8);
Na linha 20, foi usado o método dump para converter o dicionário filme em um objeto JSON e, por fim, esse objeto foi escrito no arquivo exemplo_2_json. Usamos, também, o parâmetro ensure_ascii para definir que os dados do objeto JSON sejam serializados com o padrão do teclado brasileiro;
Na linha 22, foi fechado o arquivo que foi aberto na linha 18.
Na próxima página, você pode exercitar os assuntos que foram explicados até o momento. Vamos lá!

# Tópico 3 – Pickle

## OBJETIVOS

Conhecer e comparar métodos distintos do módulo pickle;
Determinar em qual situação usar a serialização do pickle;
Relacionar a serialização do pickle com Machine Learning;

O módulo pickle do Python é outra maneira de serializar e desserializar objetos em Python. Ele difere do módulo JSON por serializar objetos em um formato binário, o que significa que o resultado não é legível por humanos. No entanto, utilizando o módulo pickle, é possível serializar todos os tipos de dados do Python e, também, estruturas mais complexas, como funções e objetos específicos. Utilizar o módulo pickle é uma boa escolha por sua facilidade de uso e capacidade de reconstruir objetos Python completos, deixando-os prontos para uso.

Se você não precisa de um formato legível ou de um formato capaz de operar de forma padrão, ou se precisa serializar objetos personalizados, vá em frente, use o pickle. Ele é muito útil quando você está trabalhando com algoritmos de aprendizado de máquina, em que deseja salvá-los para fazer novas previsões posteriormente, sem ter que reescrever tudo ou treinar o modelo novamente.

Ler e escrever em arquivos binários manualmente é uma atividade rara, como você pôde conhecer ao estudar como guardar na memória. Isso se dá, pois, na maior parte do tempo, é mais comum utilizar algum módulo especializado que sabe como decodificar (leitura) ou codificar (escrita) as informações que estão sendo utilizadas. Entretanto, em alguns casos, pode ser desejável criar um formato de armazenamento próprio para o seu programa.

Você se lembra de aprender, em algum momento, sobre programas para gerenciar coleções, como listas de tarefas ou de compras? Bom, programas como esses mantêm uma memória de longo prazo, o que sugere o uso de arquivos como artifício de memória. Existe um módulo na biblioteca padrão que permite guardar objetos arbitrariamente complexos com poucas linhas de código chamado pickle.

O módulo pickle consiste, basicamente, em quatro métodos, são eles:

pickle.dump()
pickle.dumps()
pickle.load()
pickle.loads()
Os primeiros dois métodos, pickle.dump() e pickle.dumps(), são usados ​​durante o processo de serialização. Os outros dois métodos, pickle.load() e pickle.loads(), são usados ​​durante a desserialização. A única diferença entre dump() e dumps() é que o primeiro cria um arquivo contendo o resultado da serialização, enquanto o segundo retorna uma string.

Para diferenciar dumps() a partir de dump(), é útil lembrar que o caractere “s”, no fim do nome da função, significa string. O mesmo conceito se aplica a load() e loads(): o primeiro lê um arquivo para iniciar o processo de retirada dos bits e o segundo opera em uma string.

Na próxima página, será demonstrado como utilizar dois dos métodos apresentados aqui.

O código a seguir ilustra a utilização dos métodos dumps e loads em que será serializado um elemento e observado como ele se comporta.

Vamos analisar o código:

 import pickle

 minha_lista = [1,2,3,4,5]

 meu_objeto_pickle = pickle.dumps(minha_lista)

 print(meu_objeto_pickle) # b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'

 minha_lista = None

 minha_lista_pickle = pickle.loads(meu_objeto_pickle)

 print(minha_lista) # None

 print(minha_lista_pickle) # [1, 2, 3, 4, 5]
Na linha 1, foi importado o módulo pickle;
Na linha 3, foi criada uma variável chamada minha_lista que contém uma lista com cinco elementos;
Na linha 5, foi utilizado o método dumps do pickle passando minha_lista como argumento, que retorna a representação da serialização desse elemento como uma string em bytes, ao invés de escrevê-lo em um arquivo;
Na linha 7, note que foi retornada uma string em bytes. Essa string representa a lista de cinco elementos que foram passados como argumento;
Na linha 9, a variável minha_lista foi modificada, atribuindo a ela o valor None;
Na linha 11, foi utilizado o método loads, que retorna o elemento reconstituído da representação serializada com pickle a partir de um objeto byte ou similar;
Na linha 13, você pode observar o valor da variável minha_lista, que agora é None;
Na linha 15, há o valor da variável minha_lista quando serializada, ou seja, ela ainda era uma lista naquele momento.
A seguir, será apresentado como persistir os dados binários em um arquivo.

O código a seguir ilustra a utilização do método dump. Desse modo, ele será utilizado para serializar dois elementos e persisti-los em um arquivo.

 import pickle

 minha_lista = [1,2,3,4,5]

 def eh_par(num):
   if num % 2 == 0:
      return True
   else:
      return False

 arquivo_pickle = open('exemplo_pickle.pck', 'wb')

 pickle.dump(minha_lista, arquivo_pickle)

 pickle.dump(eh_par, arquivo_pickle)

 arquivo_pickle.close()
O código seguinte gera um arquivo de saída legível, em formato binário. A imagem abaixo representa o arquivo gerado. Confira a imagem, depois avance para a próxima página, onde há uma análise do código.

Figura 2 – Exemplo de arquivo legível gerado pelo código
https://leadfortaleza.com.br/ead2pcd/conteudo/tmp/myopenolat_1_104281344980093/aula/img/Figura%20do%20codigo%20gerado.jpg

Vamos analisar o código anterior à imagem:

Da linha 5 à linha 9, foi criada uma função chamada eh_par, que recebe um número qualquer como parâmetro e retorna verdadeiro se esse número for par, e retorna falso caso contrário;
Na linha 11, foi utilizada a função open e foi passado como argumento o nome do arquivo, chamado exemplo_pickle, que possui o formato pickle (.pck) e o modo em que será aberto. Nesse caso, note que foi passada a string ‘wb’ como modo, que abre para escrita binária, apagando se o caminho existir e criando se não existir;
Nas linhas 13 e 15, foram serializados os elementos dentro do arquivo que foi aberto anteriormente, minha lista e eh_par, respectivamente;
Na linha 17, após a serialização, o arquivo pickle foi fechado.
A seguir, conheça como recuperar os dados binários de um arquivo pickle.

O código apresentado a seguir ilustra a utilização do método load. Ele será utilizado para recuperar os dois elementos que foram persistidos no arquivo exemplo_pickle, assim como foi demonstrado no código anterior.

 import pickle

 arquivo_pickle = open('exemplo_pickle.pck', 'rb')

 minha_lista_pickle = pickle.load(arquivo_pickle)

 eh_par_pickle = pickle.load(arquivo_pickle)

 arquivo_pickle.close()

 print(minha_lista_pickle)

 print(eh_par_pickle(3))

 Agora vamos analisar esse código:

Na linha 3, foi utilizada a função open e foi passado, como argumento, o nome do arquivo e o modo em que ele será aberto. Nesse caso, passamos a string ‘rb’ como modo, que abre o arquivo para leitura binária, falhando caso o caminho não exista;
Nas linhas 5 e 7, extraímos e desserializamos dois elementos diferentes contidos no arquivo pickle, utilizando um mesmo método (load). Esse método load recupera, por padrão, os elementos binários por ordem de inserção no arquivo, ou seja, primeiro a lista, depois a função. Entretanto, na linha 7, ocorrerá um erro. O problema é, em parte, porque você só tem um arquivo em seu programa e o módulo pickle não serializa definições de classe ou definição de função. Em vez disso, salva uma referência de como encontrar a classe. Para corrigir esse erro, você teria que definir a função ou a classe novamente.
Confira como fazer isso na próxima página.

Este código ilustra como corrigir o erro ocorrido, definindo novamente a função ‘eh_par’.

 import json

 def eh_par(num):
   if num % 2 == 0:
      return True
   else:
      return False

 arquivo_pickle = open('exemplo_pickle.pck', 'rb')

 minha_lista_pickle = pickle.load(arquivo_pickle)

 eh_par_pickle = pickle.load(arquivo_pickle)

 arquivo_pickle.close()

 print(minha_lista_pickle) # [1, 2, 3, 4, 5]

 print(eh_par_pickle(3)) # False
Agora que a função foi definida novamente, entre as linhas 3 e 7, você pode partir de onde parou no código anterior. Vamos analisar o código:

Nas linhas 5 e 7, foram extraídos e desserializados dois elementos diferentes contidos no arquivo pickle, utilizando um mesmo método (load), dessa vez, sem ocorrer erro;
Nas linhas 11 e 13, há o resultado da desserialização dos elementos. O interessante é que o pickle conseguiu gravar um elemento complexo, que é uma função, em um arquivo. Desse modo, é possível guardar os algoritmos de machine learning já treinados, pois ele é capaz de guardar o estado de um objeto.
Na próxima página, você confere uma curiosidade sobre o método load.

No box a seguir, você encontra um exemplo de erro que pode ser disparado durante a leitura do arquivo utilizando o módulo pickle.

Ícone Fique Atento
Ícone “Saiba Mais+”.
Uma tentativa de ler um novo objeto quando o arquivo já chegou ao fim resulta em um erro “EOFError: Ran out of input”. Além disso, não é recomendável misturar estas funções com os métodos read e write habituais de objetos de arquivo. Então, fique atento para que isso não ocorra em seus códigos!

Prosseguindo com seus estudos neste curso, conheça um exemplo de como seria serializado e desserializado um algoritmo de Macinhe Learning (ML) já treinado.

A seguir, você encontra dois códigos. O primeiro demonstra a serialização de um algoritmo de ML após o seu treinamento e o segundo demonstra a desserialização desse algoritmo já treinado.

 import pickle

 class algoritmo_ml:
   def __init__(self, coeficiente_de_x, constante):
      self.a = coeficiente_de_x
      self.b = constante

   def previsao(self, x):
      return x * self.a + self.b

 arquivo_pickle = open('exemplo_pickle.pck', 'wb')

 ex_1 = algoritmo_ml(9,3)

 pickle.dump(ex_1, arquivo_pickle)

 arquivo_pickle.close()
 import pickle

 class algoritmo_ml:
   def __init__(self, coeficiente_de_x, constante):
      self.a = coeficiente_de_x
      self.b = constante

   def previsao(self, x):
      return x * self.a + self.b

 arquivo_pickle = open('exemplo_pickle.pck', 'rb')

 ex_1_pickle = pickle.load(arquivo_pickle)

 arquivo_pickle.close()

 print(ex_1_pickle.previsao(10)) # 93
Agora, na página a seguir, confira a análise dos códigos.

Nosso algoritmo de ML será uma classe que cria objetos que calculam funções de primeiro grau, onde o treinamento é a definição de valor aos atributos do objeto. Vamos analisar o primeiro código, que demonstra a serialização de um algoritmo de ML após o seu treinamento:

Após a definição da classe algoritmo_ml (linhas 3 a 9), ele abre o arquivo em modo de escrita (linha 11);
Na linha 13, o algoritmo é treinado através dos valores passados como argumento, que são o coeficiente de x e a constante da função, respectivamente;
Por fim, o objeto é serializado no arquivo (linha 15) e, em seguida, o arquivo é fechado (linha 17).
Analisando o segundo código, que demonstra a desserialização do algoritmo já treinado:

É definida novamente a classe algoritmo_ml, pois, como já citado, o módulo pickle só guarda a referência para encontrar a classe;
Em seguida, o arquivo é aberto em modo de leitura (linha 11) e é feita a desserialização do objeto guardado (linha 13);
Em seguida, o arquivo é fechado (linha 17);
Por fim, na linha 17, note que o estado do objeto foi guardado, ou seja, ele ainda continha os valores dos atributos a e b salvos, podendo fazer previsões.
Na próxima página, exercite seus conhecimentos com a questão proposta sobre o módulo pickle.

Chegamos ao fim desta aula, espero que você tenha gostado. Com o conhecimento obtido aqui, você pode praticar a serialização para qualquer necessidade em Python.

Agora, você já sabe que existem diferentes maneiras de serializar e desserializar objetos em Python. Mas qual você deve usar? Bom, não existe uma solução única para todos. O que você faz com seus dados, uma vez que eles foram carregados na memória, dependerá do seu uso. Geralmente, seu objetivo será coletar dados de uma fonte, extrair informações úteis e passar essas informações ou manter um registro deles. Já os arquivos binários servem para quando você necessita de maior controle sobre os processos de codificação e decodificação.

Com esse conhecimento, você está bem equipado para persistir seus objetos usando o módulo Python e apto a trabalhar com algoritmos de Machine Learning já treinados, sem falar que você já conhece a estrutura padrão de envio de dados pela internet, muito útil quando você quer fazer seu algoritmo se comunicar com outras máquinas na rede.

Embora os exemplos com os quais você trabalhou aqui sejam fictícios e simples, eles ilustram um fluxo de trabalho que você pode aplicar a tarefas mais gerais.

Bons estudos!

## Referências
DATACAMP. Pickle in Python: Object Serialization. Disponível em: https://www.datacamp.com/community/tutorials/pickle-python-tutorial. Acesso em: 29 maio 2021.
DOCS PYTHON. CSV – Leitura e escrita de arquivos CSV. Disponível em: https://docs.python.org/pt-br/3/library/csv.html. Acesso em: 29 maio 2021.
DOCS PYTHON. JSON – Codificador e decodificador JSON. Disponível em: https://docs.python.org/pt-br/3/library/json.html. Acesso em: 29 maio 2021.
DOCS PYTHON. PICKLE – Serialização de objetos Python. Disponível em: https://docs.python.org/pt-br/3/library/pickle.html. Acesso em: 29 maio 2021.
ENVATOTUSTS+. Serialização e Desserialização de Objetos do Python: Parte 1. Disponível em: https://code.tutsplus.com/pt/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183. Acesso em: 29 maio 2021.
PYTHON GUIDE. Serialização de dados. Disponível em: https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/serialization.html. Acesso em: 29 maio 2021.
REAL PYTHON. Logging in Python. Disponível em: https://realpython.com/python-logging/. Acesso em: 25 maio 2021.
REAL PYTHON. Reading and Writing CSV Files in Python. Disponível em: https://realpython.com/python-csv. Acesso em: 29 maio 2021.
REAL PYTHON. Working With JSON Data in Python. Disponível em: https://realpython.com/python-json/. Acesso em: 29 maio 2021.
ROCKCONTENT. Afinal, o que é JSON e para que ele serve? Descubra agora! Disponível em: https://rockcontent.com/br/blog/json/. Acesso em: 29 maio 2021.
ROCKCONTENT. Entenda o que é o formato CSV e saiba como importar e exportar esses arquivos. Disponível em: https://rockcontent.com/br/blog/csv/. Acesso em: 29 maio 2021.
WIKIPÉDIA. Serialização. Disponível em: https://pt.wikipedia.org/wiki/Serializa%C3%A7%C3%A3o. Acesso em: 29 maio 2021.

## Glossário
Para conhecer o significado dos termos técnicos estudados em nossa aula, selecione a palavra desejada.

CSV https://leadfortaleza.com.br/ead/glossary/CSV
Desserialização https://leadfortaleza.com.br/ead/glossary/Desserializa%C3%A7%C3%A3o
JSON https://leadfortaleza.com.br/ead/glossary/JSON
Serialização https://leadfortaleza.com.br/ead/glossary/Serializa%C3%A7%C3%A3o
