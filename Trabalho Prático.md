# Trabalho prático de Banco de Dados noSQL
## Coletar informações de redes sociais e armazenar no mínimo 1MM de dados.
### Extrair informações do tipo:

1. Termos mais frequentes:
2. Volume por dia:
3. Volume por hora do dia:


###[1] **termos mais frequentes:**
Escolhemos a rede social TWITTER como objeto de nosso trabalho, por já termos tido uma experiência inicial com a mesma em aula.
Para a captura dos dados, foi desenvolvido um código em Python para capturar tweets e em seguida armazená-los. Como efeito de estudo armazenamos estes dados em dois formatos: arquivo json e dentro do Banco de Dados MongoDB para que pudéssemos praticar os dois métodos.

Um segundo código foi gerado para acessar os dados armazenados e então fazer a identificação dos temos mais frequentes.
As linguagens utilizadas foram Python e Java Script, sendo que a segunda era necessária para trabalharmos os dados no MongoDB.


#### Acesso ao Twitter
Para termos acesso ao Twitter, tivemos que primeiramente criar uma conta e em seguida criar um aplicativo para então termos condições de escutarmos o que era "twitado" na internet. Para evitarmos os bloqueios que poderíamos sofrer, criamos dois aplicativos, de forma a burlar o "xerife" do Twitter. Assim, de tempos em tempos alterávamos o aplicativos que utilizávamos.
O primeiro aplicativo se chamava [**TweetyMining69**](https://apps.twitter.com/app/13191380). 
O segundo aplicativo se chamava [**tweety mining**](https://apps.twitter.com/app/13170132/show)

#### Definição de Armazenamento
Conforme mencionado anteriormente utilizamos dois métodos distintos de armazenamento, sendo o primeiro um arquivo texto, com extensão json e o segundo um arquivo no banco de dados MongoDB.
Arquivo Json: with open("c:\\Users\\Marcelo\\Documents\\noSQL-twt.json",'a') as file:

MongoDB: 
```python
client = pymongo.MongoClient('localhost', 27017)
db = client.tweet_database
collection = db.tweet_collection
```

O Armazenamento dos dados em ambos os ambientes é muito simples e fácil de fazer.
Armazenamos os dados no arquivo texto, em formato json, para que os dados já ficassem estruturados e assim pudéssemos depois trabalhar com os mesmos. No caso do MongoDB isto é mais simples, pois ele sozinho já arquiva os dados em formato Json.
Como é de se esperar nesta fase não há diferença, perceptível, de velocidade entre uma atividade e a outra.

O armazenamento no arquivo de texto é feito pelo comando: __file.write(testdata2)__ sendo testdata2 os dados do twitter capturado.
Já no caso do MongoDB, é feito pelo comando: __tweetind = collection.insert_one(testdata2).inserted_id__.

### PALAVRAS DE BUSCA
Para este trabalho prático escolhemos palavras de busca voltadas para o momento em que estamos vivendo - Natal, Fim de Ano, Festas.
Assim as palavras selecionadas foram:
```python
Words_to_Track = ['Natal','felicidade','amor','paz','alegria','árvore','família','união',
                  'champagne','luz','trenó','presentes','beijos','abraços','renas',
                  'papai noel','saco de presentes',
                  'bebedeira','festa de fim de ano','fim de ano','sexo','camisinha','suruba',
                  'ano novo', 'dinheiro']
```                  
                  
Vemos que o range de palavras variam bastante indo de uma noção religiosa cristã à termos mais associados a festas pagãs. Com isto buscávamos abordar os diferentes grupos de indivíduos que se comunicaram durante o período.


### A COLETA E TRATAMENTO dos TWEETS
A coleta dos tweets é feita através do acesso ao Twitter, pela aplicação que foi criada inicialmente no twitter.
Quando criamos a aplicação no twitter chaves e tokens de acesso são criados para que apenas o dono da aplicação possa fazer uso da mesma.
Ex.:  
 ConsumerKey (API Key)        -> rPQLXBYOnk3TbKgzX2Qe8TfJx  
 `Consumer Secret (API Secret) -> t31Pi0v4lJfMaZ4H9csEqt2uUwotiTDLC7waxHAnAWtHA3Uf3A`  
 Access Token                 -> 805224390954782720-eLwQWp5C7ncpmgqUKWvZ72Y1hdgtjYE  
 `Access Token Secret          -> RdSsAiXmSRh1lEMeMLX0lBUdnocH73P0aEZnuRgBWtUJ8`  
 
Assim temos de passar tokens e dados de acesso a aplicação para que nosso acesso seja liberado.
Isto é feito enviando via APIs ao Twitter os dados acima:
```python
consumer_Key = "rPQLXBYOnk3TbKgzX2Qe8TfJx"
consumer_Secret = "t31Pi0v4lJfMaZ4H9csEqt2uUwotiTDLC7waxHAnAWtHA3Uf3A"
access_Token = "805224390954782720-eLwQWp5C7ncpmgqUKWvZ72Y1hdgtjYE"
access_Secret = "RdSsAiXmSRh1lEMeMLX0lBUdnocH73P0aEZnuRgBWtUJ8"

auth = OAuthHandler(consumer_Key, consumer_Secret)
auth.set_access_token(access_Token, access_Secret)
stream = Stream(auth, l)
```
Após isto podemos começar a coletar os twitters com o comando abaixo:  
```python
stream.filter(track=Words_to_Track)
```
Através do comando stream.filter iremos coletar todos os twitters que contenham as palavras que definimos anteriormente. Um fato interessante é que dependendo da hora e das palavras a coleta será rápida ou lenta.

Um fato que observamos após as coletas é que forma coletados twitters de todas as linguas, que contivessem alguma das palavras de busca. Assim foram coletados twitters em português, inglês e espanhol. Isto irá afetar, mais a frente, o tratamento das frequências dos termos, pois teremos três idiomas.

#### Tratamento dos Twitters
Aproveitamos para já dar um tratamento aos twitters tão logo os capturássemos, atuando sobre o campo 'texto' que é a mensagem que é tuitada e já a dividindo em termos independentes e não mais como uma frase. Isto quer dizer, desconsideramos as pontuações e outros caracteres.
Fizemos isto com o intuito de ganhar tempo já que o nosso objetivo neste trabalho prático é determinar com que frequência alguns termos são utilizados.
Assim, tão logo capturavamos o twitter, já transformávamos o texto em TOKENS, ou melhor, uma lista de palavras. Isto era feito com o comando:
```python
tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
```
Para esta tarefa de transformar em TOKENS o texto utilizamos os pacotes NLTK, que é uma plataforma líder para construir programas em Python para trabalhar com dados de linguagem humana.

O código completo pode ser visto no arquivo Coleta_Tweets.py.  

Para efeito de estudo, fizemos duas coletas distintas de twitters, sendo uma coletando e armazenando os twitters sem tratamento e a segunda com o texto já transformado em tokens. Assim foram criados no MongoDB duas coleções: **tweet_collection** e **tweet_coll_token** respectivamente.  


### IDENTIFICAÇÃO DOS TERMOS MAIS FREQUENTES.
Para então tratarmos os twitters que foram coletados foram desenvolvidos dois códigos distintos, sendo um em Python e o segundo em Java Script, para rodar direto do MongoDB, ou seja, utilizando as "engines" do banco de dados.

#### 1. Código Python
Nesta fase, não mais precisamos acessar o Twitter, logo só acessamos o MongoDB:
```python
    client = pymongo.MongoClient('localhost', 27017)
    db = client.tweet_database
    collection = db.tweet_collection
```
Como vê, estamos utilizando a coleção que contem o twitter puro, com seus campos intactos, por isto, fizemos a tokenização do texto na hora de contar os termos. Esta contagem é feita utilizando-se um contador, count_all = Counter().

Buscando um conhecimento melhor do sentido que as palavras teriam, utilizamos a função "bigrams" para contar dois tokens que aparecam juntos na mesma frase, desta forma conseguimos ter alguma idéia do que significado do twitter.

No código contamos os termos da sequinte forma:
```python
        terms_all = [term for term in tokens]
        terms_bigram = bigrams(terms_all) #juntei dois tokens dos mesmos tweets, buscando mais sentido.
        # Update the counter
        count_all.update(terms_bigram)
```
Por INCRÍVEL que pareça, o código em Python rodou com sucesso, porém demorou mais de uma hora para chegar ao fim.
O resultado desta análise foi a seguinte:  
[(('el', 'amor'), 73273),  
(('mi', 'amor'), 31323),  
(('❤', '️'), 26471),  
(('en', 'el'), 26029),  
(('amor', 'y'), 18267),  
(('amor', 'es'), 15639),  
(('😂', '😂'), 13190),  
(('un', 'amor'), 12408),  
(('jesus', 'christ'), 12024),  
(('amor', 'vida'), 11841),  
(('amor', 'deus'), 11255)]

Um fato interessante a se notar aqui é que as palavras mais "pagans" ou de baixo calão, não aparecem entre as 10 primeiras. Logo, podemos inferir que as pessoas neste período em que estamos dão mais valor ao sentido religioso e a união de suas famílias.
O código deste processo pode ser encontrado em **Term_Frequency.py**

#### 2. Código Java Script - MongoDB
Em um segundo momento fizemos a contagem dos termos mais frequentes utilizando a própria "engine" do MongoDB, que nos dá muita performance.
Um ponto importante aqui: É necessário criar-se um ÍNDICE antes para que o MongoDB possa operar com performance.
Outro ponto importante é que o código que roda no MongoDB está em JAVA SCRIPT.

Assim primeiramente no Shell do MongoDB criamos o Índice:
```js
db.tweet_coll_token.createIndex({'text':1})
```
Para fazermos a identificação dos termos utilizamos então a função de mapReduce do MongoDB que permite identificar os termos e somá-los.
```js
var map = function() {  
    var text = this.text;
    if (text) { 
        // quick lowercase to normalize per your requirements
        // text = text.toLowerCase(); 
        for (var i = text.length - 1; i >= 0; i--) {
            if (text[i])  {      // make sure there's something
               emit(text[i], 1); // store a 1 for each word
            }
        }
    }
};

var reduce = function( key, values ) {    
    var count = 0;    
    values.forEach(function(v) {            
        count +=v;    
    });
    return count;
}


db.tweet_coll_token.mapReduce(map, reduce, {out: "word_count"})

db.word_count.find().sort({value:-1})
```

Como vêem utilizamos a collection tweet_coll_token pois ela já estava tratada e não continga pontuação e seus termos já estavam em forma de token.

O mesmo procedimento que demorou mais de uma hora para ser concluído no Python, dentro do MongoDB demorou **menos de 05 minutos**.

O resultado foi o seguinte:
```js
> db.word_count.find().limit(100).sort({'value':-1})
{ "_id" : "amor", "value" : 461860 }
{ "_id" : "deus", "value" : 193588 }
{ "_id" : "…", "value" : 177886 }
{ "_id" : "el", "value" : 161307 }
{ "_id" : "é", "value" : 146218 }
{ "_id" : "jesus", "value" : 131832 }
{ "_id" : "y", "value" : 123877 }
{ "_id" : "la", "value" : 90653 }
{ "_id" : "en", "value" : 84001 }
{ "_id" : "oi", "value" : 83701 }
{ "_id" : "...", "value" : 83104 }
{ "_id" : "es", "value" : 73122 }
{ "_id" : "mi", "value" : 70555 }
{ "_id" : "natal", "value" : 65515 }
{ "_id" : "to", "value" : 65463 }
{ "_id" : "pra", "value" : 63406 }
{ "_id" : "❤", "value" : 60484 }
{ "_id" : "the", "value" : 60424 }
{ "_id" : "q", "value" : 52856 }
{ "_id" : "vida", "value" : 51512 }
```
Infelizmente não consegui fazer a mesma análise de bigrams com o Js e MongoDB.


###[2] **VOLUME POR DIA:**

Para descobrirmos o volume de tweets por dia teríamos de trabalhar com as datas e horas em que os twitters foram postados. Isto apresenta um novo desafio, porém passível de solução.
A solução é similar a anterior, porém ao invés de termos similares, temos de encontrar dias similares.
Assim temos de trabalhar com o timestamp dos twitters.

Utilizando-se Python e a biblioteca PANDA esta tafefa fica muito fácil, pois a panda já traz muitos algorítmos prontos para executar este tipo de tarefa. No entanto, devido ao grande tamanho do arquivo, a tarefa não pode ser concluída utilizando-se este método, pois há consumo excessivo de memória e por fim estouro, causando a parada do processo.

A solução é trabalhar diretamente com o MongoDB que possui performance e engine para tal. Como temos de trabalhar com o tempo, temos de buscar os timestamps de cada twitter e somar os que são do mesmo dia. Isto pode ser feito com a função getTimestamp() e de novo utilizando-se a função mapReduce do MongoDB.

Utilizamos a coleção tweet_collection que contém os twitters completos e sem tratamento, já que o que estamos buscando é apenas o período em que o mesmo foi postado.
Novamente, é imprescindível criarmos um Índice, pois sem o mesmo teremos um problema com o mapReduce.

```js
var map = function() {
    var datetime = this._id.getTimestamp();

    var created_at_Day = new Date(datetime.getFullYear(),
                                     datetime.getMonth(),
                                     datetime.getDate());
    emit(created_at_Day, {count: 1});
}

var reduce = function(key, values) {
    var total = 0;
    for(var i = 0; i < values.length; i++) { total += values[i].count; }
    return {count: total};
}

db.tweet_collection.mapReduce( map, reduce, { "out": "tweet_perDay" } );

db.tweet_perDay.find().limit(10).sort({"_id":-1})
```
Para a minha grande surpresa, esta pesquisa tomou menos de 1 minuto, o que aponta o poder do MongoDB em executar estas tarefas de memória e CPU intensivas.
Segue o resultado:
```js
""" Resultado: """
> db.tweet_collection.mapReduce( map, reduce, { "out": "tweet_perDay" } );
{
        "result" : "tweet_perDay",
        "timeMillis" : 41389,
        "counts" : {
                "input" : 1294918,
                "emit" : 1294918,
                "reduce" : 12952,
                "output" : 3
        },
        "ok" : 1
}

> db.tweet_perDay.find().limit(10).sort({"_id":-1})
{ "_id" : ISODate("2016-12-**12**T02:00:00Z"), "value" : { "count" : 586075 } }  
{ "_id" : ISODate("2016-12-**11**T02:00:00Z"), "value" : { "count" : 687865 } }  
{ "_id" : ISODate("2016-12-**10**T02:00:00Z"), "value" : { "count" : 20978 } } 
```

Acredito que esta operação também possa ser conseguida com a função AGGREGATE, no entanto a Aggregate não tem a função de pegar o timestamp do twitter.

###[3] **VOLUME POR HORA:**
A solução é igual a anterior. Novamente utilizaremos a collection tweet_collection.
O Código e resultados estão apresentados abaixo:
```js
var map = function() {
    var datetime = this._id.getTimestamp();

    var created_at_hour = new Date(datetime.getFullYear(),
                                     datetime.getMonth(),
                                     datetime.getDate(),
                                     datetime.getHours());
    emit(created_at_hour, {count: 1});
}

var reduce = function(key, values) {
    var total = 0;
    for(var i = 0; i < values.length; i++) { total += values[i].count; }
    return {count: total};
}

db.tweet_collection.mapReduce( map, reduce, { "out": "tweet_perHour" } );

db.tweet_perHour.find().limit(10).sort({"_id":-1})
```
#### Resultado:
```js
> db.tweet_collection.mapReduce( map, reduce, { "out": "tweet_perHour" } );  
{  
        "result" : "tweet_perHour",  
        "timeMillis" : 22658,  
        "counts" : {  
                "input" : 1294918,  
                "emit" : 1294918,  
                "reduce" : 12976,  
                "output" : 27  
             },  
        "ok" : 1  
        

> db.tweet_perHour.find().sort({"value":-1})
{ "_id" : ISODate("2016-12-12T02:00:00Z"), "value" : { "count" : 138047 } }
{ "_id" : ISODate("2016-12-12T03:00:00Z"), "value" : { "count" : 127166 } }
{ "_id" : ISODate("2016-12-11T02:00:00Z"), "value" : { "count" : 98605 } }
{ "_id" : ISODate("2016-12-12T04:00:00Z"), "value" : { "count" : 83084 } }
{ "_id" : ISODate("2016-12-11T19:00:00Z"), "value" : { "count" : 74931 } }
{ "_id" : ISODate("2016-12-11T18:00:00Z"), "value" : { "count" : 66356 } }
{ "_id" : ISODate("2016-12-11T21:00:00Z"), "value" : { "count" : 62524 } }
{ "_id" : ISODate("2016-12-11T20:00:00Z"), "value" : { "count" : 59585 } }
{ "_id" : ISODate("2016-12-11T17:00:00Z"), "value" : { "count" : 58072 } }
{ "_id" : ISODate("2016-12-11T14:00:00Z"), "value" : { "count" : 54621 } }
{ "_id" : ISODate("2016-12-12T05:00:00Z"), "value" : { "count" : 54373 } }
{ "_id" : ISODate("2016-12-12T00:00:00Z"), "value" : { "count" : 52339 } }
{ "_id" : ISODate("2016-12-11T04:00:00Z"), "value" : { "count" : 50691 } }
{ "_id" : ISODate("2016-12-12T10:00:00Z"), "value" : { "count" : 42768 } }
{ "_id" : ISODate("2016-12-11T03:00:00Z"), "value" : { "count" : 40784 } }
{ "_id" : ISODate("2016-12-12T06:00:00Z"), "value" : { "count" : 36294 } }
{ "_id" : ISODate("2016-12-12T09:00:00Z"), "value" : { "count" : 35908 } }
{ "_id" : ISODate("2016-12-11T10:00:00Z"), "value" : { "count" : 33995 } }
{ "_id" : ISODate("2016-12-12T08:00:00Z"), "value" : { "count" : 28108 } }
{ "_id" : ISODate("2016-12-12T07:00:00Z"), "value" : { "count" : 27482 } }
Type "it" for more
>
> it
{ "_id" : ISODate("2016-12-11T01:00:00Z"), "value" : { "count" : 20978 } }
{ "_id" : ISODate("2016-12-11T15:00:00Z"), "value" : { "count" : 19617 } }
{ "_id" : ISODate("2016-12-12T11:00:00Z"), "value" : { "count" : 12707 } }
{ "_id" : ISODate("2016-12-12T01:00:00Z"), "value" : { "count" : 9821 } }
{ "_id" : ISODate("2016-12-11T16:00:00Z"), "value" : { "count" : 5691 } }
{ "_id" : ISODate("2016-12-11T11:00:00Z"), "value" : { "count" : 233 } }
{ "_id" : ISODate("2016-12-12T13:00:00Z"), "value" : { "count" : 138 } }
```
### FONTES DE PESQUISA
Para executar este trabalho práticos foram utilizadas as seguintes fontes de pesquisa:  
a. Mining Twitter Data with Python - Bonzanini, Marco - (https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/) 

b. Twitter Data Analytics - Shamanth Kumar, Fred Morstatter, and Huan Liu - (http://tweettracker.fulton.asu.edu/tda/)  
c. StackOverflow - um ótimo lugar para se buscar soluções para problemas já conhecidos.  

As duas primeiras fontes de pesquisa são muito boas, pois lhe municiam de conceitos o que lhe permite depois criar. Já o StackOverflow é um bom lugar para se buscar soluções, códigos ou novos algorítimos para desenvolver os conceitos que você aprendeu.

O item (a) tem foco apenas em Python e arquivos txt ou Json, no entanto é muito rico no que tange a text mining, indo além da frequência de termos e entrando no sentimento dos textos. Muito interessante.
O item (b) tem já o foco sobre o MongoDB e tal como o primeiro lhe municia de muitos conceitos e também vai muito além da análise simples de termos. 
