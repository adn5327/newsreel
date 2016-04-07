import keys,json
import requests
import aylien

def npr_search(cur_topic, numResults=5):
    topics_dict = { 'afghanistan' : 1149,
                    'africa' : 1126,
                    'asia' : 1125,
                    'economy' : 1017,
                    'elections' : 139482413,
                    'europe' : 1124,
                    'israel' : 1101,
                    'palestine' : 1101,
                    'middle east' : 1009,
                    'politics' : 1014,
                    'us' : 1003,
                    'world' : 1004
                  }
     
    api_endpoint = 'http://api.npr.org/query'
    payload = { 'id':topics_dict[cur_topic],
                'fields':'title',
                'output':'JSON',
                'apiKey':keys.nprkey,
                'numResults':numResults
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
                
                print '---------------'
                print 'TITLE: ' + each_story['title']['$text']
                print 'ARTICLE SUMMARY \n'
                aylien.summarize(each_link['$text'])
                print '---------------'

if __name__ == "__main__":
    npr_search('israel')
