from flask import render_template
from . import main
from ..request import get_news


@main.route('/')
def index():
    """
    This returns the index page
    """
    news = get_news()
    # print(news)
    title = 'Trending News'
    return render_template('index.html', title = title, article = news)
