from  django.db import models
from uuid import uuid4

from .student import Student

class Guest(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=100, null=True)
    # cpf = models.CharField(max_length=11, null=True)
    verification_code = models.CharField(max_length=11, null=True)
    student_visited = models.ForeignKey(Student, on_delete = models.CASCADE, null=True, related_name='my_visits')
    evaluation = models.IntegerField(null=True)

    def __str__(self) -> str:
        evaluation = self.get_evaluation() 
        if self.name is None:
            return f'visita anonima -> {evaluation}'

        return f'{self.name} - {evaluation} -> {self.student_visited}'

    def get_evaluation(self):
        if self.evaluation == 1:
            return 'regular' 
            
        if self.evaluation == 2:
            return 'bom' 

        if self.evaluation == 3:
            return 'ótimo' 
    
