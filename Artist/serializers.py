from rest_framework import serializers
from Artist.models import ArtistModel


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ["name"]
