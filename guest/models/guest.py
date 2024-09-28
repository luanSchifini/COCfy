from  django.db import models

from .student import Student

class Guest(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=100, null=True)
    verification_code = models.CharField(max_length=5, null=True)
    student_visited = models.ForeignKey(Student, on_delete = models.CASCADE, null=True, related_name='my_visits')
    evaluation = models.IntegerField(null=True)
    def __str__(self) -> str:
        if self.name is None:
            return f'visita anonima -> {self.evaluation}'

        return f'{self.name} ({self.email}) -> {self.student_visited}'
    
