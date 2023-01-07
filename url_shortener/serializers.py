from rest_framework import serializers
from url_shortener.models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["id", "url", "short_url", "times_followed", "created"]
