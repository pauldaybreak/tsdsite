from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only
import xlwt
from .filters import *

from datetime import datetime, date, time
from django.shortcuts import render
from django.core.paginator import Paginator


@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			
			messages.success(request, 'Account was created for ' + username)
			
			return redirect('login_page')



	context = {'form': form}
	return render(request, 'register.html', context)

# Create your views here.
@login_required(login_url='login_page')
def index(request):
	return render(request, 'index.html')

# def main_page_repair(request):
# 	return render(request, 'display_repair.html')

def userPage(request):
	context={}
	return render(request, 'user.html', context)


@admin_only
@login_required(login_url='login_page')

def display_devices(request):
	
	context = {}

	filtered_device = WarehouseDeviceFilter(
		request.GET,
		queryset=Warehouse_device.objects.all()

	)

	context['filtered_device'] = filtered_device

	paginated_filtered_device = Paginator(filtered_device.qs, 10)  #отображает три записи
	page_number = request.GET.get('page') 
	device_page_obj = paginated_filtered_device.get_page(page_number)

	context['device_page_obj'] = device_page_obj

	return render(request, 'index.html', context=context)

@login_required(login_url='login_page')
def display_repair(request):

	context = {}

	filtered_repair = RepairDeviceFilter(
		request.GET,
		queryset=Repair_device.objects.all()

	)

	context['filtered_repair'] = filtered_repair

	paginated_filtered_repair = Paginator(filtered_repair.qs, 10)  #отображает три записи
	page_number = request.GET.get('page') 
	repair_page_obj = paginated_filtered_repair.get_page(page_number)

	context['repair_page_obj'] = repair_page_obj

	return render(request, 'display_repair.html', context=context)

@login_required(login_url='login_page')
def display_tsd(request):

	context = {}

	filtered_device = WarehouseDeviceFilter(
		request.GET,
		queryset=Warehouse_device.objects.filter(type_device='ТСД')

	)

	context['filtered_device'] = filtered_device

	paginated_filtered_device = Paginator(filtered_device.qs, 10)  #отображает три записи
	page_number = request.GET.get('page') 
	device_page_obj = paginated_filtered_device.get_page(page_number)

	context['device_page_obj'] = device_page_obj
	return render(request, 'index.html', context=context)


@login_required(login_url='login_page')
def display_techniks(request):

	context = {}

	filtered_device = WarehouseDeviceFilter(
		request.GET,
		queryset=Warehouse_device.objects.filter(type_device='Складская техника')

	)

	context['filtered_device'] = filtered_device

	paginated_filtered_device = Paginator(filtered_device.qs, 10)  #отображает три записи
	page_number = request.GET.get('page') 
	device_page_obj = paginated_filtered_device.get_page(page_number)

	context['device_page_obj'] = device_page_obj
	return render(request, 'index.html', context=context)


def search(request):
	WHDevice_list = Warehouse_device.objects.all()
	WHDevice_filter = WarehouseDeviceFilter(request.GET, queryset=user_list)
	return render(request, 'search/whdevice_filter.html', {'filter': WHDevice_filter}) 	


@login_required(login_url='login_page')

@admin_only
def add_device(request):
	if request.method == "POST":
		form = DeviceForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_devices')
	else:
		form = DeviceForm()
		return render(request, 'add_new.html', {'form': form})

@login_required(login_url='login_page')

@admin_only
def edit_device(request, pk):
	item = get_object_or_404(Warehouse_device, pk=pk)

	if request.method == "POST":
		form = DeviceForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_devices')
	else:
		form = DeviceForm(instance=item)
		return render(request, 'edit_item.html', {'form': form})


@login_required(login_url='login_page')
def add_repair(request):
	if request.method == "POST":
		form = RepairDeviceForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_devices')

	else:
		form = RepairDeviceForm()
		return render(request, 'add_repair.html', {'form': form})


@login_required(login_url='login_page')
def edit_repair(request, pk):
	item = get_object_or_404(Repair_device, pk=pk)

	if request.method == "POST":
		form = RepairDeviceForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display_repair')

	else: 
		form = RepairDeviceForm(instance=item)

		return render(request, 'edit_repair.html', {'form': form})


@unauthenticated_user
def login_page(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username OR Password is incorrect')
			#return render(request, 'login_page.html', context)

	context = {}
	return render (request, 'login_page.html', context)

@login_required(login_url='login_page')
def go_to_remont(request, pk):
	item = get_object_or_404(Warehouse_device, pk=pk)

	if request.method == "POST":
		form = ToRemontForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = ToRemontForm(instance=item)

	

	

		return render(request, 'go_to_remont.html', {'form': form})
		


def logout_user(request):
	logout(request)
	return redirect('login_page')



def add_to_remont(request, pk):
	
	items = Warehouse_device.objects.all()
#	Warehouse_device.objects.filter(type_device = "ТСД")
	context = {
		'items': items,
		'header': 'Devices'
	}
	return render(request, 'index.html', context)



def export_excel(request):
	response=HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename=WDs'+ \
		str(datetime.now())+'.xls'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('WDs')
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = ['id_Device_on_Table', 'type_device', 'number_PC_ID', 'serial_number_device']

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	font_style = xlwt.XFStyle()

	rows = Warehouse_device.objects.all().values_list('id_Device_on_Table', 'type_device', 'number_PC_ID', 'serial_number_device')

	for row in rows:
		row_num+=1

		for col_num in range(len(row)):
			ws.write(row_num, col_num, str(row[col_num]), font_style)

	wb.save(response)

	return response



# def edit_device(request, pk):
# 	item = get_object_or_404(Warehouse_device, pk=pk)

# 	if request.method == "POST":
# 		form = DeviceForm(request.POST, instance=item)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('index')
# 	else:
# 		form = DeviceForm(instance=item)
# 		return render(request, 'edit_item.html', {'form': form})




