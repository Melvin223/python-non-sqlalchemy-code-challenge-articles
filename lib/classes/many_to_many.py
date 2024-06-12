class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.author.articles.append(self)
        self.magazine.articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value
        
class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article
    
    def magazines(self):
        magazines = set([article.magazine for article in self.articles])
        return list(magazines)

    def topic_areas(self):
        if not self.articles:
            return None
        topics = set([article.magazine.category for article in self.articles])
        return list(topics)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self.articles

    def contributors(self):
        authors = set([article.author for article in self.articles])
        return list(authors)

    def article_titles(self):
        if not self.articles:
            return None
        titles = [article.title for article in self.articles]
        return titles

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        if not contributing_authors:
            return None
        return contributing_authors

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazines = {}
        for article in Article.all:
            magazine = article.magazine
            magazines[magazine] = magazines.get(magazine, 0) + 1
        top_magazine = max(magazines, key=magazines.get)
        return top_magazine