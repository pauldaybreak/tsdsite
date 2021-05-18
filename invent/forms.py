from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .views import *
from .models import *

class DateInput(forms.DateInput):
	input_type='date'

class DateForm(forms.Form):
	my_date_field = forms.DateField(widget=DateInput)

class DeviceForm(forms.ModelForm):
	class Meta:
		     
		model = Warehouse_device
		fields = ('type_device','number_PC_ID','serial_number_device','MVZ_Device','status_devices',
			'price','date_postavki','primechanie','who_change')
		widgets = {
      'date_postavki': DateInput(),
      }
		

class RepairDeviceForm(forms.ModelForm):
	class Meta:
		model = Repair_device
		fields = ('id_Repair','id_Device_on_repair','number_PC_ID_repair','number_repair','firm_repair',
			'status_repair','cost_repair','date_v_remont','date_iz_remonta','primechanie')

		widgets = {
      'date_v_remont': DateInput(),
      'date_iz_remonta': DateInput(),
      }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ToRemontForm(forms.ModelForm):
	class Meta:
		model = Warehouse_device
		fields = ['status_devices', 'primechanie', 'who_change']
		
		

