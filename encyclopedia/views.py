# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false


from django.shortcuts import render, redirect
from django.urls import reverse
from markdown2 import Markdown as markdown
from . import util
import random
from django import forms


class SearchForm(forms.Form):
    """ Form Class for Search Bar """
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
      "class": "search",
      "placeholder": "Search Encyclopedia"}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form": SearchForm()
    })

def entry(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": wiki_entry,
        "search_form": SearchForm(),
    })

def editpage(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "entry": wiki_entry,
        "search_form": SearchForm()
    })

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            wiki_entry = util.get_entry(title)
            if wiki_entry:
                return redirect(reverse('entry', args=[title]))
            else:
                return redirect(reverse('index'))



def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
          "search_form": SearchForm()
        })


def randompage(request):
    all_entries = util.list_entries()
    random_title = random.choice(all_entries)
    return redirect(reverse('entry', args=[random_title]))

