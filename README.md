# Análise de Sentimentos com AI.

#1 Criar seu app no twitter.

#2 Utilizar o framework tweepy. (Oauth) 
    Instalar pip no Windows ( console python -m pip install -U pip ) Gerenciador de pacotes do python
    Instalar o tweepy ( pip install tweepy )
    Instalar nltk ( pip install nltk )
    executar o script no python import nltk nltk.download('punkt')
    A cada requisição na API do twitter tem que esperar 15 minutos.

#3 Filtrando os tweets de uma # em um arquivo python.json
    Contar quantos tweets foram no PowerShell ( windows )  Get-Content python.json | Measure-Object -Line

#Descrição
    Utilizando a linguagem de programação python e o framework tweepy podemos fazer requisições na API REST do  tweeter,
    pegando dados.

#o objeto tweet possuí
    text: the text of the tweet itself
    created_at: the date of creation
    favorite_count, retweet_count: the number of favourites and retweets
    favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
    lang: acronym for the language (e.g. “en” for english)
    id: the tweet identifier
    place, coordinates, geo: geo-location information if available
    user: the author’s full profile
    entities: list of entities like URLs, @-mentions, hashtags and symbols
    in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
    in_reply_to_status_id: status identifier id the tweet is a reply to a specific status


# regexp 
    Expressões regulares para indentificar a emoji e hashtag

# Tecnicas
    Tokenise 
    Contar o termo mais usado, mas não necessáriamente é o mais relevante.