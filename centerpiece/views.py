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
def usa_top(request):
    top_stories = nytimes.top_stories('politics')
    cur_list =[]
    npr.npr_search('usa',numResults=2,listy=cur_list)
    guardian.guardian_search('usa',psize=2,listy=cur_list)
    context = {'title':'USA','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/world.html', context)
def middle_east_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    #npr.npr_search('middle east',numResults=2,listy=cur_list)
    #guardian.guardian_search('middle east',psize=2,listy=cur_list)
    iran=[]
    israel=[]
    #iran = guardian.guardian_search('iran',psize=2)
    #israel = npr.npr_search('israel',numResults=2)
    context = {'title':'MIDDLE EAST','top_stories':top_stories, 'stlist': cur_list, 'iran':iran, 'israel':israel}
    return render(request, 'centerpiece/middle_east.html', context)
def europe_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('europe',numResults=2,listy=cur_list)
    guardian.guardian_search('europe',psize=2,listy=cur_list)
    context = {'title':'EUROPE','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/world.html', context)
def asia_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('asia',numResults=2,listy=cur_list)
    guardian.guardian_search('asia',psize=2,listy=cur_list)
    context = {'title':'ASIA','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/world.html', context)
