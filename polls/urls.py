from django.urls import path
from .views import FormSearchView

urlpatterns = [
    path('form/', FormSearchView.as_view()),                # Para traer todos si no hay búsqueda
    path('form/<str:search>/', FormSearchView.as_view()),   # Para buscar por palabra
]