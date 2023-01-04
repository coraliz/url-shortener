from django.core.validators import URLValidator
from django.db import models
from django.core.exceptions import ValidationError
from random import choice
from string import ascii_letters, digits

URL_LENGTH = 7
AVAILABLE_CHARS = ascii_letters + digits


def validate_short_url(short_url: str) -> None:
    """
    Makes sure that the short url consists of only 7 letters or numbers.
    """
    if not short_url.isalnum():
        raise ValidationError(f"The short url '{short_url}' is not valid. It must consist of only letters and numbers")
    if len(short_url) != URL_LENGTH:
        raise ValidationError(f"the short url '{short_url}' is not valid.Its length must be seven.")


def validate_url(long_url: str) -> None:
    """
    Makes sure the long url is valid by relying on Django's URLValidator function.
    """
    validator = URLValidator()
    try:
        validator(long_url)
    except ValidationError:
        raise ValidationError(f"The long url {long_url} is invalid. Please try again with a proper url.")


def create_random_code(chars=AVAILABLE_CHARS) -> str:
    """
    Creates a random string with the predetermined size.
    """
    return "".join(
        [choice(chars) for _ in range(URL_LENGTH)]
    )


class Shortener(models.Model):
    """
    Creates a shortened URL path according to the given URL.

    created -> Hour and date a shortener was created

    times_followed -> The number of visits the shortened link has received.

    url -> The original link

    short_url ->  shortened link https://domain/(short_url)
    """
    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    url = models.URLField(validators=[validate_url])

    # unique - build an index AND enforce unique constraint.
    short_url = models.CharField(max_length=URL_LENGTH, unique=True, blank=True, validators=[validate_short_url],
                                 default=create_random_code)

    def save(self, *args, **kwargs):
        """
        Saves the object in the DB. If the generated short url is already exists, this function will regenerate it
        and try to save this object for a limited number of attempts.
        """
        tries = 3
        for i in range(0, tries):
            try:
                self.full_clean()
                super().save(*args, **kwargs)
                break
            except ValidationError as e:
                if (short_url_error := e.error_dict.get('short_url')) is None or short_url_error[0].code != 'unique':
                    raise
                else:
                    print("Trying to save the object again with a different short url.")
                    self.short_url = create_random_code()
