import requests,json

def country_search(countryName):
    api_endpoint = "https://restcountries.eu/rest/v1/name/" + countryName
    payload = {'fullText':'true'}
    r = requests.get(api_endpoint, params=payload)
    json_obj = r.json()
    print json.dumps(json_obj,indent=4,sort_keys=True)

if __name__ =="__main__":
    country_search("india")
    
