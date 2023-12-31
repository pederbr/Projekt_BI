from .models import semestere, bedrift_data
import pandas as pd
import datetime as dt

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