from .models import url_data

from rest_framework import serializers

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = url_data
        fields = ('id', 'url', 'count', 'date_updated', 'date_added')