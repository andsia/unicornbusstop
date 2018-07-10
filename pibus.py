from UHScroll import *
import pywapi
import unicornhat as unicorn

def nextBus(stop):
    stop = str(stop)
    r = requests.get('http://api.tfl.gov.uk/stopPoint/'+stop)
    json_result = r.json()
    all_stops = json_result['arrivals']
    my_stops = []
    for x in all_stops:
        if x['isRealTime']== True and x['isCancelled'] == False and x['routeName']=="71":
            x = str(x['estimatedWait'][:-4])
            if x == '':
                x = '0'
            mystops.append(x)
        return my_stops

while True:
    try:
        a = nextBus('490013457N')

    except:
\
        a = 'Tfl error'

    for i in range (0,1):
        unicorn_scroll(a, 'green',255,0.04)}
