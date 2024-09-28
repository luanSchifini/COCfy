from  django.db import models

class Eletiva(models.Model):
    eletiva_name = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.eletiva_name} ({self.pk})'





