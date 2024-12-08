from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, CursoViewSet, InscripcionViewSet, ProfesorViewSet
from . import views


router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'profesores', ProfesorViewSet, basename='profesores')

urlpatterns = [
    path('', include(router.urls)), 
    path('custom-api/', views.CustomAPI.as_view(), name='custom_api'),
    
]

