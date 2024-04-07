from django.shortcuts import render


def about(request):

    # Отправка данных в шаблон и возврат ответа
    return render(request, 'about.html')