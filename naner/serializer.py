from rest_framework import serializers
from naner.models import  Nota, Jogo



class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'
