from django.shortcuts import render, redirect
from .forms import AppointmentForm


def index(request):
    return render(request, 'index.html', {'title': 'Главное меню клиники'})


def services(request):
    return render(request, 'services.html', {'title': 'Our Services'})


def signup(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']

            # Сохраняем данные в файл appointments.txt
            with open("sign-ups.txt", 'a', encoding='utf-8') as file:
                file.write(f"Имя: {name}, Телефон: {phone}, Дата: {date}\n")

            # Перенаправляем пользователя на главную страницу
            return redirect('index')
    else:
        form = AppointmentForm()
    return render(request, 'signup.html', {'form': form, 'title': 'Sign Up'})


def contact(request):
    return render(request, "contact.html", {'title': 'Контакты'})


def feedback(request):
    return render(request, "feedback.html", {'title': 'Отзывы'})


def about(request):
    return render(request, "about.html", {'title': 'О нас'})


def whatsapp(request):
    return render(request, "whatsapp.html", {'title': 'WhatsApp'})
