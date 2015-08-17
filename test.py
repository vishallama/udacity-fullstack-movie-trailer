# test.py
import unittest
from entertainment_center \
    import city_lights, shawshank_redemption, godfather


# Test: City Lights
class MovieTestCityLights(unittest.TestCase):

    def test_title(self):
        self.assertEqual(
            "City Lights", city_lights.title)

    def test_poster_image_url(self):
        self.assertEqual(
            "https://upload.wikimedia.org/wikipedia/en/f/f2/City_Lights_film.jpg",
            city_lights.poster_image_url)

    def test_trailer_youtube_url(self):
        self.assertEqual(
            "https://www.youtube.com/watch?v=b2NTUnujk1I",
            city_lights.trailer_youtube_url)

    def test_lead_actors_charles_chaplin(self):
        self.assertEqual("Charles Chaplin", city_lights.lead_actors[0])

    def test_lead_actors_hank_mann(self):
        self.assertEqual("Hank Mann", city_lights.lead_actors[-1])

    def test_release_date(self):
        self.assertEqual("7 March 1931", city_lights.release_date)

    def test_trivia(self):
        self.assertEqual(
            "Charles Chaplin's personal favorite of all his films.",
            city_lights.trivia[1])


# Test: The Shawshank Redemption
class MovieTestShawshankRedemption(unittest.TestCase):

    def test_title(self):
        self.assertEqual(
            "The Shawshank Redemption", shawshank_redemption.title)

    def test_poster_image_url(self):
        self.assertEqual(
            "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
            shawshank_redemption.poster_image_url)

    def test_trailer_youtube_url(self):
        self.assertEqual(
            "https://www.youtube.com/watch?v=6hB3S9bIaco",
            shawshank_redemption.trailer_youtube_url)

    def test_lead_actors_charles_chaplin(self):
        self.assertEqual("Tim Robbins", shawshank_redemption.lead_actors[0])

    def test_lead_actors_hank_mann(self):
        self.assertEqual("James Whitmore", shawshank_redemption.lead_actors[-1])

    def test_release_date(self):
        self.assertEqual("14 October 1994", shawshank_redemption.release_date)

    def test_trivia(self):
        self.assertEqual(
            "Morgan Freeman's favorite film of his own.",
            shawshank_redemption.trivia[0])


# Test: The Godfather
class MovieTestGodfather(unittest.TestCase):

    def test_title(self):
        self.assertEqual(
            "The Godfather",godfather.title)

    def test_poster_image_url(self):
        self.assertEqual(
            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
            godfather.poster_image_url)

    def test_trailer_youtube_url(self):
        self.assertEqual(
            "https://www.youtube.com/watch?v=sY1S34973zA",
            godfather.trailer_youtube_url)

    def test_lead_actors_charles_chaplin(self):
        self.assertEqual("Marlon Brando", godfather.lead_actors[0])

    def test_lead_actors_hank_mann(self):
        self.assertEqual("Diane Keaton", godfather.lead_actors[-1])

    def test_release_date(self):
        self.assertEqual("24 March 1972", godfather.release_date)

    def test_trivia(self):
        self.assertEqual(
            "According to Francis Ford Coppola, the film took 62 days to shoot.",
            godfather.trivia[-1])


if __name__ == '__main__':
    unittest.main()

