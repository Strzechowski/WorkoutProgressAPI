from rest_framework import serializers
from .models import Profile, Training, Exercise, Set, User

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True, read_only=True)
    class Meta:
        model = Exercise
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = Training
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    trainings = TrainingSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'trainings', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

