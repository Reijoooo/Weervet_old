from django.shortcuts import render


def article(request):

    # Отправка данных в шаблон и возврат ответа
    return render(request, 'article.html')