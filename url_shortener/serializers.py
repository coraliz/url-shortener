from rest_framework import serializers
from url_shortener.models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["id", "times_followed", "url", "url", "short_url"]