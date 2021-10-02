from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models



class Jogo(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, models.CASCADE)
    data_criado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
class Milhar_Jogo(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)
    milhar = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(9999)])
    nome = models.ForeignKey(Jogo, models.CASCADE)
