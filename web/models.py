from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length = 120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50) #TODO: do not save password




class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    #newuser = str(user)
    def __str__(self):
        return 'Token %s' % self.user 

class Exopense(models.Model):
    text = models.CharField(_("Name"), max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        #return  '%s' % self.user , self.text, self.amount
        return '{} {} {}'.format(self.user, self.text, self.amount)



class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        #return  '%s' % self.user , self.text, self.amount
        return '{} {} {}'.format(self.user, self.text, self.amount)
