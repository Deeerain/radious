from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Ganre(models.Model):
    name = models.CharField('Название', max_length=100, unique=True,
                            db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('radio:ganre-detail', kwargs={'slug': self.slug})


class Radio(models.Model):
    name = models.CharField('Название', max_length=255, db_index=True)
    stream_url = models.URLField('Url потока', db_index=True, unique=True)
    ganre = models.ManyToManyField(verbose_name='Жанр', to=Ganre, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    created = models.DateField('Время создания', auto_now_add=True)
    visible = models.BooleanField('Видимость', default=True)
    preview = models.ImageField('Превью', upload_to='previews/', null=True,
                                blank=True)

    class Meta:
        verbose_name = 'Радио'
        verbose_name_plural = 'Радио'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('radio:radio-detail', kwargs={'slug': self.slug})


class Feedback(models.Model):
    username = models.CharField('Имя', max_length=100, db_index=True)
    email = models.EmailField('Электронная почта', db_index=True)
    rating = models.PositiveIntegerField('Оценка', db_index=True,
                                         validators=[MinValueValidator(0),
                                                     MaxValueValidator(5)])
    message = models.TextField('Сообщение', max_length=1000, blank=True,
                               null=True)
    radio = models.ForeignKey(verbose_name='Радио', to=Radio,
                              related_name='feedbacks',
                              on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', auto_now_add=True,
                                   db_index=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self) -> str:
        return self.username
