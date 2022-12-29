from django.core.validators import URLValidator
from django.db import models
from django.core.exceptions import ValidationError
from random import choice
from string import ascii_letters, digits

MAXIMUM_URL_CHARS = 7
AVAILABLE_CHARS = ascii_letters + digits


def validate_short_url(short_url: str) -> None:
    """
    Makes sure that the short url consists of only 7 letters or numbers.
    """
    if not short_url.isalnum():
        raise ValidationError(f"The short url '{short_url}' is not valid. It must consist of only letters and numbers")
    if len(short_url) != MAXIMUM_URL_CHARS:
        raise ValidationError(f"the short url '{short_url}' is not valid.Its length must be seven.")


def validate_long_url(long_url: str) -> None:
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
    # we have 7 places where there can be up to 62 available characters for each place.
    # Therefore, the possible permutations are 2,478,652,606,080.
    # todo: define the letters here?
    return "".join(
        [choice(chars) for _ in range(MAXIMUM_URL_CHARS)]
        )


class Shortener(models.Model):
    """
    Creates a shortened URL path according to the given URL.

    created -> Hour and date a shortener was created

    times_followed -> The number of visits the shortened link has received.

    long_url -> The original link

    short_url ->  shortened link https://domain/(short_url)
    """
    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    long_url = models.URLField(validators=[validate_long_url])

    # unique - build an index AND enforce unique constraint.
    short_url = models.CharField(max_length=15, unique=True, blank=True, validators=[validate_short_url],
                                 default=create_random_code)

    def __str__(self):
        return f'created={self.created} || times_followed={self.times_followed} || long_url={self.long_url} ' \
               f'|| short_url={self.short_url}'

    def save(self, *args, **kwargs):
        """
        Saves the object in the DB. If the generated short url is already exists, this function will regenerate it
        and try to save this object for a limited number of attempts.
        """
        tries = 3
        for i in range(0, tries):
            try:
                if not self.short_url:
                    self.short_url = self.__create_random_code()
                self.full_clean()
                super().save(*args, **kwargs)
                break
            except ValidationError as e:
                if e.messages == ['Shortener with this Short url already exists.']:
                    print("This short url already exists. Trying to save the object again with a different short url.")
                    self.short_url = self.__create_random_code()
                else:
                    raise
