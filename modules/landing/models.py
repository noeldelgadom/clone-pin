from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        null=True
    )
    image = models.ImageField(upload_to='images/')
