from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, render_to_response, \
    RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from models import Device, Type, OS, Status, Printer, Server, HistoricalRecords, Ticket, Department, ServerType, Ports, \
    Building
from django.contrib.auth.decorators import login_required
from forms import DeviceForm, TypeForm, OSform, StatusForm, PrinterForm, ServerForm, TicketForm, UserTicketForm, \
    ServerTypeForm, DepartmentForm, PortsForm, BuildingForm


# Create your views here.

@login_required()
def home(request):
    total = Device.objects.count()
    repair = Device.objects.filter(Status__Status="Repair").count()
    replace = Device.objects.filter(Status__Status="Replace").count()
    inspect = Device.objects.filter(Status__Status="Inspect").count()
    warranty = Device.objects.filter(Status__Status="Warranty").count()
    updates = Device.objects.filter(Status__Status="Needs Updates").count()
    changename = Device.objects.filter(Status__Status="Change Name").count()
    win7 = Device.objects.filter(OS__OS="Windows 7").count()
    win8 = Device.objects.filter(OS__OS="Windows 8").count()
    win81 = Device.objects.filter(OS__OS="Windows 8.1").count()
    win10 = Device.objects.filter(OS__OS="Windows 10").count()
    mac = Device.objects.filter(OS__OS="Mac").count()
    desktops = Device.objects.filter(Type__Type="Desktop").count()
    laptops = Device.objects.filter(Type__Type="Laptop").count()
    printers = Printer.objects.count()
    servers = Server.objects.count()
    domaincontroller = Server.objects.filter(ServerType__type="Domain Controller").count()
    return render(request, 'home.html', locals())


@login_required()
def alldevices(request):
    devices = Device.objects.all()
    total = Device.objects.count()
    a = datetime.now()

    return render(request, 'devices.html', locals())


@login_required()
def devicedetails(request, device_id):
    """display all of the equipment details"""
    device = Device.objects.get(id=device_id)

    return render(request, 'devicedetails.html', locals())


def navdepartments(request):

    return render(request, 'navbar.html', locals())


@login_required()
def newdevice(request):
    if request.POST:
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device added!')
            return HttpResponseRedirect('/devices/')
    else:
        form = DeviceForm()

    return render(request, 'newdevice.html', locals())


