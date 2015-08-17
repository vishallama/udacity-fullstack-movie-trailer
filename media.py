# media.py

class Movie(object):
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

