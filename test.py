# test.py
import unittest
from entertainment_center import city_lights


# Test: City Lights
class MovieTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()

