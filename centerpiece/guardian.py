import keys
import requests
import aylien
from .models import Article
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
def guardian_search(searchTerm,numResults=5,orderby='relevance',listy=[], sentNum=5):
    searchTerm = searchTerm.replace(' ','%20')
    api_endpoint = 'http://content.guardianapis.com/search'
    payload = {'page-size':numResults, 'q':searchTerm, 'order-by':orderby, 'api-key':keys.guardiankey}
    r = requests.get(api_endpoint,params=payload)
    #print r.url
    json = r.json()
    result_list = json['response']['results']
    for result in result_list:
        #print '---------------'
        #print 'TITLE: ' + result['webTitle']
        #print 'URL: ' + result['webUrl']
        #print
        #print 'ARTICLE SUMMARY \n'
        cur_url = result['webUrl']
        try:
            entry = Article.objects.get(url=cur_url)
            str = entry.text
        except Article.DoesNotExist:
            str= aylien.summarize(result['webUrl'],sentNum) 
            entry = Article(url=cur_url, text=str)
            entry.save()
        #print '---------------'
        #print '\n' 
        listy.append({'title':result['webTitle'],'url':result['webUrl'],'summary':str})
    return listy 

if __name__=="__main__":
    guardian_search('bernie sanders',numResults=2)
