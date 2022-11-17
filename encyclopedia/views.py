# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false


from django.shortcuts import render, redirect
from django.urls import reverse
from markdown2 import Markdown as markdown
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": wiki_entry
    })

def editpage(request, title):
    wiki_entry = markdown().convert(util.get_entry(title))
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "entry": wiki_entry
    })

def search(request, title):
    wiki_entry = util.get_entry(title)
    return redirect(reverse('entry', args=[title]))
    #return render(request, "encyclopedia/search.html", {
    #    "title": title
    #})


def newpage(request, title):
    pass


def randompage(request):
    all_entries = util.list_entries()
    random_title = random.choice(all_entries)
    return redirect(reverse('entry', args=[random_title]))

