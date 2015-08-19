# media.py


class Movie(object):
    """ Movie class for creating a movie """
    def __init__(self,
                 title,
                 storyline,
                 poster_image_url,
                 trailer_youtube_url,
                 lead_actors,
                 release_date,
                 mpaa_rating,
                 language,
                 runtime,
                 production_companies,
                 trivia
                 ):
        """
        Args:
            title (str): Title of the movie.
            storyline (str): Brief storyline of the movie.
            poster_image_url (str): URL of the movie's poster image.
            trailer_youtube_url (str): Youtube URL of the movie's trailer.
            lead_actors (List[str]): A list of the main cast.
            release_date (str): Release date of the movie.
            mpaa_rating (str): MPAA rating of the movie.
            language (str): Language of the movie.
            runtime (str): Runtime of the movie.
            production_companies (List[str]): A list of the production companies.
            trivia (List[str]): A list of some movie trivia.
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.lead_actors = lead_actors
        self.release_date = release_date
        self.mpaa_rating = mpaa_rating
        self.language = language
        self.runtime = runtime
        self.production_companies = production_companies
        self.trivia = trivia

