from django.shortcuts import render, redirect
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def getToken(request):
    appId = 'e8d3a945709b4dc09759fde0e4a6e92c'
    appCertificate = '37e530132910493389a4d122809c282b'
    channelName = request.GET.get('channel')
    uid =  random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')

# @csrf_exempt
# def createUser(request):
#     data = json.loads(request.body)

#     member, created = RoomMember.objects.get_or_create(
#         name=data['name'],
#         uid = data['uid'],
#         room_name = data['room_name']
#         )
        
#     # print(data)
#     return JsonResponse({'name': data['name']}, safe=False)

# def getUser(request):
#     uid = request.GET.get('uid')
#     room_name = request.GET.get('room_name')

#     member = RoomMember.objects.get(
#         uid = uid,
#         room_name = room_name
#     )

#     name = member.name
#     return JsonResponse({'name': member.name}, safe=False)

# @csrf_exempt
# def deleteUser(request):
#     data = json.loads(request.body)

#     member = RoomMember.objects.get(
#         name=data['name'],
#         uid = data['uid'],
#         room_name = data['room_name']
#         )
#     member.delete()
#     return JsonResponse('member deleted!', safe=False)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    

    form = CreateUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lobby')
        else:
            messages.info(request, 'Username or password is incorrect')
            

    context = {'form': form}
    return render(request, 'base/login.html', context)

def signup(request):

    if request.user.is_authenticated:
        return redirect('/')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, "Account successfully created for " + username )
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')