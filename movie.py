class Movie:
    def __init__(self, id, title, poster, overview=None, genere=None, budget=None, cast=None):
        self.id = id
        self.title = title
        self.poster = poster
        self.overview = overview
        self.genere = genere
        self.budget = budget
        self.cast = cast