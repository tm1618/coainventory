from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from simple_history.models import HistoricalRecords

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def all_devices(self):
        return self.device_set.all().values()


class ServerType(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ['type']

    def splittype(self):
        return self.splittype.split('\n')

    def __unicode__(self):
        return self.type


class Type(models.Model):
    Type = models.CharField(max_length=100)

    class Meta:
        ordering = ['Type']

    def __unicode__(self):
        return self.Type


class OS(models.Model):
    OS = models.CharField(max_length=100)

    class Meta:
        ordering = ['OS']

    def __unicode__(self):
        return self.OS


class Status(models.Model):
    Status = models.CharField(max_length=100)

    class Meta:
        ordering = ['Status']

    def __unicode__(self):
        return self.Status


class Building(models.Model):
    building = models.CharField(max_length=100)
    code = models.CharField(max_length=3)

    def __unicode__(self):
        return '%s %s' % (self.building, self.code)


class Printer(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Location = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    IP = models.GenericIPAddressField(max_length=100)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.Name


class Server(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    ServerType = models.ForeignKey(ServerType, null=True)
    Role = models.CharField(max_length=100)
    IP = models.GenericIPAddressField(max_length=100)
    Notes = models.TextField(blank=True, max_length=500)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.Name


class Device(models.Model):
    UniqueID = models.CharField(max_length=100, unique=True, verbose_name="Computer ID")
    department = models.ForeignKey(Department, null=True, blank=True)
    Location = models.CharField(max_length=100)
    Type = models.ForeignKey(Type)
    OS = models.ForeignKey(OS)
    User = models.CharField(max_length=100)
    Date = models.DateField(blank=True, null=True, verbose_name="Last Date Inspected")
    Status = models.ForeignKey(Status)
    Notes = models.TextField(blank=True, max_length=500)
    history = HistoricalRecords()

    class Meta:
        ordering = ['UniqueID']

    def __unicode__(self):
        return '%s %s' % (self.UniqueID, self.department)


class TicketStatus(models.Model):
    Status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Status


class Ticket(models.Model):
    UniqueID = models.ForeignKey(Device, blank=True, null=True, verbose_name="Computer ID")
    User = models.CharField(max_length=100, verbose_name="Submitted By")
    Summary = models.TextField(max_length=1000)
    Status = models.ForeignKey(TicketStatus, default=1)
    Assignee = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __unicode__(self):
        return "%s %s" % (self.User, self.Assignee)


class Ports(models.Model):
    number = models.CharField(max_length=3, verbose_name="Port Number")
    description = models.CharField(max_length=100)
    room = models.CharField(max_length=3, verbose_name="Room Number")
    building = models.ForeignKey(Building, null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.number, self.building)

    class Meta:
        ordering = ['building', 'number']
