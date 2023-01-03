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
        try:
            return Shortener.objects.get(short_url=short_url)
        except Shortener.DoesNotExist:
            raise Http404

    def get(self, request, short_url):
        shortener = self.get_object(short_url)
        # avoid a race condition by using the F expression
        Shortener.objects.filter(short_url=short_url).update(times_followed=F('times_followed') + 1)
        return redirect(shortener.url)

    @staticmethod
    def post(request):
        data = JSONParser().parse(request)
        serializer = ShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            short_url = serializer.data["short_url"]
            short_url_path = f"/s/{short_url}"
            return Response(request.build_absolute_uri(short_url_path), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @staticmethod
# def get(request, short_url):
#     try:
#         shortener = Shortener.objects.get(short_url=short_url)
#         Shortener.objects.filter(short_url=short_url).update(times_followed=F('times_followed') + 1)
#         return redirect(shortener.url)
#     except Shortener.DoesNotExist:
#         raise Http404

# @api_view(['POST'])
# def create_short_url(request):
#     if request.method == 'POST':
#         try:
#             long_url = json.loads(request.body)["url"]
#             shortener = Shortener.objects.create(long_url=long_url)
#             short_url_path = f"/{SHORT_URL_PATH}/{shortener.short_url}"
#             return HttpResponse(request.build_absolute_uri(short_url_path), status=status.HTTP_201_CREATED)
#         except ValidationError as e:
#             return HttpResponseBadRequest(e.message)
#
#
# @api_view(['POST'])
# def create_short_url(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ShortenerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             short_url = serializer.data["short_url"]
#             short_url_path = f"/{SHORT_URL_PATH}/{short_url}"
#             return Response(request.build_absolute_uri(short_url_path), status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def redirect_url_view(request, shortened_part):
#     try:
#         if request.method == 'GET':
#             shortener = Shortener.objects.get(short_url=shortened_part)
#             # to avoid a race condition we'll use the F expression
#             Shortener.objects.filter(short_url=shortened_part).update(times_followed=F('times_followed') + 1)
#             return redirect(shortener.url)
#             return HttpResponseRedirect(shortener.url)
#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# def redirect_url_view(request, shortened_part):
#     try:
#         if request.method == 'GET':  # todo: get?
#             shortener = Shortener.objects.get(short_url=shortened_part)
#             # to avoid a race condition we'll use the F expression
#             Shortener.objects.filter(short_url=shortened_part).update(times_followed=F('times_followed')+1)
#             return HttpResponseRedirect(shortener.long_url)
#     except ObjectDoesNotExist:
#         raise Http404('Sorry this link does not exist :(')
