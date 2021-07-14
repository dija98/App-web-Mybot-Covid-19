import requests 
import json 
import urllib
import pandas as pd


def get_data(url):
    import requests
    data = requests.get(url )
    return data.json()


url = 'https://pomber.github.io/covid19/timeseries.json'
result = get_data(url)


df = pd.DataFrame(result)
last=dict()
last= df['Morocco'].iloc[-1]

a= "The statistics of COVID-19 in Morocco for date : %s ,    confirmed : %s,     deaths: %s,   recovered: %s " % (last.get('date'), last.get('confirmed'), last.get('deaths'), last.get('recovered'))
#print("The statistics of COVID-19 in Morocco for date : %s" % last.get('date'))
#print("confirmed : %s" % last.get('confirmed'))
#print("deaths: %s" % last.get('deaths'))
#print("recovered: %s" % last.get('recovered'))










#df=pd.read_json('https://pomber.github.io/covid19/timeseries.json')
#r= requests.get('https://pomber.github.io/covid19/timeseries.json').json
#print(r.json())
#s=json.dumps(r)
#data= json.loads(s)
#for symbol in data["Morocco"]:
     #print(symbol)


#for key,v in result.items():#
    #if key=='Morocco':
        #print(v)

#if _name_ == '_main_':
#import main

#test=pd.DataFrame([['tag',"statistique"],['patterns',"how many cases?", " recovered cases?",],['responses', a,'b']], columns=['intents', 'value1','value2'])
#print(test)
#d={}
#for i in df['tag'].unique():
    #d[i]= [{df['value1'][j]: df['value2'][j]} for j in df[df['tag']==i].index]
#with open('intents.json','w') as outfile:

#print(df)     
     











#a= "les statistiques de covid19 au maroc pour la date : %s ,    Cas confirmés : %s,     décés: %s,   guéris: %s " % (last.get('date'), last.get('confirmed'), last.get('deaths'), last.get('recovered'))