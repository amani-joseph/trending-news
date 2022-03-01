import urllib.request, json

from .model import News

# GETTING THE API KEY
api_key = None

# GETTING THE NEWS URL
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    This will get the JSON response to the URL request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            print(news_results_list)
            news_results = process_results(news_results_list)
            # print(list(news_results))

    return news_results


def process_results(news_list):
    '''
    This function processes  the news results and transforms them into a list of objects

    
    Args:
        news_list: A list of dictionaries that contain the news details
        
    Returns :
        news_results: A list of news objects
    
    '''
    news_results = []

    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')
        url = news_item.get('url')

        news_object = News(title, description, urlToImage, content, publishedAt, url)
        # for k,v in news_object.items():
        #          print(k, v)

        news_results.append(news_object)
        # print(news_results)
    return news_results

    # print(news_results)
