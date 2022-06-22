from django.db import models
from django.urls import reverse
from django.utils import timezone


class profile(models.Model):
    fio = models.CharField(max_length=50)
    ID_worker = models.DecimalField(max_digits=5, decimal_places=0)
    position = models.CharField(max_length=50)
    b_date = models.DateField(auto_now_add=False)
    w_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    phone = models.DecimalField(max_digits=9, decimal_places=0)

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('prof', kwargs={'prof_id': self.pk})

class tool_n(models.Model):
    tool = models.CharField(max_length=50)

    def __str__(self):
        return self.tool


class tool_use(models.Model):
    date_of_take = models.DateTimeField(auto_now_add=False)
    date_of_give = models.DateTimeField(null=True)
    tool_s = models.BooleanField(null=False)
    t_n = models.ForeignKey('tool_n', on_delete=models.PROTECT)


class Tasker(models.Model):
    tas = models.CharField(max_length=50)
    opisan = models.TextField()

    def __str__(self):
        return self.tas

class TehProc(models.Model):
    Teh_name = models.CharField(max_length=50)
    tas_n = models.ForeignKey('Tasker', on_delete=models.PROTECT, null=True)
    to_on = models.ForeignKey('tool_n', on_delete=models.PROTECT)

    def __str__(self):
        return self.Teh_name

class Teh_use(models.Model):
    ID_worker_t = models.ForeignKey('profile', on_delete=models.PROTECT, null=True)
    comment = models.TextField(blank=True)
    er = models.BooleanField(null=False)
    Date = models.DateField(null=False)
    U_tool = models.ForeignKey('tool_use', on_delete=models.PROTECT, null=True)  # а он тут нужен?
    N_Tec = models.ForeignKey('TehProc', on_delete=models.PROTECT, null=True)
