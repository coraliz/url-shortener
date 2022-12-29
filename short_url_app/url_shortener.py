from random import choice
from string import ascii_letters, digits

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


# def create_random_code(chars=AVAILABLE_CHARS) -> str:
#     """
#     Creates a random string with the predetermined size.
#     """
#     # we have 7 places where there can be up to 62 available characters for each place.
#     # Therefore, the possible permutations are 2,478,652,606,080
#     return "".join(
#         [choice(chars) for _ in range(MAXIMUM_URL_CHARS)]
#     )
#
#
#     return random_code
