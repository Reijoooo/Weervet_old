from django.shortcuts import render

def index(request):
    # Получение данных из базы данных или других источников
    my_data = {'foo': 'bar', 'baz': 'qux'}

    # Отправка данных в шаблон и возврат ответа
    return render(request, 'index.html', {'my_data': my_data})