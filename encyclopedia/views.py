from django.shortcuts import render
import markdown

from . import util


def convertMarkdown(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def intres(request,title):
    htmlContent =  convertMarkdown(title)
    print(htmlContent)
    return render(request, "encyclopedia/inter.html", {
      "bomba":htmlContent
      })

def search(request):
    userSearch = request.POST.get('q')
    util.get_entry(userSearch)
    htmlContent =  convertMarkdown(userSearch)
    return render(request, "encyclopedia/inter.html", {
      "bomba":htmlContent
      })
