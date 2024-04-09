from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from schedule.models import MyEvent
from schedule.forms import MyEventForm

@login_required
def event_list(request, user_id):
    user = request.user
    event = MyEvent.objects.filter(user=user)

    return render(request, 'event_list.html', {'user': user, 'event': event})



    # events = MyEvent.objects.filter(user=user_id)  # Предположим, что события привязаны к пользователю
    # if events.exists():
    #     return render(request, 'event_list.html', {'events': events})
    # else:
    #     return render(request, 'no_events.html')  # Шаблон для случая, когда у пользователя нет событий



    # events = Event.objects.all()
    # return render(request, 'event_list.html', {'events': events})

@login_required
def event_detail(request, user_id):
    try:
        user = MyEvent.objects.get(user_id=user_id)
        return render(request, 'event_detail.html', {'user': user})
    except MyEvent.DoesNotExist:
        return render(request, 'event_not_found.html')  # Шаблон для случая, когда событие не найдено
    # event = Event.objects.get(id=event_id)
    # return render(request, 'event_detail.html', {'event': event})

@login_required
def create_event(request, user_id):
    if request.method == 'POST':
        form = MyEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list', user_id=request.user.id)
    else:
        form = MyEventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = MyEvent.objects.get(id=event_id)
    if request.method == 'POST':
        form = MyEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = MyEventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = MyEvent.objects.get(id=event_id)
    event.delete()
    return redirect('event_list')

@login_required
def ajax_event_list(request):
    events = MyEvent.objects.all()
    data = {'events': list(events.values())}
    return JsonResponse(data)
