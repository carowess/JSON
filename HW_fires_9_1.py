import json

infile = open('US_fires_9_1.json','r')

fire_data = json.load(infile)

lons = []
lats = []
brights = []
hover_texts = []

for fire in fire_data:
    lon = fire["longitude"]
    lat = fire["latitude"]
    bright = fire["brightness"]
    date = fire["acq_date"]
    lons.append(lon)
    lats.append(lat)
    if bright > 450:
        brights.append(bright)
    hover_texts.append(date)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon=lons,lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [b/100 for b in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout = Layout(title='US Fires - 9/1/2020 through 9/13/2020')

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='US_fires_9_1.html')

