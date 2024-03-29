from django.shortcuts import render,redirect
import markdown
import random
from . import util
import os
from django.urls import reverse

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
      "bomba":htmlContent,"title":title})


def search(request):
    userSearch = request.POST.get('q').lower()
    allentries_lower = [entry.lower() for entry in util.list_entries()]
    list = []
    nothinginlist = False
    recommendation = False
    if userSearch not in allentries_lower:
        recommendation = True
        for i in userSearch:
            for l in allentries_lower:
                if i in l:
                    if l in list:
                        
                        continue
                    else:
                        list.append(l)
            else:
                continue
        else:
            if list == []:
                nothinginlist = True
                return render(request, "encyclopedia/index.html", {"nothinginlist":nothinginlist,"recommendation":recommendation})
            else:
                # This block will execute if no break occurred in the inner loop
                # if search is non and recomndation is non return a massage no recomndation using list 
                uperlist = [ uplist.upper() for uplist in list]
                entries = uperlist
                print(list)
                return render(request, "encyclopedia/index.html", {"entries": entries,"recommendation": recommendation,"list": list, "nothinginlist":nothinginlist})
    # If userSearch is in allentries_lower, execute the following block
    if userSearch in allentries_lower:
        print("the last line")
        util.get_entry(userSearch)
        htmlContent = convertMarkdown(userSearch)
        return render(request, "encyclopedia/inter.html",{"bomba": htmlContent})



def randompage(request):
   listOfAllEntres = util.list_entries()
   randomNumber = random.randint(0,len(listOfAllEntres) -1)
   print(randomNumber)
   cc =  util.list_entries()[randomNumber]
   htmlenret = convertMarkdown(cc)

   return render(request, "encyclopedia/inter.html", {
       "dd":htmlenret
   })

def creatpage(request):
    return render(request, "encyclopedia\creat_newpage.html",)


def savepage(request):
    title = request.POST.get('titleq')
    description = request.POST.get('content')
    if title in util.list_entries():
        return render(request, "encyclopedia\error.html")
    else:
        util.save_entry(title, description)
        htmlContent =  convertMarkdown(title)
        print(htmlContent)
        return render(request, "encyclopedia/inter.html", {
        "bomba":htmlContent,"title":title})


def editpage(request):
    if request.method == 'POST':
        title = request.POST.get('titleq')
        description = request.POST.get('description')
        util.save_entry(title, description)
        entry =  util.get_entry(title)
        return redirect('intres', title=title)
    else:
        title = request.GET.get('entry_title')
        content = util.get_entry(title)
        return render(request,"encyclopedia\editpage.html", {"title":title,"content":content})
        

def deletepage(request):
    ll = request.POST.get('entry_title')
    print(ll)
    os.remove(f"entries\{request.POST.get('entry_title')}.md")
    return redirect('index')