from django.contrib import auth
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.conf import settings
import random
from .forms import RegisterForm, LoginForm, TipForm
from .models import Tip


def request_session_update(request):
    if 'user' not in request.session or request.session.get_expiry_age() == 0:
        request.session['user'] = random.choice(settings.ANONYMOUS_USER_NAMES)
        request.session.set_expiry(value=42)
        request.session.clear_expired()
    return request


def index(request):
    template_name = "ex/index.html"
    tips = Tip.objects.all().order_by('-date')
    if request.method == 'POST':
        if 'deletetip' in request.POST:
            if (request.user.has_perm('ex.deletetip') or
                    model_to_dict(Tip.objects.get(id=request.POST['tipid'])).get('auteur') == request.user.username):
                form = TipForm()
                t = Tip.objects.filter(id=request.POST['tipid'])
                t.delete()
        elif 'upvote' in request.POST:
            form = TipForm()
            ts = Tip.objects.filter(id=request.POST['tipid'])
            if len(ts) > 0:
                t = ts[0]
                t.upvoteForUser(request.user.username)
        elif 'downvote' in request.POST:
            form = TipForm()
            ts = Tip.objects.filter(id=request.POST['tipid'])
            if len(ts) > 0:
                t = ts[0]
                t.downvoteForUser(request.user.username)
        else:
            form = TipForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                tip = Tip(content=data['content'], auteur=request.user.username)
                tip.save()
    else:
        form = TipForm()

    response = render(request_session_update(request), template_name,
                      {'user_anon': request.session['user'], 'tips': tips, 'form': form})

    return response


def login(request):
    template_name = "ex/login.html"
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = auth.authenticate(username=data['username'], password=data['password'])
            if u and u.is_active:
                auth.login(request, u)
                return redirect('/')
            else:
                form.errors['username'] = ['Unknown or inactive user']
    else:
        form = LoginForm()

    return render(request_session_update(request), template_name,
                  {'user_anon': request.session['user'], 'form': form, })


def registration(request):
    template_name = "ex/registration.html"
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['password'])
            u.save()
            auth.login(request, u)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request_session_update(request), template_name,
                  {'user_anon': request.session['user'], 'form': form, })


def logout(request):
    auth.logout(request)
    return redirect('/')
