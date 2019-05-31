import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode = 'linecharts', name ='markers')
data = [trace]

layout = go.Layout(title = 'Line Charts', hovermode='closest')
fig = go.Figure(data = data, layout=layout)

pyo.plot(fig, filename='linecharts.html')
