from django.db import models

# Create your models here.

class TpsCylinder(models.Model):
    name = models.CharField(max_length=20, unique=True, error_messages={
        'unique': 'Existe un tipo de cilindro con el mismo nombre',
    })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dts_user = models.ForeignKey('auth.User', related_name='tps_cylinder_user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tps_cylinder'
        ordering = ('name',)

class DtsCylinder(models.Model):
    size = models.CharField(max_length=20, unique=True, error_messages={
        'unique': 'Existe un cilindro con el mismo nombre',
    })
    weight = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tps_cylinder = models.ForeignKey('common.TpsCylinder', related_name='tps_cylinder', on_delete=models.CASCADE)
    dts_user = models.ForeignKey('auth.User', related_name='dts_cylinder_user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dts_cylinder'
        ordering = ('weight',)

class DtsPerson(models.Model):
    class Sex(models.IntegerChoices):
        MEMENINE = 1
        MALE = 2

    dni = models.IntegerField(unique=True, error_messages={
        'unique': 'Existe una persona con el mismo número de dni',
    })
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_surname = models.CharField(max_length=30)
    sex = models.IntegerField(choices=Sex.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dts_user = models.ForeignKey('auth.User', related_name='dts_person_user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dts_person'
        ordering = ('dni',)

class DtsCylinderPerson(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dts_cylinder = models.ForeignKey('common.DtsCylinder', related_name='dts_cylinder', on_delete=models.CASCADE)
    dts_person = models.ForeignKey('common.DtsPerson', related_name='dts_person', on_delete=models.CASCADE)
    dts_user = models.ForeignKey('auth.User', related_name='dts_cylinder_person', on_delete=models.CASCADE)