from rest_framework import serializers
from .models import Studentc01


class StudentC01Serializer(serializers.ModelSerializer):
    class Meta:
        model = Studentc01
        fields = '__all__'
        