"""
Shortener views
"""

from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db.models import F


# Model
from .models import Shortener
import json


SHORT_URL_PATH = "s"


@csrf_exempt
def create_short_url(request):
    if request.method == 'POST':
        try:
            long_url = json.loads(request.body)["url"]
            shortener = Shortener.objects.create(long_url=long_url)
            short_url_path = f"/{SHORT_URL_PATH}/{shortener.short_url}"
            return HttpResponse(request.build_absolute_uri(short_url_path), status=200)
        except ValidationError as e:
            return HttpResponseBadRequest(e.message)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        # to avoid a race condition we'll use the F expression
        Shortener.objects.filter(short_url=shortened_part).update(times_followed=F('times_followed')+1)
        return HttpResponseRedirect(shortener.long_url)
    except ObjectDoesNotExist:
        raise Http404('Sorry this link does not exist :(')
