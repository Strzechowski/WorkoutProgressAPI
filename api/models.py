from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length = 30, blank=True, null=True)
    surname = models.CharField(max_length = 30, blank=True, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(
        validators = [MaxValueValidator(130), MinValueValidator(1)],
        blank=True,
        null=True
    )
    sex = models.CharField(
        choices = [
            ('Man', 'Man'),
            ('Woman', 'Woman'),
        ],
        max_length = 5,
        blank=True,
        null=True
    ),
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user

class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainings')
    name = models.CharField(max_length = 30)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + ' ' + self.name

class Exercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    weight = models.FloatField(validators=[MinValueValidator(0)])
    repetitions = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.exercise.name + ' set #' + str(self.pk)