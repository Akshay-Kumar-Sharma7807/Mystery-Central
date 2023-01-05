from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LogInForm
from .forms import CreateMysteryForm, AnswerForm

from .models import User, Mystery, Answer

# Index page for the website
def index(request):
    mysteries = Mystery.objects.all()
    return render(request, 'index.html', {
        "mysteries": mysteries
    })

# Form for creating new mystery
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
    user_answer = Answer.objects.filter(answered_by=request.user, mystery=mystery).first()
    all_answers = Answer.objects.filter(mystery=mystery)
    print(mystery)
    return render(request, "mystery.html", {
        "mystery": mystery,
        "user_answer": user_answer,
        "all_answers": all_answers
    })

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
        


def about(request):
    return render(request, 'about.html')

def mysteries(request):
    mysteries = Mystery.objects.all()
    return render(request, 'mysteries.html', {
        "mysteries": mysteries
    })

def profile(request):
    user_profile = User.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'user_profile': user_profile})


def view_profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

    
def logout_view(request):
    logout(request)
    return redirect('index')