import random
import plotly

N = 1000
trace = plotly.graph_objs.Scatter(
    x = [random.randint(0,N) for x in range(N)],
    y = [random.randint(0,N) for y in range(N)],
    mode = 'markers'
)

plotly.offline.plot([trace], filename='basic-line.html', auto_open=False)
