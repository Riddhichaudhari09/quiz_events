from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions

from .serializers import QuizSerializer
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event


# ----------------------------
# PUBLIC PAGES
# ----------------------------

def home(request):
    return render(request, "quizapp/home.html")


def events(request):
    events_list = Event.objects.all().order_by("date")
    return render(request, "quizapp/events.html", {"events": events_list})


def result(request, submission_id):
    submission = UserSubmission.objects.get(id=submission_id)
    return render(request, "quizapp/result.html", {"submission": submission})


# ----------------------------
# AUTHENTICATION
# ----------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")     # redirect to dashboard

    return render(request, "quizapp/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")                 # redirect to login after logout


# ----------------------------
# REST API (Bonus Feature)
# ----------------------------

class QuizListAPI(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# LOGGED-IN USER FEATURES
# ----------------------------

@login_required(login_url='login')
def dashboard(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizapp/dashboard.html", {"quizzes": quizzes})


@login_required(login_url='login')
def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        user_name = request.user.username   # always logged-in user's name

        submission = UserSubmission.objects.create(
            quiz=quiz,
            user_name=user_name,
            score=0
        )

        score = 0

        for question in questions:
            selected_answer_id = request.POST.get(str(question.id))

            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                is_correct = selected_answer.is_correct
            else:
                selected_answer = None
                is_correct = False

            UserAnswer.objects.create(
                submission=submission,
                question=question,
                answer=selected_answer,
                is_correct=is_correct
            )

            if is_correct:
                score += 1

        submission.score = score
        submission.save()

        return redirect("result", submission_id=submission.id)

    return render(request, "quizapp/quiz_attempt.html", {"quiz": quiz, "questions": questions})


@login_required(login_url='login')
def quizzes_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizapp/quizzes.html", {"quizzes": quizzes})


@login_required(login_url='login')
def quiz_history(request):
    submissions = UserSubmission.objects.filter(
        user_name=request.user.username
    ).order_by("-submitted_at")

    return render(request, "quizapp/history.html", {"submissions": submissions})


# ----------------------------
# DASHBOARD – ADD QUIZ
# ----------------------------

@login_required(login_url='login')
def add_quiz(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        Quiz.objects.create(title=title, description=description)
        return redirect("dashboard")

    return render(request, "quizapp/add_quiz.html")
