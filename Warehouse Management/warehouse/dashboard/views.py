from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:register')
    return render(request, 'dashboard/register.html', {'form':form})