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
```
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
|ConsumerKey (API Key)|rPQLXBYOnk3TbKgzX2Qe8TfJx|
|---|---|
|Consumer Secret (API Secret)|t31Pi0v4lJfMaZ4H9csEqt2uUwotiTDLC7waxHAnAWtHA3Uf3A|
|---|---|
Assim temos de passar tokens e dados de acesso a aplicação para que nosso acesso seja liberado.








