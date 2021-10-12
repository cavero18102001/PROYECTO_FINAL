from django.shortcuts import render, redirect
from .models import Persona, Consulta, Mensaje

from .victorBot import victorBot

from gtts import gTTS
import os
import os.path as path

from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
# Create your views here.
import re
import time
import pyttsx3 
# Create your views here.

def inicio(request):
    if request.method == 'GET':
        return render(request,"inicio.html")
    else:
        nombre=request.POST['nombre']
        persona = Persona.objects.create(nombre=nombre)
        persona.save()
        return render(request,"eleccion.html")



def reproducirAudio(respuesta):
    respuesta=re.sub("[<br>]","",respuesta)
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty ('rate', 120)
    engine.setProperty('voices',voices[1].id)
    engine.say(respuesta)
    engine.runAndWait()
    engine.stop()


def message_view(request):
    return render(request, "messages.html",
                  {'users': "User.objects.exclude(username=request.user.username)",
                   'receiver': "User.objects.get(id=receiver)",
                   'messages': "hola"})


def inicio1(request):
    now = datetime.now()
    numeroAletorio = random.randint(1, 10000)
    tiempo = now.strftime("%m-%d-%Y,%H:%M:%S")
    idConsulta = str(numeroAletorio)+'-'+tiempo
    consulta = Consulta.objects.create(idConsulta=idConsulta)
    consulta.save()
    return redirect('/'+idConsulta+'/')
    # redirect('/'+idConsulta+'/?usuario='+ciudadano)


def consulta(request, idConsulta):
    respuesta = ["Hola que tal!", "¿Cómo te va?", "un gusto de verte"]
    respuestaAletoria = random.choice(respuesta)
    usuario = "VICTOR"
    new_message = Mensaje.objects.create(
        mensaje=respuestaAletoria, usuario=usuario, idConsulta=idConsulta)
    new_message.save()

    reproducirAudio(respuestaAletoria)
    
    return render(request, 'messages.html', {
        'username': 'Ciudadano',
        'idConsulta': idConsulta,
    })


def getMessages(request, idConsulta):

    messages = Mensaje.objects.filter(idConsulta=idConsulta)
    return JsonResponse({"messages": list(messages.values())})


def send(request, idConsulta):

    message = request.POST['mensaje']
    usuario = "CIUDADANO"
    new_message = Mensaje.objects.create(
        mensaje=message, usuario=usuario, idConsulta=idConsulta)
    new_message.save()

    respuesta = victorBot(message)
    usuario = "VICTOR"
    new_message = Mensaje.objects.create(
        mensaje=respuesta, usuario=usuario, idConsulta=idConsulta)
    new_message.save()
    reproducirAudio(respuesta)
    return HttpResponse('Message sent successfully')
