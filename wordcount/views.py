from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def get_count(request):
    mytext= request.GET['mytext']
    print (mytext)
    data= mytext.split()
    worddictionary= {}
    for word in data:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 0
            worddictionary[word] += 1
    worddictionary= sorted(worddictionary.items(), key= operator.itemgetter(1), reverse= True)
    return render(request, 'count.html', {"wordcount": worddictionary})
