from django.db import models
#from django.contrib.auth.models import User
from modules.users.models import User
from django.contrib.postgres.fields import ArrayField

def user_directory_path(instance, filename):
    # file will be oploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.usuario.id, filename)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        null=True
    )
    image = models.ImageField(upload_to=user_directory_path)
