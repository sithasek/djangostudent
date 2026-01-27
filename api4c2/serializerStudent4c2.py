from rest_framework import serializers
from api4c2.models import Student4c2
class Student4c2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student4c2
        fields = '__all__'

