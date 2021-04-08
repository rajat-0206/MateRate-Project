from django.db import models


# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000,null=False)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Responses(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey('Questions',on_delete=models.CASCADE)
    name = models.CharField(max_length=500,null=False)
    response = models.CharField(max_length=500)

