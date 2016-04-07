import requests, json
import keys
def article_search():
    pass
def top_stories(section):
    endpoint = 'http://api.nytimes.com/svc/topstories/v1/' 
    endpoint += section
    endpoint += '.json'
    payload = {'api-key':keys.nyttopkey}
    r = requests.get(endpoint, params=payload)
    json_vals = r.json()
    #print json.dumps(json_vals,indent=1)
    num_results = json_vals['num_results']
    iterate_num = num_results
    if num_results > 5: 
        iterate_num = 5
    for i in range(iterate_num):
        cur = json_vals['results'][i]
        print '----------------'
        print cur['title'] + ', ' + cur['url'] 
if __name__=="__main__":
    article_search()
    top_stories('world')
