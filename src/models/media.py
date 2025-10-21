from abc import ABC

class Media(ABC):
    def __init__(self, title, year, genre=None):
        self.title = title
        self.year = year
        self.genre = genre

class Book(Media):
    def __init__(self, title, year, genre, author, pages):
        super().__init__(title, year, genre)
        self.author = author
        self.pages = pages

class Movie(Media):
    def __init__(self, title, year, genre, director, duration):
        super().__init__(title, year, genre)
        self.director = director
        self.duration = duration

class VideoGame(Media):
    def __init__(self, title, year, genre, platform, developer):
        super().__init__(title, year, genre)
        self.platform = platform
        self.developer = developer
