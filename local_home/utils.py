import matplotlib.pyplot as plt
import base64
from io import BytesIO
from pymongo import MongoClient
from datetime import datetime
import numpy as np
from PIL import Image

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,4))
    plt.title('White')
    plt.plot(x,y[0],x,y[1],x,y[2],x,y[3],x,y[4],x,y[5])
    plt.xlabel('time')
    plt.ylabel('LED')
    graph=get_graph()
    return graph

def get_image(query_data):
    for data in query_data:
        dt=data.metadata
        ts=dt['timestamp']
        dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')

        img=data.data
        imgdata = np.zeros((5, 5, 3), dtype=np.uint8)
        imgdata[:,:,0]=img['red']['matrix']
        imgdata[:,:,1]=img['green']['matrix']
        imgdata[:,:,2]=img['blue']['matrix']
        img = Image.fromarray(imgdata, 'RGB')
        buffer = BytesIO()
        img.save(buffer, format='PNG')

        buffer.seek(0)
        image_png=buffer.getvalue()
        img=base64.b64encode(image_png)
        img=img.decode('utf-8')
        buffer.close()
        return img

def get_climate_recipe(query_data):
    # start with empty list
    x=[]
    y = [[] for _ in range(9)]
    for data in query_data:
        dt=data.timestamps
        key=list(dt.keys())
        i=0
        for data_ in key:
            ts=data_
            ts = datetime.strptime(ts, '%d.%m.%Y %H:%M')
            x.append(ts)

            entry=dt[data_]
            if i>0:
                previous_entry=dt[key[i-1]]
                x.append(ts)
                y[0].append(previous_entry['sensors']['temperature']['air']['targetvalue'])
                y[1].append(previous_entry['sensors']['temperature']['water']['targetvalue'])
                y[2].append(previous_entry['sensors']['humidity']['targetvalue'])
                y[3].append(previous_entry['sensors']['soilmoisture']['targetvalue'])
                y[4].append(previous_entry['sensors']['waterlevel']['targetvalue'])
                y[5].append(previous_entry['actuators']['led']['blue']['targetvalue'])
                y[6].append(previous_entry['actuators']['led']['green']['targetvalue'])
                y[7].append(previous_entry['actuators']['led']['red']['targetvalue'])
                y[8].append(previous_entry['actuators']['led']['farred']['targetvalue'])

            y[0].append(entry['sensors']['temperature']['air']['targetvalue'])
            y[1].append(entry['sensors']['temperature']['water']['targetvalue'])
            y[2].append(entry['sensors']['humidity']['targetvalue'])
            y[3].append(entry['sensors']['soilmoisture']['targetvalue'])
            y[4].append(entry['sensors']['waterlevel']['targetvalue'])
            y[5].append(entry['actuators']['led']['blue']['targetvalue'])
            y[6].append(entry['actuators']['led']['green']['targetvalue'])
            y[7].append(entry['actuators']['led']['red']['targetvalue'])
            y[8].append(entry['actuators']['led']['farred']['targetvalue'])

            i=i+1
        growthrecipe_chart = get_plot(x,y)

        return growthrecipe_chart

# def get_db_handle(db_name, host, port, username, password):
#     client = MongoClient(host=host,
#                       port=int(port),
#                       username=username,
#                       password=password
#                      )
#     db_handle = client['db_name']
#     return db_handle, client
