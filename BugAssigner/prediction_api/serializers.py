from rest_framework import serializers
from .models import Result, Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'description',)
        model = Request

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('request','result',)
        model = Result
