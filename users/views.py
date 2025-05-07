from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegistrationForm
from .models import CustomUser


class RegisterView(View):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            send_mail(
                'Добро пожаловать на мой сайт',
                'Вы зарегистрированы на сайте',
                'kovylek.ul@mail.ru',
                [user.email],
                fail_silently=False,
            )
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})