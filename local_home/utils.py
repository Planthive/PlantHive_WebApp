import matplotlib.pyplot as plt
import base64
from io import BytesIO

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
