from rest_framework import serializers
from .models import Profile, Training, Exercise, Set, User

class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    sets = SetSerializer(many=True)
    class Meta:
        model = Exercise
        fields = '__all__'

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = Training
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    trainings = TrainingSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'trainings', 'profile']