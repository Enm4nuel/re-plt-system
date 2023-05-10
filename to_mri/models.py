from django.db import models
from plantillas.models import *

# Create your models here.


class ToMri(models.Model):
    cmbatch = models.CharField(max_length=10)  # numero de batch
    item = models.IntegerField(primary_key=True, verbose_name="ITEM")  # por cada fila incrementa su valor, de 1 a n numeros
    bldgid = models.CharField(max_length=10)  # edificio al que se esta facturando
    leasid = models.CharField(max_length=10)  # numero de contrato
    trandate = models.DateField()  # fecha de facturacion
    inccat = models.CharField(max_length=6)  # income category
    srccode = models.CharField(
        max_length=2, default="CH"
    )  # por default es CH, source code y ch es que se va facturar
    descrptn = models.CharField(max_length=50)  # descripcion breve de este campo
    tranamt = models.DecimalField(max_digits=9, decimal_places=2)  # valor a facturar
    chkdesc = models.CharField(max_length=30, default="")  # SIN USO
    refnmbr = models.CharField(max_length=30, default="")  # SIN USO
    taxmod = models.CharField(max_length=30, default="")  # SIN USO
    rtaxamt = models.CharField(max_length=30, default="")  # SIN USO
    invoice = models.CharField(max_length=30, default="")  # SIN USO
    cashtype = models.CharField(max_length=30, default="")  # SIN USO
    taxitem = models.CharField(default="N", max_length=1)  # por default lleva N
    jobcode = models.CharField(max_length=30, default="")  # SIN USO
    bankid = models.CharField(max_length=30, default="")  # SIN USO
    retropd = models.CharField(max_length=30, default="")  # SIN USO
    rtaxgrpid = models.CharField(max_length=6)  # se extrae de una vista X
    department = models.CharField(default="@", max_length=30)  # por default lleva @
    postorder = models.CharField(max_length=30, default="")  # SIN USO
    currcode = models.CharField(max_length=3)  # Moneda en la que se esta facturando
    bcurcode = models.CharField(max_length=3, default="DOP")  # moneda base
    bctranamt = models.CharField(max_length=30, default="")  # SIN USO
    bcrtaxamt = models.CharField(max_length=30, default="")  # SIN USO
    bcexchgref = models.CharField(max_length=30, default="")  # SIN USO
    adjinvoice = models.CharField(max_length=30, default="")  # SIN USO
    adjflag = models.CharField(max_length=30, default="")  # SIN USO
    wtaxid = models.CharField(max_length=30, default="")  # SIN USO
    recpttypeid = models.CharField(max_length=30, default="")  # SIN USO
    jc_phasecode = models.CharField(max_length=30, default="")  # SIN USO
    applyflag = models.CharField(max_length=30, default="")  # SIN USO
    autoexception = models.CharField(max_length=30, default="")  # SIN USO
    recptno = models.CharField(max_length=30, default="")  # SIN USO
    recptscreen = models.CharField(max_length=30, default="")  # SIN USO
    addldesc = models.CharField(max_length=30, default="")  # SIN USO
    sdtranid = models.CharField(max_length=30, default="")  # SIN USO

    def __str__(self):
        template = "{0.bldgid} {0.leasid} {0.descrptn} {0.tranamt}"
        return template.format(self)

    def getColumns(self):
        columns = [
            "CMBATCH",
            "ITEM",
            "BLDGID",
            "LEASID",
            "TRANDATE",
            "INCCAT",
            "SRCCODE",
            "DESCRPTN",
            "TRANAMT",
            "CHKDESC",
            "REFNMBR",
            "TAXMOD",
            "RTAXAMT",
            "INVOICE",
            "CASHTYPE",
            "TAXITEM",
            "JOBCODE",
            "BANKID",
            "RETROPD",
            "RTAXGRPID",
            "DEPARTMENT",
            "POSTORDER",
            "CURRCODE",
            "BCURCODE",
            "BCTRANAMT",
            "BCRTAXAMT",
            "BCEXCHGREF",
            "ADJINVOICE",
            "ADJFLAG",
            "WTAXID",
            "RECPTTYPEID",
            "JC_PHASECODE",
            "APPLYFLAG",
            "AUTOEXCEPTION",
            "RECPTNO",
            "RECPTSCREEN",
            "ADDLDESC",
            "SDTRANID",
        ]
        return columns

    class Meta:
        verbose_name = "Dato para MRI"
        verbose_name_plural = "Datos para MRI"
        db_table = "tomri_data"
        ordering = ["item"]
