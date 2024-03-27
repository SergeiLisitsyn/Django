from django.shortcuts import render
from .forms import TextForm, UserForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView



# Create your views here.
def welcome(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'form_data.html', {'form': form, 'data_dict': data, })

    else:
        form = UserForm()
    return render(request, 'my_form.html', {'form': form})


def count(request):
    sighns = ['.', ',', '/', '\\', '?', ':', '!', ';']
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_input']
            # Now, you can process the text as required
            words = text.split(' ')
            word_dict = {}
            for word in words:
                word = word.lower()
                for el in sighns:
                    word = word.strip(el)
                    word_dict[word] = word_dict.get(word, 0) + 1
                else:
                    word_dict[word] = word_dict.get(word, 0) + 1
            return render(request, 'word_count_result.html', {'word_dict': word_dict})
        else:
            form = TextForm()
    else:
        form = TextForm()
    return render(request, 'text_form_manual.html', {'form': form})


def count_words(request):
    common_words = ['the', 'is', 'and', 'of', 'in', 'to', 'a', 'with', 'as', 'for']
    sighns = ['.', ',', '/', '\\', '?', ':', '!', ';']
    if request.method == "POST":
        text = request.POST['text']
        try:
            filtration = request.POST['filter']
        except:
            filtration = 0
        words = text.split(' ')
        word_dict = {}
        for word in words:
            word = word.lower()
            for el in sighns:
                word = word.strip(el)
            if filtration:
                if word not in common_words:
                    word_dict[word] = word_dict.get(word, 0) + 1
            else:
                word_dict[word] = word_dict.get(word, 0) + 1
        return render(request, 'word_count.html', {'word_dict': word_dict})
    return render(request, 'word_count.html')

