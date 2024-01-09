from tkinter import font
from turtle import title

from matplotlib.pyplot import margins, subplot
from .models import semestere, bedrift_data
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio



def check_semester():
    for semester in semestere.objects.all():
        if not bedrift_data.objects.filter(semester=semester).exists():
            semestere.objects.filter(semester=semester).delete()



def process_csv_for_table(df, lunspres:bool)->tuple:
    #svarene på enten/eller spm
    q_list_1=[   
    df.loc[1:2],    #prosentandel kvinner
    df.loc[6:7],    #prosentandel data
    df.loc[40:41]]  #prosentandel som kunne tenke seg å jobbe der

    #finner prosentandeler
    temp=[]
    for elem in q_list_1:
        question=elem.values.tolist()
        ans1=int(question[0][1])
        ans2=int(question[1][1])
        temp.append(round((ans1/(ans1+ans2)),2))

        #svarene på veldig_bra til veldig_dårlig spørsmålene
    if lunspres:
        q_list=[
        df.loc[10:14],  #fordeling_klassetrinn
        df.loc[65:69],  #fremforing_presentasjon
        df.loc[72:76],  #kunnskap_bedrift_pre
        df.loc[79:83],  #kunnskap_bedrift_post
        df.loc[86:90],  #info_jobb
        df.loc[58:62],  #innhold_presentasjon
        df.loc[17:21],  #intterresant_arbeid
        df.loc[33:37],  #sosialt_miljø
        df.loc[44:48],  #arbeidsvilkår
        df.loc[51:55],  #helhetsvurdering_bedrift
        df.loc[104:108]]#inntrykk_arrangement
    else:
        q_list=[
        df.loc[10:14],  #fordeling_klassetrinn
        df.loc[72:76],  #fremforing_presentasjon
        df.loc[65:69],  #innhold_presentasjon
        df.loc[79:83],  #kunnskap_bedrift_pre
        df.loc[86:90],  #kunnskap_bedrift_post
        df.loc[93:97],  #info_jobb
        df.loc[58:62],  #mingling
        df.loc[17:21],  #intterresant_arbeid
        df.loc[33:37],  #sosialt_miljø
        df.loc[44:48],  #arbeidsvilkår
        df.loc[51:55],  #helhetsvurdering_bedrift
        df.loc[111:115]]#inntrykk_arrangement

    #gjør om svarene til gjennomsnitt og setter de inn i en tuppel i samme rekkefølge som i q_list
    temp1=[]
    for elem in q_list:
        question=elem.values.tolist()
        summ = 0
        votes = 0
        try:
            for index, score in enumerate(question):
                points = 5-index
                votes += int(score[1])
                summ += points*int(score[1])
            temp1.append(round((summ/votes),2))
        except:
            temp1.append(temp1[len(temp1)-1])
    if lunspres:
        temp1.insert(6, 0) #legger til 0 i listen for siden lunsjpreser ikke har mingling

    average_score_questions=tuple(temp+temp1)
    return average_score_questions



def process_csv_for_graph(df, lunspres:bool)->list:
    #svarene på enten/eller spm
    q_list_1=[   
    df.loc[1:2],    #kvinner/menn
    df.loc[6:7],    # data/komtek
    df.loc[40:41]]  #kunne tenke seg å jobbe der

    out_list_1=[]
    for elem in q_list_1:
        question=elem.values.tolist()
        temp=[]
        for elem in question:
            if type(elem[1]) == str:
                temp.append(tuple([elem[0] ,int(elem[1])] ) )
        if temp:
            out_list_1.append(temp)

        #svarene på veldig_bra til veldig_dårlig spørsmålene
    if lunspres:
        q_list=[
        df.loc[10:14],  #fordeling_klassetrinn
        df.loc[65:69],  #fremforing_presentasjon
        df.loc[72:76],  #kunnskap_bedrift_pre
        df.loc[79:83],  #kunnskap_bedrift_post
        df.loc[86:90],  #info_jobb
        df.loc[58:62],  #innhold_presentasjon
        df.loc[17:21],  #intterresant_arbeid
        df.loc[33:37],  #sosialt_miljø
        df.loc[44:48],  #arbeidsvilkår
        df.loc[51:55],  #helhetsvurdering_bedrift
        df.loc[104:108],#inntrykk_arrangement
        df.loc[24:30]]  #hva bedriften tilbyr
    else:
        q_list=[
        df.loc[10:14],  #fordeling_klassetrinn
        df.loc[72:76],  #fremforing_presentasjon
        df.loc[65:69],  #innhold_presentasjon
        df.loc[79:83],  #kunnskap_bedrift_pre
        df.loc[86:90],  #kunnskap_bedrift_post
        df.loc[93:97],  #info_jobb
        df.loc[58:62],  #mingling
        df.loc[17:21],  #intterresant_arbeid
        df.loc[33:37],  #sosialt_miljø
        df.loc[44:48],  #arbeidsvilkår
        df.loc[51:55],  #helhetsvurdering_bedrift
        df.loc[111:115],#inntrykk_arrangement
        df.loc[24:30]]  #hva bedriften tilbyr   

    out_list_2=[]
    for elem in q_list:
        question=elem.values.tolist()
        temp=[]
        for elem in question:
            if type(elem[1]) == str:
                temp.append(tuple([elem[0] ,int(elem[1])] ) )
        if temp:
            out_list_2.append(temp)   
    return out_list_1 + out_list_2



