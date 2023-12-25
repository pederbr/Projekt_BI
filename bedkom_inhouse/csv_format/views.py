from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import bedrift_data
from .forms import filForm



def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

filForm()
def upload(request):
  if request.method == "POST":
    form = filForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("statistikk")
  else:
    form=filForm() 
  return render(request, "upload.html", {"form": form})


def statistikk(request):
  mydata = bedrift_data.objects.all()
  template = loader.get_template('statistikk.html')
  context = {
    'bedriftdata': mydata,
  }
  return HttpResponse(template.render(context, request))

