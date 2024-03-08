from django.shortcuts import render
import markdown
import random
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
    userSearch = request.POST.get('q').lower()
    allentries_lower = [entry.lower() for entry in util.list_entries()]
    list = []
    recommendation = True
    if userSearch not in allentries_lower:
        recommendation = False
        for i in userSearch:
            print(f"{i} for i")
            for l in allentries_lower:
                print(f"{l} for l")
                if i in l:
                    if l in list:
                        continue
                    else:
                        list.append(l)
                        print(f"for last loop / {list}")
            else:
                continue
            break
        else:
            # This block will execute if no break occurred in the inner loop
            uperlist = [ uplist.upper() for uplist in list]
            entries = uperlist
            return render(request, "encyclopedia/index.html", {"entries": entries,})
    # If userSearch is in allentries_lower, execute the following block
    if userSearch in allentries_lower:
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
    b = 'db'
    return render(request, "encyclopedia\creat_newpage.html",
                  {"b":b})


def savepage(request):
    title = request.POST.get('titleq')
    description = request.POST.get('description')
    util.save_entry(title, description)
    
    return render(request, "encyclopedia\index.html")
