from django import forms
from django.contrib.admin import widgets
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, MultiField, Field, Div, ButtonHolder, HTML


class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        widgets = {
            'Date': forms.DateInput(attrs={'class':'datepicker'}),
            'Notes': forms.Textarea(attrs={'rows':8,
                                           'cols':30,
                                           'style':'max-width:230px;'}),
        }
        fields = ('UniqueID', 'User', 'department', 'Location', 'Type', 'OS', 'Date', 'Status', 'Notes')


class PrinterForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('Name', 'Location', 'Brand', 'Model', 'IP')


class ServerForm(forms.ModelForm):

    class Meta:
        model = Server
        widget = {
            'Name': forms.TextInput(attrs={'size': 300})
        }
        fields = ('Name', 'ServerType', 'Role', 'IP', 'Notes')

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


'''class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('Location',)'''


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('Status',)


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('Type',)


class OSform(forms.ModelForm):

    class Meta:
        model = OS
        fields = ('OS',)


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('UniqueID', 'User', 'Summary', 'Status', 'Assignee')


class UserTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('UniqueID', 'User', 'Summary')


class ServerTypeForm(forms.ModelForm):

    class Meta:
        model = ServerType
        fields = ('type',)


class DepartmentForm(forms.ModelForm):

    class Meta:
        model= Department
        fields = ('name', 'code',)


class PortsForm(forms.ModelForm):

    class Meta:
	model=Ports
	fields = ('number', 'description', 'building', 'room')


class BuildingForm(forms.ModelForm):

    class Meta:
	model=Building
	fields = ('building', 'code')