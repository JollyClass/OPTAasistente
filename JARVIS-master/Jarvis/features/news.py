import requests
import json



def get_news():
    url = 'https://cnnespanol.cnn.com/seccion/mundo/'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://cnnespanol.cnn.com/seccion/mundo/'
