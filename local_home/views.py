from django.shortcuts import render
from pymongo import MongoClient
from .utils import get_plot

def home(request):
    client= MongoClient('localhost',27017)
    db=client["game"]
    collection=db["test"]
    collection.count_documents({})
    A = collection.find()
    x=[]
    y=[]
    i=0
    for data in A:
        #x.append(data['metadata']['timestamp'])
        x.append(i)
        y.append(data['actuators']['led']['white']['value'])
        i = i+1
        chart = get_plot(x,y)

    return render(request, 'local_home/home.html',{'chart': chart})
