from django.db import models


class BooksModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kitob'
        verbose_name_plural = 'kitoblar'


