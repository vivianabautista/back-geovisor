from django.urls import path
from .views import FormView, SectionView, QuestionView, QuestionTypeView

urlpatterns = [
    path("form/", FormView.as_view()),
    path("form/<str:search>/", FormView.as_view()),
    path("section/<str:search>/", SectionView.as_view()),
    path("section/", SectionView.as_view()),
    path("question/<str:search>/", QuestionView.as_view()),
    path("question/", QuestionView.as_view()),
    path("question-type/", QuestionTypeView.as_view())
    
]
