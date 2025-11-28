from django.urls import path
from . import views
from .views import QuizListAPI

urlpatterns = [

    # ----------------------------
    # Public pages
    # ----------------------------
    path('', views.home, name="home"),
    path('events/', views.events, name="events"),

    # ----------------------------
    # Quizzes list page
    # ----------------------------
    path('quizzes/', views.quizzes_list, name='quizzes'),

    # ----------------------------
    # Quiz attempt + Result
    # ----------------------------
    path('quiz/<int:quiz_id>/', views.quiz_attempt, name="quiz_attempt"),
    path('result/<int:submission_id>/', views.result, name="result"),

    # ----------------------------
    # User history
    # ----------------------------
    path('my-history/', views.quiz_history, name='quiz_history'),

    # ----------------------------
    # Authentication
    # ----------------------------
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ----------------------------
    # Dashboard
    # ----------------------------
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/add-quiz/", views.add_quiz, name="add_quiz"),

    # ----------------------------
    # API
    # ----------------------------
    path("api/quizzes/", QuizListAPI.as_view(), name="api_quizzes"),
]
