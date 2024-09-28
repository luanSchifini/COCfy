from  django.db import models

from .group import Group 

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    eletiva_group = models.ForeignKey(Group, on_delete = models.CASCADE, null=True)
    
    def get_visits(self):
        # guests_that_visited_me = Guest.objects.filter(student_visited=self)
        # visits = len(guests_that_visited_me)

        # visits = Guest.objects.filter(student_visited=self).count()

        visits = self.my_visits.count()

        return visits


    def __str__(self) -> str:
        return f'{self.student_name} -> {self.eletiva_group} -> {self.get_visits()}'
