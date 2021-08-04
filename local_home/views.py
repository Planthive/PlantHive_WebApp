from django.shortcuts import render
from pymongo import MongoClient
from .utils import get_plot
from datetime import datetime
import os, json

def output(request):


    # this finds our json files
    path_to_json = 'C:\\JSON'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    client= MongoClient('localhost',27017)
    db=client["game"]
    collection=db["test"]

    # we need both the json and an index number so use enumerate()
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_data = json.load(json_file)

            collection.insert_one(json_data)

            client.close()

    for filename in os.listdir(path_to_json):
        file_path = os.path.join(path_to_json, filename)
        os.remove(file_path)

    return render(request, 'local_home/home.html',{'json_files': json_files} )


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
