from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
from .utils import get_plot, get_image, get_climate_recipe
from datetime import datetime
from rest_framework import viewsets
import io, os, json
import json,requests
import numpy as np
from PIL import Image
import base64
from .models import sensors, images, growthrecipe

def get(request):
    path_to_json = 'C:\\JSON'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            data = json.load(json_file)
    return render(request, 'local_home/home.html',{'data': data})


def send(self, request):

    return render(request, 'local_home/home.html',{'json_data': json_data} )


def state(request):
    # this finds our json files

    return render(request, 'local_home/home.html',{} )

def importData(request):
    # this finds our json files

    return render(request, 'local_home/home.html',{} )

def exportData(request):
        # this finds our json files

    return render(request, 'local_home/home.html',{} )


def home(request):
    # get sensor data for display
    query_data=sensors.objects.all()

    x=[]
    y = [[] for _ in range(6)]
    for data in query_data:
        dt=data.metadata
        ts=dt['timestamp']
        dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')
        x.append(dt)
        actuators=data.actuators
        y[0].append(actuators['led']['white']['value'])
        y[1].append(actuators['led']['blue']['value'])
        y[2].append(actuators['led']['green']['value'])
        y[3].append(actuators['led']['red1']['value'])
        y[4].append(actuators['led']['red2']['value'])
        y[5].append(actuators['led']['farred']['value'])
        chart = get_plot(x,y)
    # get image data for display
    query_data=images.objects.all()
    img = get_image(query_data)

    # get growth recipe for display
    query_data=growthrecipe.objects.all()
    growthrecipe_chart=get_climate_recipe(query_data)



    return render(request, 'local_home/home.html', {'chart': chart, 'img': img, 'growthrecipe_chart': growthrecipe_chart })
