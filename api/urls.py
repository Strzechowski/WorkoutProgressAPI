from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('profiles', views.ProfileView)
router.register('trainings', views.TrainingView)
router.register('exercises', views.ExerciseView)
router.register('sets', views.SetView)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]
