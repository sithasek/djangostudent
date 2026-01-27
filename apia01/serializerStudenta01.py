from rest_framework import serializers
from .models import Studenta01
class Studenta01Serializer(serializers.ModelSerializer):
    class Meta:
        model = Studenta01
        fields = '__all__'