from datetime import datetime
from email.policy import default
from django.db import models

class opplastede_filer(models.Model):
    navn = models.CharField(max_length=255)
    fil = models.FileField(upload_to="static/CSV")
    dato_lagret = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.navn

class bedrift_data(models.Model):

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

#test=bedrift_data(navn_bedrift="WS_e_tjenesten", andel_kvinner=0.26, andel_data=0.23, andel_interreserte=0.92, fordeling_klassetrinn=2.67, fremforing_presentasjon=4.51, innhold_presentasjon=4.46, kunnskap_bedrift_pre=2.64, kunnskap_bedrift_post=3.74, info_jobb=4.18, mingling=3.9, intterresant_arbeid=4.79, sosialt_miljø=4.15, arbeidsvilkår=4.23, helhetsvurdering=4.77, inntrykk_arrangement=2.33)




