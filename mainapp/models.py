from django.db import models


class LocationGame(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='где отображается на сайте')

    def __str__(self):
        return self.name




class Games(models.Model):
    site_location = models.ForeignKey(LocationGame, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    image = models.ImageField(upload_to='game_images')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)


    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __str__(self):
        return f'{self.name} ({self.site_location.name})'



