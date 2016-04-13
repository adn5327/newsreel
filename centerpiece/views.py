from django.shortcuts import render
from django.http import HttpResponse
from . import nytimes, npr, guardian

# Create your views here.
def index(request):
    context = {
            'user':request.user,
    }
    return render(request, 'centerpiece/index.html', context)
def world_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('world',numResults=2,listy=cur_list)
    guardian.guardian_search('world',psize=2,listy=cur_list)
    context = {'title':'WORLD','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/world.html', context)
def africa_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('africa',numResults=2,listy=cur_list)
    guardian.guardian_search('africa',psize=2,listy=cur_list)
    context = {'title':'AFRICA','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/world.html', context)
