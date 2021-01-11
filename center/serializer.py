from rest_framework import serializers
from .models import Center

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'employee', 'anouncment')
        model = Center