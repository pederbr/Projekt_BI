from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import bedrift_data
from .forms import filForm
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def upload(request):
  if request.method == "POST":
    form = filForm(request.POST, request.FILES)
    data_from_file=tuple()
    if form.is_valid():
      document=form.save()
      dataframe = pd.read_csv(document.fil)
      tp = process_csv(dataframe)
      new_entry=bedrift_data(
         navn_bedrift=request.POST["navn"], 
         andel_kvinner = tp[0], 
         andel_data = tp[1], 
         andel_interreserte = tp[2], 
         fordeling_klassetrinn = tp[3], 
         fremforing_presentasjon = tp[4], 
         innhold_presentasjon = tp[5], 
         kunnskap_bedrift_pre = tp[6], 
         kunnskap_bedrift_post = tp[7], 
         info_jobb = tp[8], 
         mingling = tp[9], 
         intterresant_arbeid = tp[10], 
         sosialt_miljø = tp[11], 
         arbeidsvilkår = tp[12], 
         helhetsvurdering = tp[13], 
         inntrykk_arrangement = tp[14]
         )
      new_entry.save()
      return redirect("statistikk")
  else:
    form=filForm() 
    data_from_file=tuple()
  return render(request, "upload.html", {"form": form, "data_from_file":data_from_file})


def statistikk(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))



def process_csv(df)->tuple:


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

