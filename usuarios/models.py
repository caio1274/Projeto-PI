from django.db import models

class Usuarios(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.email