from django.db import models
from django.utils.translation import gettext_lazy as _

class Vehicle(models.Model):
    #  enum
    class Vehicle_Manufactures(models.TextChoices):
        FORD = 'Ford', _('Ford')
        GMC = 'GMC', _('GMC')
        TESLA = 'TESLA', _('TESLA')

    #  enum
    class Vehicle_Status(models.TextChoices):
        ACTIVE = 'Active', _('Active')
        INOPERATIVE = 'Inoperative', _('Inoperative')
        INACTIVE = 'Inactive', _('Inactive')

    unit_num = models.CharField(max_length=100, unique=True, primary_key=True)
    mileage = models.IntegerField()
    manufacturer = models.CharField(choices=Vehicle_Manufactures.choices, max_length=5)
    status = models.CharField(choices=Vehicle_Status.choices, max_length=15)

    @property
    def history(self):
        return self.history_set.all()


class History(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    mileage = models.IntegerField()

    def milageFromCurrentDate(self, currentMileage):
        return currentMileage - self.mileage




