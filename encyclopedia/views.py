# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false

from django.shortcuts import render, redirect
from django.urls import reverse
from markdown2 import Markdown as markdown
from . import util
import random
from django import forms


class Searchclass(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
      "class": "search",
      "placeholder": "Search Encyclopedia"}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_class": Searchclass()
    })

def entry(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": wiki_entry,
        "search_class": Searchclass(),
    })

def editpage(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "entry": wiki_entry,
        "search_class": Searchclass()
    })

def search(request):
    if request.method == "POST":
        form = Searchclass(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            wiki_entry = util.get_entry(title)
            if wiki_entry:
                return redirect(reverse('entry', args=[title]))
            else:
                return render(request, "encyclopedia/search.html", {
                    "title": title,
                    "search_class": Searchclass()
                })



def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
          "search_class": Searchclass()
        })


def randompage(request):
    all_entries = util.list_entries()
    random_title = random.choice(all_entries)
    return redirect(reverse('entry', args=[random_title]))

