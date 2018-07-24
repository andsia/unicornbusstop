import requests

def getTime():
    r = requests.get("http://api.tfl.gov.uk/stopPoint/490013457N/Arrivals")
    json_result = r.json()
    my_stops = []
    for x in json_result:
        y = str(int(x['timeToStation']/60)).zfill(2) + ' min ' + str(x['lineId'])
        my_stops.append(y)

    print(my_stops)
    my_stops.sort()
    print(my_stops)


getTime()

