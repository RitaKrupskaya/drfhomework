from django.db import models

from config import settings


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Course", help_text="Укажите название курса"
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Preview",
        help_text="Загрузите превью курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Добавьте описание курса",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Owner",
        null=True,
        blank=True,
        help_text="Укажите владельца курса",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Lesson", help_text="Укажите название урока"
    )
    preview = models.ImageField(
        upload_to="lms/preview",
        blank=True,
        null=True,
        verbose_name="Preview",
        help_text="Загрузите превью урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Добавьте описание урока",
    )
    url_on_video = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL on Video",
        help_text="Добавьте ссылку на видео",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Course",
        related_name="lessons",
        blank=True,
        null=True,
        help_text="Выберите курс",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Owner",
        null=True,
        blank=True,
        help_text="Укажите владельца урока",
    )

    def __str__(self):
        return {self.name}

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
