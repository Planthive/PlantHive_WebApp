from django.shortcuts import render
from pymongo import MongoClient
from .utils import get_plot
from datetime import datetime

def home(request):
    client= MongoClient('localhost',27017)
    db=client["game"]
    collection=db["test"]
    collection.count_documents({})
    A = collection.find()
    x=[]
    y = [[] for _ in range(6)]
    i=0
    for data in A:
        dt=data['metadata']['timestamp']
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
        x.append(dt)
        LED_white=data['actuators']['led']['white']['value'];
        y[0].append(data['actuators']['led']['white']['value'])
        y[1].append(data['actuators']['led']['blue']['value'])
        y[2].append(data['actuators']['led']['green']['value'])
        y[3].append(data['actuators']['led']['red1']['value'])
        y[4].append(data['actuators']['led']['red2']['value'])
        y[5].append(data['actuators']['led']['farred']['value'])
        chart = get_plot(x,y)

    return render(request, 'local_home/home.html',{'chart': chart})
