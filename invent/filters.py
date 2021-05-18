import django_filters
from django import forms

from .models import *

class WarehouseDeviceFilter(django_filters.FilterSet):
	
	#type_device_filter = django_filters.CharFilter(lookup_expr='icontains')
	
	class Meta:
		model = Warehouse_device
		fields = ['type_device','number_PC_ID','MVZ_Device','status_devices',
			'price',
		]


class RepairDeviceFilter(django_filters.FilterSet):
	class Meta:
		model = Repair_device
		fields = ['id_Repair','number_PC_ID_repair', 'firm_repair', 'status_repair',
			'cost_repair',
		]