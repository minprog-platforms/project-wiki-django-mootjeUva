# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false

from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    pass
