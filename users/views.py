from django.urls import reverse_lazy
from django.views import View
from .forms import UserRegistrationForm

class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:')