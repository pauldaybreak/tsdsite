from django.contrib import admin
from .models import *


admin.site.register(Department)
admin.site.register(Sotrudnik)
admin.site.register(Type_status)
admin.site.register(Repair_status)


@admin.register(Repair_device)
class Repair_device_admin(admin.ModelAdmin):
	list_display = ("id_Repair", "id_Device_on_repair",  "number_PC_ID_repair", "number_repair", "firm_repair", "status_repair", "cost_repair", "date_v_remont", "date_iz_remonta", "primechanie")
	search_fields = ["firm_repair", "number_PC_ID_repair"]

	

@admin.register(Warehouse_device)
class Warehouse_device(admin.ModelAdmin):
	list_display = ("id_Device_on_Table", "type_device", "number_PC_ID", "serial_number_device", "MVZ_Device", "status_devices", "price", "date_postavki", "primechanie", 'slug_devices') 
	search_fields = ["number_PC_ID"]
	prepopulated_fields = {'slug_devices': ('number_PC_ID',)}



# Register your models here.
