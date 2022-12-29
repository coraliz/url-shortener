from django.test import TestCase
from short_url_app.models import Shortener
from django.core.exceptions import ValidationError


# todo: add this case to tests -> Shortener.objects.create()
# todo: handle those that have the specific domain written in them
class ShortenerTestCase(TestCase):
    def setUp(self):
        pass
        # Shortener.objects.create(long_url="https://docs.djangoproject.com")
        # Shortener.objects.create(long_url="https://www.wolframalpha.com")

    # def test_short_url_length(self):
    #     djangoproject = Shortener.objects.get(long_url="https://docs.djangoproject.com")
    #     wolframalpha = Shortener.objects.get(long_url="https://www.wolframalpha.com")
    #     self.assertEqual(len(djangoproject.short_url), 7)
    #     self.assertEqual(len(wolframalpha.short_url), 7)
    #
    # todo: def test_randon_str (contains only strings I want), test_randomness
    # def test_get_or_create_transaction(self):
    #     (new1, created1) = Shortener.objects.get_or_create(long_url="https://docs.coralavitan.com", short_url="ABCtzx")
    #     if created1:
    #         print("created")
    #     print(new1)
    #     (new2, created2) = Shortener.objects.get_or_create(long_url="https://docs.corala.com", short_url="ABCtzx")
    #     if created2:
    #         print("created")
    #     print(new2)
    # def test_invalid_short_url_chars_exception(self):
    #     Shortener.objects.create(long_url="https://www.google.com/", short_url="14--")

    # def test_invalid_log_url_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="wwwwwww")
    #         self.fail('Succeeded in creating an object when it received an invalid long url')
    #     except ValidationError:
    #         pass
    #
    # def test_invalid_short_url_chars_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="https://www.google.com/", short_url="14--")
    #         self.fail('Succeeded in creating an object when it received an invalid short url chars')
    #     except ValidationError:
    #         pass
    #
    # def test_invalid_short_url_length_exception(self):
    #     try:
    #         Shortener.objects.create(long_url="https://www.googlee.com/", short_url="ABDcccccccc")
    #         self.fail('Succeeded in creating an object when it received an invalid short url length')
    #     except ValidationError:
    #         pass

    def test_invalid_short_url_unique(self):
        first = Shortener.objects.create(long_url="https://docs.djangoproject123.com")
        second = Shortener.objects.create(long_url="https://docs.djangoproject.com", short_url=first.short_url)
        Shortener.objects.create(long_url="https://docs.djangoprojectrtr.com", short_url="14//55")
    # try:
    #     first = Shortener.objects.get(long_url="https://docs.djangoproject.com")
    #     second = Shortener.objects.create(long_url="https://docs.djangoproject.com", short_url=first.short_url)
    #     self.fail('Succeeded in creating an object when it received an invalid short url length')
    # except ValidationError as e:
    #     print(e.message)

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

    # def test_invalid_short_url(self):
    #     a = Shortener.objects.create(long_url="https://stackoverflowwwww.com", short_url="ABCdefg")
    #     print("HERE")
    #     b =  Shortener.objects.create(long_url="https://stackoverflow.com", short_url="ABCdefg")
    #     stackoverflow = Shortener.objects.get(long_url="https://stackoverflow.com")
    #     self.assertNotEqual(a.short_url, b.short_url)
