from django.test import TestCase
from short_url_app.models import Shortener
from django.core.exceptions import ValidationError


# todo: add this case to tests -> Shortener.objects.create()
# todo: handle those that have the specific domain written in them
class ShortenerTestCase(TestCase):
    def setUp(self):
        Shortener.objects.create(long_url="https://docs.djangoproject.com")
        # Shortener.objects.create(long_url="https://stackoverflow.com")

    def test_short_url_length(self):
        djangoproject = Shortener.objects.get(long_url="https://docs.djangoproject.com")
        stackoverflow = Shortener.objects.get(long_url="https://www.stackoverflow.com")
        self.assertEqual(len(djangoproject.short_url), 7)
        # self.assertEqual(len(stackoverflow.short_url), 7)

    # def test_short_url_randomness(self):
    #     djangoproject = Shortener.objects.get(long_url="https://docs.djangoproject.com")
    #     stackoverflow = Shortener.objects.get(long_url="https://www.stackoverflow.com")
    #     self.assertNotEqual(djangoproject.short_url, stackoverflow.short_url)
    #
    # def test_invalid_log_url_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="wwwwwww")
    #         self.fail('Succeeded in creating an object when it received an invalid long url')
    #     except ValidationError:
    #         pass
    #
    # def test_invalid_short_url_characters_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="https://www.google.com/", short_url="14--")
    #         self.fail('Succeeded in creating an object when it received an invalid short url characters')
    #     except ValidationError:
    #         pass
    #
    # def test_invalid_short_url_length_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="https://www.google.com/", short_url="ABDcccccccc")
    #         self.fail('Succeeded in creating an object when it received an invalid short url length')
    #     except ValidationError:
    #         pass
    #
    # def test_invalid_short_url_unique(self):
    #     djangoproject = Shortener.objects.get(long_url="https://docs.djangoproject.com")
    #     stackoverflow = Shortener.objects.get(long_url="https://www.stackoverflow.com",
    #                                           short_url=djangoproject.short_url)
    #     self.assertNotEqual(djangoproject.short_url, stackoverflow.short_url)
    #
    # def test_short_url_redirection(self):
    #     wolframalpha = Shortener.objects.get(long_url="https://www.wolframalpha.com")
    #     s = 'http://127.0.0.1:8000/s/' + wolframalpha.short_url
    #     response = self.client.get(s)
    #     self.assertRedirects(response, wolframalpha.long_url, fetch_redirect_response=False)
    #
    # def test_short_url_failure_redirection(self):
    #     response = self.client.get('http://127.0.0.1:8000/s/1122') # this shor url is not valid
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_times_followed_update(self):
    #     wolframalpha = Shortener.objects.get(long_url="https://www.wolframalpha.com")
    #     s = 'http://127.0.0.1:8000/s/' + wolframalpha.short_url
    #     times_followed = wolframalpha.times_followed
    #     self.client.get(s)
    #     wolframalpha = Shortener.objects.get(long_url="https://www.wolframalpha.com")
    #     self.assertEqual(wolframalpha.times_followed, times_followed+1)
