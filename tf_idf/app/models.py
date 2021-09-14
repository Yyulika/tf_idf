from django.db import models
import uuid


class Files(models.Model):
    name = models.CharField('Имя файла', max_length=150)

    def __str__(self):
        return self.name


def save(self, *args, **kwargs):
    self.name = str(uuid.uuid4())
    super(Files, self).save(*args, **kwargs)
