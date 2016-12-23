# Trabalho prático de Banco de Dados noSQL
## Coletar informações de redes sociais e armazenar no mínimo 1MM de dados.
### Extrair informações do tipo:
- [ ] Termos mais frequentes:
- [ ] Volume por dia:
- [ ] Volume por hora do dia:

- [x] **termos mais frequentes:**
> Escolhemos a rede social TWITTER como objeto de nosso trabalho, por já termos tido uma experiência inicial com a mesma em aula.
Para a captura dos dados, foi desenvolvido um código em Python para capturar tweets e em seguida armazená-los. Como efeito de estudo armazenamos estes dados em dois formatos: arquivo json e dentro do Banco de Dados MongoDB.

> segue o código do arquivo para coleta:


        1) dentro do próprio código Python

        2) utilizando a função mapreduce dentro do Banco de Dados Mondodb (para Windows).





        Código de Captura : arquivo: Coleta_Tweets.py

        Código de tratamento dos tweets e contagem : Term_Frequency.py

        Código de mapreduce: xxxxxxxx.txt



O resultados dos temos mais frequentes pode ser visto aqui:

uaproveitei e fiz uma contagem juntando dois termos mais frequentes nos tweets, de forma que possamos ter uma maior noção do que o autor queria dizer.



"C:\Program Files\Anaconda3\python.exe" C:/Users/Marcelo/PycharmProjects/Tweets-noSQL/Term_Frequency.py

