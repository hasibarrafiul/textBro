from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import textsForm
from .models import texts


def index(request):
    form = textsForm()
    if request.method == 'POST':
        form = textsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
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
        return redirect('/edit/' + link + '/' + enterPassword)
    return render(request, 'password.html', context)


def saveText(request, link, password):
    instance = texts.objects.get(text_link=link)
    if request.method == "POST":
        textEditBox = request.POST['edit-box']
    instance.text = textEditBox
    instance.save()
    return redirect('/edit/' + link + '/' + password)


def verify(request):
    instance = None
    if request.method == "POST":
        link_input = request.POST['text-link']
        password_input = request.POST['text-password']
        try:
            instance = texts.objects.get(text_link=link_input, text_password=password_input)
        except Exception as e:
            print(e)
        if instance is not None:
            return redirect('/edit/' + link_input+'/'+password_input)
        else:
            return redirect('/')
    return redirect('/')