from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        print(username, 'ram')
        password = form.cleaned_data['password']
        print(password, 'ram12')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {'form': form, 'error': 'you are not authorized'})

        return super().form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
