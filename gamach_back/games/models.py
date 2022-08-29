from django.db import models


class Games(models.Model):
    PC_REQUIREMENTS = [
        (1, 'Суперкомпьютер'),
        (2, 'Уверенный середнячок'),
        (3, 'Умная колонка')
    ]
    Tor_Available = [
        (1, 'Да'),
        (2, 'Нет')
    ]
    requirements = models.PositiveSmallIntegerField(choices=PC_REQUIREMENTS, default=2, verbose_name="Системные "
                                                                                                     "требования")
    title = models.CharField(blank=True, max_length=256, verbose_name="Название игры")
    release_date = models.DateField(blank=True, verbose_name="Дата релиза")
    description = models.CharField(blank=True, max_length=1000, verbose_name="Описание")
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', verbose_name="Картинка")
    torrent_available = models.PositiveSmallIntegerField(choices=Tor_Available, default=1, verbose_name="Альтернативно"
                                                                                                        " бесплатно?")
