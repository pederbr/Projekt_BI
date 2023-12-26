from datetime import datetime
from email.policy import default
from django.db import models

class opplastede_filer(models.Model):
    navn = models.CharField(max_length=255)
    fil = models.FileField()
    dato_bedpres = models.DateField()
    dato_lagret = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.navn

class bedrift_data(models.Model):
    dato_bedpres = models.DateField()
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





