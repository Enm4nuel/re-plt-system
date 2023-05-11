from django.db import models
from plantillas.models import *

# Create your models here.


class ToMri(models.Model):
    cmbatch = models.CharField(max_length=10, db_column="CMBATCH")  # numero de batch
    item = models.IntegerField(primary_key=True, db_column="ITEM")  # por cada fila incrementa su valor, de 1 a n numeros
    bldgid = models.CharField(max_length=10, db_column="BLDGID")  # edificio al que se esta facturando
    leasid = models.CharField(max_length=10, db_column="LEASID")  # numero de contrato
    trandate = models.DateField(db_column="TRANDATE")  # fecha de facturacion
    inccat = models.CharField(max_length=6, db_column="INCCAT")  # income category
    srccode = models.CharField(
        max_length=2, default="CH", db_column="SRCCODE"
    )  # por default es CH, source code y ch es que se va facturar
    descrptn = models.CharField(max_length=50, db_column="DESCRPTN")  # descripcion breve de este campo
    tranamt = models.DecimalField(max_digits=9, decimal_places=2, db_column="TRANAMT")  # valor a facturar
    chkdesc = models.CharField(max_length=30, default="", db_column="CHKDESC")  # SIN USO
    refnmbr = models.CharField(max_length=30, default="", db_column="REFNMBR")  # SIN USO
    taxmod = models.CharField(max_length=30, default="", db_column="TAXMOD")  # SIN USO
    rtaxamt = models.CharField(max_length=30, default="", db_column="RTAXAMT")  # SIN USO
    invoice = models.CharField(max_length=30, default="", db_column="INVOICE")  # SIN USO
    cashtype = models.CharField(max_length=30, default="", db_column="CASHTYPE")  # SIN USO
    taxitem = models.CharField(default="N", max_length=1, db_column="TAXITEM")  # por default lleva N
    jobcode = models.CharField(max_length=30, default="", db_column="JOBCODE")  # SIN USO
    bankid = models.CharField(max_length=30, default="", db_column="BANKID")  # SIN USO
    retropd = models.CharField(max_length=30, default="", db_column="RETROPD")  # SIN USO
    rtaxgrpid = models.CharField(max_length=6, db_column="RTAXGRPID")  # se extrae de una vista X
    department = models.CharField(default="@", max_length=30, db_column="DEPARTMENT")  # por default lleva @
    postorder = models.CharField(max_length=30, default="", db_column="POSTORDER")  # SIN USO
    currcode = models.CharField(max_length=3, db_column="CURRCODE")  # Moneda en la que se esta facturando
    bcurcode = models.CharField(max_length=3, default="DOP", db_column="BCURCODE")  # moneda base
    bctranamt = models.CharField(max_length=30, default="", db_column="BCTRANAMT")  # SIN USO
    bcrtaxamt = models.CharField(max_length=30, default="", db_column="BCRTAXAMT")  # SIN USO
    bcexchgref = models.CharField(max_length=30, default="", db_column="BCEXCHGREF")  # SIN USO
    adjinvoice = models.CharField(max_length=30, default="", db_column="ADJINVOICE")  # SIN USO
    adjflag = models.CharField(max_length=30, default="", db_column="ADJFLAG")  # SIN USO
    wtaxid = models.CharField(max_length=30, default="", db_column="WTAXID")  # SIN USO
    recpttypeid = models.CharField(max_length=30, default="", db_column="RECPTTYPEID")  # SIN USO
    jc_phasecode = models.CharField(max_length=30, default="", db_column="JC_PHASECODE")  # SIN USO
    applyflag = models.CharField(max_length=30, default="", db_column="APPLYFLAG")  # SIN USO
    autoexception = models.CharField(max_length=30, default="", db_column="AUTOEXCEPTION")  # SIN USO
    recptno = models.CharField(max_length=30, default="", db_column="RECPTNO")  # SIN USO
    recptscreen = models.CharField(max_length=30, default="", db_column="RECPTSCREEN")  # SIN USO
    addldesc = models.CharField(max_length=30, default="", db_column="ADDLDESC")  # SIN USO
    sdtranid = models.CharField(max_length=30, default="", db_column="SDTRANID")  # SIN USO

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
