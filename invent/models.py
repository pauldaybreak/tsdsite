from django.db import models


### Справочник пользователей портала ###
# class Users_portal(object):
# 	login = models.Charfield(max_length=40, verbose_name="Логин пользователей")
# 	password = models.Charfield(max_length=40, verbose_name="пароль")
	
# 	"""docstring for Users_portal"""
# 	login = models.Charfield(max_length=40, verbose_name="Логин пользователей")
# 	password = models.Charfield(max_length=40, verbose_name="пароль")
# 	__init__(self, arg):
# 		super(Users_portal, self)._
# 		login = models.Charfield(max_length=40, verbose_name="Логин пользователей")
# 		password = models.Chrarfield(max_length=40, verbose_name="пароль")
# 		_init__()
# 		self.arg = arg
		


### Справочник отдел ###
class Department(models.Model):
	MVZ_Department = models.BigIntegerField(primary_key=True, verbose_name="МВЗ отдела")
	name_Departmnet = models.CharField(max_length=40, null=False, verbose_name="Название отдела")

	def __str__(self):
		return self.name_Departmnet

### Справочник сотрудник ###
class Sotrudnik(models.Model):
	tabel_number = models.IntegerField(primary_key=True, verbose_name="Табельный номер")
	name_sotridnik = models.CharField(max_length=40, verbose_name="ФИО")

	def __str__(self):
		return str(self.name_sotridnik)



##### Справочник "Cтатус" #####
class Type_status(models.Model):        # Справочник Статуса
    name_status = models.CharField(max_length=20, verbose_name="Тип статуса")

    def __str__(self):
        return self.name_status

class Repair_status(models.Model):
	name_status_repair = models.CharField(max_length=20, verbose_name="Статус ремонта")

	def __str__(self):
		return self.name_status_repair


class Warehouse_device(models.Model):   # Таблица оборудования на ЛЦ
	id_Device_on_Table = models.AutoField(primary_key=True, verbose_name="Номер устройства в ситсеме") # Первичный ключ
	type_device = models.CharField(max_length=40, null=False, verbose_name="Тип устройства")
	number_PC_ID = models.CharField(max_length=40, null=False, verbose_name="Имя устройства")
	serial_number_device = models.CharField(max_length=50, null=False, verbose_name="Серийный номер")
	MVZ_Device = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="МВЗ")
	status_devices = models.ForeignKey(Type_status, on_delete=models.SET_NULL, null=True, verbose_name="ID статус")
	price = models.IntegerField(null=False, verbose_name="Цена")
	date_postavki = models.DateTimeField(verbose_name="Дата поставки", blank=True, null=True)
	primechanie = models.CharField(max_length=300, verbose_name="Примечание")
	slug_devices = models.SlugField(max_length = 200, verbose_name="Ссылка URL")
	who_change = models.CharField(max_length=40, null=False, verbose_name="Кто изменил")

	def __str__(self):
		return self.number_PC_ID




class Repair_device(models.Model):
	id_Repair = models.AutoField(primary_key=True, verbose_name="Номер ремонта")
	id_Device_on_repair = models.ForeignKey(Warehouse_device, on_delete=models.SET_NULL, null=True, verbose_name = "Имя устройства СВЯЗЬ")
	number_PC_ID_repair = models.CharField(max_length=40, blank = False, verbose_name="Имя устройства на ремонт")
	number_repair = models.IntegerField(null=False, verbose_name="Номер АКТА")
	firm_repair = models.CharField(max_length=40, null=False, verbose_name="Фирма")
	status_repair = models.ForeignKey(Repair_status, on_delete=models.SET_NULL, null=True, verbose_name="ID статус")
	cost_repair = models.IntegerField(null=False, verbose_name="Стоимость ремонта", default=1000)
	date_v_remont = models.DateTimeField(verbose_name="Дата отправки в ремонт", blank=True, null=True)
	date_iz_remonta = models.DateTimeField(verbose_name="Дата приемки из ремонта", blank=True, null=True)
	primechanie = models.CharField(max_length=300, verbose_name="Примечание")


	def __str__(self):
		return str(self.id_Repair)





# Create your models here.
