import pandas as pd

def avg_values(filename:str)->tuple:

    df = pd.read_csv(filename)

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
        for index, score in enumerate(question):
            points = 5-index
            votes += int(score[1])
            summ += points*int(score[1])
        temp1.append(round((summ/votes),2))

    average_score_questions=tuple(temp+temp1)
    return average_score_questions


