from rest_framework import serializers
from provider.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'id',
            'name',
            'url',
            'email',
            'phone',
        )