@login_required()
def editdevice(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    history = Device.history.filter(id=device_id)
    t = "Edit"

    tickets = Ticket.objects.filter(UniqueID=device_id)

    if request.POST:
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/device/edit/%s' % device_id)

    else:
        form = DeviceForm(instance=device)

    return render_to_response("editdevice.html", {
        'form': form,
        't': t,
        'device': device,
        'history': history,
        'tickets': tickets,
    }, context_instance=RequestContext(request))


@login_required()
def deletedevice(request, device_id):
    device = get_object_or_404(Device, pk=device_id).delete()

    messages.success(request, 'Device Removed!')
    return render(request, 'devicedeleted.html', locals())


@login_required()
def devicehistory(request, history_id):
    history = Device.history.get(pk=history_id)

    return render(request, 'history.html', locals())


@login_required()
def allPrinters(request):
    printers = Printer.objects.all();

    return render(request, 'printers.html', locals())


@login_required()
def device_set(request, department_code):

    devices = Device.objects.filter(department__code=department_code)

    return render(request, 'devices.html', locals())


@login_required()
def server_set(request, servertype_type):

    title = "Servers"
    servers = Server.objects.filter(ServerType=servertype_type)

    return render(request, 'servers.html', locals())


@login_required()
def status_set(request, status_id):

    status = Status.objects.get(pk=status_id)
    devices = Device.objects.filter(Status_id=status_id)

    return render(request, 'by_status.html', locals())


@login_required()
def addprinter(request):
    if request.POST:
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Printer added!')
            return HttpResponseRedirect('/printers/add/')
    else:
        form = PrinterForm()

    return render(request, 'addprinter.html', locals())


@login_required()
def editprinter(request, printer_id):
    printer = get_object_or_404(Printer, pk=printer_id)
    t = "Edit"

    if request.POST:
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/printers/')

    else:
        form = PrinterForm(instance=printer)

    return render_to_response("editprinter.html", {
        'form': form,
        't': t,
        'printer': printer,
    }, context_instance=RequestContext(request))


@login_required()
def deleteprinter(request, printer_id):
    printer = get_object_or_404(Printer, pk=printer_id).delete()

    messages.success(request, 'Printer Removed!')
    return render(request, 'devicedeleted.html', locals())


@login_required()
def allServers(request):
    servers = Server.objects.all();

    return render(request, 'servers.html', locals())


@login_required()
def addserver(request):
    if request.POST:
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Server added!')
            return HttpResponseRedirect('/servers/add/')
    else:
        form = ServerForm()

    return render(request, 'addserver.html', locals())


@login_required()
def editserver(request, server_id):
    servers = get_object_or_404(Server, pk=server_id)
    t = "Edit"

    if request.POST:
        form = ServerForm(request.POST, instance=servers)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/servers/')

    else:
        form = ServerForm(instance=servers)

    return render_to_response("editserver.html", {
        'form': form,
        't': t,
    }, context_instance=RequestContext(request))



@login_required()
def status(request):

    if request.POST:
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/status/')
    else:
        form = StatusForm()

    types = Status.objects.all()
    title = "Status Types"
    url = "status"

    return render(request, 'add.html', locals())


@login_required()
def editstatus(request, status_id):
    types = get_object_or_404(Status, pk=status_id)
    t = "Edit"

    if request.POST:
        form = StatusForm(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/status/')

    else:
        form = StatusForm(instance=types)

    types = Status.objects.all()
    title = "Edit Status Type"
    url = "status"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


@login_required()
def type(request):

    if request.POST:
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/type/')
    else:
        form = TypeForm()

    types = Type.objects.all()
    title = "Device Types"
    url = "type"

    return render(request, 'add.html', locals())


@login_required()
def edittype(request, type_id):
    types = get_object_or_404(Type, pk=type_id)
    t = "Edit"

    if request.POST:
        form = TypeForm(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/type/')

    else:
        form = TypeForm(instance=types)

    types = Type.objects.all()
    title = "Edit Device Type"
    url = "type"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


@login_required()
def os(request):

    if request.POST:
        form = OSform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/os/')
    else:
        form = OSform()

    types = OS.objects.all()
    title = "OS Types"
    url = "os"

    return render(request, 'add.html', locals())


@login_required()
def editos(request, os_id):
    types = get_object_or_404(OS, pk=os_id)
    t = "Edit"

    if request.POST:
        form = OSform(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/os/')

    else:
        form = OSform(instance=types)

    types = OS.objects.all()
    title = "Edit OS"
    url = "os"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


@login_required()
def servertype(request):

    if request.POST:
        form = ServerTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/servertypes/')
    else:
        form = ServerTypeForm()

    title = "Server Types"
    types = ServerType.objects.all()
    url = "servertypes"

    return render(request, 'add.html', locals())


@login_required()
def editservertype(request, type_id):
    types = get_object_or_404(ServerType, pk=type_id)
    t = "Edit"

    if request.POST:
        form = ServerTypeForm(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/servertypes/')

    else:
        form = ServerTypeForm(instance=types)

    types = ServerType.objects.all()
    title = "Edit Server Types"
    url = "servertypes"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


@login_required()
def departments(request):

    if request.POST:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/departments/')
    else:
        form = DepartmentForm()

    title = "Departments"
    types = Department.objects.all()
    url = "departments"

    return render(request, 'add.html', locals())


@login_required()
def editdepartments(request, type_id):
    types = get_object_or_404(Department, pk=type_id)
    t = "Edit"

    if request.POST:
        form = DepartmentForm(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/departments/')

    else:
        form = DepartmentForm(instance=types)

    types = Department.objects.all()
    title = "Edit Departments"
    url = "departments"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


def changename(request):
    devices = Device.objects.filter(Status__Status="Change Name")
    title = "Computers that need name changes"
    return render(request, "status.html", locals())


def update(request):
    devices = Device.objects.filter(Status__Status="Needs Updates")
    title = "Computers that need updates"

    return render(request, "status.html", locals())

def repair(request):
    devices = Device.objects.filter(Status__Status="Repair")
    title = "Computers that need to be repaired"

    return render(request, "status.html", locals())

def inspect(request):
    devices = Device.objects.filter(Status__Status="Inspect")
    title = "Computers that need to be inspected"

    return render(request, "status.html", locals())


def replace(request):
    devices = Device.objects.filter(Status__Status="Replace")
    title = "Computers that need to be replaced"

    return render(request, "status.html", locals())


@login_required
def createticket(request):
    if request.POST:
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket added!')
            return HttpResponseRedirect('/tickets/')
    else:
        if request.user.is_superuser:
            form = TicketForm()
        else:
            form = UserTicketForm()

    return render(request, 'createticket.html', locals())


@login_required()
def alltickets(request):
    tickets = Ticket.objects.filter(Status=1)
    name = "All Tickets"
    return render(request, 'tickets.html', locals())


@login_required()
def userTickets(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    tickets = Ticket.objects.filter(Assignee__username=username, Status=1)
    name = "My Tickets"

    return render(request, 'tickets.html', locals())


@login_required()
def closedTickets(request):

    tickets = Ticket.objects.filter(Status=2)
    name = "Closed Tickets"

    return render(request, 'tickets.html', locals())


@login_required()
def unassignedTickets(request):

    tickets = Ticket.objects.filter(Assignee_id=None)
    name = "Unassigned Tickets"

    return render(request, 'tickets.html', locals())


@login_required()
def ticketdetails(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    tickets = Ticket.history.filter(id=ticket_id)
    t = "Edit"

    if request.POST:
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/tickets/')

    else:
        form = TicketForm(instance=ticket)

    return render_to_response("ticketdetails.html", {
        'form': form,
        't': t,
        'tickets': tickets,
    }, context_instance=RequestContext(request))


@login_required()
def addport(request):

    if request.POST:
        form = PortsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ports/')
    else:
        form = PortsForm()

    ports = Ports.objects.all()
    title = "Ports"
    url = "ports"

    return render(request, 'addport.html', locals())


@login_required()
def editport(request, ports_id):
    ports = get_object_or_404(Ports, pk=ports_id)
    t = "Edit"

    if request.POST:
        form = PortsForm(request.POST, instance=ports)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/ports/')

    else:
        form = PortsForm(instance=ports)

    ports = Ports.objects.all()
    title = "Edit Port"
    url = "ports"
    link = ports_id

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


@login_required()
def allports(request):
    ports = Ports.objects.all()

    return render(request, 'ports.html', locals())


def buildingport(request, building_code):
    ports = Ports.objects.filter(building__code=building_code)

    return render(request, 'ports.html', locals())


@login_required()
def deleteport(request, port_id):
    port = get_object_or_404(Ports, pk=port_id).delete()

    messages.success(request, 'Port Removed!')
    return render(request, 'devicedeleted.html', locals())


@login_required()
def addbuilding(request):

    if request.POST:
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/building/add')
    else:
        form = BuildingForm()

    buildings = Building.objects.all()
    title = "Buildings"
    url = "building"

    return render(request, 'addbuilding.html', locals())


@login_required()
def editbuilding(request, building_id):
    buildings = get_object_or_404(Building, pk=building_id)
    t = "Edit"

    if request.POST:
        form = BuildingForm(request.POST, instance=buildings)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/building/')

    else:
        form = BuildingForm(instance=buildings)

    buildings = Building.objects.all()
    title = "Edit Building"
    url = "buildings"

    return render_to_response("edit.html", {
            'form': form,
            't': t,
    }, context_instance=RequestContext(request, locals()))


def lobby(request):

	return render(request, 'lobby.html')