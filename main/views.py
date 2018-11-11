from django.shortcuts import render
from .models import Message

# Create your views here.

def message(req):
    messages = Message.objects.all()
    return render(req, 'main/message.html', {"messages": messages})
