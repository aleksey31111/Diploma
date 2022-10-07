from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import reverse, render_to_response
from django.views import View
from django.core.mail import send_mail

from .forms import ContactForm
from shop import settings
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


class EContactsView(View):
    template_name = 'home/contacts.html'

    # В случае get запроса, мы будем отправлять просто страницу с контактной формой
    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))  # Обязательно добавьте в шаблон защитный токен
        context['contact_form'] = ContactForm()

        return render_to_response(self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}

        form = ContactForm(request.POST)

        # Если не выполнить проверку на правильность ввода данных,
        # то не сможем забрать эти данные из формы... хотя что здесь проверять?
        if form.is_valid():
            email_subject = 'EVILEG :: Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])

            # и отправляем сообщение
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['target_email@example.com'],
                      fail_silently=False)

        return render_to_response(template_name=self.template_name, context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегистрировались на сайте '
                             'Магазин Устройств')
            return redirect('login')
    else:
        form = UserRegistrationForm
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(
            data=request.POST,
            files=request.FILES,
            instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    context = {
        'form': form,
        'baskets': Basket.objects.filter(user=user)
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


