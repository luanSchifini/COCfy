from  django.db import models
from uuid import uuid4

from .group import Group 


class Student(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    student_name = models.CharField(max_length=30)
    eletiva_group = models.ForeignKey(Group, on_delete = models.CASCADE, null=True)
    
    def get_visits(self):
        visits = self.my_visits.count()

        return visits


    def __str__(self) -> str:
        return f'{self.student_name} -> {self.eletiva_group} -> {self.get_visits()} visitas'
    

