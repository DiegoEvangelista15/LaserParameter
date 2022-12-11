from django.db import models


class Base(models.Model):

    criado = models.DateField('criado', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)

    class Meta:
        abstract = True


class Parameter(Base):

    TYPEMACHINE_CHOICE = (
        ('Chapa', 'Chapa'),
        ('Tubo', 'Tubo'),
    )

    MATERIAL_CHOICES = (
        ('carbon_steel', 'carbon_steel'),
        ('stainless_steel', 'stainless_steel'),
        ('aluminum', 'aluminum'),
        ('brass', 'brass'),
        ('galvanized', 'galvanized'),
        ('copper', 'copper'),
    )

    GAS_CHOICES = (
        ('O2', 'O2'),
        ('N2', 'N2'),
        ('Air', 'Air'),
    )

    PIERCING_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    #  sao os básicos para seleção dos parâmetros
    tipo = models.CharField('Tipo', max_length=50, choices=TYPEMACHINE_CHOICE)
    potencia = models.PositiveSmallIntegerField()
    espessura = models.PositiveSmallIntegerField()
    material = models.CharField(
        'Material', max_length=50, choices=MATERIAL_CHOICES)
    gas = models.CharField('Gas', max_length=50, choices=GAS_CHOICES)
    # parte os de corte padrão
    cut_speed = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    lift_height = models.DecimalField(
        max_digits=8, decimal_places=3, default=0)
    cut_height = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    cut_pressure = models.DecimalField(
        max_digits=8, decimal_places=3, default=0)
    peak_power = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    duty_cycle = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    pulse_frequency = models.DecimalField(
        max_digits=8, decimal_places=3, default=0)
    focus = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    laser_on_delay = models.DecimalField(
        max_digits=8, decimal_places=3, default=0)

    pierce_stage = models.CharField(
        'Piercing Stage', max_length=50, choices=PIERCING_CHOICES)

    # piercing 1
    step_time = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_height = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_gas = models.CharField('Gas', max_length=50, choices=GAS_CHOICES, null=True, blank=True)
    piercing_pressure = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_peak_power = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_duty_cycle = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_frequency = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_focus = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_time = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_extra_blow = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)

    # piercing 2
    step_time2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_height2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_gas2 = models.CharField('Gas', max_length=50, choices=GAS_CHOICES, null=True, blank=True)
    piercing_pressure2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_peak_power2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_duty_cycle2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_frequency2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_focus2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_time2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_extra_blow2 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)

    # piercing 3
    step_time3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_height3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_gas3 = models.CharField('Gas', max_length=50, choices=GAS_CHOICES, null=True, blank=True)
    piercing_pressure3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_peak_power3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_duty_cycle3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_frequency3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_focus3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_time3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)
    piercing_extra_blow3 = models.DecimalField(
        max_digits=8, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.tipo, self.potencia, self.espessura, self.material, self.gas)
