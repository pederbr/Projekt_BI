import re
from urllib import request
from django.http import HttpResponse, Http404
from django.template import loader, TemplateDoesNotExist
from django.shortcuts import redirect, render
from .models import bedrift_data, opplastede_filer, semestere
from .forms import filForm
from .utils import process_csv_for_graph, process_csv_for_table, get_semester, check_semester, draw_pie, draw_bar
import pandas as pd
from django.contrib import messages

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def upload(request):
  form=filForm() 
  if request.method == "POST":
    form = filForm(request.POST, request.FILES)
    print(request.POST["dato_bedpres"])
    if form.is_valid():
      document=form.save()
      lunsjpres = form.cleaned_data['lunsjpres']
      try:
        print(document.fil)
        dataframe = pd.read_csv(document.fil)
        try:
          tp = process_csv_for_table(dataframe, lunsjpres)
          if len(tp)==15: #sjekker om fila er behandlet på riktig måte
              new_entry=bedrift_data( #laster opp data fra tuplen til modellen
                dato_bedpres = request.POST["dato_bedpres"],
                navn_bedrift = request.POST["navn"], 
                semester = get_semester(request.POST["dato_bedpres"]),
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
        except Exception as e:  # handle specific exceptions
          print(f"An error occurred: {e}")
          messages.error(request, "feil i filen, sjekk at den er formatert riktig")
          return redirect("upload")
      except Exception as e:  # handle specific exceptions
        print(f"An error occurred: {e}")
        messages.error(request, "feil filformat.")
        return redirect("upload")
  return render(request, "upload.html", {"form": form})


def statistikk(request):
  if request.GET.get('id'):
    semester = (request.GET.get('id'))
  else: 
    semester = "v24"
  bedriftdata = bedrift_data.objects.filter(semester=semester)
  alle_semestre = semestere.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'alle_semestre': alle_semestre,
    'bedriftdata': bedriftdata,
    'semester': semester
  }
  return HttpResponse(template.render(context, request))

def del_bedpres(request):
  id = int(request.GET.get('id'))
  try:
      mydata = bedrift_data.objects.get(id=id)
      mydata.delete()
  except bedrift_data.DoesNotExist:
      pass
  check_semester()
  return redirect("statistikk")

def statistikk_mal(request):
  lunsjpres = False
  if request.GET.get('id'):
    id = (request.GET.get('id'))
  else: 
    id = 1
  try:
      file_data = opplastede_filer.objects.get(id=id)
  except opplastede_filer.DoesNotExist:
      raise Http404("File not found.")
  try:
      dataframe = pd.read_csv(file_data.fil.path)
  except pd.errors.ParserError:
      return HttpResponse("Error reading CSV file.")
  try:
      data = process_csv_for_graph(dataframe, lunsjpres)
  except Exception as e:
      return HttpResponse(f"Error processing CSV file: {e}")
  try:
    list_of_graphs = [
      draw_pie(data[0]),    #kvinner/menn
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
      draw_bar(data[-2])]  #helhetsvurdering_arrangement
  except Exception as e:
    return HttpResponse(f"Error drawing graphs: {e}")
  try:
      template = loader.get_template('statistikk_mal.html')
  except TemplateDoesNotExist:
      return HttpResponse("Template not found.")
  context = {
      'list_of_graphs': list_of_graphs
  }
  return HttpResponse(template.render(context, request))