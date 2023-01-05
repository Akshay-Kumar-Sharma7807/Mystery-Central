from django.shortcuts import render, redirect
from .forms import CreateMysteryForm

# Index page for the website
def index(request):
  return render(request, 'index.html')

# Form for creating new mystery
def create_mystery(request):
    if request.method == 'POST':
        form = CreateMysteryForm(request.POST)
        if form.is_valid():
            mystery = form.save(commit=False)
            mystery.created_by = request.user
            mystery.save()
            return redirect('view_mystery', mystery_id=mystery.id)
    else:
        form = CreateMysteryForm()
    return render(request, 'create_mystery.html', {'form': form})
