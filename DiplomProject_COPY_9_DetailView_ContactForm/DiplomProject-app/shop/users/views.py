from django.shortcuts import render, redirect
from django.contrib import auth, messages
# from django.views.generic import FormView
# from django.urls import reverse_lazy

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, \
    UserProfileForm  # , ContactForm


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


# class ContactFormView(FormView):
#     form_class = ContactForm
#     template_name = 'users/contact.html'
#     success_url = reverse_lazy('index')
#
#     def get(self, request, *args, **kwargs):
#         # context = {}
#         # context.update(csrf(request))  # Обязательно добавьте в шаблон защитный токен
#         context = {
#             'contact_form' = ContactForm(),
#             'title' = 'Обратная связь',
#         }
#         return reverse_lazy('users/contact.html', context)
#         # return render(request, 'users/contact.html', context)
#
