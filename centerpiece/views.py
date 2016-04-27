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
    guardian.guardian_search('world',numResults=2,listy=cur_list)
    context = {'title':'WORLD','top_stories':top_stories, 'stlist': cur_list} 
    return render(request, 'centerpiece/generic_subcat.html', context)
def africa_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('africa',numResults=2,listy=cur_list)
    guardian.guardian_search('africa',numResults=2,listy=cur_list)
    kenya,egypt,nigeria,zimbabwe = [],[],[],[]
    guardian.guardian_search('kenya',numResults=2,listy=kenya)
    guardian.guardian_search('egypt',numResults=2,listy=egypt)
    guardian.guardian_search('nigeria',numResults=2,listy=nigeria)
    guardian.guardian_search('zimbabwe',numResults=2,listy=zimbabwe)
    context = {'title':'AFRICA','top_stories':top_stories, 'stlist': cur_list,
                'sub':{'kenya':kenya,'egypt':egypt,'nigeria':nigeria,'zimbabwe':zimbabwe}}
    context['div'] = 12/len(context['sub'])
    return render(request, 'centerpiece/generic_subcat.html', context)
def usa_top(request):
    top_stories = nytimes.top_stories('politics')
    cur_list =[]
    npr.npr_search('usa',numResults=2,listy=cur_list)
    guardian.guardian_search('usa',numResults=2,listy=cur_list)
    elections,politics,healthcare=[],[],[]
    npr.npr_search('elections',numResults=2,listy=elections)
    npr.npr_search('politics',numResults=2,listy=politics)
    npr.npr_search('healthcare',numResults=2,listy=healthcare)
    context = {'title':'USA','top_stories':top_stories, 'stlist': cur_list}
    context['sub'] = {'healthcare':healthcare,'elections':elections,
                'politics':politics} 
    context['div'] = 12/len(context['sub'])
    return render(request, 'centerpiece/generic_subcat.html', context)
def middle_east_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('middle east',numResults=2,listy=cur_list)
    guardian.guardian_search('middle east',numResults=2,listy=cur_list)
    iran = []
    israel = []
    syria = []
    libya = [] 
    
    iran = guardian.guardian_search('iran',numResults=2,listy=iran)
    israel = npr.npr_search('israel',numResults=2, listy=israel)
    syria = guardian.guardian_search('syria',numResults=2, listy=syria)
    libya = guardian.guardian_search('libya',numResults=2,listy=libya)
    context = {'title':'MIDDLE EAST','top_stories':top_stories, 'stlist': cur_list,}
    context['sub'] = {'iran':iran, 'israel':israel, 'syria':syria, 'libya':libya,}
    context['div'] = 12/len(context['sub'])
    return render(request, 'centerpiece/generic_subcat.html', context)
def europe_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('europe',numResults=2,listy=cur_list)
    guardian.guardian_search('europe',numResults=2,listy=cur_list)
    russia,eu,greece,britain= [],[],[],[]
    guardian.guardian_search('russia',numResults=2,listy=russia)
    guardian.guardian_search('european union',numResults=2,listy=eu)
    guardian.guardian_search('greece',numResults=2,listy=greece)
    guardian.guardian_search('britain',numResults=2,listy=britain)
    context = {'title':'EUROPE','top_stories':top_stories, 'stlist': cur_list}
    context['sub']= {'russia':russia,'eu':eu,'greece':greece,'britain':britain } 
    context['div'] = 12/len(context['sub'])
    return render(request, 'centerpiece/generic_subcat.html', context)
def asia_top(request):
    top_stories = nytimes.top_stories('world')
    cur_list =[]
    npr.npr_search('asia',numResults=2,listy=cur_list)
    guardian.guardian_search('asia',numResults=2,listy=cur_list)
    china,japan,india,myanmar =[],[],[],[]
    guardian.guardian_search('china', numResults=2,listy=china)
    guardian.guardian_search('india', numResults=2,listy=india)
    guardian.guardian_search('japan', numResults=2,listy=japan)
    guardian.guardian_search('myanmar', numResults=2,listy=myanmar)
    context = {'title':'ASIA','top_stories':top_stories, 'stlist': cur_list,}
    context['sub'] = {'china':china, 'india':india,'japan':japan, 'myanmar':myanmar} 
    context['div'] = 12/len(context['sub'])
    return render(request, 'centerpiece/generic_subcat.html', context)
