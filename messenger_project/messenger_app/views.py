from rest_framework import generics
from .forms import *
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *
from .serializers import *


def rooms(request):
    rooms = Room.objects.all()
    return render(request, "rooms.html", {'rooms': rooms})


def room(request, slug):
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    users = User.objects.filter(message__room=Room.objects.get(slug=slug)).distinct()
    context = {
        "slug": slug,
        "room_name": room_name,
        "messages":messages,
        "users":users,
        }
    return render(request, "room.html", context)


@login_required
def create_message(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            form.save(room=room)
            return redirect('room', slug=slug)
    else:
        form = MessageForm(user=request.user)
    return render(request, 'create_message.html', {'form': form, 'room': room})


@login_required
def delete_message(request, slug, message_id):
    room = get_object_or_404(Room, slug=slug)
    message = get_object_or_404(Message, id=message_id, room=room, user=request.user)

    if request.method == 'POST':
        message.delete()
        return redirect('room', slug=slug)

    return render(request, 'delete_message.html', {'message': message, 'room': room})


class RoomAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@login_required
def profile_view (request):
    return render(request, "profile.html")

