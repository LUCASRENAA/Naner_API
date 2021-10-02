from rest_framework import serializers
from naner.models import  Milhar_Jogo, Jogo



class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milhar_Jogo
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'
