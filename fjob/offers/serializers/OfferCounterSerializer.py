from rest_framework import serializers


class OfferCounterSerializer(serializers.Serializer):
    count = serializers.IntegerField()
