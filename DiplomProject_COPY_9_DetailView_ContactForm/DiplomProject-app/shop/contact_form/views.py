from django.shortcuts import render, redirect
# from django.views.generic import CreateView
from django.http import HttpResponse, BadHeaderError
from django.core.mail import send_mail
# from django.urls import reverse_lazy
#
from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'aleksejbaskirov31@gmail.com',
                          ['bashkirov1985@internet.ru'])
            except BadHeaderError:
                return HttpResponse('Найден не корректный загоовок')
            return redirect("index")
    form = ContactForm
    return render(request, "contact_form/contact.html", {'form': form})

#
#
# class ContactCreate(CreateView):
#     model = Contact
#     fields = ["first_name", "last_name", "message"]
#     success_url = reverse_lazy('success_page.html')
#     form_class = ContactForm
#
#     def form_valid(self, form):
#         data = form.data
#         subject = f"Сообщение с формы Contact от {data['first_name']} {data['last_name']}" \
#                   f"Почта отправителя: {data['email']}"
#         email = (subject, data["message"])
#         return super().form_valid(form)
#
#     def email(subject, content):
#         send_mail(subject, content)
#
#
# def success_page(request):
#     if request.POST:
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         element = Contact(
#             first_name=first_name,
#             last_name=last_name,
#             email=email)
#         element.save()
#         send_mail()
#     return HttpResponse('Писмо отправленно')

