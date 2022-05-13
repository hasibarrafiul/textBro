from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import textsForm
from .models import texts
import hashlib


def index(request):
    form = textsForm()
    if request.method == 'POST':
        form = textsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.text_password = hashlib.sha256(instance.text_password.encode('utf-8')).hexdigest()
            instance.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = textsForm()
    return render(request, 'homepage.html', {'form': form})


def editText(request, link, password):
    instance = texts.objects.get(text_link=link, text_password=password)
    context = {'link': instance.text_link, 'text': instance.text, 'password': instance.text_password}
    return render(request, 'editText.html', context)


def editTextAskPassword(request, link):
    context = {'link': link}
    enterPassword = ""
    if request.method == "POST":
        enterPassword = request.POST['enter-text-password']
    if enterPassword != "":
        check_password = hashlib.sha256(enterPassword.encode('utf-8')).hexdigest()
        return redirect('/' + link + '/' + check_password)
    return render(request, 'password.html', context)


def saveText(request, link, password):
    instance = texts.objects.get(text_link=link)
    if request.method == "POST":
        textEditBox = request.POST['edit-box']
    instance.text = textEditBox
    instance.save()
    return redirect('/' + link + '/' + password)


def verify(request):
    instance = None
    if request.method == "POST":
        link_input = request.POST['text-link']
        password_input = request.POST['text-password']
        check_password = hashlib.sha256(password_input.encode('utf-8')).hexdigest()
        try:
            instance = texts.objects.get(text_link=link_input, text_password=check_password)
        except Exception as e:
            print(e)
        if instance is not None:
            return redirect('/' + link_input+'/'+check_password)
        else:
            return redirect('/')
    return redirect('/')