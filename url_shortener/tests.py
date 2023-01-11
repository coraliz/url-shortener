from django.test import TransactionTestCase
from url_shortener.models import Shortener, URL_LENGTH
from django.core.exceptions import ValidationError


class UrlShortenerTestCase(TransactionTestCase):
    def setUp(self):
        self.djangoproject = Shortener.objects.create(url="https://docs.djangoproject.com")
        self.stackoverflow = Shortener.objects.create(url="https://stackoverflow.com")

    def test_short_url_length(self):
        self.assertEqual(len(self.djangoproject.short_url), URL_LENGTH)
        self.assertEqual(len(self.stackoverflow.short_url), URL_LENGTH)

    def test_short_url_randomness(self):
        self.assertNotEqual(self.djangoproject.short_url, self.stackoverflow.short_url)

    def test_invalid_url_exception(self):
        try:
            Shortener.objects.create(url="wwwwwww")
            self.fail('Succeeded in creating an object when it received an invalid long url')
        except ValidationError:
            pass

    def test_invalid_short_url_characters_exception(self):
        try:
            Shortener.objects.create(url="https://www.google.com/", short_url="14--")
            self.fail('Succeeded in creating an object when it received an invalid short url characters')
        except ValidationError:
            pass

    def test_invalid_short_url_length_exception(self):
        try:
            Shortener.objects.create(url="https://www.google.com/", short_url="ABDcccccccc")
            self.fail('Succeeded in creating an object when it received an invalid short url length')
        except ValidationError:
            pass

    def test_invalid_short_url_unique(self):
        google = Shortener.objects.create(url="https://www.google.com",
                                          short_url=self.djangoproject.short_url)
        self.assertNotEqual(self.djangoproject.short_url, google.short_url)

    def test_short_url_redirection(self):
        s = 'http://127.0.0.1:8000/s/' + self.djangoproject.short_url
        response = self.client.get(s)
        self.assertRedirects(response, self.djangoproject.url, status_code=302, fetch_redirect_response=False)

    def test_short_url_failure_redirection(self):
        response = self.client.get('http://127.0.0.1:8000/s/1122')
        self.assertEqual(response.status_code, 404)

    def test_times_followed_update(self):
        times_followed = self.djangoproject.times_followed
        s = 'http://127.0.0.1:8000/s/' + self.djangoproject.short_url
        self.client.get(s)
        self.djangoproject.refresh_from_db()
        self.assertEqual(self.djangoproject.times_followed, times_followed + 1)
        self.client.get(s)
        self.djangoproject.refresh_from_db()
        self.assertEqual(self.djangoproject.times_followed, times_followed + 2)
