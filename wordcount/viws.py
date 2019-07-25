from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    wordlist = request.GET['counter']

    list1 = wordlist.split()
    list2 = len(list1)
    worddict = {}

    for word in list1:

        if word in worddict:

            worddict[word] += 1

        else:

            worddict[word] = 1

    sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'wordlist':wordlist, 'words':list2, 'sortedword': sortedword})

def about(request):
    return render(request, 'about.html')
