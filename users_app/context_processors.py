def user_id(request):
    return {'user_id': request.user.id if request.user.is_authenticated else None}