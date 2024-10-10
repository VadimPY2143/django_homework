from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app.forms import UserForm
from app.models import User


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        form.save()
        return redirect(user_list)
    else:
        form = UserForm(instance=user)
        return render(request, 'user_create.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    else:
        return render(request, 'user_delete.html', {'user': user})

