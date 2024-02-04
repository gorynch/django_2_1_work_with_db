from django.db import models
from django.utils import timezone


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    release_date = models.DateTimeField(default=timezone.now)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", default='', null=False)

    def __str__(self):
        return f'model - {self.name}, price - {self.price}, lte -  {self.lte_exists}'

