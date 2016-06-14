from django.contrib import admin
from models import Device, OS, Type, Status, Printer, Server, Ticket, TicketStatus, Department, ServerType, Ports, \
    Building

# Register your models here.

admin.site.register(OS)
admin.site.register(Type)
admin.site.register(Device)
admin.site.register(Status)
admin.site.register(Printer)
admin.site.register(Server)
admin.site.register(Ticket)
admin.site.register(TicketStatus)
admin.site.register(Department)
admin.site.register(ServerType)
admin.site.register(Ports)
admin.site.register(Building)