[(('el', 'amor'), 73273), (('mi', 'amor'), 31323), (('❤', '️'), 26471), (('en', 'el'), 26029), (('amor', 'y'), 18267), (('amor', 'es'), 15639), (('😂', '😂'), 13190), (('un', 'amor'), 12408), (('jesus', 'christ'), 12024), (('amor', 'vida'), 11841), (('amor', 'deus'), 11255), (('graças', 'deus'), 11212), (('é', 'amor'), 10620), (('😍', '😍'), 10615), (('mi', 'vida'), 10527), (('amor', 'é'), 10347), (('deus', 'é'), 10203), (('amor', 'mi'), 9617), (('el', 'sexo'), 8791), (('ano', 'novo'), 8271), (('en', 'la'), 8254), (('faltam', 'apenas'), 8115), (('es', 'el'), 7656), (('amor', '❤'), 7631), (('amor', '...'), 7421), (('es', 'amor'), 7323), (('jesus', 'is'), 7213), (('❤', '❤'), 6596), (('️', '❤'), 6575), (('la', 'vida'), 5994), (('del', 'amor'), 5960), (('el', 'peru'), 5834), (('in', 'the'), 5623), (('y', 'el'), 5364), (('hoje', 'é'), 5224), (('acabar', 'ano'), 5183), (('sexo', 'según'), 5148), (('of', 'jesus'), 5142), (('tus', 'tweets'), 5119), (('edad', 'mental'), 5114), (('mental', 'el'), 5110), (('descubre', 'edad'), 5108), (('según', 'tus'), 5107), (('tweets', 'aquí'), 5106), (('aquí', '⏩'), 5106), (('es', 'un'), 5037), (('oi', '@scinternacional'), 4851), (('grande', 'amor'), 4828), (('natal', 'ano'), 4552), (('pra', 'mim'), 4539), (('y', 'amor'), 4514), (('todos', 'los'), 4416), (('amor', '😍'), 4355), (('apenas', 'semanas'), 4353), (('@scinternacional', '😍'), 4282), (('é', 'deus'), 4230), (('deus', 'abençoe'), 4227), (('es', 'una'), 4194), (('amor', 'en'), 4118), (('big', 'data'), 4114), (('pro', 'natal'), 4099), (('papai', 'noel'), 4077), (('va', 'en'), 4036), (('todo', 'el'), 4010), (('con', 'el'), 3964), (('apenas', 'dias'), 3943), (('amor', 'el'), 3893), (('deus', 'céu'), 3885), (('al', 'amor'), 3877), (('presente', 'en'), 3870), (('vai', 'ser'), 3816), (('droga', 'amor'), 3785), (('árvore', 'natal'), 3779), (('deus', 'quiser'), 3767), (('bom', 'dia'), 3740), (('deus', 'livre'), 3736), (('of', 'the'), 3719), (('con', 'amor'), 3668), (('amor', 'la'), 3630), (('is', 'the'), 3565), (('deus', 'sabe'), 3557), (('última', 'rodada'), 3541), (('quero', 'amor'), 3536), (('todo', 'amor'), 3531), (('é', 'aniversário'), 3468), (('mucho', 'amor'), 3458), (('tanto', 'amor'), 3449), (('é', 'bom'), 3434), (('y', 'la'), 3427), (('y', 'su'), 3323), (('tudo', 'bem'), 3313), (('https', '…'), 3303), (('jorge', 'jesus'), 3273), (('thank', 'you'), 3210), (('en', 'mi'), 3202), (('su', 'amor'), 3174), (('ai', 'deus'), 3120), (('amor', 'con'), 3103), (('🎉', '🎊'), 3070), (('🎊', '🎉'), 3042), (('¿', 'va'), 3015), (('in', 'jesus'), 3001), (('es', 'la'), 2977), (('to', 'fome'), 2970), (('y', 'si'), 2967), (('tudo', 'bom'), 2965), (('delação', 'odebrecht'), 2960), (('michel', 'temer'), 2950), (('dias', 'acabar'), 2943), (('😭', '😭'), 2890), (('todo', 'mundo'), 2880), (('en', 'un'), 2859), (('q', 'vc'), 2853), (('con', 'la'), 2831), (('😍', 'oi'), 2815), (('é', 'tão'), 2795), (('vai', 'ter'), 2755), (('é', 'melhor'), 2745), (('amor', 'https://t.co/nki1c8urhy'), 2738), (('@elcosodelapizza', '¿'), 2737), (('semanas', 'natal'), 2700), (('amor', 'cover'), 2699), (('oliveira', 'ari'), 2689), (('cover', 'acústico'), 2688), (('filhos', 'puta'), 2683), (('sofia', 'oliveira'), 2670), (('to', 'the'), 2629), (('🎄', '🎄'), 2606), (('amor', 'mika'), 2592), (('#queronotvz', 'quero'), 2567), (('cone', 'crew'), 2543), (('ari', 'cone'), 2543), (('crew', 'droga'), 2542), (('@criudinoteria', 'sofia'), 2512), (('acústico', 'https://t.co/3f0x1gdawc'), 2512), (('😍', '❤'), 2472), (('🙏', '🏻'), 2468), (('deus', 'amo'), 2467), (('el', 'presente'), 2440), (('la', 'gente'), 2433), (('y', 'yo'), 2387), (('pra', 'acabar'), 2368), (('oi', 'meninas'), 2355), (('dias', 'pra'), 2346), (('tô', 'fome'), 2344), (('eso', 'es'), 2335), (('amor', 'amor'), 2329), (('amor', 'eterno'), 2320), (('vídeo', '@youtube'), 2317), (('jesus', 'and'), 2310), (('todo', 'lo'), 2299), (('yo', 'en'), 2296), (('peru', 'y'), 2267), (('¿', 'qué'), 2256), (('boa', 'noite'), 2234), (('es', 'lo'), 2193), (('to', 'be'), 2190), (('natal', 'faltam'), 2180), (('novo', 'faltam'), 2179), ((':/', '…'), 2178), (('semanas', 'ano'), 2175), (('https', ':/'), 2159), (('deus', '...'), 2158), (('d', '…'), 2156), (('you', 'jesus'), 2145), (('presente', 'natal'), 2140), (('é', 'grande'), 2137), (('gostei', 'vídeo'), 2126), (('lord', 'jesus'), 2098), (('amor', 'si'), 2087), (('y', 'en'), 2075), (('obrigado', 'deus'), 2070), (('amor', 'verdadero'), 2069), (('jesus', 'é'), 2051), (('el', 'tiempo'), 2043), (('vc', 'é'), 2040), (('amor', '…'), 2032), (('deus', 'q'), 2025), (('alan', 'garcia'), 2023), (('hiperinflación', 'en'), 2023), (('la', 'hiperinflación'), 2023), (('peru', 'gob'), 2023), (('gob', 'alan'), 2023), (('n', '…'), 2018), (('nuestro', 'amor'), 2002), (('and', 'the'), 2000), (('oi', 'vamo'), 1985), (('hoje', 'vou'), 1972), (('con', 'mi'), 1972), (('this', 'is'), 1972), (('is', 'my'), 1960), (('amor', 'amo'), 1958), (('ese', 'amor'), 1953), (('feliz', 'aniversário'), 1946), (('hay', 'amor'), 1925), (('posso', 'ser'), 1924), (('dias', 'natal'), 1924), (('amor', 'del'), 1915), (('y', 'lo'), 1901), (('amor', '..'), 1900), (('amor', 'próprio'), 1888), (('vote', 'niall'), 1885), (('jesus', 'cristo'), 1885), (('directs', 'vote'), 1879), (('primer', 'amor'), 1870), (('montar', 'árvore'), 1864), (('t', '…'), 1861), (('niall', 'now'), 1859), (('amor', 'yo'), 1853), (('amor', 'lo'), 1851), (('y', 'tanto'), 1845), (('jesus', 'name'), 1840), (('deus', '#twd7nafox'), 1838), (('and', 'jesus'), 1838), (('amor', 'carinho'), 1837), (('amor', 'pra'), 1836), (('governo', 'temer'), 1833), (('oi', 'tudo'), 1829), (('y', 'fue'), 1828), (('ser', 'feliz'), 1824), (('ano', '…'), 1822), (('cada', 'vez'), 1820), (('is', 'lord'), 1820), (('natal', 'posso'), 1816), (('fé', 'deus'), 1814), (('y', 'eso'), 1810), (('los', 'en'), 1807), (('del', 'año'), 1803), (('siempre', 'amor'), 1802), (('@micaviciconte', 'gracias'), 1800), (('amo', 'amor'), 1799), (('amor', 'dios'), 1793), (('su', 'hiperinflación'), 1786), (('pra', 'festa'), 1781), (('ser', 'mesma'), 1778), (('el', 'mundo'), 1773), (('deus', 'to'), 1769), (('año', 'y'), 1769), (('económico', 'en'), 1769), (('peru', 'hiperinflación'), 1768), (('@veraholtzinreal', 'montar'), 1768), (('mesma', 'https://t.co/0g4qk6pyq9'), 1768), (('shock', 'económico'), 1768), (('paz', 'amor'), 1767), (('muero', 'amor'), 1766), (('vou', 'ensinar'), 1763), (('i', 'am'), 1758), (('falta', 'amor'), 1739), (('️', '️'), 1730), (('si', 'es'), 1705), (('en', 'una'), 1692), (('oi', 'gente'), 1689), (('saiu', 'clipe'), 1685), (('dia', 'dezembro'), 1678), (('name', 'of'), 1674), (('ano', 'to'), 1673), (('s', '…'), 1661), (('q', 'deus'), 1655), (('the', 'name'), 1652), (('una', 'vez'), 1651), (('ultimo', 'del'), 1649), (('fue', 'perfecto'), 1649), (('gracias', 'llevar'), 1647), (('quiero', 'un'), 1647), (('llevar', 'siempre'), 1647), (('tanto', 'entusiasmo'), 1647), (('perfecto', 'gracias'), 1647), (('@freddyleyva', 'ultimo'), 1646), (('dezembro', 'é'), 1637), (('un', 'día'), 1632), (('amor', 'al'), 1629), (('clipe', 'infinity'), 1626), (('jesus', 'melhor'), 1625), (('if', 'you'), 1624), (('p', '…'), 1623), (('—', 'amor'), 1618), (('hace', 'bien'), 1617), (('planos', 'pro'), 1615), (('del', 'mundo'), 1610), (('on', 'the'), 1605), (('dia', 'ano'), 1605), (('quais', 'planos'), 1601), (('vídeo', 'hoje'), 1596), (('importa', 'calares'), 1584), (('é', 'exatamente'), 1584), (('tahun', 'baru'), 1583), (('amor', '💙'), 1580), (('@iahgos', 'oi'), 1578), (('🙏', '🏼'), 1567), (('the', 'lord'), 1567), (('calares', 'https://t.co/4oa5vzi848'), 1566), (('fdssss', '😂'), 1566), (('melhor', 'fdssss'), 1566), (('😂', 'importa'), 1566), (('@rpdacosta4', 'jesus'), 1565), (('con', 'un'), 1559), (('ano', 'faltam'), 1559), (('é', 'natal'), 1557), (('with', 'jesus'), 1546), (('@vocenaosabiaq', 'hoje'), 1535)]



