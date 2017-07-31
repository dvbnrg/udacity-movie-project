import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

VALID_RAINGS = ["G",
                "PG",
                "PG-13",
                "R"]


def __init__(bob, movie_title, movie_storyline, poster_image, trailer_youtube):
        bob.title = movie_title
        bob.storyline = movie_storyline
        bob.poster_image_url = poster_image
        bob.trailer_youtube_url = trailer_youtube


def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