def get_semester(date_str:str)->str:
    date=dt.datetime.strptime(date_str, "%Y-%m-%d").date()
    year=str(date.year)
    semester=""
    if date.month in [1,2,3,4,5,6]:
        semester="v"+year[2:4]
    elif date.month in [7,8,9,10,11,12]:
        semester="h"+year[2:4]
    if semester:
        obj, created = semestere.objects.get_or_create(semester=semester)
        if created:
            obj.save()
    return semester



def draw_pie(data):
    labels = [x[0] for x in data]
    values = [x[1] for x in data]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, textinfo='label+percent')])  # hole parameter creates the donut shape
    return fig


def draw_bar(data):
    labels = [x[0] for x in data]
    values = [x[1] for x in data]
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    return fig

def create_html(data, name):
    subplot_types = [
        [{ "type":'domain' }], 
        [{ "type":'domain' }], 
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'domain' }], 
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }],
        [{ "type":'xy' }]]
    subplot_titles = [
        "Kjønnsfordeling",
        "Linjefordeling",
        "klassefordeling",
        "Hvor mye visste du om bedriften før presentasjonen?",
        "Hva vet du om bedriften etter presentasjonen?",
        "Kunne du tenke deg å jobbe for denne bedriften?",
        "Virker de daglige arbeidsoppgavene til bedriften interresante?",
        "hvilke av disse egenskapene tror du bedriften kan tilby?",
        "Hva er ditt inntrykk av arbeidsvilkårene til bedriften?",
        "Hva synes du om fremføringen av presentasjonen?",
        "Hva synes du om innholdet i presentasjonen?",
        "Hvordan var informasjonen om sommerjobber og ledige stillinger",
        "Hvordan gikk minglingen etter presentasjonen?",
        "Hva er ditt inntrykk av det sosiale miljøet i bedriften?",
        "Hva er din helhetsvurdering av bedriften?",
        "Hva er din helhetsvurdering av arrangementet?"]
    fig = make_subplots(
        rows=16, cols=1, 
        specs=subplot_types, 
        subplot_titles=subplot_titles, 
        vertical_spacing=0.03,
        x_title="Antall svar")     
    list_of_graphs = [
        draw_pie(data[0]),    #/mennkvinner
        draw_pie(data[1]),    #retning
        draw_bar(data[3]),    #klassetrinn
        draw_bar(data[6]),    #kunnskap_bedrift_pre
        draw_bar(data[7]),    #kunnskap_bedrift_post
        draw_pie(data[2]),    #kunne tenke seg å jobbe der
        draw_bar(data[-6]),   #intterresant_arbeid
        draw_bar(data[-1]),   #hva bedriften tilbyr
        draw_bar(data[-4]),   #arbeidsvilkår
        draw_bar(data[4]),    #fremforing_presentasjon
        draw_bar(data[5]),    #innhold_presentasjon
        draw_bar(data[8]),    #info_jobb
        draw_bar(data[9]),    #mingling
        draw_bar(data[-5]),   #sosialt_miljø
        draw_bar(data[-3]),   #helhetsvurdering_bedrift
        draw_bar(data[-2])]   #helhetsvurdering_arrangement
    for i, graph in enumerate(list_of_graphs, start=1):
        fig.add_trace(graph.data[0], row=i, col=1)
    fig.update_layout(height=6000, width=842, title_text=name, showlegend=False)
    fig.show()