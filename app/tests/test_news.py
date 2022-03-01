import unittest
from app.model import News


class NewsTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.news_object = News("Russia invades Ukraine: Live updates - CNN",
                                "Russia has ramped up war efforts, and President Putin ordered his country's deterrence forces — including nuclear arms — be placed on high alert. Follow here for live news updates from the ground in Ukraine.",
                                "https://cdn.cnn.com/cnnnext/dam/assets/220228120025-03-ukraine-0228-super-tease.jpg",
                                "Russian Prime Minister Mikhail Mishustin announced capital control measures to stop an exodus of foreign businesses from the country, Russian state news agencies TASS and RIA reported on Tuesday. Mi… [+1297 chars]",
                                "2022-03-01T12:41:00Z", "https://www.cnn.com/europe/live-news/ukraine-russia-putin-news-03-01-22/index.html")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_object, News))

    def test_init(self):
        '''
        test_init test case to test if the News object is initialized properly
        '''

        self.assertEqual(self.news_object.title, "Russia invades Ukraine: Live updates - CNN")
        self.assertEqual(self.news_object.description,
                         "Russia has ramped up war efforts, and President Putin ordered his country's deterrence forces — including nuclear arms — be placed on high alert. Follow here for live news updates from the ground in Ukraine.")
        self.assertEqual(self.news_object.urlToImage,
                         "https://cdn.cnn.com/cnnnext/dam/assets/220228120025-03-ukraine-0228-super-tease.jpg")
        self.assertEqual(self.news_object.content,
                         "Russian Prime Minister Mikhail Mishustin announced capital control measures to stop an exodus of foreign businesses from the country, Russian state news agencies TASS and RIA reported on Tuesday. Mi… [+1297 chars]")
        self.assertEqual(self.news_object.publishedAt, "2022-03-01T12:41:00Z")
        self.assertEqual(self.news_object.url, "https://www.cnn.com/europe/live-news/ukraine-russia-putin-news-03-01-22/index.html")
