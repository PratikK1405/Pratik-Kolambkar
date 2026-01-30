from django.urls import path, include
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import (
    ProfileViewSet, ProjectViewSet, SkillViewSet,
    ExperienceViewSet, EducationViewSet, contact_submit
)

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'education', EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_submit, name='contact'),
]