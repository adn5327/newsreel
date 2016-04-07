from aylienapiclient import textapi
import keys

def summarize(url, sentences_number = 10):
    client = textapi.Client(keys.aylienid, keys.aylienkey)
    
    #change this so afghanistan is not hardcoded in for now
    summary = client.Summarize({'url':url, 'sentences_number':10})
    for s in summary['sentences']:
        print s

if __name__ == "__main__":
    summarize('http://en.wikipedia.org/wiki/Afghanistan')
