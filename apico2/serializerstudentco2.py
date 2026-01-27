from rest_framework import serializers


from apico2.models import Studentc02


class Studentc02Serializer(serializers.ModelSerializer):
    class Meta:
        model = Studentc02
        fields = '__all__'
        