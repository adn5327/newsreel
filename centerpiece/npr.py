import keys,json,topics
import requests
import aylien

def npr_search(cur_topic, numResults=5, listy=[]):
     
    api_endpoint = 'http://api.npr.org/query'
    payload = { 'id':topics.npr_dict[cur_topic],
                'fields':'title',
                'output':'JSON',
                'apiKey':keys.nprkey,
                'numResults':numResults,
                'sort':'relevance',
              }
    #could make 'fields':['title','text'] if you wanted the text of the article
    #query string = ?id=1149&fields=title,text&output=JSON&apiKey=demo
    r = requests.get(api_endpoint,params=payload)
    json_vals = r.json()
    #print json.dumps(json_vals,indent=1)
    #print json.dumps(json_vals['list']['story'],indent=1)
    for each_story in json_vals['list']['story']:
        for each_link in each_story['link']:
            if each_link['type'] == 'html':
                
                #print '---------------'
                #print 'TITLE: ' + each_story['title']['$text']
                #print 'URL: ' + each_link['$text']
                #print 'ARTICLE SUMMARY \n'
                str = aylien.summarize(each_link['$text'])
                #print '---------------'
                listy.append({'title':each_story['title']['$text'],'url':each_link['$text'],'summary':str})
    return listy 

if __name__ == "__main__":
    npr_search('israel')
