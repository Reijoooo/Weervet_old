from django.shortcuts import render


def contact(request):

    # Отправка данных в шаблон и возврат ответа
    return render(request, 'contact.html')