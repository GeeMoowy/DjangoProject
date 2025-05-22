from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from .forms import UserRegistrationForm, UserProfileForm
from .models import CustomUser


class RegisterView(FormView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'Добро пожаловать на мой сайт',
            'Вы зарегистрированы на сайте',
            'kovylek.ul@mail.ru',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class ProfileEditView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user