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


def editText(request, link):
    instance = texts.objects.get(text_link=link)
    context = {'link': instance.text_link, 'text': instance.text}
    return render(request, 'editText.html', context)


def saveText(request, link):
    instance = texts.objects.get(text_link=link)
    if request.method == "POST":
        textEditBox = request.POST['edit-box']
    instance.text = textEditBox
    instance.save()
    return redirect('/edit/' + link)