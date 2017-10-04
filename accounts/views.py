from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from core.models import Route, Area, Region


from django.contrib.auth import get_user_model
User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_redirect(request):
	return redirect('/accounts/profile/' + request.user.username)

@login_required
def profile(request, username=''):
	if User.objects.filter(username__iexact=username).exists():
		return render(request, 'accounts/profile.html', {'viewed_user': User.objects.get(username__iexact=username)})
	else: 
		return render(request, 'accounts/profile_nonexistant.html',{})
