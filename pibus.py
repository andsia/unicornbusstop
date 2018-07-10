{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
from UHScroll import *\
import pywapi\
import unicornhat as unicorn\
\
def nextBus(stop):\
    stop = str(stop)\
    r = requests.get('http://api.tfl.gov.uk/stopPoint/'+stop)\
    json_result = r.json()\
    all_stops = json_result['arrivals']\
    my_stops = []\
    for x in all_stops:\
        if x['isRealTime']== True and x['isCancelled'] == False and x['routeName']=="71":\
            x = str(x['estimatedWait'][:-4])\
            if x == '':\
                x = '0'\
            mystops.append(x)\
        return my_stops\
\
while True:\
    try:\
        a = nextBus('490013457N')\
\
    except:\
\
        a = 'Tfl error'\
        \
    for i in range (0,1):\
        unicorn_scroll(a, 'green',255,0.04)}