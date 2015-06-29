class Movie(object):
    """A simple representation of a Movie
    Attributes:
        movie_title = name of the movie
        poster_image_url = url to movie art
        trailer_youtube_url = youtube url to the movie trailer
    """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
