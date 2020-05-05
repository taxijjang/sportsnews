from .models import NaverSports
from rest_framework import serializers

class NaverSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaverSports

        fields = ('rank','url','title')
        #read_only_fields = ('id',)