.2) Volume por dia.

    Tentei através de código Python fazer esta tarefa, porém a grande demora e o estouro da memória, tornaram esta tarefa impossível por esta abordagem.

    Utilizei então a função mapReduce novamente, o que funcionou muito bem.



    Verificar a Dia com mais tweets

s



var map = function() {

    var datetime = this._id.getTimestamp();



    var created_at_Day = new Date(datetime.getFullYear(),

                                     datetime.getMonth(),

                                     datetime.getDate());

    emit(created_at_Day, {count: 1});

}

e

var reduce = function(key, values) {

    var total = 0;

    for(var i = 0; i < values.length; i++) { total += values[i].count; }

    return {count: total};

}



db.tweet_collection.mapReduce( map, reduce, { "out": "tweet_perDay" } );



db.tweet_perDay.find().limit(10).sort({"_id":-1})

R

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

{ "_id" : ISODate("2016-12-12T02:00:00Z"), "value" : { "count" : 586075 } }

{ "_id" : ISODate("2016-12-11T02:00:00Z"), "value" : { "count" : 687865 } }

{ "_id" : ISODate("2016-12-10T02:00:00Z"), "value" : { "count" : 20978 } }





.3) Volume por dia.

    Como a solução via Python já não havia funcionado, fomos direto para o mapReduce no MongoDB.

    Tentei utilizar a função Aggregate, porém com ela não conseguia pegar os timestamps. Há como fazer isto?

    

    Segue o código e o resultado:

    

    Verificar a hora com mais tweets





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



Resultado:

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

