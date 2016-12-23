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


#### Acesso ao Twitter
Para termos acesso ao Twitter, tivemos que primeiramente criar uma conta e em seguida criar um aplicativo para então termos condições de escutarmos o que era "twitado" na internet. Para evitarmos os bloqueios que poderíamos sofrer, criamos dois aplicativos, de forma a burlar o "xerife" do Twitter. Assim, de tempos em tempos alterávamos o aplicativos que utilizávamos.
O primeiro aplicativo se chamava [**TweetyMining69**](https://apps.twitter.com/app/13191380)

O segundo aplicativo se chamava [**tweety mining**](https://apps.twitter.com/app/13170132/show)

#### Definição de Armazenamento
Conforme mencionado anteriormente utilizamos dois métodos distintos de armazenamento, sendo o primeiro um arquivo texto, com extensão json e o segundo um arquivo no banco de dados MongoDB.
Arquivo Json: with open("c:\\Users\\Marcelo\\Documents\\noSQL-twt.json",'a') as file:

MongoDB: client = pymongo.MongoClient('localhost', 27017)
         db = client.tweet_database
         collection = db.tweet_collection
--------------------------------------------------------------------------------------------------------------------------------------



