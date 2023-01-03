from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import redirect
from django.db.models import F
from django.http import Http404
from short_url_app.models import Shortener
from short_url_app.serializers import ShortenerSerializer


class ShortenerDetail(APIView):
    """
    Create, retrieve and update a shortener instance.
    """
    @staticmethod
    def get_object(short_url):
        """
        Gets the shortener object from the DB.
        """
        try:
            return Shortener.objects.get(short_url=short_url)
        except Shortener.DoesNotExist:
            raise Http404

    def get(self, request, short_url):
        """
        Redirects to the relevant url according to the short url.
        """
        shortener = self.get_object(short_url)
        # avoid a race condition when update a shortener object by using the F expression
        Shortener.objects.filter(short_url=short_url).update(times_followed=F('times_followed') + 1)
        return redirect(shortener.url)

    @staticmethod
    def post(request):
        """
        Creates a new shortener object in the db.
        """
        data = JSONParser().parse(request)
        serializer = ShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            short_url = serializer.data["short_url"]
            short_url_path = f"/s/{short_url}"
            return Response(request.build_absolute_uri(short_url_path), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)