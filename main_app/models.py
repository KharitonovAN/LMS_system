from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """Модель для сущности Course"""
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='course.py/', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.description} / {self.course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель для сущности Lesson"""
    title = models.CharField(max_length=150, default='User', verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='Изображение', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey('main_app.Course', related_name='name_course',
                               on_delete=models.CASCADE, verbose_name='Курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title} / {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
