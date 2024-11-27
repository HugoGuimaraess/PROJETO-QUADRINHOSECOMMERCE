from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Loja(models.Model):
    OPCAO=[
        ('DC','DC'),
        ('MARVEL','Marvel'),
        ('IMAGE COMICS','Image Comics'),
        ('CGC','CGC')
    ]

    OPCAO2 = [
        ('a','a'),
        ('BATMAN','Batman'),
        ('SUPERMAN','Superman'),
        ('HOMEM ARANHA','Homem aranha'),
        ('FLASH','Flash'),
        ('MULHER MARAVILHA','Mulher Maravilha'),
        ('HOMEM DE FERRO','Homem de Ferro'),
        ('HULK','Hulk'),
    ]

    quadrinho = models.CharField(max_length=100,null=False,blank=False)
    categoria = models.CharField(max_length=100,default='',choices=OPCAO)
    categoria_favoritos = models.CharField(max_length=100,default='a',choices=OPCAO2)
    roterista = models.CharField(max_length=100,null=False,blank=False)
    artista = models.CharField(max_length=100,null=False,blank=False)
    arte_capa = models.CharField(max_length=100,null=False,blank=False)
    prevenda = models.BooleanField(default=False)
    descricao = models.TextField(null=False,blank=False)
    disponivel = models.BooleanField(default=True)
    data = models.DateTimeField(default=datetime.now,blank=False)
    foto = models.ImageField(upload_to='Fotos/%Y/%m/%d/',blank=True)
    usuario = models.ForeignKey(
        to=User,
        related_name='user',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    preco = models.IntegerField()
    stock = models.IntegerField()




    def __str__(self):
        return self.quadrinho