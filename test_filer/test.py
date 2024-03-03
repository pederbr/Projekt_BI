import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

data = [
[#kvinner/menn
    ('Kvinne', 2), 
    ('Mann', 37)], 
[#retning
    ('Datateknologi', 25), 
    ('Kommunikasjonsteknologi og digital sikkerhet', 14)],
[#kunne tenke seg å jobbe der
    ('Ja', 38), 
    ('Nei', 1)],
[#klassetrinn
    ('5.', 2), 
    ('4.', 5), 
    ('3.', 1), 
    ('2.', 10), 
    ('1.', 21)]
  ]

def draw_pie(data):
    labels = [x[0] for x in data]
    values = [x[1] for x in data]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])  # hole parameter creates the donut shape
    return fig


def draw_bar(data):
    labels = [x[0] for x in data]
    values = [x[1] for x in data]
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    return fig

def create_html(data, name="bedriftspresentasjon"):
    subplot_types = [
        [{ "type":'domain' }], 
        [{ "type":'domain' }], 
        [{ "type":'xy' }]]
    subplot_titles = [
        "Kjønnsfordeling",
        "Linjefordeling",
        "Klassefordeling"]
    fig = make_subplots(
        rows=3, cols=1, 
        specs=subplot_types, 
        subplot_titles=subplot_titles, 
        vertical_spacing=0.03,
        x_title="Antall svar" 
        )
    list_of_graphs = [
        draw_pie(data[0]),    #/mennkvinner
        draw_pie(data[1]),    #retning
        draw_bar(data[3]),    #klassetrinn
    ]
    for i, graph in enumerate(list_of_graphs, start=1):
        fig.add_trace(graph.data[0], row=i, col=1)
    fig.update_layout(height=1000, width=842, title_text=name, showlegend=False)
create_html(data)
