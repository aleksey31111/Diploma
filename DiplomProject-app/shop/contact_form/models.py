from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    email = models.EmailField(max_length=200, verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Сообщение")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['-time']
