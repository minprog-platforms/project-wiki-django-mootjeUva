# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false

from django.shortcuts import render
from markdown2 import Markdown as markdown
from . import util


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
