from  django.db import models
from uuid import uuid4

from .group import Group 


class Student(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    registration = models.IntegerField(null=True)
    student_name = models.CharField(max_length=50)
    anosemestre = models.IntegerField(null=True)
    student_class =models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.student_name)

    def get_visits(self):
        visits = self.my_visits.count()

        return visits

    # def __str__(self) -> str:
    #     return f'{self.registration} -> {self.student_name} -> {self.get_visits()} visitas'
    

