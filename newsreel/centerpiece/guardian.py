import keys
import requests
import aylien

def guardian_search(searchTerm,psize=5,orderby='relevance'):
    searchTerm = searchTerm.replace(' ','%20')
    api_endpoint = 'http://content.guardianapis.com/search'
    payload = {'page-size':psize, 'q':searchTerm, 'order-by':orderby, 'api-key':keys.guardiankey}
    r = requests.get(api_endpoint,params=payload)
    #print r.url
    json = r.json()
    result_list = json['response']['results']
    for result in result_list:
        print '---------------'
        print 'TITLE: ' + result['webTitle']
        print 'URL: ' + result['webUrl']
        print
        print 'ARTICLE SUMMARY \n'
        aylien.summarize(result['webUrl'],5) 
        print '---------------'
        print '\n' 

if __name__=="__main__":
    guardian_search('bernie sanders',2)