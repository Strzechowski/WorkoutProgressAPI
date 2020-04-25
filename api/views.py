from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile, Training, Exercise, Set, User
from .serializers import ProfileSerializer, TrainingSerializer, ExerciseSerializer, SetSerializer, UserSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class ExerciseView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class SetView(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer