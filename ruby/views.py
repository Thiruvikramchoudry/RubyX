from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from .models import  bot_messages
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    if request.user.username=="":
        return render(request,'ruby/index.html',{'login_status':False})
    else:
        return render(request,'ruby/index.html',{'login_status':True,'username':request.user})



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

    else:
        return render(request,'ruby/login.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        bot_message=bot_messages(username=username,message_type="bot",message="Hi This is Ruby ,How can i help you....")
        bot_message.save()
        user = authenticate(username=username, password=password)
        auth.login(request, user)
        return redirect('/')
    else:
        print("else")
        return render(request,'ruby/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def getmessages(request):
    room = bot_messages.objects.filter(username=request.user)
    return JsonResponse({"messages": list(room.values())[::-1]})

def send_message(request):
    print("called")
    message = request.POST['message']
    username = request.user
    new_message = bot_messages.objects.create(username=username,message_type="user",message=message)
    new_message.save()


