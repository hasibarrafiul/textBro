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


def newTab(request, link, password):
    sendText = ""
    sendTab = ""
    instance = texts.objects.get(text_link=link, text_password=password)
    if instance.text1 == "":
        sendText = instance.text1
        sendTab = "text1"
    elif instance.text2 == "":
        sendText = instance.text2
        sendTab = "text2"
    elif instance.text3 == "":
        sendText = instance.text3
        sendTab = "text3"
    elif instance.text4 == "":
        sendText = instance.text4
        sendTab = "text4"
    elif instance.text5 == "":
        sendText = instance.text5
        sendTab = "text5"
    elif instance.text6 == "":
        sendText = instance.text6
        sendTab = "text6"
    elif instance.text7 == "":
        sendText = instance.text7
        sendTab = "text7"
    elif instance.text8 == "":
        sendText = instance.text8
        sendTab = "text8"
    elif instance.text9 == "":
        sendText = instance.text9
        sendTab = "text9"
    else:
        return HttpResponse("All tab full")

    context = {'link': instance.text_link, 'text': sendText, 'password': instance.text_password, 'tab': sendTab}
    return render(request, 'newTab.html', context)


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


def saveTextNewTab(request, link, password, tab):
    instance = texts.objects.get(text_link=link)
    print(tab)

    if request.method == "POST":
        textEditBox = request.POST['edit-box-tab']
    if tab == "text1":
        instance.text1 = textEditBox
    elif tab == "text2":
        instance.text2 = textEditBox
    elif tab == "text3":
        instance.text3 = textEditBox
    elif tab == "text4":
        instance.text4 = textEditBox
    elif tab == "text5":
        instance.text5 = textEditBox
    elif tab == "text6":
        instance.text6 = textEditBox
    elif tab == "text7":
        instance.text7 = textEditBox
    elif tab == "text8":
        instance.text8 = textEditBox
    elif tab == "text9":
        instance.text9 = textEditBox


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