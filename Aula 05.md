#Aula 05 - Resolução de exercícios

##Instruções:  
Para cada uma das situações dos exercícios escolha a infraestrutura que você acha mais adequada e justifique sua escolha.

###Exercício 01
Você e um grupo de amigos da faculdade decidem-se juntar e criar uma empresa de na área de IoT. Todos seus amigos são excelentes programadores porém estão em dúvida como montar a infraestrutura para suportar a grande quantidade de dados gerados pelos sensores da aplicação. O que vocês devem fazer?

###Resposta
Devido a característica da solução, de se trabalhar com coleta de dados de sensore em real-time e da grande quantidade de dados gerados a solução deverá obrigatóriamente considerar uma infraestrutura robusta o bastante para ter velocidade e diversidade de armazenamento.  
Assim a Solução seria a utilização de um Ambiente com um banco de dados não relacional (noSQL) e um ambiente de processamento real-time, como SPARK. Através desta configuração, criaríamos estruturas de filas para receber os dados enviados pelos sensores e estes seriam então tratados e armazenados no bando de dados, permitindo que o recebimento dos dados e seu armazenamento ocorressem de forma assíncrona, evitando impactos na performance da aplicação.

### Exercício 02
Dentro de sua empresa certamente existem pontos que podem ser adaptados para uma arquitetura Big Data. Explique a infraestrutura atual e o que você mudaria para melhorar a eficiência.
