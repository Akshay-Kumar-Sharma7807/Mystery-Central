import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import SignUpForm, LogInForm
from .forms import CreateMysteryForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt

from .models import User, Mystery, Answer

# Index page for the website
def index(request):
    mysteries = Mystery.objects.all()
    return render(request, 'index.html', {
        "mysteries": mysteries
    })

# Form for creating new mystery

@login_required
def create_mystery(request):
    if request.method == 'POST':
        form = CreateMysteryForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            mystery = form.save(commit=False)
            mystery.created_by = request.user
            mystery.save()
            return redirect('view_mystery', myst_id=mystery.id)
    else:
        form = CreateMysteryForm()
    return render(request, 'create_mystery.html', {'form': form})

def view_mystery(request, myst_id):
    mystery = Mystery.objects.filter(id=myst_id).first()
    try:
        user_answer = Answer.objects.filter(answered_by=request.user, mystery=mystery).first()
    except:
        user_answer = None
    all_answers = Answer.objects.filter(mystery=mystery)
    reviews = Answer.objects.filter(mystery=mystery, reviewed=False)
    print(mystery)
    return render(request, "mystery.html", {
        "mystery": mystery,
        "user_answer": user_answer,
        "all_answers": all_answers,
        "reviews": reviews
    })

@login_required
def answer_mystery(request, myst_id):
    mystery = Mystery.objects.filter(id=myst_id).first()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.answered_by = request.user
            answer.mystery = mystery
            answer.save()
            return redirect('view_mystery', myst_id=mystery.id)
    else:
        return render(request, 'answer_mystery.html')


@csrf_exempt
@login_required
def review_answer(request, ans_id):
    if request.method == "PUT":
        answer = Answer.objects.get(id=ans_id)
        data = json.loads(request.body)
        if data.get("correct") is not None:
            answer.correct = data["correct"]
            answer.reviewed = True
        answer.save()
        return HttpResponse(status=204)
    else:
        pass

def mysteries(request):
    mysteries = Mystery.objects.all()
    return render(request, 'mysteries.html', {
        "mysteries": mysteries
    })


def about(request):
    return render(request, 'about.html')

def settings(request):
    return render(request, 'settings.html')

@login_required
def profile(request):
    user_profile = User.objects.get(id=request.user.id)
    answers = Answer.objects.filter(answered_by=user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile, "answers": answers})


def view_profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    answers = Answer.objects.filter(answered_by=user_profile)
    return render(request, 'profile.html', {'user_profile': user_profile, "answers": answers})


def sign_up(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sign_up.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "sign_up.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "sign_up.html")

def log_in(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "log_in.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "log_in.html")

    
def logout_view(request):
    logout(request)
    return redirect('index')