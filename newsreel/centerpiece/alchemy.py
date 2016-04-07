import keys,json,requests, sys

def entity(url):
    entity_endpoint = 'http://gateway-a.watsonplatform.net/calls/url/URLGetRankedNamedEntities'
    payload = { 'url': url,
                'apikey':keys.alchemykey,
                'outputMode':'json',
              }
    
    r = requests.get(entity_endpoint, params=payload)
    print r.url
    json_vals = r.json()
    #print json.dumps(json_vals,indent=1)
    print 'ENTITIES'
    for each in json_vals['entities']:
        if float(each['relevance']) >.75:
            print '---------------'
            print 'ENTITY: '+ each['text'] +'\n'
            if 'disambiguated' in each:
                print 'DISAMBIGUATIONS'
                if 'subType' in each['disambiguated']:
                    for each_type in each['disambiguated']['subType']:
                        print each_type
                if 'website' in each['disambiguated']:
                    each['disambiguated']['website']
            print '---------------\n'
            


if __name__ == "__main__":
    entity('http://www.nytimes.com/2016/04/07/world/europe/to-discourage-prostitution-france-passes-bill-that-penalizes-clients.html')
