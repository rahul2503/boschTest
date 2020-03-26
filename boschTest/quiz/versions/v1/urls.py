# from django.conf.urls import url
from django.urls import path
from .views import QuizCategoryView

urlpatterns = [
    path('quiz/categories', QuizCategoryView.as_view(), name='quiz_category'),
]