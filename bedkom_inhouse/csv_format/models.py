from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

class opplastede_filer(models.Model):
    navn = models.CharField(max_length=255)
    fil = models.FileField()
    dato_bedpres = models.DateField()
    dato_lagret = models.DateTimeField(default=timezone.now)
    lunsjpres = models.BooleanField(default=False)
    def __str__(self):
        return self.navn

class semestere(models.Model):
    semester= models.CharField(max_length=255, default="h23")
    def __str__(self):
        return self.semester

class bedrift_data(models.Model):
    id_opplastede_filer = models.IntegerField()
    dato_bedpres = models.DateField()
    semester= models.CharField(max_length=255, default="h23")
    navn_bedrift = models.CharField(max_length=255)
    andel_kvinner = models.FloatField()
    andel_data = models.FloatField()
    andel_interreserte = models.FloatField()
    fordeling_klassetrinn = models.FloatField()
    fremforing_presentasjon = models.FloatField()
    innhold_presentasjon = models.FloatField()
    kunnskap_bedrift_pre = models.FloatField()
    kunnskap_bedrift_post = models.FloatField()
    info_jobb = models.FloatField()
    mingling = models.FloatField()
    intterresant_arbeid = models.FloatField()
    sosialt_miljø = models.FloatField()
    arbeidsvilkår = models.FloatField()
    helhetsvurdering = models.FloatField()
    inntrykk_arrangement = models.FloatField()





