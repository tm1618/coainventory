from models import Department, ServerType, Status, Ports, Building


def navbar(request):
    departments = Department.objects.all()
    servertypes = ServerType.objects.all()
    status_type = Status.objects.all()
    ports = Ports.objects.all()
    buildings = Building.objects.all()

    return locals()
