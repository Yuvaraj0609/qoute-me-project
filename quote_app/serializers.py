from rest_framework import serializers
from .models import ParcelQuote

class ParcelQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelQuote
        fields = '__all__'
